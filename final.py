import pygame
import sys
import os
import random
import os.path
import pickle


class Highscores():
    def write(self, level, score):
        'Writes the scores data and exports it to scorefile'
        scorefile = open("scorefile.pkl", "rb")
        highscores = pickle.load(scorefile)
        scorefile.close()
        scorefile = open("scorefile.pkl", "wb")
        if level == "easy" and score > highscores["Easy"]:
                highscores["Easy"] = score
        elif level == "medium" and score > highscores["Medium"]:
                highscores["Medium"] = score
        elif level == "hard" and score > highscores["Hard"]:
                highscores["Hard"] = score
        pickle.dump(highscores, scorefile)
        scorefile.close()

    def read(self):
        'Reads the scores data from the scorefile and assigns the highscores to \
        levels'
        scorefile = open("scorefile.pkl", "rb")
        highscores = pickle.load(scorefile)
        scorefile.close()
        return highscores


class MainMenu:
    def __init__(self):
        self.selection = 1
        self.sound = "on"
        self.text_x = 180
        self.text_y = 280
        self.step = 70
        self.text_snake = font_gigantic.render('snake', True, black)
        self.text_snake_box = self.text_snake.get_rect()
        self.text_snake_box.center = (window_width / 2, 130)
        self.image_button_x = pygame.image.load("button_x.png")

    def draw(self):
        'Draws the menu screen'
        if self.selection == 1:
            self.text_play = font_medium.render('Play', True, red)
        else:
            self.text_play = font_medium.render('Play', True, black)
        self.text_play_box = self.text_play.get_rect()
        self.text_play_box = (self.text_x, self.text_y)
        if self.selection == 2:
            self.text_hof = font_medium.render('Hall of fame', True, red)
        else:
            self.text_hof = font_medium.render('Hall of fame', True, black)
        self.text_hof_box = self.text_hof.get_rect()
        self.text_hof_box = (self.text_x, self.text_y + self.step)
        if self.selection == 3:
            self.text_quit = font_medium.render('Quit', True, red)
        else:
            self.text_quit = font_medium.render('Quit', True, black)
        self.text_quit_box = self.text_quit.get_rect()
        self.text_quit_box = (self.text_x, self.text_y + 2 * self.step)
        window.fill(snakegreen)
        pygame.draw.line(window, black, line_point3, line_point4, 10)
        pygame.draw.polygon(window, black, [polygon_point1, polygon_point2,
                            polygon_point5, polygon_point6], 10)
        window.blit(self.text_snake, self.text_snake_box)
        window.blit(self.text_play, self.text_play_box)
        window.blit(self.text_hof, self.text_hof_box)
        window.blit(self.text_quit, self.text_quit_box)
        if self.sound == "on":
            text_soundon = font_small.render('Sound on', True, black)
            text_soundon_box = text_soundon.get_rect()
            text_soundon_box.center = (window_width - 100, window_height - 50)
            window.blit(text_soundon, text_soundon_box)
        elif self.sound == "off":
            text_soundoff = font_small.render('Sound off', True, black)
            text_soundoff_box = text_soundoff.get_rect()
            text_soundoff_box.center = (window_width - 100, window_height - 50)
            window.blit(text_soundoff, text_soundoff_box)
        window.blit(self.image_button_x,
                    (window_width - 200, window_height - 60))
        pygame.display.flip()

    def run(self):
        'Runs the MainMenu screen code'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.selection == 1:
                            self.selection = 3
                        else:
                            self.selection -= 1
                    if event.key == pygame.K_DOWN:
                        if self.selection == 3:
                            self.selection = 1
                        else:
                            self.selection += 1
                    if event.key == pygame.K_RETURN:
                        if self.selection == 1:
                            LevelsMenu(self.sound).run()
                            self.selection = 1
                        elif self.selection == 2:
                            HallOfFame().run()
                            self.selection = 1
                        elif self.selection == 3:
                            sys.exit()
                    if event.key == pygame.K_x:
                        if self.sound == "on":
                            self.sound = "off"
                        elif self.sound == "off":
                            self.sound = "on"
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
            self.draw()


class LevelsMenu:
    def __init__(self, sound):
        self.sound = sound
        self.selection = 1
        self.text_levels = font_gigantic.render('level', True, black)
        self.text_levels_box = self.text_levels.get_rect()
        self.text_levels_box.center = (window_width / 2, 130)
        self.text_easy_box = (250, 280)
        self.text_medium_box = (250, 350)
        self.text_hard_box = (250, 420)
        self.text_back = font_small.render('Back to menu', True, black)
        self.text_back_box = self.text_back.get_rect()
        self.text_back_box.center = (window_width / 2 + 70, 630)

    def draw(self):
        'Draws the levels selection screen'
        if self.selection == 1:
            text_easy = font_medium.render('Easy', True, red)
        else:
            text_easy = font_medium.render('Easy', True, black)
        if self.selection == 2:
            text_medium = font_medium.render('Medium', True, red)
        else:
            text_medium = font_medium.render('Medium', True, black)
        if self.selection == 3:
            text_hard = font_medium.render('Hard', True, red)
        else:
            text_hard = font_medium.render('Hard', True, black)

        window.fill(snakegreen)
        pygame.draw.line(window, black, line_point3, line_point4, 10)
        pygame.draw.polygon(window, black, [polygon_point1, polygon_point2,
                            polygon_point5, polygon_point6], 10)
        window.blit(self.text_levels, self.text_levels_box)
        window.blit(text_easy, self.text_easy_box)
        window.blit(text_medium, self.text_medium_box)
        window.blit(text_hard, self.text_hard_box)
        window.blit(self.text_back, self.text_back_box)
        window.blit(image_button_back, (225, 605))
        pygame.display.flip()

    def run(self):
        'Runs the Levels screen code'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.selection == 1:
                            self.selection = 3
                        else:
                            self.selection -= 1
                    if event.key == pygame.K_DOWN:
                        if self.selection == 3:
                            self.selection = 1
                        else:
                            self.selection += 1
                    if event.key == pygame.K_RETURN:
                        if self.selection == 1:
                            level = "easy"
                            Game(level, self.sound).run()
                        if self.selection == 2:
                            level = "medium"
                            Game(level, self.sound).run()
                        if self.selection == 3:
                            level = "hard"
                            Game(level, self.sound).run()
                    if event.key == pygame.K_BACKSPACE:
                        self.selection = 1
                        MainMenu().run()
            self.draw()


class HallOfFame:
    def __init__(self):
        self.text_hof1 = font_large.render('Hall', True, black)
        self.text_hof1_box = self.text_hof1.get_rect()
        self.text_hof1_box.center = (window_width / 2, 70)
        self.text_hof2 = font_big.render('of fame', True, black)
        self.text_hof2_box = self.text_hof2.get_rect()
        self.text_hof2_box.center = (window_width / 2, 150)
        self.text_back = font_small.render('Back to menu', True, black)
        self.text_back_box = self.text_back.get_rect()
        self.text_back_box.center = (window_width / 2 + 70, 630)

    def draw(self):
        'Draws the hall of fame screen displaying the highscores'
        window.fill(snakegreen)
        pygame.draw.line(window, black, line_point3, line_point4, 10)
        pygame.draw.polygon(window, black, [polygon_point1, polygon_point2,
                            polygon_point5, polygon_point6], 10)
        window.blit(self.text_hof1, self.text_hof1_box)
        window.blit(self.text_hof2, self.text_hof2_box)
        text_hof_easy = \
            font_medium.render("Easy: " + str(self.highscores["Easy"]) +
                               " points", True, black)
        text_hof_easy_box = text_hof_easy.get_rect()
        text_hof_easy_box.center = (window_width / 2, 300)
        text_hof_medium = \
            font_medium.render("Medium: " + str(self.highscores["Medium"]) +
                               " points", True, black)
        text_hof_medium_box = text_hof_medium.get_rect()
        text_hof_medium_box.center = (window_width / 2, 350)
        text_hof_hard = \
            font_medium.render("Hard: " + str(self.highscores["Hard"]) +
                               " points", True, black)
        text_hof_hard_box = text_hof_hard.get_rect()
        text_hof_hard_box.center = (window_width / 2, 400)
        window.blit(text_hof_easy, text_hof_easy_box)
        window.blit(text_hof_medium, text_hof_medium_box)
        window.blit(text_hof_hard, text_hof_hard_box)
        window.blit(self.text_back, self.text_back_box)
        window.blit(image_button_back, (225, 605))
        pygame.display.flip()

    def run(self):
        'Runs HallOfFame screen code'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN \
                            or event.key == pygame.K_BACKSPACE:
                        MainMenu().run()
            self.highscores = Highscores().read()
            self.draw()


class Game:
    def __init__(self, level, sound):
        self.sound_eat = pygame.mixer.Sound("pickup.wav")
        self.sound_gameover = pygame.mixer.Sound("gameover.wav")
        self.level = level
        self.sound = sound
        self.image_checkerboard_easy = \
            pygame.image.load("checkerboard_easy.png")
        self.image_checkerboard_medium = \
            pygame.image.load("checkerboard_medium.png")
        self.image_checkerboard_hard = \
            pygame.image.load("checkerboard_hard.png")
        self.direction = "right"
        self.snake_xy = [300, 400]
        self.snakelist = [[300, 400], [280, 400], [260, 400]]
        self.counter = 0
        self.score_position = (45, 45)
        self.foodonscreen = 0
        self.growsnake = 0
        self.snakegrowunit = 2
        if self.level == "easy":
            self.grid_size = 30
            # easy level requires slightly different dimensions
            self.snake_xy = [300, 390]
            self.snakelist = [[300, 400], [270, 400], [240, 400]]
            self.gamespeed = 14
        elif self.level == "medium":
            self.grid_size = 20
            self.gamespeed = 11
        elif self.level == "hard":
            self.grid_size = 10
            self.gamespeed = 8
        self.gameregulator = self.gamespeed
        self.score = 0
        self.block_size = [self.grid_size, self.grid_size]
        self.countdown()

    def countdown(self):
        'Draws the countdown screen'
        text_countdown1 = font_medium.render('Get ready', True, black)
        text_countdown1_box = text_countdown1.get_rect()
        text_countdown1_box.center = \
            (window_width / 2, window_height / 2 - 100)
        for i in range(3, -1, -1):
            window.fill(snakegreen)
            pygame.draw.polygon(window, black, [polygon_point1, polygon_point2,
                                polygon_point5, polygon_point6], 10)
            window.blit(text_countdown1, text_countdown1_box)
            if i == 0:
                text_countdown2 = font_gigantic.render(str(i), True, red)
            else:
                text_countdown2 = font_gigantic.render(str(i), True, black)
            text_countdown2_box = text_countdown2.get_rect()
            text_countdown2_box.center = (window_width / 2, window_height / 2)
            window.blit(text_countdown2, text_countdown2_box)
            pygame.display.flip()
            pygame.time.delay(1000)

    def draw(self):
        'Draws the game screen consisting of two surfaces'
        window.fill(snakegreen)
        pygame.draw.polygon(window, black, [polygon_point1, polygon_point2,
                            polygon_point3, polygon_point4], 10)
        window.blit(arena, (polygon_point3[0] + 6, polygon_point3[1] + 6))
        if self.level == "easy":
            arena.blit(self.image_checkerboard_easy, (0, 0))
        elif self.level == "medium":
            arena.blit(self.image_checkerboard_medium, (0, 0))
        elif self.level == "hard":
            arena.blit(self.image_checkerboard_hard, (0, 0))
        pygame.draw.line(window, black, line_point1, line_point2, 10)
        text_score = font_large.render(str(self.score), True, black)
        text_score_box = text_score.get_rect()
        text_score_box.center = self.score_position
        text_score = font_large.render(str(self.score), True, black)
        window.blit(text_score, text_score_box)
        for element in self.snakelist:
            pygame.draw.rect(arena, black,
                             pygame.Rect(element, self.block_size))
        pygame.draw.rect(arena, red,
                         pygame.Rect(self.food_xy, self.block_size))
        pygame.display.flip()

    def pause(self):
        'Draws the pause screen appearing when ESC is pressed in-game'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run()
                    if event.key == pygame.K_BACKSPACE:
                        MainMenu().run()
            text_pause = font_large.render('Paused', True, red)
            text_pause_box = text_pause.get_rect()
            text_pause_box.center = (window_width / 2, window_height / 2)
            window.blit(text_pause, text_pause_box)
            pygame.display.flip()

    def gameover(self):
        'Draws the gameover layer over the current game situation'
        text_gameover = font_big.render('Game over', True, red)
        text_gameover_box = text_gameover.get_rect()
        text_gameover_box.center = (window_width / 2, window_height / 2)
        window.blit(text_gameover, text_gameover_box)
        pygame.display.flip()
        pygame.time.delay(1000)

    def key_detect(self):
        'Detects the arrows keys pressed and returns a tuple with them'
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            direct = "left"
            return direct
        elif pressed_keys[pygame.K_RIGHT]:
            direct = "right"
            return direct
        elif pressed_keys[pygame.K_UP]:
            direct = "up"
            return direct
        elif pressed_keys[pygame.K_DOWN]:
            direct = "down"
            return direct

    def run(self):
        'Runs the actual Game code'
        while True:
            self.block_size = [self.grid_size, self.grid_size]
            self.clock = pygame.time.Clock()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()

            self.newdirection = self.key_detect()

            if self.gameregulator == self.gamespeed:
                if self.newdirection == "left" \
                        and not self.direction == "right":
                    self.direction = self.newdirection
                elif self.newdirection == "right" \
                        and not self.direction == "left":
                    self.direction = self.newdirection
                elif self.newdirection == "up" \
                        and not self.direction == "down":
                    self.direction = self.newdirection
                elif self.newdirection == "down" \
                        and not self.direction == "up":
                    self.direction = self.newdirection
                # the actual movement of the snake
                if self.direction == "right":
                    self.snake_xy[0] = self.snake_xy[0] + self.grid_size
                elif self.direction == "left":
                    self.snake_xy[0] = self.snake_xy[0] - self.grid_size
                elif self.direction == "up":
                    self.snake_xy[1] = self.snake_xy[1] - self.grid_size
                elif self.direction == "down":
                    self.snake_xy[1] = self.snake_xy[1] + self.grid_size
                # crossing border
                if self.snake_xy[0] > arena_width or self.snake_xy[0] < 0 \
                        or self.snake_xy[1] < -self.grid_size \
                        or self.snake_xy[1] > arena_heigth:
                    if self.sound == "on":
                        self.sound_gameover.play()
                    self.gameover()
                    Gameover(self.level, self.score).run()
                # eating self
                if len(self.snakelist) > 3\
                        and self.snakelist.count(self.snake_xy) > 0:
                    if self.sound == "on":
                        self.sound_gameover.play()
                    self.gameover()
                    Gameover(self.level, self.score).run()
                # spawning food
                while self.foodonscreen == 0:
                    self.food_x = \
                        random.randrange(0, int(arena_width / self.grid_size))
                    self.food_y = \
                        random.randrange(0, int(arena_heigth / self.grid_size))
                    self.food_xy = [int(self.food_x * self.grid_size),
                                    int(self.food_y * self.grid_size)]
                    if not self.snakelist.count(self.food_xy) == 0:
                        continue
                    self.foodonscreen = 1
                self.snakelist.insert(0, list(self.snake_xy))
                # eating
                if self.snake_xy[0] == self.food_xy[0] \
                        and self.snake_xy[1] == self.food_xy[1]:
                    if self.sound == "on":
                        self.sound_eat.play()
                    self.foodonscreen = 0
                    self.score = self.score + 1
                    self.growsnake = self.growsnake + 1
                elif self.growsnake > 0:
                    self.growsnake = self.growsnake + 1
                    if self.growsnake == self.snakegrowunit:
                        self.growsnake = 0
                else:
                    self.snakelist.pop()  # making the snake tail move properly
                self.gameregulator = 0
            self.gameregulator += 1
            self.draw()
            self.clock.tick(120)


class Gameover:
    def __init__(self, level, score):
        self.level = level
        self.score = score
        self.selection = 1
        self.text_gameover2 = font_big.render('Game over', True, black)
        self.text_gameover2_box = self.text_gameover2.get_rect()
        self.text_gameover2_box.center = (window_width / 2, 100)

    def draw(self):
        'Draws the Gameover screen with the score displayed'
        text_youscored = font_small.render('You scored ' + str(self.score) +
                                           ' points', True, black)
        text_youscored_box = text_youscored.get_rect()
        text_youscored_box.center = (window_width / 2, 180)

        if self.selection == 1:
            text_gameover_menu = font_medium.render('Menu', True, red)
        else:
            text_gameover_menu = font_medium.render('Menu', True, black)
        text_gameover_menu_box = text_gameover_menu.get_rect()
        text_gameover_menu_box.center = (window_width / 2, 295)

        if self.selection == 2:
            text_gameover_quit = font_medium.render('quit', True, red)
        else:
            text_gameover_quit = font_medium.render('quit', True, black)
        text_gameover_quit_box = text_gameover_quit.get_rect()
        text_gameover_quit_box.center = (window_width / 2, 365)
        window.fill(snakegreen)
        pygame.draw.line(window, black, line_point3, line_point4, 10)
        pygame.draw.polygon(window, black, [polygon_point1, polygon_point2,
                            polygon_point5, polygon_point6], 10)
        window.blit(self.text_gameover2, self.text_gameover2_box)

        window.blit(text_youscored, text_youscored_box)
        window.blit(text_gameover_menu, text_gameover_menu_box)
        window.blit(text_gameover_quit, text_gameover_quit_box)
        pygame.display.flip()

    def run(self):
        'Runs Gameover screen code'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.selection == 1:
                            self.selection = 2
                        else:
                            self.selection -= 1
                    if event.key == pygame.K_DOWN:
                        if self.selection == 2:
                            self.selection = 1
                        else:
                            self.selection += 1
                    if event.key == pygame.K_RETURN:
                        if self.selection == 1:
                            self.selection = 1
                            MainMenu().run()
                        elif self.selection == 2:
                            sys.exit()
                    if event.key == pygame.K_ESCAPE:
                        exit()
            Highscores().write(self.level, self.score)
            self.draw()


def scorefilecheck():
    'Checks whether a scorefile exists. If not, it creates one'
    if not os.path.exists("scorefile.pkl"):
        base_scores = {"Easy": 0, "Medium": 0, "Hard": 0}
        scorefile = open("scorefile.pkl", "wb")
        pickle.dump(base_scores, scorefile)
        scorefile.close()


def main():
    'Main function of the program'
    scorefilecheck()
    MainMenu().run()


# colors
black = (0, 0, 0)
white = (255, 255, 255)
snakegreen = (154, 197, 3)
red = (195, 53, 53)

# window setup
pygame.display.set_icon(pygame.image.load("icon.png"))
os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
pygame.mixer.pre_init(44100, -16, 2, 2048)  # fixing the sound delay
pygame.mixer.init()
pygame.init()
window_width = 700  # actual window parametres
window_height = 700
arena_width = 660  # arena parametres - the snake is displayed there
arena_heigth = 540
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
arena = pygame.Surface((arena_width, arena_heigth))

# text tools
pygame.font.init()
joystix_monospace = "joystix_monospace.ttf"
font_gigantic = pygame.font.Font(joystix_monospace, 150)
font_large = pygame.font.Font(joystix_monospace, 90)
font_big = pygame.font.Font(joystix_monospace, 80)
font_mediumbig = pygame.font.Font(joystix_monospace, 55)
font_medium = pygame.font.Font(joystix_monospace, 40)
font_small = pygame.font.Font(joystix_monospace, 20)

# loading media
image_button_esc = pygame.image.load("button_esc.png")
image_button_back = pygame.image.load("button_back.png")

# in-game particles coordinates
polygon_point1 = [684, 674]
polygon_point2 = [14, 674]
polygon_point3 = [14, 124]
polygon_point4 = [684, 124]
polygon_point5 = [14, 14]
polygon_point6 = [684, 14]
line_point1 = [10, 95]
line_point2 = [690, 95]
line_point3 = [40, 210]
line_point4 = [650, 210]

if __name__ == "__main__":
    main()
