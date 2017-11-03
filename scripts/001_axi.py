from axi import Device, Drawing
import time

PATHS = [[(0, 0), (1, 0), (1, 1), (0, 1), (0,0)]]
drawing = Drawing(PATHS)

d = Device()
d.enable_motors()
d.run_drawing(drawing)
d.disable_motors()
