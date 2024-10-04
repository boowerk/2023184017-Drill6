from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')

def handle_events():

    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

while running:

    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    handle_events()

    pass

close_canvas()