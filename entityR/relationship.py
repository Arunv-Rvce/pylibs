from enum import Enum
from typing import TypeVar, Generic

B = TypeVar('B')
S = TypeVar('S')


class RelationshipType(Enum):
    ONE = 'ONE'
    MANY = 'MANY'
    LIMITED = 'LIMITED'


class Relationship(Generic[B, S]):
    def __int__(self,
                base_entity: B,
                sub_entity: S,
                base_relationship: RelationshipType,
                sub_relationship: RelationshipType,
                max_base_entities: int = None,
                max_sub_entities: int = None):
        self.base_entity_type: type = type(base_entity)
        self.sub_entity_type: type = type(sub_entity)
        self.base_relationship: RelationshipType = base_relationship
        self.sub_relationship: RelationshipType = sub_relationship
        self.max_base_entities: int = self.__validate_max_relationship(base_relationship, max_base_entities)
        self.max_sub_entities: int = self.__validate_max_relationship(sub_relationship, max_sub_entities)

    @classmethod
    def __validate_max_relationship(cls, relationship: RelationshipType, max_entities: int) -> int:
        if relationship == RelationshipType.ONE and max_entities != 1:
            raise ValueError('RelationshipType.ONE can contain max_base_entities as 1')
        if relationship == RelationshipType.LIMITED and max_entities < 2:
            raise ValueError('RelationshipType.LIMITED should contain max_base_entities > 1')
        if relationship == RelationshipType.MANY and max_entities is not None:
            raise ValueError('RelationshipType.MANY should contain max_base_entities as None, '
                             'use RelationshipType.LIMITED for specifying the max limit')
        return max_entities
