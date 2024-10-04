from cgitb import reset

from pico2d import *
import random

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

def reset_hand_position():
    global hand_x, hand_y
    hand_x = random.randint(0, TUK_WIDTH)
    hand_y = random.randint(0, TUK_HEIGHT)

    pass


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
direction = 1
speed = 5

reset_hand_position()

while running:

    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hand_x, hand_y)

    if x < hand_x:
        x += speed
        direction = 1
    elif x > hand_x:
        x -= speed
        direction = -1

    if y < hand_y:
        y += speed
    elif y > hand_y:
        y -= speed

    if abs(x - hand_x) < 10 and abs(y - hand_y) < 10:
        reset_hand_position()

    if direction == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)

    update_canvas()
    handle_events()

    frame = (frame + 1) % 8

    delay(0.01)

    pass

close_canvas()
