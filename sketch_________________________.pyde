x=0
def setup():
    size(800,800)
def draw():
    global x
    #translate(300,200)
    fill(x,x,x)
    ellipse(400,400,x,x)
    x=x+1
    if x==700:
     background(211, 211, 211)
     x=x-700
    #if x==700:
     #background(211, 211, 211)
     #x=x-700
     
