from scene import SceneBase
import pygame
import game
import config

class Main(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter 
                self.SwitchToScene(game.Main())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen 
        screen.fill((25, 0, 51))
        startrect = pygame.draw.rect(screen, self.conf["colors"]["textcolor"], (10, 10, 50, 100))
