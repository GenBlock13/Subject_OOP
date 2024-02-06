import tkinter as tk
from tkinter import ttk


class Shape:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y

    def display(self):
        pass


class Triangle(Shape):
    def __init__(self, canvas, x, y, size):
        super().__init__(canvas, x, y)
        self.size = size

    def display(self):
        self.canvas.create_polygon(self.x, self.y,
                                   self.x + self.size, self.y,
                                   self.x + self.size / 2, self.y - self.size,
                                   fill="red")


class Rectangle(Shape):
    def __init__(self, canvas, x, y, width, height):
        super().__init__(canvas, x, y)
        self.width = width
        self.height = height

    def display(self):
        self.canvas.create_rectangle(self.x, self.y,
                                     self.x + self.width, self.y + self.height,
                                     fill="blue")


class Trapezoid(Shape):
    def __init__(self, canvas, x, y, base1, base2, height):
        super().__init__(canvas, x, y)
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def display(self):
        self.canvas.create_polygon(self.x, self.y,
                                   self.x + self.base1, self.y,
                                   self.x + self.base2, self.y + self.height,
                                   self.x, self.y + self.height,
                                   fill="green")


class Cone(Shape):
    def __init__(self, canvas, x, y, radius, height):
        super().__init__(canvas, x, y)
        self.radius = radius
        self.height = height


class Circle(Shape):
    def __init__(self, canvas, x, y, radius):
        super().__init__(canvas, x, y)
        self.radius = radius

    def display(self):
        self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                self.x + self.radius, self.y + self.radius,
                                fill="orange")


# Создание окна tkinter
window = tk.Tk()
window.title("Geometric Shapes")
window.geometry("400x400")

# Создание холста
canvas = tk.Canvas(window, width=400, height=450)
canvas.pack()

frame = ttk.Frame(window)
frame.pack()

# Создание экземпляров фигур и их отображение
triangle = Triangle(canvas, 50, 50, 50)
triangle.display()

rectangle = Rectangle(canvas, 200, 50, 100, 50)
rectangle.display()

trapezoid = Trapezoid(canvas, 50, 200, 100, 100, 50)
trapezoid.display()

cone = Cone(canvas, 200, 200, 50, 100)
cone.display()

circle = Circle(canvas, 150, 350, 50)
circle.display()

window.mainloop()
