import random
import turtle as t


#사용자에게 물어보기 - 기분이 어때 (1,2,3)
fir = int( input("""어떤 이유로 디지털 만다라 애니메이션을 찾으셨나요?
                                1. 미래에 대한 불안
                                2. 학업에 대한 불안
                                3. 인간관계에 대한 스트레스
                                """))


#if/else 써가지고 1,2,3에 각기 다른 프로그램 주기

#warm color list 10
warm = ["red", "orange", "gold", "yellow", "brown", "darkorange", "tomato", "coral", "chocolate", "firebrick"]

#neutral color list 10
neutral = ["black", "white", "gray", "wheat", "lightgray", "slategray", "silver", "beige", "ivory", "gainsboro"]

#rainbow color list 20
rainbow = rainbow_gradient = [
    "#FF0000",  # Red
    "#FF4000",  # Reddish-orange
    "#FF8000",  # Orange
    "#FFC000",  # Yellowish-orange
    "#FFFF00",  # Yellow
    "#C0FF00",  # Yellow-green
    "#80FF00",  # Greenish-yellow
    "#40FF00",  # Light green
    "#00FF00",  # Green
    "#00FF40",  # Greenish-cyan
    "#00FF80",  # Cyan-green
    "#00FFC0",  # Light cyan
    "#00FFFF",  # Cyan
    "#00C0FF",  # Cyan-blue
    "#0080FF",  # Blue-cyan
    "#0040FF",  # Light blue
    "#0000FF",  # Blue
    "#4000FF",  # Bluish-violet
    "#8000FF",  # Violet
    "#C000FF"   # Magenta
]

#dark color list 10
dark = ["darkred", "darkorange", "darkgoldenrod", "darkgreen", "darkblue", "darkviolet", "darkgray", "midnightblue", "maroon", "black"]

#bright color list 10
bright = ["cyan", "magenta", "lime", "yellow", "pink", "deepskyblue", "chartreuse", "gold", "hotpink", "turquoise"]

#1. 미래에 대한 불안-> bk/warm. turtle/rainbow. speed/slow. shapes/square,circle

if fir == 1 :

    #choose bk color
    screen = t.Screen()
    screen.bgcolor(random.choice(warm))

    c = random.randint(2,5)
    t.speed(random.randint(5,10))
    t.pensize(random.randint(2,5))
    d = random.randint(80,100)

    for a in range(c) :
        for b in rainbow : 
            t.color(b)
            t.circle(d)
            for e in range(3):
                t.fd(d*2)
                t.lt(120)
            t.lt(10)


#2. 학업에 대한 불안-> bk/dark. color/neutral. speed/slowish medium. shapes/triangle,circle

#3. 인간간계에 대한 스트레스-> bk/bright. color/warm. speed/medium. shapes/circle
