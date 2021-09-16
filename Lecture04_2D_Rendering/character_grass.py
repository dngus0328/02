from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
while x < 800:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x += 2
    delay(0.01)

y = 0
while y < 510:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(800, y + 90)
    y += 2
    delay(0.01)

x = 800
while 0 < x:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 600)
    x -= 2
    delay(0.01)


close_canvas()
