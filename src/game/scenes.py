"""Game scenes for Lost and Found Kingdom."""

import pygame
from abc import ABC, abstractmethod


class Scene(ABC):
    """Base class for game scenes."""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.background = pygame.Surface((width, height))
        self.background.fill((240, 240, 220))
    
    @abstractmethod
    def handle_event(self, event):
        """Handle input events."""
        pass
    
    @abstractmethod
    def update(self):
        """Update scene state."""
        pass
    
    @abstractmethod
    def draw(self, screen):
        """Draw the scene."""
        pass


class WarehouseScene(Scene):
    """The warehouse where the adventure begins."""
    
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.items = [
            {"name": "Old Teddy Bear", "x": 200, "y": 300},
            {"name": "Rusty Umbrella", "x": 500, "y": 250},
            {"name": "Metal Robot", "x": 800, "y": 400},
            {"name": "Golden Key", "x": 350, "y": 150},
            {"name": "Tattered Map", "x": 900, "y": 150}
        ]
        self.collected_items = []
    
    def handle_event(self, event):
        """Handle warehouse interactions."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for item in self.items[:]:
                if self.is_clicked(item["x"], item["y"], mouse_x, mouse_y):
                    self.collected_items.append(item["name"])
                    self.items.remove(item)
    
    @staticmethod
    def is_clicked(item_x: int, item_y: int, mouse_x: int, mouse_y: int, radius: int = 30) -> bool:
        """Check if an item was clicked."""
        distance = ((item_x - mouse_x) ** 2 + (item_y - mouse_y) ** 2) ** 0.5
        return distance <= radius
    
    def update(self):
        """Update warehouse scene."""
        pass
    
    def draw(self, screen):
        """Draw the warehouse scene."""
        screen.blit(self.background, (0, 0))
        
        # Draw title
        font = pygame.font.Font(None, 48)
        title = font.render("The Lost Warehouse", True, (100, 50, 50))
        screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))
        
        # Draw items
        for item in self.items:
            pygame.draw.circle(screen, (180, 140, 100), (item["x"], item["y"]), 20)
            small_font = pygame.font.Font(None, 14)
            label = small_font.render(item["name"], True, (50, 50, 50))
            screen.blit(label, (item["x"] - label.get_width() // 2, item["y"] + 30))
        
        # Draw collected items
        if self.collected_items:
            small_font = pygame.font.Font(None, 20)
            collected_text = small_font.render(f"Collected: {', '.join(self.collected_items)}", True, (50, 100, 50))
            screen.blit(collected_text, (20, self.height - 40))


class KingdomScene(Scene):
    """The magical kingdom where battles occur."""
    
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.background.fill((135, 206, 250))  # Sky blue
    
    def handle_event(self, event):
        """Handle kingdom interactions."""
        pass
    
    def update(self):
        """Update kingdom scene."""
        pass
    
    def draw(self, screen):
        """Draw the kingdom scene."""
        screen.blit(self.background, (0, 0))
        
        # Draw title
        font = pygame.font.Font(None, 48)
        title = font.render("The Imaginary Kingdom", True, (255, 255, 255))
        screen.blit(title, (self.width // 2 - title.get_width() // 2, 30))
        
        # Draw castle
        pygame.draw.polygon(screen, (139, 69, 19), [
            (self.width // 2 - 100, 400),
            (self.width // 2 - 100, 250),
            (self.width // 2, 150),
            (self.width // 2 + 100, 250),
            (self.width // 2 + 100, 400)
        ])
