# Student Online automatic

Your teacher doesn't share the slides

Tired to take screenshot everytime

This program try to recover the pdf from a recording video 


## Instalation 

### Dependecies
- ffmpeg
- python3
- imagehash
- FPDF

Install first ffmpeg
```
$ sudo apt install ffmpeg
```
Install the python libraries
```
pip install ImageHash fpdf
```

## How to use it 

#### Default use
Is for the moment it's a commande line programm, just run the programm with the record to analyze and the name for the pdf file
```
python3 script_pdf.py recording.mp4 slides.pdf
```
#### Change the parameter

```python
seconds = 30  # Times between frames
resize = 0.7  # Resize to fill in a A4 pdf
height = 1297 # the height of the output rectangle
width = 973   # the width of the output rectangle
x = 311       # x and y specify the top left corner of the output rectangle
y = 0
```
In the code you can change this value to adapt to your video. `x` and `y` are the coordinates of the left top where you want to crop your video, you can also modify the width and height of the crop area.

The `seconds` is the interval of time between the screeshots, reduce it if the teacher is quick.
