import pygame
import random
import os
import sys
import json


class Snake:
    def __init__(self):
        self.kon_mode = open_mode('mode.json', chose_mode)
        self.kon = [i for i in self.kon_mode[0].values()]
        self.snake = self.kon[2]
        self.speed = int(self.kon[3])
        self.tp = self.kon[5]
        self.cont = True
        self.w = self.kon[0] * 10
        self.h = self.kon[1] * 10
        self.x_sn = 350
        self.y_sn = 250
        self.x_ch = 0
        self.y_ch = 0
        self.sn_len = 0
        self.snake_List = []
        self.snake_Head = []
        self.a_x = round(random.randrange(720 - self.w, 680 - (710 - self.w)) / 10.0) * 10.0
        self.a_y = round(random.randrange(520 - self.h, 480 - (510 - self.h)) / 10.0) * 10.0
        self.proshl_hod = []

    def chose_snake(self):
        if self.snake == 2:
            self.sn_len = 5
            self.x_sn = 120
            self.y_sn = 120
            self.x_ch = 0
            self.y_ch = 10

    def gen_snake(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, (255, 255, 255), [x[0], x[1], sn_har, sn_har])

    def get_snake(self):
        return self.snake

    def get_speed(self):
        return self.speed

    def update_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.proshl_hod[0] != -sn_har or self.proshl_hod[1] != 0:
                        self.x_ch = -sn_har
                        self.y_ch = 0
                elif event.key == pygame.K_RIGHT:
                    if self.proshl_hod[0] != sn_har or self.proshl_hod[1] != 0:
                        self.x_ch = sn_har
                        self.y_ch = 0
                elif event.key == pygame.K_UP:
                    if self.proshl_hod[0] != 0 or self.proshl_hod[1] != -sn_har:
                        self.x_ch = 0
                        self.y_ch = -sn_har
                elif event.key == pygame.K_DOWN:
                    if self.proshl_hod[0] != 0 or self.proshl_hod[1] != sn_har:
                        self.x_ch = 0
                        self.y_ch = sn_har
        self.proshl_hod.clear()
        self.proshl_hod.append(self.x_ch * -1)
        self.proshl_hod.append(self.y_ch * -1)

    def snake_update(self):
        self.x_sn += self.x_ch
        self.y_sn += self.y_ch
        self.snake_Head = []
        self.snake_Head.append(self.x_sn)
        self.snake_Head.append(self.y_sn)
        self.snake_List.append(self.snake_Head)

    def return_list(self):
        return self.snake_List

    def return_len(self):
        return self.sn_len

    def eat_apple(self):
        if self.x_sn == self.a_x and self.y_sn == self.a_y:
            self.a_x = round(random.randrange(720 - self.w, 680 - (710 - self.w)) / 10.0) * 10.0
            self.a_y = round(random.randrange(520 - self.h, 480 - (510 - self.h)) / 10.0) * 10.0
            self.sn_len += 1

    def dead_snake_1(self):
        if self.x_sn >= self.w - 10 or self.x_sn < 690 - self.w or self.y_sn >= self.h - 10 or self.y_sn < 490 - self.h:
            return 1

    def dead_snake_2(self):
        if len(self.snake_List) > self.sn_len:
            del self.snake_List[0]

    def dead_snake_3(self):
        for x in self.snake_List[:-1]:
            if x == self.snake_Head:
                return 1

    def apple_x(self):
        return self.a_x

    def apple_y(self):
        return self.a_y


class Snake_Two(Snake):
    def reload(self):
        self.sn_len = 5
        self.y_ch = -10
        self.x_sn = 580
        self.y_sn = 380
        self.snake_List = []

    def gen_snake(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, (255, 0, 0), [x[0], x[1], sn_har, sn_har])

    def return_list(self):
        return self.snake_List

    def update_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if self.proshl_hod[0] != -sn_har or self.proshl_hod[1] != 0:
                        self.x_ch = -sn_har
                        self.y_ch = 0
                elif event.key == pygame.K_d:
                    if self.proshl_hod[0] != sn_har or self.proshl_hod[1] != 0:
                        self.x_ch = sn_har
                        self.y_ch = 0
                elif event.key == pygame.K_w:
                    if self.proshl_hod[0] != 0 or self.proshl_hod[1] != -sn_har:
                        self.x_ch = 0
                        self.y_ch = -sn_har
                elif event.key == pygame.K_s:
                    if self.proshl_hod[0] != 0 or self.proshl_hod[1] != sn_har:
                        self.x_ch = 0
                        self.y_ch = sn_har
        self.proshl_hod.clear()
        self.proshl_hod.append(self.x_ch * -1)
        self.proshl_hod.append(self.y_ch * -1)




class Level:
    def __init__(self):
        self.kon_mode = open_mode('mode.json', chose_mode)
        self.kon = [i for i in self.kon_mode[0].values()]
        self.w = self.kon[0]
        self.h = self.kon[1]
        self.sn = self.kon[2]
        self.bon = self.kon[4]
        self.appl = self.kon[6]
        self.tp = self.kon[5]
        self.zone = self.kon[7]

    def generate_level(self):
        if self.tp == 0:
            razn_x = (70 - self.w) * 10
            razn_y = (50 - self.h) * 10
            pygame.draw.rect(screen, (255, 255, 255), [0, 490 - razn_y, 700, 500])
            pygame.draw.rect(screen, (255, 255, 255), [0, 0, 10 + razn_x, 500])
            pygame.draw.rect(screen, (255, 255, 255), [690 - razn_x, 0, 700, 500])
            pygame.draw.rect(screen, (255, 255, 255), [0, 0, 700, 10 + razn_y])

    def cord_x(self):
        return self.w * 10

    def cord_y(self):
        return self.h * 10

    def your_score(self, len):
        value = pygame.font.SysFont('arialblack', 34).render("Your Score: " + str(int(len) + 1), True, (255, 255, 0))
        screen.blit(value, [11, 0])

    def draw_apple(self, a_x, a_y):
        if self.appl == 1:
            pygame.draw.rect(screen, (255, 0, 0), [a_x, a_y, sn_har, sn_har])



def open_mode(mode, chose_mode):
    with open(mode) as _file:
        data = json.load(_file)
    for key, value in data.items():
        if key == chose_mode:
            kon_mode = value.copy()
            return kon_mode


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


def last_win(_len):
    _font = pygame.font.SysFont('arialblack', 42)
    value = _font.render("Конечный рекорд: " + str(int(_len) + 2), True, (21, 107, 13))
    screen.blit(value, [100, 300])


def start_screen():
    mode = 1
    with open('data/score.txt', mode="r", encoding='utf8') as lol:
        scoree = lol.read()
    intro_text = [f'Ваш максимальный рекорд: {int(scoree) - 1}', "Для выбора режима - введите его номер", "1 - Default Mode",
                  "2 - Hard Mode",
                  "3 - Mode With Teleportation",
                  "4 - Mode With Bonus",
                  "5 - Two Snake Mode",
                  "6 - Mode Fight",
                  "Для того чтобы играть нажмите 'Space'"]

    fon = pygame.transform.scale(load_image('nach.jpg'), (WIDTH, HEIGHT))
    font = pygame.font.SysFont('arialblack', 20)
    font_2 = pygame.font.SysFont('arialblack', 22)
    run = True
    while run:
        i = 0
        text_coord = 70
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = 1
                elif event.key == pygame.K_2:
                    mode = 2
                elif event.key == pygame.K_3:
                    mode = 3
                elif event.key == pygame.K_4:
                    mode = 4
                elif event.key == pygame.K_5:
                    mode = 5
                elif event.key == pygame.K_6:
                    mode = 6
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    with open('data/mode.txt', mode="w") as lol:
                        lol.write(str(mode))
                    run = False
        for line in intro_text:
            i += 1
            if i == mode + 2:
                string_rendered = font_2.render(line, True, (140, 70, 86))
            else:
                string_rendered = font.render(line, True, (150, 150, 150))
            intro_rect = string_rendered.get_rect()
            text_coord += 6
            intro_rect.top = text_coord
            intro_rect.x = 18
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        clock.tick(20)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


if __name__ == '__main__':

    pygame.init()
    WIDTH = 700
    HEIGHT = 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('SneakySnake')
    clock = pygame.time.Clock()

    fons = ['fon_1.jpg', 'fon_2.png', 'fon_3.jpg']
    fon_game = pygame.transform.scale(load_image(random.choice(fons)), (WIDTH, HEIGHT))
    dead_screen = pygame.transform.scale(load_image('dead_screen.jpg'), (WIDTH, HEIGHT))
    sn_har = 10

    running = True
    cont = False

    start_screen()
    modes = ['mode_def', 'mode_hard', 'mode_tp', 'mode_bonus', 'mode_double', 'mode_fight']
    with open('data/mode.txt', mode="r") as lol:
        mod = lol.read()
    chose_mode = modes[int(mod) - 1]
    lev = Level()
    sn = Snake()
    sn2 = Snake_Two()
    sn.chose_snake()
    sn2.reload()
    while running:
        while cont == True:
            sn_len = sn.return_len()
            screen.blit(dead_screen, (0, 0))
            last_win(sn_len - 2)
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
        if sn.get_snake() == 2:
            sn2.update_event()

        if sn.update_event() == 1:
            running = False

        if sn.dead_snake_1() == 1:
            cont = True

        screen.blit(fon_game, (0, 0))

        sn.dead_snake_2()
        if sn.dead_snake_3() == 1:
            cont = True

        sn.snake_update()
        if sn.get_snake() == 2:
            sn2.snake_update()
        sn.gen_snake(sn.return_list())
        if sn.get_snake() == 2:
            sn2.gen_snake(sn.return_list())
        sn.eat_apple()
        lev.draw_apple(sn.apple_x(), sn.apple_y())

        lev.generate_level()
        lev.your_score(sn.return_len() - 1)

        pygame.display.update()
        fps = sn.get_speed()
        clock.tick(fps)

    pygame.quit()
