#def setup():
    #size(800,600)
    #fill(0,0,0)
    #background(0,0.0)
#def draw():
    #frameRate(5)
    #stroke(random(200,211),random(200,211),random(200,211))
    #strokeWeight(random(0,5))
    #point(random(0,800),random(0,300))
    #ellipse(400,300,random(0,80),random(0,90))
    #stroke(random(0,255),random(0,255),random(0,255))
    #line(400,300,random(0,150),random(0,200))
x=0
def setup():
    size(500,500)
def draw():
    global x
    background(100)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(250+x,250+x,20,20)
    ellipse(250-x,250+x,20,20)
    ellipse(250+x,250-x,20,20)
    ellipse(250-x,250-x,20,20)
    x=x+1
    
    
