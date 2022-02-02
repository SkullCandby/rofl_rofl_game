from collections import deque

import pygame
import random

clock = pygame.time.Clock()


def get_rect(x, y):
    return x * width_r + 3, y * height_r + 2, width_r * 0.7, height_r * 0.7


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
pnts = []
for i in range(width // width_r):
    new_arr = []
    pn = []
    for j in range(height // height_r):
        new_arr.append((get_color(), (width_r * i + 3, height_r * j + 2, width_r * 0.7, height_r * 0.7)))
        pn.append(0)
    pnts.append(pn)
    print(pn)
    arr.append(new_arr)
print(pnts[15][0])


def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[x][y] else False
    #print(check_next_node(x + dx, y + dy), 'check')
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


cols, rows = width // width_r - 1, height // height_r - 1

# grid
grid = pnts
print(grid)
# dict of adjacency lists
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)


def draw_rect():
    for i in range(width // width_r):
        for j in range(height // height_r):
            pygame.draw.rect(screen, arr[i][j][0], arr[i][j][1])


print(graph)

# BFS settings

print(graph)
start = (0, 0)
print(deque)
queue = deque([start])
visited = {start: None}
cur_node = start

while not done:

    for event in pygame.event.get():
        keys = pygame.mouse.get_pressed()
        print(keys)
        if event.type == pygame.QUIT:
            done = True
        if keys[0]:
            x, y = pygame.mouse.get_pos()
            x = x // width_r
            y = y // height_r
            print(x, y)
            arr[x][y] = ((0, 0, 0), (x * width_r + 3, y * height_r + 3, height_r * 0.7, width_r * 0.7))
            print(width_r * width_r, height_r * height_r, height_r, width_r)
    x, y = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x // width_r * width_r, y // height_r * height_r, height_r, width_r))
    [pygame.draw.rect(screen, pygame.Color('forestgreen'), get_rect(x, y)) for x, y in visited]
    [pygame.draw.rect(screen, pygame.Color('darkslategray'), get_rect(x, y)) for x, y in queue]
    if queue:
        print(queue)
        cur_node = queue.popleft()
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node

    path_head, path_segment = cur_node, cur_node
    while path_segment:
        print(get_rect(*path_segment))
        pygame.draw.rect(screen, pygame.Color('white'), get_rect(*path_segment), width_r, border_radius=width_r // 3)
        path_segment = visited[path_segment]
    pygame.draw.rect(screen, pygame.Color('blue'), get_rect(*start), border_radius=width_r // 3)
    pygame.draw.rect(screen, pygame.Color('magenta'), get_rect(*path_head), border_radius=width_r // 3)

    clock.tick(7)
    pygame.display.flip()
