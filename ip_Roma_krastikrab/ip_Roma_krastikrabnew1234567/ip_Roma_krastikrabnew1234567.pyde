x=0
y=0
d=0
g=0
H=0
k=0
l=0
def setup():
    size(600,600)
    #img1=loadImage("krastikrabs.jpg")
    #image(img1,0,0,600,600)
def draw():
    global y,d,g,l
    img1=loadImage("krastikrabs.jpg")
    img4=loadImage("Bottle_Burglars_001.jpg")
    # img1=loadImage("krastikrabs.jpg")
    # image(img1,0,0,600,600)
    img2=loadImage("misterkrabs.png")
    image(img2,d,H,g+80,g+80)
    img3=loadImage("dollari.jpg")
    image(img3,300,y,80,80)
    y=y+1
    stroke(250,0,0)
    strokeWeight(5)
    if d>250 and d<300 and H > y and H< y+80:
        g=g+50
        y=-300
    if d > 550 and H > 500:
        img4=loadImage("Bottle_Burglars_001.jpg")
        image(img4,0,0,600,600)
    # if l>0 and l<80 and l>1 and l<81 and l>2 and l<82 and l>3 and l<83 and l>4 and l<84 and l>5 and l<85 and l>6 and l<86 and l>7 and l<87 and l>8 and l<88:
    #     g=g+50    
def keyPressed():
    global d,H
    if key == CODED:
        if keyCode == RIGHT:
            d=d+10
        if keyCode == LEFT:
            d=d-10
        if keyCode == DOWN:
            H=H+10
        if keyCode == UP:
            H=H-10
            
               
           
