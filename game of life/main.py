import pygame as pg
import Conway_Cells as CC
pg.init()

sky : tuple = (135,206,235)

size : tuple = (1480, 980)

cell_size : int = int(input("Give me the size of the cells : "))

width : int = int(size[0]/cell_size)
height : int = int(size[1]/cell_size)

screen : pg.Surface = pg.display.set_mode((width*cell_size, height*cell_size))
pg.display.set_caption("Game of Dad")
clock = pg.time.Clock()

cells : list = []
for i in range(width):
    line : list = []
    for j in range(height):
        line.append(CC.Cell(i*cell_size, j*cell_size, False, cell_size))
    cells.append(line)

trigger = False

cooldown = 500
update_time = pg.time.get_ticks()

running = True
while running:
    keys = pg.key.get_pressed()
    screen.fill(sky)
    
    if pg.time.get_ticks() - update_time > cooldown:
        if keys[pg.K_SPACE]:
            trigger = not trigger
            update_time = pg.time.get_ticks()
    
    if trigger:
        for x in cells:
            for cell in x:
                cell.play(cells)
                
        for x in cells:
            for cell in x:
                cell.update_state()

    else:
        for x in cells:
            for n in x:
                n.mouseClick()
    
    for x in cells:
        for c in x:
            c.draw(screen)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                 running = False
    
    pg.display.update()
    clock.tick(60)

pg.quit()