#Display simple scrolling text using SenseHat

from sense_hat import SenseHat

sense = SenseHat()

#Foreground will be bright, soft pink
fground = (255,128,255)
#Background will be dim, dark green
bground = (0,64,0)

sense.show_message("Hello World!", text_colour = fground, back_colour = bground)