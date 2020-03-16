from sense_hat import SenseHat

sense = SenseHat()

fground = (255,128,255)
bground = (0,64,0)

sense.show_message("Hello World!", text_colour = fground, back_colour = bground)