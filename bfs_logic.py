import pygame
import random
pygame.init()
width = 400
height = 300
screen = pygame.display.set_mode((width, height))
done = False
def get_color():
    cl_Arr = [(255, 0, 0)]
    return random.choice(cl_Arr)
width_r = 20
height_r = 20
arr = []

for i in range(width // width_r):
    new_arr = []
    for j in range(height // height_r):
        new_arr.append((get_color(), (width_r * i + 3, height_r * j + 2, width_r * 0.7, height_r * 0.7)))
    arr.append(new_arr)
def draw_rect():
    for i in range(width // width_r):
        for j in range(height // height_r):
            pygame.draw.rect(screen, arr[i][j][0], arr[i][j][1])
def get_next_node(x, y):
    global walls
    ways = ([1, 0], [0, 1], [-1, 0], [0, -1])
    arr = []
    for way in ways:
        if (x + way[0], y + way[1]) not in walls and 0 <= x + way[0] < width // width_r and 0 <= y + way[1] < height // height_r:
            arr.append((x + way[0], y + way[1]))
    return arr
walls = []
points = []
nehboh = {}
while not done:

    for event in pygame.event.get():
        keys = pygame.mouse.get_pressed()
        keys_ = pygame.key.get_pressed()
        if keys_[pygame.K_w]:
            x, y = pygame.mouse.get_pos()
            x = x // width_r
            y = y // height_r
            arr[x][y] = ((0, 255, 0), (x * width_r + 3, y * height_r + 3, height_r * 0.7, width_r * 0.7))
            points.append((x, y))
            neh = get_next_node(x, y)

            for ne in neh:
                arr[ne[0]][ne[1]] = ((0, 0, 255), (ne[0] * width_r + 3, ne[1] * height_r + 3, height_r * 0.7, width_r * 0.7))
        if event.type == pygame.QUIT:
            done = True
        if keys[0]:
            x, y = pygame.mouse.get_pos()
            x = x // width_r
            y = y // height_r
            arr[x][y] = ((0, 0, 0), (x * width_r + 3, y * height_r + 3, height_r * 0.7, width_r * 0.7))
            walls.append((x, y))

        if keys_[pygame.K_BACKSPACE]:
            x, y = pygame.mouse.get_pos()
            x = x // width_r
            y = y // height_r
            neh = get_next_node(x, y)
            print([1, 2, 3, 4] in [1, 2, 3, 6, 4])
            print(neh)
            flag = True
            all_nehs = []
            while flag:

                [all_nehs.append(neh_)if neh_ not in all_nehs else print() for neh_ in neh]
    x, y = pygame.mouse.get_pos()


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x // width_r * width_r, y // height_r * height_r, height_r, width_r))
    draw_rect()
    pygame.display.flip()