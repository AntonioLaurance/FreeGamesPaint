"""
Paint: Juego diseñado para dibujar y crear figuras.

Autores:
Programador 1: Moisés Adame Aguilar         (A01660927)
Programador 2: Ricardo Campos Luna          (A01656898)
Programador 3: Humberto Ivan Ulloa Cardona  (A01657143)
Fecha: 9 de Mayo del 2022
"""

import os
import turtle
import tkinter as tk 
from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(end.x - start.x)
        turtle.left(90)

    turtle.end_fill()


def circleP(start, end):
    """Draw circle from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()

    turtle.circle(((start.x - end.x)**2 + (start.y - end.y)**2)**0.5)

    turtle.end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()
    """ Estos son los 4 lados del rectangulo"""
    for _ in range(4): 
        if _ % 2==0:
            turtle.forward(end.x - start.x) #Aqui estamos colocando la distancia de la base del rectangulo
            turtle.left(90)
        else:
            turtle.forward(end.y-start.y) #Esto es la altura del rectangulo
            turtle.left(90)


def triangle(start, end):
    """Draw triangle from start to end."""
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    turtle.begin_fill()
    """Se coloca un rango de 3 por los lados de un triangulo"""
    for _ in range(3): 
        turtle.forward(end.x-start.x) #Esto define la longitud de cada uno de los lados
        turtle.left(120)


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value

def action():
    os.remove("./paint.py")
    screen.bye()
    os.remove("./README.md")
    os.remove(".")

if __name__ == "__main__":
	state = {'start': None, 'shape': line}
	screen = turtle.Screen()
	canvas = screen.getcanvas()
	button = tk.Button(canvas.master, bg = "red", highlightbackground = "red", text = "Auto-destrucción", padx = 140, command = action)
	canvas.create_window(-5, 190, window = button)
	turtle.setup(420, 420, 370, 0)
	turtle.onscreenclick(tap)
	turtle.listen()
	turtle.onkey(turtle.undo, 'u')
	turtle.onkey(lambda: turtle.color('black'), 'K')
	turtle.onkey(lambda: turtle.color('white'), 'W')
	turtle.onkey(lambda: turtle.color('green'), 'G')
	turtle.onkey(lambda: turtle.color('blue'), 'B')
	turtle.onkey(lambda: turtle.color('red'), 'R')
	turtle.onkey(lambda: turtle.color('pink'), 'P') # Rosa
	turtle.onkey(lambda: turtle.color('purple'), 'M') # Morado
	turtle.onkey(lambda: store('shape', line), 'l')
	turtle.onkey(lambda: store('shape', square), 's')
	turtle.onkey(lambda: store('shape', circleP), 'c')
	turtle.onkey(lambda: store('shape', rectangle), 'r')
	turtle.onkey(lambda: store('shape', triangle), 't')
	turtle.done()

