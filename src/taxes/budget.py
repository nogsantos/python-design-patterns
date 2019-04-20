# -*- coding: utf-8 -*-


class Budget:

    def __init__(self, value: float) -> None:
        self.__value = value

    @property
    def value(self) -> float:
        return self.__value
