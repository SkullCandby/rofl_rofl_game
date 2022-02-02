import pygame as pg
from random import random
from collections import deque


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


cols, rows = 25, 25
TILE = 30

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
# grid
grid = [[0 for col in range(cols)] for row in range(rows)]
print(grid)
# dict of adjacency lists
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

# BFS settings
print(graph)
start = (0, 0)
queue = deque([start])
visited = {start: None}
cur_node = start

while True:
    # fill screen
    for event in pg.event.get():
        keys = pg.mouse.get_pressed()
        if event.type == pg.QUIT:
            exit()

    sc.fill(pg.Color('black'))
    # draw grid
    [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5)
      for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
    # draw BFS work
    [pg.draw.rect(sc, pg.Color('forestgreen'), get_rect(x, y)) for x, y in visited]
    [pg.draw.rect(sc, pg.Color('darkslategray'), get_rect(x, y)) for x, y in queue]
    pg.display.flip()