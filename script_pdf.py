import subprocess
import sys
import os
from PIL import Image
from fpdf import FPDF
import imagehash
import argparse

def not_similar(image1,image2,n):
    hash0 = imagehash.average_hash(Image.open(image1))
    hash1 = imagehash.average_hash(Image.open(image2))
    if hash0 - hash1 < n:
        return False
    else:
        return True

def cut_video(video_path,seconds):
    subprocess.run(["mkdir","out"])
    subprocess.run(["mkdir","slides"])
    subprocess.run(["ffmpeg","-i",video_path,"-vf","fps=1/{}".format(seconds),"out/out%d.png"])

def buid_img_pdf(pdf_title,resize,height,width,x,y):
    pdf = FPDF('L', 'mm', (float(width * 0.264583), float(height * 0.264583) ) )
    directory='./out'
    for i in range(1,len(os.listdir(directory) )):
        subprocess.run(["ffmpeg","-i","out/out{}.png".format(i),'-filter:v','crop={}:{}:{}:{}'.format(height,width,x,y),"slides/slide{}.png".format(i)],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if i!=1:
            if not_similar("slides/slide{}.png".format(i),"slides/slide{}.png".format(i-1),3 ): #Try to find if the slide is changed comparing to the last frame
                pdf.add_page()
                pdf.image('slides/slide{}.png'.format(i), x = 0, y = 0, w = float(height * 0.264583), h = float(width * 0.264583))
        
    pdf.output(pdf_title, "F")

parser = argparse.ArgumentParser(description='Take a recording from classes and build the shared pdf')
parser.add_argument('recording',
                    help='the video of the classes')
parser.add_argument('pdf',
                    help='name of the pdf to be generated')
args = parser.parse_args()

seconds = 30 #Times between of frames
resize = 0.7  #Resize to fill in a A4 pdf
height = 1297 #the height of the output rectangle
width = 973   # the width of the output rectangle
x=311         # x and y specify the top left corner of the output rectangle
y=0
cut_video(args.recording,seconds)
print('Build pdf...')
buid_img_pdf(args.pdf,resize,height,width,x,y)

subprocess.run(["rm","-r","out"])
subprocess.run(["rm","-r","slides"])





