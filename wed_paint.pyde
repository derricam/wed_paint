def setup():
    size(600,400)
    background("#936759")
    fill(255,255,255)
    rect(0,0,50,50)
    fill(0,0,0)
    rect(0,50,50,50)
    fill("#F70227")
    rect(0,100,50,50)
    fill("#D8028A")
    rect(0,150,50,50)
    fill("#9002D8")
    rect(0,200,50,50)
    fill("#0224D8")
    rect(0,250,50,50)
    fill("#02D8D7")
    rect(0,300,50,50)
    fill("#02D86F")
    rect(50,0,50,50)
    fill("#25D802")
    rect(50,50,50,50)
    fill("#F7F705")
    rect(50,100,50,50)
    fill("#D6CD1E")
    rect(50,150,50,50)
    fill("#FCBC08")
    rect(50,200,50,50)
    fill("#FA8508")
    rect(50,250,50,50)
    fill("#5A4D48")
    rect(50,300,50,50)
    
def draw():
    if mousePressed:
        if pmouseX >= 100 or pmouseY >= 350:
            line(pmouseX, pmouseY, mouseX, mouseY)
    
    

def mouseClicked():
    if mouseX <= 50 and mouseY <50:
        stroke(255,255,255)
    elif mouseX <= 50 and mouseY > 50 and mouseY <=100:
        stroke(0,0,0)
    elif mouseX <= 50 and mouseY > 100 and mouseY <=150:
        stroke("#F70227")
    elif mouseX <=50 and mouseY > 150 and mouseY <=200:
        stroke("#D8028A")
    elif mouseX <=50 and mouseY > 200 and mouseY <=250:
        stroke("#9002D8")
    elif mouseX <=50 and mouseY > 250 and mouseY <=300:
        stroke("#0224D8")
    elif mouseX <=50 and mouseY > 300 and mouseY <=350:
        stroke("#02D8D7")
    elif mouseX > 50 and mouseY < 100 and mouseY <=50:
        stroke("#02D86F")
    elif mouseX > 50 and mouseY < 150 and mouseY <=100:
        stroke("#25D802")
    elif mouseX > 50 and mouseY < 200 and mouseY <=150:
        stroke("#F7F705")
    elif mouseX > 50 and mouseY < 250 and mouseY <=200:
        stroke("#D6CD1E")
    elif mouseX > 50 and mouseY < 300 and mouseY <=250:
        stroke("#FCBC08")
    elif mouseX > 50 and mouseY < 350 and mouseY <=300:
        stroke("#FA8508")
    elif mouseX > 50 and mouseY < 400 and mouseY <=350:
        stroke("#5A4D48")
