"""Character and ally system for Lost and Found Kingdom."""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Player:
    """Main player character (Sandy)."""
    name: str = "Sandy"
    level: int = 1
    experience: int = 0
    health: int = 100
    max_health: int = 100
    attack_power: int = 10
    defense: int = 5
    personality: str = "curious"  # brave, curious, cautious, silly
    
    def level_up(self):
        """Increase player level and stats."""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack_power += 5
        self.defense += 2
    
    def take_damage(self, damage: int):
        """Reduce health by damage amount."""
        self.health = max(0, self.health - damage)
    
    def heal(self, amount: int):
        """Restore health up to max."""
        self.health = min(self.max_health, self.health + amount)


@dataclass
class ImaginaryAlly:
    """Imaginary friend/ally created by the player."""
    name: str
    description: str
    type: str  # "ally", "villain", "neutral"
    personality: str
    level: int = 1
    health: int = 50
    max_health: int = 50
    attack_power: int = 8
    defense: int = 3
    special_abilities: List[str] = field(default_factory=list)
    custom_drawing: str = ""  # Path to custom drawing
    appearance_traits: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert ally to dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "personality": self.personality,
            "level": self.level,
            "health": self.health,
            "max_health": self.max_health,
            "attack_power": self.attack_power,
            "defense": self.defense,
            "special_abilities": self.special_abilities,
            "custom_drawing": self.custom_drawing,
            "appearance_traits": self.appearance_traits
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'ImaginaryAlly':
        """Create ally from dictionary."""
        return ImaginaryAlly(**data)


class ImaginaryCharacterFactory:
    """Factory for creating preset imaginary characters."""
    
    PRESETS = {
        "teddy_bear_villain": {
            "name": "Grumble Bear",
            "description": "A grumpy stuffed bear come to life",
            "type": "villain",
            "personality": "grumpy",
            "attack_power": 12,
            "defense": 4
        },
        "umbrella_hero": {
            "name": "Shelterwind",
            "description": "A magical umbrella protecting the realm",
            "type": "ally",
            "personality": "protective",
            "attack_power": 9,
            "defense": 7
        },
        "robot_companion": {
            "name": "Tin",
            "description": "A walking, talking metal robot",
            "type": "ally",
            "personality": "cheerful",
            "attack_power": 11,
            "defense": 6,
            "special_abilities": ["mechanical_punch", "rust_shield"]
        }
    }
    
    @staticmethod
    def create_from_preset(preset_name: str) -> ImaginaryAlly:
        """Create an ally from a preset."""
        if preset_name not in ImaginaryCharacterFactory.PRESETS:
            raise ValueError(f"Unknown preset: {preset_name}")
        
        preset = ImaginaryCharacterFactory.PRESETS[preset_name]
        return ImaginaryAlly(**preset)
    
    @staticmethod
    def create_custom(name: str, description: str, ally_type: str = "ally") -> ImaginaryAlly:
        """Create a custom ally."""
        return ImaginaryAlly(
            name=name,
            description=description,
            type=ally_type,
            personality="mysterious"
        )
