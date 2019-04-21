# -*- coding: utf-8 -*-


class Item:

    def __init__(self, description: str, value: float) -> None:
        self.__description = description
        self.__value = value

    @property
    def description(self) -> str:
        return self.__description

    @property
    def value(self) -> float:
        return self.__value
