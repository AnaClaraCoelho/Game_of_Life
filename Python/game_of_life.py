import numpy as np
import pygame
import time

BACKGROUND_COLOR = (10,15,12)
COLOR_GRID = (40,60,55)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_LIVE_NEXT = (255,255,255)

def update (screen, cells, size, with_progress=False):
    update_cells = np.zeros((cells.shape[0], cells.shape[1])) # Creates an empty array 

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col] # Calculate the number of alives nighboring cells
        color = BACKGROUND_COLOR if cells[row,col] == 0 else COLOR_LIVE_NEXT

        if cells[row,col] == 1: # Is alive
            if alive < 2 or alive > 3: # alive == sum of all the neighboring cells
                if with_progress:
                    color = COLOR_DIE_NEXT
            if 2<= alive <= 3:
                update_cells[row,col] = 1
                if with_progress:
                    color = COLOR_LIVE_NEXT
                else:
                    if with_progress:
                        color = BACKGROUND_COLOR
        else:
            if alive == 3: 
                update_cells[row,col] = 1
                if with_progress:
                    color = COLOR_LIVE_NEXT
        
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1)) # Drawing the individual pixels

    return update_cells


def main():
    pygame.init()
    screen  = pygame.display.set_mode((800,600))

    cells = np.zeros((60,80))
    screen.fill(COLOR_GRID)
    update(screen,cells,15)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen,cells,15)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                cells[position[1] // 10, position[0] // 10] = 1
                update(screen,cells,10)
                pygame.display.update()

            screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress = True)
            pygame.display.update()

            time.sleep(0,1)


if __name__ == '__main__':
    main()
