import pygame
import random as rand
import time


def wait_and_do(start_t, T, func, check_func, c):
    if (int((time.time() - start_t) / T) == c) and check_func():
        func()
        # print(time.time() - start_t)
        c += 1
    return c


def rnd_coord():
    return int(100 + 750 * rand.random())


def rnd_wall_coord():
    return int(200 + 550 * rand.random())


def check_borders(x, y, walls):
    for i in walls:
        x_min = i.x - 40
        x_max = i.x + i.a + 40
        y_min = i.y - 40
        y_max = i.y + i.b + 40
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return False
    return True


def check_enemy_borders(x, y, walls):
    while not (
            check_borders(x, y, walls) and
            check_borders(x - 50, y, walls) and
            check_borders(x + 50, y, walls) and
            check_borders(x, y - 50, walls) and
            check_borders(x, y + 50, walls)):
        x = rnd_coord()
        y = rnd_coord()
    return x, y


def death(window, death_counter, my_font):
    if death_counter == 0:
        pygame.mixer.music.pause()
        death_counter += 1
        pygame.mixer.music.load("Death.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()
    pygame.draw.rect(window, 'Black', (325, 895, 350, 65))
    pygame.draw.rect(window, 'White', (330, 900, 340, 55))
    death_surface = my_font.render('SORRY, YOU DIED!', False, 'Black')
    window.blit(death_surface, (350, 900))


def win_game(window, win_counter, my_font):
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


