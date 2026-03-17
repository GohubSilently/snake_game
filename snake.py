from random import choice

import pygame as pg

from constants import (
    ALL_CELLS,
    APPLE_COLOR,
    BOARD_BACKGROUND_COLOR,
    BORDER_COLOR,
    CENTRAL_CELL,
    DOWN,
    GRID_HEIGHT,
    GRID_SIZE,
    GRID_WIDTH,
    LEFT,
    RIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_COLOR,
    SPEED,
    UP
)


MOVEMENT_SNAKE = {
    pg.K_UP: UP,
    pg.K_DOWN: DOWN,
    pg.K_LEFT: LEFT,
    pg.K_RIGHT: RIGHT,
}

# Настройка игрового окна:
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pg.display.set_caption('Змейка')
clock = pg.time.Clock()


class GameObject:
    def __init__(
        self,
        body_color=None
    ):
        self.position = CENTRAL_CELL
        self.body_color = body_color

    def draw(
        self
    ):
        raise NotImplementedError(
            f'Метод draw() не выполняется в {type(self).__name__}'
        )

    def draw_one_cell(
        self,
        position,
        body_color=None
    ):
        body_color = body_color or self.body_color
        rect = pg.Rect(position, (GRID_SIZE, GRID_SIZE))
        pg.draw.rect(screen, body_color, rect)
        if body_color != BOARD_BACKGROUND_COLOR:
            pg.draw.rect(screen, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    def __init__(
        self,
        occupied_cells=CENTRAL_CELL,
        body_color=APPLE_COLOR
    ):
        super().__init__(body_color)
        self.randomize_position(occupied_cells)

    def randomize_position(
        self,
        occupied_cells
    ):
        self.position = choice(tuple(ALL_CELLS - set(occupied_cells)))

    def draw(
        self
    ):
        self.draw_one_cell(self.position)


class Snake(GameObject):
    def __init__(
        self,
        body_color=SNAKE_COLOR
    ):
        super().__init__(body_color)
        self.reset()

    def get_head_position(
        self
    ):
        return self.positions[0]

    def reset(
        self
    ):
        self.length = 1
        self.direction = choice([UP, DOWN, RIGHT, LEFT])
        self.positions = [CENTRAL_CELL]
        self.last = None

    def update_direction(
        self,
        new_position
    ):
        if (
            new_position[0] != -self.direction[0]
            and new_position[1] != -self.direction[1]
        ):
            self.direction = new_position

    def move(
        self
    ):
        head_x, head_y = self.get_head_position()
        head_movement_x, head_movement_y = self.direction

        self.positions.insert(0, (
            (head_x + head_movement_x * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + head_movement_y * GRID_SIZE) % SCREEN_HEIGHT)
        )

        self.last = (
            self.positions.pop()
            if len(self.positions) > self.length
            else None
        )

    def draw(
        self
    ):
        self.draw_one_cell(self.get_head_position())
        if self.last:
            self.draw_one_cell(self.last, BOARD_BACKGROUND_COLOR)


def handle_keys(snake):
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)
        ):
            pg.quit()
            raise SystemExit
        if event.type == pg.KEYDOWN:
            new_position = MOVEMENT_SNAKE.get(event.key)
            if new_position:
                snake.update_direction(new_position)


def main():
    pg.init()

    snake = Snake()
    apple = Apple(snake.positions)
    best_length = 1

    screen.fill(BOARD_BACKGROUND_COLOR)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(snake.positions)

        elif snake.get_head_position() in snake.positions[4:]:
            snake.reset()
            apple.randomize_position(snake.positions)
            screen.fill(BOARD_BACKGROUND_COLOR)

        elif snake.length > best_length:
            best_length = snake.length

        apple.draw()
        snake.draw()

        new_caption = (
            f'ESC | Змейка | Длина: {snake.length} '
            f'| Рекорд: {best_length}'
        )
        if new_caption != pg.display.get_caption():
            pg.display.set_caption(new_caption)

        pg.display.update()


if __name__ == '__main__':
    main()
