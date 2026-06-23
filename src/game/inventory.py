"""Inventory system for managing found items."""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Item:
    """An item found in the warehouse."""
    name: str
    description: str
    item_type: str  # "tool", "weapon", "armor", "consumable", "quest"
    location_found: str = "warehouse"
    effect: str = ""  # How this item affects gameplay
    custom_properties: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert item to dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
            "item_type": self.item_type,
            "location_found": self.location_found,
            "effect": self.effect,
            "custom_properties": self.custom_properties
        }


class Inventory:
    """Manages player's inventory of items."""
    
    def __init__(self, max_size: int = 20):
        self.items: List[Item] = []
        self.max_size = max_size
    
    def add_item(self, name: str, description: str, item_type: str = "quest") -> bool:
        """Add an item to the inventory."""
        if len(self.items) >= self.max_size:
            return False
        
        item = Item(
            name=name,
            description=description,
            item_type=item_type
        )
        self.items.append(item)
        return True
    
    def remove_item(self, item_name: str) -> bool:
        """Remove an item from the inventory."""
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.items.pop(i)
                return True
        return False
    
    def get_item(self, item_name: str) -> Item | None:
        """Get an item by name."""
        for item in self.items:
            if item.name == item_name:
                return item
        return None
    
    def get_items_by_type(self, item_type: str) -> List[Item]:
        """Get all items of a specific type."""
        return [item for item in self.items if item.item_type == item_type]
    
    def clear(self):
        """Clear all items from inventory."""
        self.items = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert inventory to dictionary for saving."""
        return {
            "max_size": self.max_size,
            "items": [item.to_dict() for item in self.items]
        }
