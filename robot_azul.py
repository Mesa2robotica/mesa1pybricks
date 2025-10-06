from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
mi = Motor(Port.A, Direction.COUNTERCLOCKWISE)
md = Motor(Port.D)

sensor1 = ColorSensor(Port.B)
sensor2d = ColorSensor(Port.C)
sensor3i = ColorSensor(Port.F)

Color.GREEND = Color(h=166, s=66, v=45)
Color.GREENI = Color(h=165, s=62, v=42)
Color.GREENI_FALSE = Color (h=204, s=29, v=42)
Color.GREEND_FALSE = Color(h=197, s=24, v=53)
Color.GREEND_FALSED = Color(h=198, s=26, v=32)
Color.GREENI_FALSEI = Color(h=198, s=27, v=31)
my_colorsD = (Color.GREEND, Color.GREEND_FALSE, Color.GREEND_FALSED, Color.WHITE, Color.BLACK)  
my_colorsI = (Color.GREENI, Color.GREENI_FALSE, Color.GREENI_FALSEI, Color.WHITE, Color.BLACK)
sensor3i.detectable_colors(my_colorsI)
sensor2d.detectable_colors(my_colorsD)
#sEGUIDOR DE LINEA------------------------------------------------
reloj = StopWatch()
while True:

     #if sensor1.reflection () > 50 and sensor2d.reflection () > 50 and sensor3i.reflection() > 50:
          
          #if reloj.time() > 4500: 

              #md.run(-70)
              #mi.run(-70)
              #print("Retrocede")
     #if sensor
     if sensor1.reflection () < 50:
      
          md.run(170)
          mi.run(170)

     if sensor2d.reflection () < 50:
          mi.run(190)
          md.run(-170)

     if sensor3i.reflection() < 50:
          mi.run(-100)
          md.run(170)
     #SEGUNDA PARTE-------------------------------------------

     
     if sensor2d.color() == Color.GREEND:
          hub.display.char("D")
          mi.stop()
          md.stop()
          wait(1000)      
          mi.run(230)
          md.run(-50)
          wait(1000)
          mi.run(500)
          md.run(500)
          wait(50)

     if sensor3i.color() == Color.GREENI:
          hub.display.char("I")
          mi.stop()
          md.stop()
          wait(1000)
          mi.run(-50)
          md.run(230)
          wait(1000)
          mi.run(500)
          md.run(500)
          wait(50)
     if sensor2d.color() == Color.GREEND and sensor3i.color() == Color.GREENI:
          mi.run_angle(400, 200)
          wait(1000)
     
#
"""
def gi():
     print("verdeizquierdo")
     hub.imu.reset_heading(0)
     while hub.imu.heading() >-90:
         print(hub.imu.heading())
         md.dc(40)
         mi.dc(-40)
     md.stop()
     mi.stop()
def gd():  
     print("verdederecho")
     hub.imu.reset_heading(0) 
     while hub.imu.heading() <90:
         print(hub.imu.heading())
         md.dc(-40)
         mi.dc(40)
     md.stop()
     mi.stop()
    

while True:
    while sensor1.reflection() > 50 and sensor2d.reflection() > 50 and sensor3i.reflection() > 50:
 
         print("avance")
        
   print("bucle")
   if sensor3i.color()==Color.GREENI:
         mi.stop()
         md.stop()
         hub.display.char("I")
         wait(5000) 
         gi()
 
   if sensor2d.color()==Color.GREEND:
         mi.stop()
         md.stop()
         hub.display.char("D")
         wait(5000)
          
         gd()      
   while sensor1.reflection() > 50  and sensor2d.reflection() < 50 and sensor3i.reflection() < 50:      
         hub.display.char("D")
         wait(500)

         print("negro")
   
# while True:

#     colord= sensor2d.hsv()
#     print(color)
#     wait(1000)
    
#     gi()
#     wait(2000)

while True:
    
   
     
    if sensor1.reflection () < 45:

         md.run(250)
         mi.run(250)

    elif sensor2d.reflection () < 25:
         mi.run(150)
         md.run(-230)

    elif sensor3i.reflection() < 25:
         mi.run(-110)
         md.run(210)
    else:
         md.run(250)
         mi.run(250)
"""
