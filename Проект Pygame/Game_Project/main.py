import pygame
import random as rand
import time

# ИНИЦИАЛИЗАЦИЯ ИГРЫ И СОЗДАНИЕ ОКНА
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("GREAT BALLS OF FIRE")
# ДОБАВИМ ШРИФТ - я сделал вывод на экран фраз при поражении/победе
pygame.font.init()
my_font = pygame.font.SysFont('ARIAL', 40)
# ДОБАВИМ МУЗЫКУ - я добавил музыкальный фон + звуки смерти/победы
pygame.mixer.music.load("Dixie.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()


def check_borders(x, y):
    if x < 50:
        x = 50
    if x > 950:
        x = 950
    if y < 50:
        y = 50
    if y > 950:
        y = 950
        return x, y


class Player:
    def __init__(self):
        self.x, self.y = 900, 900
        self.speed = 1.5
        self.alive = True
        self.winner = False

    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > 50:
            self.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x < 950:
            self.x += self.speed
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.y > 50:
            self.y -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.y < 950:
            self.y += self.speed

    def draw(self):
        pygame.draw.circle(window, 'Blue', (self.x, self.y), 50)
        pygame.draw.circle(window, 'Yellow', (self.x, self.y), 45)

    def win(self):
        if self.x < 225 and self.y < 125:
            self.winner = True


class Enemy:
    def __init__(self, x, y):
        check_borders(x, y)
        self.x, self.y = x, y
        self.speed = 0.5

    def draw(self):
        pygame.draw.circle(window, 'Blue', (self.x, self.y), 50)
        pygame.draw.circle(window, 'Red', (self.x, self.y), 45)

    def attack(self, P):
        if self.x != P.x:
            self.x += (P.x - self.x) / abs((P.x - self.x)) * self.speed
        if self.y != P.y:
            self.y += (P.y - self.y) / abs((P.y - self.y)) * self.speed
        if ((P.x - self.x) ** 2 + (P.y - self.y) ** 2) ** 0.5 <= 95:
            P.alive = False


def rnd_coord():
    return int(100 + 750 * rand.random())


def death():
    global death_counter
    if death_counter == 0:
        pygame.mixer.music.pause()
        death_counter += 1
        pygame.mixer.music.load("Death.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()
    pygame.draw.rect(window, 'Black', (325, 895, 350, 65))
    pygame.draw.rect(window, 'White', (330, 900, 340, 55))
    death_surface = my_font.render('YOU DIED! SORRY!', False, 'Black')
    window.blit(death_surface, (350, 900))


def win_game():
    global win_counter
    if win_counter == 0:
        win_counter += 1
        pygame.mixer.music.pause()
        pygame.mixer.music.load("Victory.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

    pygame.draw.rect(window, 'Black', (240, 895, 540, 65))
    pygame.draw.rect(window, 'White', (245, 900, 530, 55))
    win_surface = my_font.render('YOU WON! CONGRATULATIONS!', False, 'Black')
    window.blit(win_surface, (250, 900))


You = Player()
Enemies = []

T = 2
death_counter = 0
win_counter = 0
enemies_counter = 1

clock = pygame.time.Clock()
start_time = time.time()
run = True

while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((255, 255, 255))
    pygame.draw.rect(window, 'Blue', (0, 0, 200, 100))
    pygame.draw.rect(window, 'Green', (5, 5, 190, 90))

    if int((time.time() - start_time) / T) == enemies_counter and You.alive and not You.winner:
        Enemies.append(Enemy(rnd_coord(), rnd_coord()))
        # print(time.time() - start_time) # МОЖНО ПРОВЕРИТЬ, ЧТО ПОЯВЛЯЮТСЯ ЧЕРЕЗ T секунд
        enemies_counter += 1

    You.draw()
    for i in Enemies:
        i.draw()

    if You.alive and not You.winner:
        You.move()
        for i in Enemies:
            i.attack(You)
        You.win()
    else:
        if not You.alive:
            death()
        else:
            win_game()
    pygame.display.update()

pygame.quit()
print("\n Company 'GameBars Studio Inc.' is not responsible for the use of music without a license from the copyright "
      "holder. \n MIPT, Dolgoprudny, Moscow region, Russian Federation, planet Earth, Milky Way galaxy.")
