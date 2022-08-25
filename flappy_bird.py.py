import pygame
import random
from pygame import mixer

class Bird:
    def __init__(self):
        pygame.init()  
        self.xScreen, self.yScreen = 500, 600  
        linkBackGround = 'data/background.jpg' 
        self.linkImgBird = "./data/bird.png"  
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen)) 
        pygame.display.set_caption("Flappybird")
        self.background = pygame.image.load(linkBackGround)
        self.gamerunning = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)
        
        self.xSizeBird = 40 
        self.ySizeBird = 40  
        self.xBird = self.xScreen/2  
        self.yBird = self.yScreen/2
        self.VBirdUp = 60 
        self.VBirdDown = 3  
       
        self.xColunm = self.yScreen+250 
        self.yColunm = 0
        self.xSizeColunm = 100  
        self.ySizeColunm = self.yScreen
        self.Vcolunm = 4  
        self.colunmChange = 0

        self.scores = 0
        self.checkLost = False

    def image_draw(self, url, xLocal, yLocal, xImg, yImg): 
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(
            PlanesImg, (xImg, yImg)) 
        self.screen.blit(PlanesImg, (xLocal, yLocal))

    def show_score(self, x, y, scores, size): 
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score, (x, y))

    def colunm(self):
        maginColunm = 80
        yColunmChangeTop = -self.ySizeColunm/2 - maginColunm + \
            self.colunmChange  
        yColunmChangeBotton = self.ySizeColunm/2 + maginColunm+self.colunmChange
        self.image_draw("./data/colunm.png", self.xColunm,
                        yColunmChangeTop, self.xSizeColunm, self.ySizeColunm)
        self.image_draw("./data/colunm.png", self.xColunm,
                        yColunmChangeBotton, self.xSizeColunm, self.ySizeColunm)
        self.xColunm = self.xColunm - self.Vcolunm
        if self.xColunm < -100: 
            self.xColunm = self.xScreen 
            # Random khoảng cách cột
            self.colunmChange = random.randint(-100, 100)
            self.scores += 1
        return yColunmChangeTop+self.ySizeColunm, yColunmChangeBotton  
    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get(): 
               
                if event.type == pygame .QUIT:  
                    self.gamerunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.yBird -= self.VBirdUp 
                    self.music("./data/wet-click.wav")
                if event.type == pygame.KEYDOWN:  
                        self.yBird -= self.VBirdUp  # Bird bay lên
            self.yBird += self.VBirdDown  
            yColunmChangeTop, yColunmChangeBotton = self.colunm()
            
            if self.yBird < yColunmChangeTop and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            if self.yBird+self.ySizeBird > yColunmChangeBotton and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            
            if (self.yBird + self.ySizeBird > self.yScreen) or self.yBird < 0:
                self.yBird = self.yScreen/2
                self.checkLost = True
            print(self.Vcolunm)
            while(self.checkLost):  
                self.xColunm = self.xScreen+100
                for event in pygame.event.get():   
                    if event.type == pygame.QUIT:  
                        self.gamerunning = False
                        self.checkLost = False
                        break
                    if event.type == pygame.KEYDOWN: 
                        self.checkLost = False
                        self.scores = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.checkLost = False
                        self.scores = 0
                self.show_score(100, 100, "Scores:{}".format(
                    self.scores), 40)  # In điểm
                self.show_score(self.xScreen/2-100, self.yScreen /
                                2-100, "GAME OVER", 50) 
                self.Vcolunm = 6
                self.VBirdDown = 7
                pygame.display.update()
            self.image_draw(self.linkImgBird, self.xBird,
                            self.yBird, self.xSizeBird, self.ySizeBird)
            self.show_score(self.xScreen - 200, 20, "", 15)
            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)
            pygame.display.update() 
            clock = pygame.time.Clock()
            clock.tick(80)
if __name__ == "__main__":
    bird = Bird()
    bird.run()