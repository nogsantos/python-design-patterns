# -*- coding: utf-8 -*-


class Budget:

    def __init__(self) -> None:
        self.__items = []

    @property
    def total(self) -> float:
        total = 0.0
        for item in self.__items:
            total += item.value
        return round(total, 3)

    # Freeze budget items returning a tuple
    @property
    def items(self) -> tuple:
        return tuple(self.__items)

    @property
    def items_len(self) -> int:
        return len(self.__items)

    def add(self, item) -> None:
        self.__items.append(item)
