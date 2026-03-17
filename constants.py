SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480  # Ширина и высота экрана
GRID_SIZE = 20  # Размер одной клетки
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # Кол-во клеток по горизонтали (ширина - X)
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # Кол-во клеток по вертикали (высота - Y)
CENTRAL_CELL = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Координаты центральной клетки

ALL_CELLS = {
    (x * GRID_SIZE, y * GRID_SIZE)
    for x in range(GRID_WIDTH)
    for y in range(GRID_HEIGHT)
}  # Множество всех клеток на поле (каждая клетка представляет координату)

UP = (0, -1)  # Вверх по Y
DOWN = (0, 1)  # Вниз по Y
LEFT = (-1, 0)  # Влево по X
RIGHT = (1, 0)  # Вправо по X

SPEED = 10  # Скорость движения змейки

BOARD_BACKGROUND_COLOR = (128, 128, 128)  # Задний фон (серый)
BORDER_COLOR = (128, 128, 128)  # Цвет границ (серый)
APPLE_COLOR = (255, 0, 0)  # Цвет яблока (красный)
SNAKE_COLOR = (0, 255, 0)  # Цвет змейки (зеленый)
