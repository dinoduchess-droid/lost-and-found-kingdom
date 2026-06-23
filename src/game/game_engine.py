"""Core game engine for Lost and Found Kingdom."""

import pygame
from enum import Enum
from game.inventory import Inventory
from game.character import Player, ImaginaryAlly
from game.scenes import WarehouseScene, KingdomScene


class GameState(Enum):
    WAREHOUSE = 1
    KINGDOM = 2
    BATTLE = 3
    DRAWING = 4
    DIALOGUE = 5
    ENDING = 6


class GameEngine:
    """Main game engine managing game state and logic."""
    
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        
        self.state = GameState.WAREHOUSE
        self.player = None
        self.inventory = Inventory()
        self.allies = []
        self.current_scene = None
        
        self.warehouse_scene = WarehouseScene(width, height)
        self.kingdom_scene = KingdomScene(width, height)
    
    def start_new_game(self):
        """Initialize a new game."""
        self.player = Player(name="Sandy", level=1)
        self.state = GameState.WAREHOUSE
        self.current_scene = self.warehouse_scene
        self.allies = []
        self.inventory.clear()
    
    def handle_event(self, event):
        """Handle player input events."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.state == GameState.WAREHOUSE:
                # Transition to kingdom
                self.transition_to_kingdom()
        
        # Pass events to current scene
        if self.current_scene:
            self.current_scene.handle_event(event)
    
    def transition_to_kingdom(self):
        """Transition from warehouse to kingdom."""
        self.state = GameState.KINGDOM
        self.current_scene = self.kingdom_scene
    
    def add_item_to_inventory(self, item_name, description):
        """Add an item to the player's inventory."""
        self.inventory.add_item(item_name, description)
    
    def add_ally(self, ally):
        """Add an imaginary ally to the player's team."""
        self.allies.append(ally)
        self.player.level_up()
    
    def start_battle(self, enemy):
        """Start a battle with an enemy."""
        self.state = GameState.BATTLE
    
    def open_drawing_interface(self):
        """Open the draw-to-life character creation interface."""
        self.state = GameState.DRAWING
    
    def update(self):
        """Update game state."""
        if self.current_scene:
            self.current_scene.update()
    
    def draw(self):
        """Render the game."""
        if self.current_scene:
            self.current_scene.draw(self.screen)
        
        # Draw HUD
        self.draw_hud()
    
    def draw_hud(self):
        """Draw heads-up display with player info."""
        if self.player is None:
            return
            
        font = pygame.font.Font(None, 24)
        
        # Player level and allies
        level_text = font.render(f"Level: {self.player.level}", True, (50, 50, 50))
        allies_text = font.render(f"Allies: {len(self.allies)}", True, (50, 50, 50))
        
        self.screen.blit(level_text, (20, 20))
        self.screen.blit(allies_text, (20, 50))
