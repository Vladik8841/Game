import pygame as pg
pg.init()
src =pg.display.set_mode((1, 1))
pg.display.set_caption('kriki mnoi pridumannych ljudej')
w = ((255, 255, 255))
g = ((0, 255, 0))
rx = 500
ry = 700
rw = 100
rh = 100
cx = 700
cy = 500
cr = 101
cr2 = 102
rx2 = 300
ry2 = 700
rw2 = 100
rh2 = 100
run = True
while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	
	src.fill((0, 0, 0))
	mx, my = pg.mouse.get_pos()
	pg.draw.rect(src, g, (rx, ry, rw, rh))
	pg.draw.circle(src, w, (300, 500), cr2)
	pg.draw.rect(src, g, (rx2, ry2, rw2, rh2))
	pg.draw.circle(src, w, (cx, cy),  cr)
	mb = pg.mouse.get_pressed()
	if mb[0] and rx <= mx <= rx + rw and ry <= my <= ry + rh:
		cr += 3
		cr2 -= 3
	if mb[0] and rx2 <= mx <= rx2 + rw2 and ry2 <= my <= ry + rh2:
		cr -= 3
		cr2 += 3
		
	pg.display.flip()
pg.quit()
