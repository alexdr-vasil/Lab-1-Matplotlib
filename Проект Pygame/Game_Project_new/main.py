from classes import *


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

Background = pygame.image.load("Background.jpg")

You = Player()
Enemies = []
Walls = [Wall(rnd_wall_coord(), rnd_wall_coord()) for i in range(0, 5)]

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

    window.blit(Background, (0, 0))
    pygame.draw.rect(window, 'Blue', (0, 0, 200, 100))
    pygame.draw.rect(window, 'Green', (6, 6, 188, 88))
    finish_surface = my_font.render('FINISH', False, 'Blue')
    window.blit(finish_surface, (45, 30))

    enemies_counter = wait_and_do(start_time, T, lambda: Enemies.append(Enemy(rnd_coord(), rnd_coord(), Walls)),
                                  lambda: You.alive and not You.winner, enemies_counter)

    for i in Enemies:
        i.draw(window, my_font)
    for i in Walls:
        i.draw(window)
    You.draw(window, my_font)

    if You.alive and not You.winner:
        You.move(Walls)
        for i in Enemies:
            i.attack(You, Walls)
        You.win()
    else:
        if not You.alive:
            death(window, death_counter, my_font)
        else:
            win_game(window, win_counter, my_font)
    pygame.display.update()

pygame.quit()
print("\n Company 'GameBars Studio Inc.' is not responsible for the using of music without a license from the "
      "copyright holder. \n MIPT, Dolgoprudny, Moscow region, Russian Federation, planet Earth, Milky Way galaxy.")
