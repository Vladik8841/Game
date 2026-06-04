import pygame as pg
import random
pg.init()
src = pg.display.set_mode((1350, 750))
pg.display.set_caption("python zmejka!")
zmejki = [[80, 100], [90, 100], [100, 100], [110, 100], [120, 100]]
clock = pg.time.Clock()
n = 0
r = [False, False, False, False]
run = True
applex = random.randint(1, 132) * 10
appley = random.randint(1, 69) * 10
def gor(zmejki, applex, appley, n):
    z = [zmejki[-1][0] + 10, zmejki[-1][1]]
    zmejki.append(z)
    if zmejki[-1][0] == applex and zmejki[-1][1] == appley:
        applex = random.randint(1, 132) * 10
        appley = random.randint(1, 69) * 10
        n += 1
    else:
        del zmejki[0]
    return applex, appley, n
def god(zmejki, applex, appley, n):
    z = [zmejki[-1][0], zmejki[-1][1] + 10]
    zmejki.append(z)
    if zmejki[-1][0] == applex and zmejki[-1][1] == appley:
        applex = random.randint(1, 132) * 10
        appley = random.randint(1, 69) * 10
        n += 1
    else:
        del zmejki[0]
    return applex, appley, n
def gol(zmejki, applex, appley, n):
    z = [zmejki[-1][0] - 10, zmejki[-1][1]]
    zmejki.append(z)
    if zmejki[-1][0] == applex and zmejki[-1][1] == appley:
        applex = random.randint(1, 132) * 10
        appley = random.randint(1, 69) * 10
        n += 1
    else:
        del zmejki[0]
    return applex, appley, n
def gou(zmejki, applex, appley, n):
    z = [zmejki[-1][0], zmejki[-1][1] - 10]
    zmejki.append(z)
    if zmejki[-1][0] == applex and zmejki[-1][1] == appley:
        applex = random.randint(1, 132) * 10
        appley = random.randint(1, 69) * 10
        n += 1
    else:
        del zmejki[0]
    return applex, appley, n
font = pg.font.Font(None, 36)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT and r[2] != True:
                for i in range(4):
                    r[i] = False
                r[0] = True
                break
            if event.key == pg.K_DOWN and r[3] != True:
                for i in range(4):
                    r[i] = False
                r[1] = True
                break
            if event.key == pg.K_LEFT and r[0] != True:
                for i in range(4):
                    r[i] = False
                r[2] = True
                break
            if event.key == pg.K_UP and r[1] != True:
                for i in range(4):
                    r[i] = False
                r[3] = True
                break
    text = font.render(f"{n}", True, (255, 255, 255))
    src.blit(text, (10, 710))

    pg.draw.rect(src,(150, 0, 150), (0, 0, 1330, 710), 10)
    pg.draw.rect(src,(150, 0, 0), (applex, appley, 10, 10))
    pg.draw.rect(src,(0, 100, 0), (zmejki[-1][0], zmejki[-1][1], 10, 10))
    for i in zmejki[:-1]:
        pg.draw.rect(src, (10, 150, 20), (i[0], i[1], 10, 10))
        if zmejki[-1] == i:
            print("game over", n)
            run = False
        if zmejki[-1][0] >= 1330:
            print("game over", n)
            run = False
        elif zmejki[-1][0] <= 0:
            print("game over", n)
            run = False
        elif zmejki[-1][1] >= 720:
            print("game over", n)
            run = False
        elif zmejki[-1][1] <= 0:
            print("game over", n)
            run = False
    if r[0]:
        applex, appley, n = gor(zmejki, applex, appley, n)
    if r[1]:
        applex, appley, n = god(zmejki, applex, appley, n)
    if r[2]:
        applex, appley, n = gol(zmejki, applex, appley, n)
    if r[3]:
        applex, appley, n = gou(zmejki, applex, appley, n)
    pg.display.flip()
    src.fill((0, 0, 0))
    clock.tick(10)
pg.quit()
