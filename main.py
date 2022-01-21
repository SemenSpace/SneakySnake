import pygame
import random
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('D:/SneakySnake/', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def last_win(_len):
    _font = pygame.font.SysFont('arialblack', 42)
    value = _font.render("Конечный рекорд: " + str(_len), True, (21, 107, 13))
    screen.blit(value, [100, 300])


def start_screen():

    with open('D:/SneakySnake/score.txt', mode="r", encoding='utf8') as lol:
            scoree = lol.read()
    intro_text = [f'Ваш максимальный рекорд {int(scoree) - 1}', "Для выбора режима - введите его номер", "1 - Default Mode",
                  "2 - В разработке",
                  "3 - В разработке",
                  "4 - В разработке",
                  "Для того чтобы играть нажмите 'Space'"]

    fon = pygame.transform.scale(load_image('nach.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 70
    i = 0
    for line in intro_text:
        i += 1
        if i == 1:
            string_rendered = font.render(line, True, (156, 33, 61))
        else:
            string_rendered = font.render(line, True, pygame.Color('Black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [11, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    for y0 in range(len(level)):
        for x0 in range(len(level[y0])):
            if level[y0][x0] == '#':
                y0 *= 10
                x0 *= 10
                pygame.draw.rect(screen, (105, 105, 105), [x0, y0, x0 + 10, y0 + 10])
                y0 //= 10
                x0 //= 10



if __name__ == '__main__':

    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    WIDTH = 700
    HEIGHT = 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('SneakySnake')

    clock = pygame.time.Clock()

    fons = ['fon_1.jpg', 'fon_2.png', 'fon_3.jpg']
    fon_game = pygame.transform.scale(load_image(random.choice(fons)), (WIDTH, HEIGHT))
    dead_screen = pygame.transform.scale(load_image('dead_screen.jpg'), (WIDTH, HEIGHT))
    snake_block = 10
    FPS = 8

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont('arialblack', 34)

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    sn_len = 1

    foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    running = True
    cont = False

    start_screen()

    while running:
        len_sc = False
        while cont == True:
            screen.blit(dead_screen, (0, 0))
            ###Your_score(sn_len - 1)
            last_win(sn_len - 1)
            pygame.display.update()
            with open('data/score.txt', mode="r") as lol:
                text = lol.read()
            if int(text) < int(sn_len):
                with open('data/score.txt', mode="w") as lo:
                    lo.write(str(sn_len))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        cont = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            cont = True
        x1 += x1_change
        y1 += y1_change
        screen.blit(fon_game, (0, 0))
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        generate_level(load_level('level_1.txt'))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > sn_len:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                cont = True

        our_snake(snake_block, snake_List)
        Your_score(sn_len - 1)

        pygame.display.update()
        print(snake_List)
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            sn_len += 1

        clock.tick(FPS)

    pygame.quit()
