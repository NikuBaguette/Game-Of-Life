import pygame as pg

class Cell:
    
    def __init__(self, x : int, y : int, state : bool = False, size : int = 60):
        self.state = state
        self.new_state = False
        self.box = pg.Rect(x, y, size, size)
        self.size = size
        self.update_time = pg.time.get_ticks()
    
    def __repr__(self) -> str:
        return f"State : {self.state} | Coords : {self.box.x//self.size, self.box.y//self.size}"
    
    def mouseIn(self):
        mouse = pg.mouse.get_pos()
        if mouse[0] > self.box.left and mouse[0] < self.box.right and mouse[1] < self.box.bottom and mouse[1] > self.box.top:
            return True
        else:
            return False
    
    def mouseClick(self):
        mouse = pg.mouse.get_pos()
        buttons = pg.mouse.get_pressed()
        
        cooldown = 300
        if pg.time.get_ticks() - self.update_time > cooldown:
            if mouse[0] > self.box.left and mouse[0] < self.box.right and mouse[1] > self.box.top and mouse[1] < self.box.bottom:
                if buttons[0]:
                    self.state = not self.state
                    self.update_time = pg.time.get_ticks()
        
    def draw(self, surface):
        if self.mouseIn():
            ratio = self.size//5
            over = self.box
            pg.draw.rect(surface, (0,255,0), over)
            
            self.box.x += ratio//2
            self.box.y += ratio//2
            
            self.box.width -= ratio
            self.box.height -= ratio
            
            if self.state:
                pg.draw.rect(surface, (0,0,0), self.box)
            else:
                pg.draw.rect(surface, (255,255,255), self.box)
            
            self.box.x -= ratio//2
            self.box.y -= ratio//2
            
            self.box.width += ratio
            self.box.height += ratio
            
        else:
            if self.state:
                pg.draw.rect(surface, (0,0,0), self.box)
            else:
                pg.draw.rect(surface, (255,255,255), self.box)

    
    def play(self, cells):
        x, y = self.box.x//self.size, self.box.y//self.size
        around = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i < 0 or y + j < 0:
                    around.append(False)
                elif x + i >= len(cells) or y + j >= len(cells[x]):
                    around.append(False)
                else:
                    around.append(cells[x + i][y + j].state)
        around.pop(4)
        cooldown = 500
        if pg.time.get_ticks() - self.update_time > cooldown:
            count = 0
            for t in around:
                if t:
                    count += 1
            
            if count < 2:
                self.new_state = False
            elif count > 4:
                self.new_state = False
            elif count == 3:
                self.new_state = True
            elif count == 2:
                self.new_state = self.state
            
            self.update_time = pg.time.get_ticks()
    
    def update_state(self):
        self.state = self.new_state