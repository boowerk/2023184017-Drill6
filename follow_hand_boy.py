from pico2d import *

open_canvas()

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')

def handle_events():



    pass

running = True

while running:

    clear_canvas()
    background.clip_draw(0, 0, 1200, 1800, 400, 300, 800, 600)

    update_canvas()
    handle_events()

    pass

close_canvas()