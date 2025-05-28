import pygame
import tkinter as tk
from tkinter import messagebox
from game.utils import Color, WIN_HEIGHT, WIN_WIDTH
from game.controlPanel import ControlPanel
from game.game import Game
from game.login import ManHinhDangNhap


# Increase sharpness
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
pygame.init()
# Window's Configuration
info = pygame.display.Info()
WIN_WIDTH =  WIN_WIDTH
WIN_HEIGHT = WIN_HEIGHT

WIN = pygame.display.set_mode(  
    (WIN_WIDTH, WIN_HEIGHT), pygame.FULLSCREEN
)  # initilize win form
pygame.display.set_caption("Chinese Chess Game")  # win caption
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 15)


def draw(game, controlPanel):
    """
    Drawing the game to window
    """
    WIN.fill(Color.TURQUOISE)
    game.updateGame()

    controlPanel.draw(WIN)
    pygame.display.update()


def main():
    """
    Main function
    """
    
    root = tk.Tk()
    login_screen = ManHinhDangNhap(root)
    root.mainloop()
    user_info = login_screen.user_info
    

    game = Game(WIN)
    controlPanel = ControlPanel(game, user_info)

    run = True
    while run:
        draw(game, controlPanel)
        # Loop through all events in 1 frames
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if not game.isOver:
                    game.checkForMove(pos)
                else:
                    print("Game is over")

                controlPanel.checkForClick(pos)


if __name__ == "__main__":
    main()
