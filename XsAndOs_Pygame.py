# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import sys


# создаем игру и окно с клетками
pygame.init()
# pygame.mixer.init()  # для звука
SIZE_BLOCK = 100    # задаем размер игровых клеток
MARGIN = 15         # расстояние между клетками
width = height = SIZE_BLOCK * 3 + MARGIN * 4    # получаем размеры игрового поля
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("крестики-нолики")
img = pygame.image.load('XsAndOs.png')
pygame.display.set_icon(img)
FPS = 60         # частота кадров в секунду
clock = pygame.time.Clock()
# Задаем цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
board = [[0] * 3 for i in range(3)]   # создаем пустой массив 3х3
count = 1  # номер хода
game_over = False


def check_win(board, sign):
    zerous = 0
    for row in board:
        zerous += row.count(0)
        if row.count(sign) == 3:
            return f'{sign} победили!'
    for column in range(3):
        if board[0][column] == sign and board[1][column] == sign and board[2][column] == sign:
            return f'{sign} победили!'
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return f'{sign} победили!'
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return f'{sign} победили!'
    if zerous == 0:
        return 'Это ничья'
    return False


def print_text(text, text_size, text_color):
    screen.fill(BLACK)
    font = pygame.font.SysFont('arial', text_size)
    text = font.render(text, True, text_color)
    text_rect = text.get_rect()    # координаты текста
    # координаты экрана
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])   # размещение текста по координатам
    font = pygame.font.SysFont('arial', 20)
    text1 = font.render('для запуска новой игры', True, GREEN)
    screen.blit(text1, [15, height - 2 * MARGIN - 2 * text1.get_height()])
    text2 = font.render('нажмите пробел', True, GREEN)
    screen.blit(text2, [15, height - MARGIN - text2.get_height()])


# Цикл игры
while True:
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # проверить закрытие окна
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()   # координаты мышки
            # нажимаемая клетка:
            column = x_mouse // (SIZE_BLOCK + MARGIN)
            row = y_mouse // (SIZE_BLOCK + MARGIN)
            if board[row][column] == 0:  # проверяем, пуста ли клетка
                if count % 2 != 0:  # проверяем, чей ход
                    board[row][column] = 'x'     # первый ход - всегда 'x'
                else:
                    board[row][column] = 'o'
                count += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            board = [[0] * 3 for i in range(3)]
            count = 0
            screen.fill(BLACK)
    clock.tick(FPS)
    if not game_over:
        for row in range(3):
            for column in range(3):
                x = column * SIZE_BLOCK + (column + 1) * MARGIN
                y = row * SIZE_BLOCK + (row + 1) * MARGIN
                pygame.draw.rect(screen, WHITE, (x, y, SIZE_BLOCK, SIZE_BLOCK))
                if board[row][column] == 'x':
                    pygame.draw.line(screen, BLACK, (x + 5, y + 5),
                                     (x - 5 + SIZE_BLOCK, y - 5 + SIZE_BLOCK), 10)
                    pygame.draw.line(screen, BLACK, (x - 5 + SIZE_BLOCK, y + 5),
                                     (x + 5, y - 5 + SIZE_BLOCK), 10)
                elif board[row][column] == 'o':
                    pygame.draw.circle(screen, BLACK, (x + SIZE_BLOCK // 2, y + SIZE_BLOCK // 2),
                                       SIZE_BLOCK // 2 - 2, 8)
    if (count - 1) % 2 != 0:    # x
        game_over = check_win(board, 'x')
    else:
        game_over = check_win(board, 'o')

    if game_over:
        print_text(game_over, 40, RED)
    pygame.display.update()
