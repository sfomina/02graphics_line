from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line (250, 250, 250,500, screen, color)
draw_line (250, 250, 250, 0, screen, color)
draw_line (250, 250, 500, 250, screen, color)
draw_line (250, 250, 0, 250, screen, color)
draw_line (250, 250,500 , 500, screen, color)
draw_line (250, 250,375,500, screen, color)
draw_line (250, 250,500 ,375, screen, color)
draw_line (0,250, 250 , 250, screen, color)
draw_line (125,500,250 ,250, screen, color)
draw_line (0,375,250, 250, screen, color)
draw_line (0,0,250 , 250, screen, color)
draw_line (0,125, 250 , 250, screen, color)
draw_line (125, 0, 250 , 250, screen, color)
draw_line (250, 250,500 , 125, screen, color)
draw_line (250, 250,500 , 0, screen, color)
draw_line (250, 250, 375 , 0, screen, color)
draw_line (0, 500,250 , 250, screen, color)
#print screen

#display(screen)

save_ppm(screen, 'img.ppm')
