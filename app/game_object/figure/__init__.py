from typing import Type

from app.game_object.figure import S
from app.game_object.figure.I import I
from app.game_object.figure.J import J
from app.game_object.figure.L import L
from app.game_object.figure.O import O
from app.game_object.figure.S import S
from app.game_object.figure.T import T
from app.game_object.figure.Test import Test
from app.game_object.figure.Z import Z


def get_figures() -> list[Type[I | J | L | O | S | T | Z]]:

    return [I]
    return [I, J, L, O, S, T, Z]
