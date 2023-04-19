x=0
y=0
def setup():
    size(600,600)
def draw():
    global x,y
    img1=loadImage("krastikrabs.jpg")
    image(img1,0,0,600,600)
    img2=loadImage("misterkrabs.png")
    image(img2,300,300,y+80,y+80)
    img3=loadImage("dollari.jpg")
    image(img3,300,x,80,80)
    x=x+1
    #y=y+1
    if x==220:
        x=x-300
        y=y+50
def keyPressed():
    global y
    if key == CODED:
       if keyCode == RIGHT:
           y=y+1
           if img2 == 600,600:
               
           
