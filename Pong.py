# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-random.randrange(60, 180) / 60, random.randrange(120, 240) / 60]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[1] = -random.randrange(60, 180) / 60
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120, 240) / 60
    else:
        ball_vel[0] = -random.randrange(120, 240) / 60


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    if random.randrange(0, 11) % 2 == 0:
        spawn_ball("RIGHT")
    else:
        spawn_ball("LEFT")


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel > 0 + HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel

    if paddle2_pos + paddle2_vel > 0 + HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    p1_start = [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT]
    p1_end = [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT]
    p2_start = [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT]
    p2_end = [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]

    # draw paddles
    canvas.draw_line(p1_start, p1_end, PAD_WIDTH, "White")
    canvas.draw_line(p2_start, p2_end, PAD_WIDTH, "White")

    # determine whether paddle and ball collide
    spawn_dir = "Keepon"

    # ball offlimits
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        spawn_dir = "None"
        if (ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT or
                ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT):
            spawn_dir = "Left"
    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        spawn_dir = "None"
        if (ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT or
                ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT):
            spawn_dir = "Right"

    if spawn_dir == "None":
        ball_vel[0] = - (ball_vel[0] + ball_vel[0] * 0.1)
        ball_vel[1] += ball_vel[1] * 0.1
    elif spawn_dir != "Keepon":
        spawn_ball(spawn_dir)
        if spawn_dir == "Left":
            score1 += 1
        else:
            score2 += 1

    if ball_pos[1] + BALL_RADIUS >= HEIGHT or ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] = -ball_vel[1]

    # draw scores
    canvas.draw_text(str(score1), [WIDTH // 3, HEIGHT // 4], 40, "Red")
    canvas.draw_text(str(score2), [2 * WIDTH // 3, HEIGHT // 4], 40, "Blue")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS) or ball_pos[1] <= (BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT):
            spawn_ball("RIGHT")
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1

    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT):
            spawn_ball("LEFT")
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1


def keydown(key):
    global paddle1_vel, paddle2_vel
    speed = 5

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - speed
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = speed
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -speed
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = speed


def keyup(key):
    global paddle1_vel, paddle2_vel
    speed = 5

    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()