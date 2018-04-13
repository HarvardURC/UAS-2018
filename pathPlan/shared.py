__author__ = 'Murray Tannock'
import sys

import pyglet

STEP_SIZE = 20
RADIUS = 30
neighbourhood_size = STEP_SIZE
screen = pyglet.window.get_platform().get_default_display().get_screens()[0]
default_screen = pyglet.window.get_platform().get_default_display().get_screens()[0]
window_width = 800
window_height = 600
screen_width = screen.width
screen_height = screen.height
running = False
batch = pyglet.graphics.Batch()
node_count = 0
base_max = 5000
max_nodes = 5000
goal = None
optimizedPath = []
root_path = []
root_path_length = sys.maxsize
nodes = []
obstacles = []
x_domain = 0, window_width
y_domain = 50, window_height
x_range = x_domain[1] - x_domain[0]
y_range = y_domain[1] - y_domain[0]
method = None
fullscreen = False
region = None
continual = False
outfile_base = "levels/level"
outfile_ext = ".json"
collision_divisions = 10

incrementalAnimation = False;