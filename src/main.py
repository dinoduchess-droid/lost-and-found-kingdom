"""Lost and Found Kingdom - Main Entry Point"""

import pygame
import sys
from game.game_engine import GameEngine
from ui.menu import MainMenu


def main():
    """Initialize and run the game."""
    pygame.init()
    
    # Game configuration
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    FPS = 60
    
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Lost and Found Kingdom")
    clock = pygame.time.Clock()
    
    # Initialize game engine
    game_engine = GameEngine(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Start with main menu
    menu = MainMenu(screen, game_engine)
    current_state = "menu"
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if current_state == "menu":
                next_state = menu.handle_event(event)
                if next_state:
                    current_state = next_state
                    if next_state == "game":
                        game_engine.start_new_game()
            
            elif current_state == "game":
                game_engine.handle_event(event)
        
        # Update
        if current_state == "menu":
            menu.update()
        elif current_state == "game":
            game_engine.update()
        
        # Draw
        screen.fill((240, 240, 220))  # Light cream background
        
        if current_state == "menu":
            menu.draw()
        elif current_state == "game":
            game_engine.draw()
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
