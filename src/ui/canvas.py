"""Drawing canvas for creating imaginary characters."""

import pygame
from typing import List, Tuple


class DrawingCanvas:
    """Canvas for drawing characters using brush strokes."""
    
    def __init__(self, width: int = 400, height: int = 400):
        self.width = width
        self.height = height
        self.canvas = pygame.Surface((width, height))
        self.canvas.fill((255, 255, 255))
        self.strokes: List[List[Tuple[int, int, int]]] = []  # List of strokes, each stroke is a list of points
        
        self.current_stroke: List[Tuple[int, int, int]] = []
        self.brush_size = 5
        self.brush_color = (0, 0, 0)  # Black
        self.available_colors = [
            (0, 0, 0),      # Black
            (255, 0, 0),    # Red
            (0, 0, 255),    # Blue
            (0, 255, 0),    # Green
        ]
        self.available_brushes = ["round", "square", "watercolor"]
        self.current_brush = "round"
        self.unlocked_colors = 1
        self.unlocked_brushes = 1
    
    def start_stroke(self, x: int, y: int):
        """Begin a new drawing stroke."""
        self.current_stroke = [(x, y, self.brush_size)]
    
    def add_to_stroke(self, x: int, y: int):
        """Add a point to the current stroke."""
        if self.current_stroke:
            self.current_stroke.append((x, y, self.brush_size))
    
    def end_stroke(self):
        """End the current stroke and add it to the canvas."""
        if self.current_stroke:
            self.strokes.append(self.current_stroke)
            self.redraw()
            self.current_stroke = []
    
    def redraw(self):
        """Redraw the canvas from stored strokes."""
        self.canvas.fill((255, 255, 255))
        
        for stroke in self.strokes:
            for i in range(len(stroke) - 1):
                x1, y1, size1 = stroke[i]
                x2, y2, size2 = stroke[i + 1]
                pygame.draw.line(self.canvas, self.brush_color, (x1, y1), (x2, y2), int(size1))
    
    def clear(self):
        """Clear the canvas."""
        self.canvas.fill((255, 255, 255))
        self.strokes = []
        self.current_stroke = []
    
    def set_brush_color(self, color_index: int):
        """Set the brush color by index."""
        if color_index < len(self.available_colors):
            self.brush_color = self.available_colors[color_index]
    
    def set_brush_size(self, size: int):
        """Set the brush size."""
        self.brush_size = max(1, min(50, size))  # Clamp between 1 and 50
    
    def unlock_color(self, color_index: int):
        """Unlock a new color through gameplay."""
        self.unlocked_colors = max(self.unlocked_colors, color_index + 1)
    
    def unlock_brush(self, brush_name: str):
        """Unlock a new brush through gameplay."""
        if brush_name in self.available_brushes:
            idx = self.available_brushes.index(brush_name)
            self.unlocked_brushes = max(self.unlocked_brushes, idx + 1)
    
    def get_image_data(self) -> pygame.Surface:
        """Get the current canvas drawing."""
        return self.canvas.copy()
