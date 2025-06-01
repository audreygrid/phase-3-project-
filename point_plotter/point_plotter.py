import os

WIDTH = 100
HEIGHT = 40

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def render_canvas(canvas):
    # Draw top border
    print('+' + '-' * WIDTH + '+')
    for row in canvas:
        print('|' + ''.join(row) + '|')
    # Draw bottom border
    print('+' + '-' * WIDTH + '+')

def plot_point(canvas, x, y, char='*'):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        canvas[y][x] = char

def draw_line(canvas, x0, y0, x1, y1, char='*'):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            plot_point(canvas, x, y, char)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
        plot_point(canvas, x, y, char)
    else:
        err = dy / 2.0
        while y != y1:
            plot_point(canvas, x, y, char)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
        plot_point(canvas, x, y, char)

class PointClass:
    def __init__(self, name, description, points):
        self.name = name
        self.description = description
        self.points = points

    def plot(self, canvas, char='*', connect=True):
        if not self.points:
            return
        prev = None
        for x, y in self.points:
            print(f"Plotting point: ({x}, {y})")  # 👈 helpful debug
            if connect and prev:
                draw_line(canvas, prev[0], prev[1], x, y, char)
            else:
                plot_point(canvas, x, y, char)
            prev = (x, y)

def main():
    canvas = create_canvas(WIDTH, HEIGHT)

    # Use SMALLER coordinates so they're visible in terminal
    triangle = PointClass(
        "Triangle",
        "Just a triangle",
        [
            (10, 5), (20, 10), (30, 5), (10, 5)  # closing the shape
        ]
    )

    triangle.plot(canvas)
    clear_screen()
    print(f"{triangle.name} - {triangle.description}")
    render_canvas(canvas)

if __name__ == "__main__":
    main()
