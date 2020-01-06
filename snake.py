import random
import curses

start_game = curses.initscr()
curses.curs_set(0)
snake_height, snake_width = start_game.getmaxyx()
window = curses.newwin(snake_height, snake_width, 0, 0)
window.keypad(1)
window.timeout(100)

snake_cood_x = snake_width/4
snake_cood_y = snake_height/2
snake = [
    [snake_cood_y, snake_cood_x],
    [snake_cood_y, snake_cood_x-1],
    [snake_cood_y, snake_cood_x-2]
]

snake_food = [snake_height/2, snake_width/2]
window.addch(int(snake_food[0]), int(snake_food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, snake_height] or snake[0][1]  in [0, snake_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == snake_food:
        snake_food = None
        while snake_food is None:
            nf = [
                random.randint(1, snake_height-1),
                random.randint(1, snake_width-1)
            ]
            snake_food = nf if nf not in snake else None
        window.addch(snake_food[0], snake_food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')

    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)