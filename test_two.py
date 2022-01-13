import pygame
import random
import os
import sys


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if tile_type == 'wall':
            wall_group.add(self)


class Snake(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(snake_group, all_sprites)
        self.image = snake_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, event):
        global running
        global cont
        global xs
        global ys
        global sn_pos
        if event.key == pygame.K_ESCAPE:
            running = False
        if event.key == pygame.K_UP:
            ys = -sn_pos
            xs = 0
        if event.key == pygame.K_DOWN:
            ys = sn_pos
            xs = 0
        if event.key == pygame.K_RIGHT:
            xs = sn_pos
            ys = 0
        if event.key == pygame.K_LEFT:
            xs = -sn_pos
            ys = 0
        if pygame.sprite.spritecollideany(self, wall_group):
            cont = True


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x0, y0 = None, None, None
    for y0 in range(len(level)):
        for x0 in range(len(level[y0])):
            if level[y0][x0] == '.':
                Tile('empty', x0, y0)
            elif level[y0][x0] == '@':
                Tile('empty', x0, y0)
                new_player = Snake(x0, y0)
            elif level[y0][x0] == '#':
                Tile('wall', x0, y0)
    return new_player, x0, y0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Meow", "",
                  "Meow Meow",
                  "Meow Meow Meow-Meoooow,",
                  "Meow Meow-Meow Meow Meow Meow"]

    fon = pygame.transform.scale(load_image('nach.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 10
    for line in intro_text:
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
    value = score_font.render("Your Score: " + str(score), True, (255, 0, 0))
    screen.blit(value, [0, 0])


def snake(sn_pos, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 0, 0), [x[0], x[1], sn_pos, sn_pos])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def move(x_kon, y_kon):
    snake_image.get_rect().move(tile_width * x_kon + 15, tile_height * y_kon + 5)

WIDTH = 700
HEIGHT = 500
sn_pos = 1

sn_telo = []
sn_len = 1
food_x = round(random.randrange(0, WIDTH - sn_pos) / 10.0) * 10.0
food_y = round(random.randrange(0, HEIGHT - sn_pos) / 10.0) * 10.0

fons = ['fon_1.jpg', 'fon_2.png', 'fon_3.jpg']
fon_game = pygame.transform.scale(load_image(random.choice(fons)), (WIDTH, HEIGHT))
dead_screen = pygame.transform.scale(load_image('dead_screen.jpg'), (WIDTH, HEIGHT))
FPS = 60

x1 = WIDTH / 2
y1 = HEIGHT / 2

xs = 0
ys = 0
x_kon, y_kon = 33, 26

running = True
cont = False

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('SneakySnake')

    clock = pygame.time.Clock()
    player = None


    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont('ArialBlack', 20)

    tile_images = {
        'wall': load_image('wall.png'),
        'empty': load_image('pov.png')
    }
    snake_image = load_image('snake.jpg')

    tile_width = tile_height = 10
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()

    snake_group = pygame.sprite.Group()
    """snakes = pygame.sprite.Sprite()
    snakes.image = load_image("snake.jpg")
    snakes.rect = snakes.image.get_rect()
    all_sprites.add(snakes)
    snakes.rect.x = sn_pos
    snakes.rect.y = sn_pos
    all_sprites.draw(screen)"""

    wall_group = pygame.sprite.Group()
    start_screen()

    new_player, level_x, level_y = generate_level(load_level('level_1.txt'))

    while running:
        while cont == True:
            screen.blit(dead_screen, (0, 0))
            Your_score(sn_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        cont = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites.update(event)
                snake_image.get_rect().move(tile_width * x_kon + 15, tile_height * y_kon + 5)
        
        #screen.blit(fon_game, (0, 0))
        #pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, sn_pos, sn_pos])
        ##all_sprites.draw(screen)
        x_kon = x_kon + xs
        y_kon = y_kon + ys

        sn_head = []
        sn_head.append(x1)
        sn_head.append(y1)
        sn_telo.append(sn_head)
        if len(sn_telo) > sn_len:
            del sn_telo[0]

        for x in sn_telo[:-1]:
            if x == sn_head:
                cont = True

        ##snake(sn_pos, sn_telo)
        Your_score(sn_len - 1)

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - sn_pos) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - sn_pos) / 10.0) * 10.0
            sn_len += 1

        pygame.display.update()
        tiles_group.draw(screen)
        snake_group.draw(screen)
        clock.tick(FPS)
    pygame.quit()
