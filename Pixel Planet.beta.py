import pygame
import sys
import random
import math


###cderwb dfbu dfesbu feduo ef
# hbi dfrgbh bufgrj ubofjbuhj evdfujuhjvdfnujhknvfdugfvbhujdfk uvf hbdkjvnbhfvcf nkfgmjvhcrb mfcrhjkefbmecrkjhvfbn3chbvnemfvjhercnmvfjhrcenmgvbhrj ngmmvmfmvrfjrvcmevlngufvrckemlvtng jiuvkr ctlfnjgiufkvrcenvg ubck evfgukvrcmngkrc vgbgvrcf rmvbvgkrcf fcm vbvgfcmkvgb
# fcm gnbvgfcmgvnb vgfmcgvnmbgmf vbnjcdhkbcejbhj sbhi
def game():
    # Initialize the Pygame
    pygame.init()
    # life line
    ESLN = True
    cirim = pygame.image.load('The cir.png')
    cirim = pygame.transform.scale_by(cirim, 5)
    ydg = False
    flag = True

    ITPAS = [True]
    h = 0
    # exp
    explosion = False
    counter = 0
    exp1 = pygame.image.load('exp1.png')
    exp2 = pygame.image.load('exp2.png')
    exp3 = pygame.image.load('exp3.png')
    exp4 = pygame.image.load('exp4.png')
    exp5 = pygame.image.load('exp5.png')
    conter = 0

    # enemy thingy
    # Basic Space ship
    class enemy_spaceship:
        def __init__(self):
            self.name = "Basic"
            self.ex = random.randrange(10, 1490)
            self.ey = random.randrange(10, 200)
            self.counter = 0
            self.window = window
            self.crash_sound = crash_sound
            self.rip_sound = rip_sound
            self.Δx = 1000
            self.Δy = 1000
            self.speed = random.uniform(0.0008, 0.0012)
            self.dying = False
            self.dead = False

        # Wat the guy will look like before his death

        def YPD(self):
            if self.dying == True:
                self.explode()
                return
            pygame.draw.polygon(self.window, (120, 120, 120), [(self.ex, self.ey), (self.ex + 100, self.ey - 200),
                                                               (self.ex, self.ey - 130), (self.ex - 100, self.ey - 200),
                                                               (self.ex, self.ey)])

        # How he just runs to his death
        def MTMD(self, shx, shy):

            if self.dying == True:
                return
            self.Δx = self.ex - shx
            self.Δy = self.ey - shy
            self.ex = self.ex + (self.Δx * -self.speed) + random.uniform(-1, 1)
            self.ey = self.ey + (self.Δy * -self.speed) + random.uniform(-1, 1)

            if self.Δy < 5 and self.Δy > -5 and self.Δx < 10 and self.Δx > -10:
                ITPAS.append(False)

        # How he will face death
        def explode(self):

            if self.dead == True:
                return
            self.dying = True
            self.counter = self.counter + 1
            if self.counter < 20:
                window.blit(exp1, (self.ex - 35, self.ey - 40))
            elif self.counter < 40:
                window.blit(exp2, (self.ex - 35, self.ey - 40))
            elif self.counter < 60:
                window.blit(exp3, (self.ex - 35, self.ey - 40))
            elif self.counter < 80:
                window.blit(exp4, (self.ex - 35, self.ey - 40))
            elif self.counter < 100:
                window.blit(exp5, (self.ex - 35, self.ey - 40))
                self.dead = True

    class asena:
        def __init__(self):
            self.name = "asena"
            self.ex = random.randrange(10, 1490)
            self.ey = random.randrange(10, 200)
            self.counter = 0
            self.window = window
            self.crash_sound = crash_sound
            self.rip_sound = rip_sound
            self.Δx = 1000
            self.Δy = 1000
            self.speed = random.uniform(0.004, 0.008)
            self.dying = False
            self.dead = False
            self.colour = 200

        # Wat the guy will look like before his death
        def YPD(self):
            if self.dying == True:
                self.explode()
                return
            if self.colour > 30:
                self.colour -= 0.1
            pygame.draw.polygon(self.window, (1, 1, int(self.colour)),
                                [(self.ex, self.ey), (self.ex + 1, self.ey - 2),
                                 (self.ex, self.ey - 1.3), (self.ex - 1, self.ey - 2),
                                 (self.ex, self.ey)])

        # How he just runs to his death
        def MTMD(self, shx, shy):

            if self.dying == True:
                return
            self.Δx = self.ex - shx
            self.Δy = self.ey - shy
            self.ex = self.ex + (self.Δx * -self.speed) + random.uniform(-1, 1)
            self.ey = self.ey + (self.Δy * -self.speed) + random.uniform(-1, 1)

            if self.Δy < 5 and self.Δy > -5 and self.Δx < 10 and self.Δx > -10:
                ITPAS.append(False)

        # How he will face death
        def explode(self):

            if self.dead == True:
                return
            self.dying = True
            self.counter = self.counter + 1
            if self.counter < 20:
                window.blit(exp1, (self.ex - 35, self.ey - 40))
            elif self.counter < 40:
                window.blit(exp2, (self.ex - 35, self.ey - 40))
            elif self.counter < 60:
                window.blit(exp3, (self.ex - 35, self.ey - 40))
            elif self.counter < 80:
                window.blit(exp4, (self.ex - 35, self.ey - 40))
            elif self.counter < 100:
                window.blit(exp5, (self.ex - 35, self.ey - 40))
                self.dead = True

    # This enemy bonces of the sides
    class BONKY_boi:
        def __init__(self):
            self.name = "bonky"
            self.ex = random.randrange(10, 1490)
            self.ey = random.randrange(10, 200)
            self.counter = 0  # Time tracker
            self.window = window
            self.crash_sound = crash_sound
            self.rip_sound = rip_sound
            self.Δx = 1000
            self.Δy = 1000
            # Change below for speed
            self.speed = random.uniform(1, 2)
            self.xs = random.uniform(-1, 1)
            self.ys = random.uniform(-1, 1)
            # Change above for speed
            self.dying = False
            self.dead = False

        # How enemy looks
        def YPD(self):
            if self.dying == True:
                self.explode()
                return

            pygame.draw.polygon(self.window, (0, 255, 0), [(self.ex, self.ey), (self.ex + 100, self.ey - 200),
                                                           (self.ex, self.ey - 130), (self.ex - 100, self.ey - 200),
                                                           (self.ex, self.ey)])

        # Movement includes chages from all speeds when bonces off Wall
        def MTMD(self, shx, shy):

            if self.dying == True:
                return
            self.Δx = self.ex - shx
            self.Δy = self.ey - shy
            self.ex = self.ex + self.xs * self.speed
            self.ey = self.ey + self.ys * self.speed

            if self.ex < 5 and self.xs < 0:
                self.xs = -self.xs

            if self.ex > 1495 and self.xs > 0:
                self.xs = -self.xs

            if self.ey > 595 and self.ys > 0:
                self.ys = -self.ys

            if self.ey < 5 and self.ys < 0:
                self.ys = -self.ys

            if self.Δy < 50 and self.Δy > -50 and self.Δx < 100 and self.Δx > -100:
                ITPAS.append(False)

        # The rare death
        def explode(self):

            if self.dead == True:
                return
            self.dying = True
            self.counter = self.counter + 1
            if self.counter < 20:
                window.blit(exp1, (self.ex - 35, self.ey - 40))
            elif self.counter < 40:
                window.blit(exp2, (self.ex - 35, self.ey - 40))
            elif self.counter < 60:
                window.blit(exp3, (self.ex - 35, self.ey - 40))
            elif self.counter < 80:
                window.blit(exp4, (self.ex - 35, self.ey - 40))
            elif self.counter < 100:
                window.blit(exp5, (self.ex - 35, self.ey - 40))
                self.dead = True

    # Diangle death his name can really stand out btw
    class DD:
        def __init__(self):
            self.name = "DD"
            self.ex = random.randrange(10, 1490)
            self.ey = random.randrange(10, 200)
            self.counter = 0
            self.window = window
            self.crash_sound = crash_sound
            self.rip_sound = rip_sound
            self.Δx = 0
            self.Δy = 0
            self.speed = random.uniform(0.1, 1)
            self.dying = False
            self.dead = False
            self.queue_x = [0 for _ in range(100)]
            self.queue_y = [0 for _ in range(100)]

        # This is his details similer to other ships.
        def YPD(self):
            if self.dying == True:
                self.explode()
                return
            pygame.draw.polygon(self.window, (200, 0, 0), [(self.ex, self.ey), (self.ex + 10, self.ey - 20),
                                                           (self.ex, self.ey - 13), (self.ex - 10, self.ey - 20),
                                                           (self.ex, self.ey)])

        # Movement includes only moving in diangle direction
        def MTMD(self, shx, shy):
            if self.dying == True:
                return
            # Create a queue to delay X Y values

            self.queue_x.append(self.ex - shx)
            self.queue_y.append(self.ey - shy)
            # Grab the old X Y position values
            self.Δx = self.queue_x.pop(0)
            self.Δy = self.queue_y.pop(0)
            if self.Δy < 0 and self.Δx > 3:
                self.ex -= self.speed
                self.ey += 0.5 * self.speed
            if self.Δy < 0 and self.Δx < -3:
                self.ex += self.speed
                self.ey += 0.5 * self.speed
            if self.Δy > 0 and self.Δx > 3:
                self.ex -= self.speed
                self.ey -= 0.5 * self.speed
            if self.Δy > 0 and self.Δx < -3:
                self.ex += self.speed
                self.ey -= 0.5 * self.speed
            if self.Δy == 0:
                self.ex = self.ex + (self.Δx * -self.speed) + random.uniform(-1, 1)
                self.ey = self.ey + (self.Δy * -self.speed) + random.uniform(-1, 1)

            self.Δx = self.ex - shx
            self.Δy = self.ey - shy

            if self.Δy < 5 and self.Δy > -5 and self.Δx < 10 and self.Δx > -10:
                ITPAS.append(False)

        # same as others
        def explode(self):

            if self.dead == True:
                return
            self.dying = True
            self.counter = self.counter + 1
            if self.counter < 20:
                window.blit(exp1, (self.ex - 35, self.ey - 40))
            elif self.counter < 40:
                window.blit(exp2, (self.ex - 35, self.ey - 40))
            elif self.counter < 60:
                window.blit(exp3, (self.ex - 35, self.ey - 40))
            elif self.counter < 80:
                window.blit(exp4, (self.ex - 35, self.ey - 40))
            elif self.counter < 100:
                window.blit(exp5, (self.ex - 35, self.ey - 40))
                self.dead = True

    # Made for moving in a circle... and thats it.
    class The_Cir:
        def __init__(self):
            self.size = 100
            self.angle = 0
            self.name = "The Cir"
            self.ex = random.randrange(20, 1470)
            self.ey = random.randrange(30, 200)
            self.center = (self.ex, self.ey)
            self.counter = 0
            self.window = window
            self.crash_sound = crash_sound
            self.rip_sound = rip_sound
            self.Δx = 0
            self.Δy = 0
            self.speed = random.uniform(0.005, 0.007)
            self.dying = False
            self.dead = False

        # The only ship that looks diffrent from others.
        def YPD(self):
            if self.dying == True:
                self.explode()
                return
            window.blit(cirim, (self.ex - 70, self.ey - 70))

        # Apprently this is "bassic" code to get something moving in a circle
        def MTMD(self, shx, shy):
            if self.dying == True:
                return
            self.Δx = self.ex - shx
            self.Δy = self.ey - shy

            self.center = (self.center[0] - self.Δx * self.speed * 0.06, self.center[1] - self.Δy * self.speed * 0.06)

            self.angle = (self.angle + self.speed) % (2 * 3.14)
            self.ex = self.center[0] + self.size * math.cos(self.angle) + random.uniform(-1, 1)
            self.ey = self.center[1] + self.size * math.sin(self.angle) + random.uniform(-1, 1)

            if self.Δy < 15 and self.Δy > -15 and self.Δx < 40 and self.Δx > -40:
                ITPAS.append(False)

            # good i spare
            # Ignore that ^ Totally wasnt going to turn ship into comment

        # He dead
        def explode(self):

            if self.dead == True:
                return
            self.dying = True
            self.counter = self.counter + 1
            if self.counter < 20:
                window.blit(exp1, (self.ex - 35, self.ey - 40))
            elif self.counter < 40:
                window.blit(exp2, (self.ex - 35, self.ey - 40))
            elif self.counter < 60:
                window.blit(exp3, (self.ex - 35, self.ey - 40))
            elif self.counter < 80:
                window.blit(exp4, (self.ex - 35, self.ey - 40))
            elif self.counter < 100:
                window.blit(exp5, (self.ex - 35, self.ey - 40))
                self.dead = True

    # Set the size of the display window
    window_size = (1500, 600)
    window = pygame.display.set_mode(window_size)
    stars = []
    # Define the colors. Each color is defined by (R, G, B) value.
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)

    # Supa sound bar
    crash_sound = pygame.mixer.Sound("Ripdaship.mp3")
    laza_sound = pygame.mixer.Sound("laser.mp3")
    rip_sound = pygame.mixer.Sound("boom.mp3")
    rip2_sound = pygame.mixer.Sound("bd.mp3")
    # code for stars
    for _ in range(100):
        x = random.randrange(0, window_size[0])
        y = random.randrange(0, window_size[1])
        stars.append((x, y))

    # Main loop

    shx, shy = (750, 400)
    enemy_list = []
    stoobidscore = 0
    # Amount of ships that spawn at start of game
    enemy_list.append(asena())
    # real main loop
    running = True
    while running:
        conter = conter + 1

        smallfont = pygame.font.SysFont('Winddings', 35)
        text = smallfont.render('You have murded ' + str(stoobidscore) + ' innocent people you monster', True,
                                (255, 255, 255))
        d = pygame.font.SysFont('Centaur', 100)

        # pygame.time.delay(3)
        # Fill the background with white color
        window.fill((0, 0, 25))

        # Death player
        if ITPAS[-1] == False:
            if h == 0:
                h = conter
                pygame.mixer.Sound.play(rip_sound)
                pygame.mixer.Sound.play(rip2_sound)
            if conter < h + 20:
                window.blit(exp1, (shx - 40, shy - 30))
            elif conter < h + 40:
                window.blit(exp2, (shx - 40, shy - 30))
            elif conter < h + 60:
                window.blit(exp3, (shx - 40, shy - 30))
            elif conter < h + 80:
                window.blit(exp4, (shx - 40, shy - 30))
            elif conter < h + 100:
                window.blit(exp5, (shx - 40, shy - 30))
                enemy_list = []

        # THE WAY GIANT RED DWARFS ARE MADE ALERT!!!!!!!
        for star in stars:
            x, y = star
            pygame.draw.circle(window, (100, 0, 0), (x, y), 1.2)
            pygame.draw.line(window, (255, 100, 100), (x, y), (x, y))

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed
        # Basic player movement
        if ITPAS[-1] == True:
            if keys[pygame.K_w]:
                shy -= 2

            if keys[pygame.K_s]:
                shy += 2

            if keys[pygame.K_a]:
                shx -= 2

            if keys[pygame.K_d]:
                shx += 2

            if shy <= 0:
                shy = 1

            if shx <= 9:
                shx = 10

            if shx >= 1490:
                shx = 1489

            if shy >= 580:
                shy = 579

        # spaceship code.
        if ITPAS[-1] == True:
            pygame.draw.polygon(window, white,
                                [(shx, shy), (shx + 10, shy + 20), (shx, shy + 13), (shx - 10, shy + 20), (shx, shy)])

            # beam press this to kill al enemys
            if conter % 100 < 20:  # on for 10 counts, off for 90 counts

                if keys[pygame.K_SPACE]:
                    pygame.draw.line(window, (0, 240, 252), (shx, shy), (shx, 0), width=5)
                    pygame.mixer.Sound.play(laza_sound)
                    ydg = True

            else:
                ydg = False

        # Enemy

        for enemy in enemy_list:
            enemy.MTMD(shx, shy)
            enemy.YPD()

            if abs(enemy.Δx) < 20 and ydg == True and enemy.ey < shy and enemy.dying == False:
                enemy.explode()
                pygame.mixer.Sound.play(enemy.crash_sound)
                pygame.mixer.Sound.play(enemy.rip_sound)
                # if enemy.name == "asena":
                # enemy_list.append(asena())

                if ITPAS[-1] == True:
                    stoobidscore += 1








                else:
                    print("...:):):):):):):):);):);):););)")

        if ITPAS[-1] == True:
            if conter % 1000 == 0:
                enemy_list.append(The_Cir())

        #Enemy respaen code 1 dies you have 3 to fight
        if conter% 500 == 0:
            enemy_list.append(enemy_spaceship())

        # He comes and he goes bonki
        if conter% 2000 == 0:
            enemy_list.append(BONKY_boi())

        # every 10 secondsish your death spawns. (until we nerfed it)
        if conter% 1500 == 0:
            enemy_list.append(DD())

        # code that we have destoid
       # elif enemy.name == "DD":
            #enemy_list.append(DD())
            #Denemy_list.append(DD())

        # If you are wondring where this is from... It resembles touture.
        enemy_list[:] = [enemy for enemy in enemy_list if enemy.dead == False]

        # Check for QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.blit(text, (10, 10))
        if ITPAS[-1] == False:
            text2 = d.render('Game Over', True, (255, 0, 0))
            window.blit(text2, (550, 250))
            if flag == True:
                with open("HS.txt", "a") as GO:
                    GO.write(str(stoobidscore))
                    GO.write("\n")
                flag = False

        # Update the display
        pygame.display.flip()

    # Quit the Pygame
    pygame.quit()
    sys.exit()


# code to make sure we can start game from here
if __name__ == "__main__":
    game()


