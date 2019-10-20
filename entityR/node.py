from typing import TypeVar, Generic, List

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, entity: T, related_entities: List = None) -> None:
        self.__entity: T = entity
        self.__related_entities: List = related_entities

    def get_entity(self):
        return self.__entity

    def add_related_entities(self,  related_entities: List) -> None:
        if related_entities is None:
            raise ValueError("related_entities can't be None")

        if self.__related_entities is None:
            self.__related_entities = []
        self.__related_entities.append(related_entities)

    def get_related_entities(self):
        return self.__related_entities
