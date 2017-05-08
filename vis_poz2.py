from visual import *
import Image
import time

#dane
wysokosc = 10
promien = 0.25
vx = 13
g = 9.81
vy = -5
y = wysokosc + promien
dt = 0.003
x = 0
scale_factor = 0.3

#customowa tekstura
im = Image.open('C:\Python27\jacek256.jpg')
tekstura = materials.texture(data = im, mapping = 'rectangular')

#parametry okna
okno = display(title = "Takie tam pierdoly", x = 90, y = 0, width = 1280,
  height = 720, background = color.black, center = (5,5,0))

#uklad wspolrzednych
dlugosc_osi = 20
osX = arrow(pos = (0,0,0), axis = (dlugosc_osi,0,0), shaftwidth = 0.1,
            color = color.blue)
podpisX = text(text = "x", pos = (dlugosc_osi,-0.5,0), height = 0.5)
osY = arrow(pos = (0,0,0), axis = (0,dlugosc_osi,0), shaftwidth = 0.1,
            color = color.blue)
podpisY = text(text = "y", pos = (0.5,dlugosc_osi,0), height = 0.5)
osZ = arrow(pos = (0,0,0), axis = (0,0,dlugosc_osi), shaftwidth = 0.1,
            color = color.blue)

#obiekty
#blok
blok = box(pos = (-0.5,5,0), lenght = 2, width = 2, height = wysokosc,
           color = color.red)
#kulka
kulka= sphere(pos = (0, wysokosc+promien ,0), radius = promien, color = color.cyan,
               make_trail = true)
#wektory
vx_vector = arrow(pos = (kulka.pos.x,kulka.pos.y,0), axis = (vx*scale_factor,0,0),
                  shaftwidth = 0.1, color = color.orange)
vy_vector = arrow(pos = (kulka.pos.x,kulka.pos.y,0), axis = (0,vy*scale_factor,0),
                  shaftwidth = 0.1, color = color.orange)
#tarcza
tarcza = box(pos = (15.5,3.5,0), lenght = 1, width = 3, height = 3, material = tekstura) #material = tekstura


#time.sleep(3.0)
while kulka.pos.y >= promien:
    rate(30)
    y = y - vy*dt - (g*dt**2)/2
    vy = vy + g*dt
    x = x + vx*dt
    kulka.pos = (x,y,0)
    vx_vector.pos = kulka.pos
    vy_vector.pos = kulka.pos
    vy_vector.axis.y = -vy*scale_factor
    #if kulka.pos.x == 14.5-promien and kulka.pos.y <= 4.5 and kulka.pos.y >= 2.5:
    #    break
