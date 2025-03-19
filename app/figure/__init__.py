from typing import List, Type

from app.figure import I, J, L, O, S, T, Z
from app.figure.I import I
from app.figure.J import J
from app.figure.L import L
from app.figure.O import O
from app.figure.S import S
from app.figure.T import T
from app.figure.Test import Test
from app.figure.Z import Z
from app.figure.figure_abstract import FigureAbstract


def get_figures() -> list[Type[I | J | L | O | S | T | Z]]:
    return [Test]

    return [I, J, L, O, S, T, Z]
