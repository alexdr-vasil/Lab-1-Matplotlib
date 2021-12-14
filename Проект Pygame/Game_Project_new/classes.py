from functions import *


class Player:
    def __init__(self):
        self.x, self.y = 900, 900
        self.speed = 1.5
        self.alive = True
        self.winner = False
        self.health = 5
        self.image = pygame.image.load("player.png")

    def move(self, walls):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > 50 and check_borders(self.x - self.speed, self.y,
                                                                                       walls):
            self.x -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x < 950 and check_borders(self.x + self.speed, self.y,
                                                                                         walls):
            self.x += self.speed
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.y > 50 and check_borders(self.x, self.y - self.speed,
                                                                                     walls):
            self.y -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.y < 950 and check_borders(self.x, self.y + self.speed,
                                                                                        walls):
            self.y += self.speed

    def draw(self, Window, my_font):
        pygame.draw.circle(Window, 'Black', (self.x, self.y), 50)
        pygame.draw.circle(Window, 'Yellow', (self.x, self.y), 45)
        # Window.blit(self.image, (self.x - 50, self.y - 50))
        # player_surface = my_font.render('player', False, 'White')
        # Window.blit(player_surface, (self.x - 44, self.y + 35))
        pygame.draw.rect(Window, 'Black', (self.x - 53, self.y - 69, 103, 13), 8)
        pygame.draw.rect(Window, 'White', (self.x - 50, self.y - 66, 100, 10))
        pygame.draw.rect(Window, 'Red', (self.x - 50, self.y - 66, int(20 * self.health), 10))

    def win(self):
        if self.x < 225 and self.y < 125:
            self.winner = True


class Enemy:
    def __init__(self, x, y, walls):
        self.image = pygame.image.load("enemy.png")
        speed = 0.3
        x, y = check_enemy_borders(x, y, walls)
        self.x, self.y = x, y
        self.speed = speed

    def draw(self, Window, font):
        pygame.draw.circle(Window, 'Black', (self.x, self.y), 50)
        pygame.draw.circle(Window, 'Red', (self.x, self.y), 45)
        # Window.blit(self.image, (self.x - 50, self.y - 50))
        # enemy_surface = font.render('enemy', False, 'White')
        # Window.blit(enemy_surface, (self.x - 48, self.y + 35))

    def attack(self, P, walls):
        if self.x != P.x:
            if (P.x - self.x) > 0:
                dx = self.speed
            else:
                dx = -self.speed
            if check_borders(self.x + dx, self.y, walls):
                self.x += dx
        if self.y != P.y:
            dy = (P.y - self.y) / abs((P.y - self.y)) * self.speed
            if check_borders(self.x, self.y + dy, walls):
                self.y += dy
        if ((P.x - self.x) ** 2 + (P.y - self.y) ** 2) ** 0.5 <= 90:
            if P.health > 0:
                P.health -= 1 / 60
                # print(P.health)
            else:
                P.alive = False


class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        a = 100
        b = 200
        if rand.random() > 0.5:
            t = a
            a = b
            b = t
        self.a = a
        self.b = b

    def draw(self, window):
        pygame.draw.rect(window, 'Black', (self.x, self.y, self.a, self.b))
        pygame.draw.rect(window, (100, 100, 100), (self.x + 8, self.y + 8, self.a - 15, self.b - 15))
