'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import data
import pygame
from pygame.locals import *
import menus
import config

conf = config.Config().settings

def main():
    """

    :rtype : None
    """

    pygame.init()

    displaysurf = pygame.Surface((conf["width"], conf["height"]))
    if (conf["fullscreen"]):
        screen = pygame.display.set_mode((conf["display_width"],conf["display_height"]), FULLSCREEN)
    else:
        screen = pygame.display.set_mode((conf["display_width"],conf["display_height"]))
    #print data.load('sample.txt').read()

    displaysurf.convert()


    clock = pygame.time.Clock()

    active_scene = menus.Main()

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering 
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(displaysurf)
        
        active_scene = active_scene.next
        if (conf["show_fps"]):
            font = pygame.font.SysFont('', size=32)
            fps_label = font.render(str(clock.get_fps()), 1, (255,255,0), (0,0,0))
            displaysurf.blit(fps_label, (0,0))
        pygame.transform.scale(displaysurf, (conf["display_width"],conf["display_height"]), screen)
        pygame.display.flip()
        clock.tick()
        #clock.tick(conf["fps"])
    