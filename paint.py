"""
Paint: Juego diseñado para dibujar y crear figuras.

Autores:
Programador 1: Moisés Adame Aguilar         (A01660927)
Programador 2: Ricardo Campos Luna          (A01656898)
Programador 3: Humberto Ivan Ulloa Cardona  (A01657143)

Fecha: 9 de Mayo del 2022
"""

import turtle 
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
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    circle(((start.x - end.x)**2 + (start.y - end.y)**2)**0.5)

    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


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


state = {'start': None, 'shape': line}
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
turtle.onkey(lambda: turtle.store('shape', line), 'l')
turtle.onkey(lambda: turtle.store('shape', square), 's')
turtle.onkey(lambda: turtle.store('shape', circle), 'c')
turtle.onkey(lambda: turtle.store('shape', rectangle), 'r')
turtle.onkey(lambda: turtle.store('shape', triangle), 't')
turtle.done()

