"""Main menu interface."""

import pygame


class MainMenu:
    """Main menu screen."""
    
    def __init__(self, screen, game_engine):
        self.screen = screen
        self.game_engine = game_engine
        self.width = screen.get_width()
        self.height = screen.get_height()
        
        self.buttons = {
            "start": pygame.Rect(self.width // 2 - 100, 250, 200, 50),
            "quit": pygame.Rect(self.width // 2 - 100, 350, 200, 50)
        }
        self.hovered_button = None
    
    def handle_event(self, event):
        """Handle menu input."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons["start"].collidepoint(mouse_pos):
                return "game"
            elif self.buttons["quit"].collidepoint(mouse_pos):
                return "quit"
        
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            for button_name, button_rect in self.buttons.items():
                if button_rect.collidepoint(mouse_pos):
                    self.hovered_button = button_name
                    return None
            self.hovered_button = None
        
        return None
    
    def update(self):
        """Update menu state."""
        pass
    
    def draw(self):
        """Draw the menu."""
        # Draw title
        font_large = pygame.font.Font(None, 64)
        title = font_large.render("Lost and Found Kingdom", True, (100, 50, 50))
        self.screen.blit(title, (self.width // 2 - title.get_width() // 2, 50))
        
        # Draw subtitle
        font_small = pygame.font.Font(None, 24)
        subtitle = font_small.render("A story of imagination and adventure", True, (150, 100, 100))
        self.screen.blit(subtitle, (self.width // 2 - subtitle.get_width() // 2, 130))
        
        # Draw buttons
        font_button = pygame.font.Font(None, 32)
        
        for button_name, button_rect in self.buttons.items():
            # Button color changes on hover
            color = (200, 100, 100) if button_name == self.hovered_button else (150, 100, 100)
            pygame.draw.rect(self.screen, color, button_rect)
            pygame.draw.rect(self.screen, (50, 50, 50), button_rect, 2)
            
            # Button text
            text = "Start Game" if button_name == "start" else "Quit"
            text_surface = font_button.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)
