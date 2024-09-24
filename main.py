import math
from random import random
import pygame


# declaring globals
backgroundColor = '#445552'
HEX_SIZE = 100

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

def drawHex(xPos, yPos):
    # Calculate the vertices of the hexagon
    points = []
    for i in range(6):
        angle = math.radians(60 * i)  # Angle for each vertex
        point_x = xPos + HEX_SIZE * math.cos(angle)  # x position
        point_y = yPos + HEX_SIZE * math.sin(angle)  # y position
        points.append((point_x, point_y))

    # Draw the hexagon using line segments
    pygame.draw.polygon(screen, "#FFFFFF", points, 1)  # 1 for line thickness

def tessellate_hexagons(surface, hex_size, color):
    hex_width = hex_size * 2
    hex_height = hex_size * math.sqrt(3)

    for row in range(10):  # Adjust the range for more rows
        for col in range(10):  # Adjust the range for more columns
            # Calculate the center of each hexagon
            x = col * hex_width * 0.75
            y = row * hex_height

            # Offset every other row
            if col % 2 == 1:
                y += hex_height / 2

            drawHex(x, y)
def main():


    running = True
    while running:
        # screen setup
        screen.fill(backgroundColor)
        clock.tick(60)  # limits FPS to 60

        # quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # drawing hexagons
        tessellate_hexagons(screen, HEX_SIZE, "#FFFFFF")

        pygame.display.flip()
    pygame.quit()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
