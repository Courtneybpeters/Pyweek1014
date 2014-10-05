from scene import SceneBase
import pygame
import game
import config
import gui

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
        UI = gui.UI(screen)
        screen.fill((25, 0, 51))
        center_width = self.conf["width"]/2
        center_height = self.conf["height"]/2
        start_button = UI.make_button('start',((center_width-125), (center_height-40), 250, 80))
        options_button = UI.make_button('options', ((center_width-125), ((center_height-40)+ 90), 250, 80))


