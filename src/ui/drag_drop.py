"""Drag and drop mechanics for the game."""

import pygame
from typing import Optional


class DragDropItem:
    """An item that can be dragged and dropped."""
    
    def __init__(self, name: str, x: int, y: int, width: int = 40, height: int = 40):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
    
    def handle_event(self, event, mouse_x: int, mouse_y: int):
        """Handle drag and drop events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.dragging = True
                self.offset_x = mouse_x - self.x
                self.offset_y = mouse_y - self.y
        
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y
            self.rect.x = self.x
            self.rect.y = self.y
    
    def draw(self, screen):
        """Draw the item."""
        color = (200, 150, 100) if self.dragging else (180, 130, 80)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (50, 50, 50), self.rect, 2)
        
        # Draw text
        font = pygame.font.Font(None, 12)
        text = font.render(self.name, True, (50, 50, 50))
        screen.blit(text, (self.x + 5, self.y + 12))


class DragDropManager:
    """Manages multiple drag and drop items."""
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, name: str, x: int, y: int) -> DragDropItem:
        """Add a new draggable item."""
        item = DragDropItem(name, x, y)
        self.items[name] = item
        return item
    
    def handle_event(self, event):
        """Handle events for all items."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for item in self.items.values():
            item.handle_event(event, mouse_x, mouse_y)
    
    def draw(self, screen):
        """Draw all items."""
        for item in self.items.values():
            item.draw(screen)
