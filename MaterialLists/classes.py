from dataclasses import dataclass
from typing import Any, Optional
import lookups


@dataclass
class Entity:
    """
    Class for entities to be dropped.
    """
    _Id: int
    _EntityType: str
    _Comment: str
    _Quantity: Optional[float]

    def __hash__(self) -> int:
        return hash(f"{self._Id}{self._EntityType}")

    def __init__(self, drop: Any):
        self.__initialize_idtype(drop)
        self.__initialize_quantity(drop)

    def __initialize_idtype(self, drop: dict):
        drop_type = drop["ItemType"]
        drop_value = drop["Item"]

        if drop_type == "Material" or drop_type == "Wyrmprint":
            self._Id = drop_value
            self._EntityType = drop_type
        elif drop_type == "Resource":
            self._Id = 0
            if drop_value == "Eldwater":
                self._EntityType = "Dew"
            else:
                self._EntityType = drop_value
        elif drop_type == "Gift":
            self._Id = lookups.GIFT_LOOKUP[drop_value]
            self._EntityType = "DragonGift"
        elif drop_type == "Consumable":
            match drop_value:
                case "Summon Voucher":
                    self._Id = 10101  # Single summon voucher
                    self._EntityType = "SummonTicket"
                case "Exquisite Honey":
                    self._Id = 100603
                    self._EntityType = "Item"
                case "Blessed Ethon Ashes":
                    self._Id = 100702
                    self._EntityType = "Item"
            self._Comment = drop_value
        else:
            raise ValueError(f"Unhandled drop type: {drop_type}")

    def __initialize_quantity(self, drop: dict):
        drop_type = drop["ItemType"]

        if drop.get("ExactDrop", None):
            self._Quantity = int(drop["ExactDrop"])

        self._Comment = drop.get("Comment", None)

        if drop_type == "Wyrmprint":
            self._Quantity = 0.1

        if drop_type == "Material":
            self._Quantity = 50

        if (self._Comment and "Boon" in self._Comment):
            self._Quantity = 5

        if drop_type == "Gift":
            self._Quantity = 1

        if drop_type == "Consumable":
            self._Quantity = 5

        if self._Quantity is None:
            raise ValueError("Missing quantity")


@dataclass
class ParsedQuest:
    """
    Class for an entry in the resulting JSON file.
    """
    _QuestId: int
    _Rupies: int
    _Mana: int
    _Drops: Any
