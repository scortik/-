x=0
y=0
d=0
g=0
def setup():
    size(600,600)
def draw():
    global y,d,g
    img1=loadImage("krastikrabs.jpg")
    image(img1,0,0,600,600)
    img2=loadImage("misterkrabs.png")
    image(img2,d,300,g+80,g+80)
    img3=loadImage("dollari.jpg")
    image(img3,300,y,80,80)
    y=y+1
    stroke(250,0,0)
    strokeWeight(5)
    if y==270:
        y=y-300
        if d>250 and d<300:
            g=g+50
def keyPressed():
    global d
    if key == CODED:
        if keyCode == RIGHT:
            d=d+1
        if keyCode == LEFT:
            d=d-1
           #if img2 == 600,600:
               
