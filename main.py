from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random

width, height = letter
existing_circles = []


def is_overlapping(x, y, existing_circles, radius):
    padding = 10
    for ex, ey in existing_circles:
        if ((x - ex) ** 2 + (y - ey) ** 2) ** 0.5 < 2 * radius + padding:
            return True
    return False


def circles(c, y_line):
    radius = 50
    for _ in range(25):
        attempts = 0
        while attempts < 1000:
            x = random.randint(radius, width - radius)
            y = random.randint(radius, y_line - 25 - radius)
            if not is_overlapping(x, y, existing_circles, radius):
                existing_circles.append((x, y))
                c.circle(x, y, radius)
                break
            attempts += 1


def line(c, y):
    c.line(0, y, width, y)

if __name__ == '__main__':
    c = canvas.Canvas("circles.pdf", pagesize=letter)
    y_line = height - 150
    line(c, y_line)
    circles(c, y_line)
    c.save()
    print("PDF Created")
