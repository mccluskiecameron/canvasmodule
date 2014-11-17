import document
from time import time
print("hello")
class Canvas:
    def __init__(self, canvas_id, fps=120):
        self.canvas = document.getElementById(canvas_id)
        self.ctx = self.canvas.getContext("2d")
        self.fps = fps
        self.looping = False
        self.elements = []
        self.binds = []
        self.loops = []
    def _redraw(self):
        self.canvas.clearRect(0, 0, self.canvas.width, self.canvas.height)
        for drawable in self.elements:
            drawable._draw()
    def _get_binds(self):
        for bind in self.binds:
            bind.retrieve()
    def _run_loops(self):
        for x, loop in self.loops:
            loop.run()
            if not loop.persistent:
                del loop
    def add_element(self, element):
        self.elements.append(element)
        return len(self.elements) - 1
    def remove_element(self, index):
        del self.elements[index]
    def clear_elements(self):
        self.elements = []
    def add_loop(self, loop):
        self.loops.append(loop)
        return len(self.loop) - 1
    def remove_loop(self, index):
        del self.loops[index]
    def clear_loops(self):
        self.loops = []
    def end(self):
        self.looping = False
    def mainloop(self):
        self.looping = True
        expected_time = time() + 1/self.fps
        while self.looping:
            while time() < expected_time:
                pass
            expected_time = time() + 1/ self.fps
            self._get_binds()
            self._run_loops()
            self._redraw()

class Drawable:
    def __init__(self, canvas):
        self.canvas = canvas
        self.index = self.canvas.add_element(self)
    def _draw(self):
        pass
    def __del__(self):
        self.canvas.remove_element(self.index)

class Rectangle(Drawable):
    def __init__(self, canvas, x1, y1, width, height, color="black"):
        Drawable.__init__(self, canvas)
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = color
    def _draw(self):
        self.canvas.ctx.fillStyle = self.color
        self.canvas.ctx.fillRect(self.x1, self.y1, self.width, self.height)
    def shift(self, amountx, amounty):
        self.x1 += amountx
        self.y1 += amounty
    def is_within(self, x, y):
        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            return True
        return False

class Square(Rectangle):
    def __init__(self, cornerX, cornerY, width=1, **kwargs):
        Rectangle.__init__(self, cornerX, cornerY, width, width, **kwargs)
    def resize(self, new_width):
        self.width = new_width
        self.height = new_width
    def _draw(self):
        self.height = self.width
        Rectangle._draw(self)
