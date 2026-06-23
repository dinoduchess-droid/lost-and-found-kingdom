# Lost and Found Kingdom

A charming, watercolor-style adventure game where you play as Sandy, a bored child who discovers a magical kingdom hidden in an old warehouse.

## Game Features

- **Watercolor Art Style**: Hand-drawn aesthetic with watercolor visual effects
- **Interactive Storytelling**: Multiple endings and branching narratives
- **Drag & Drop Mechanics**: Find items in the warehouse that shape your adventure
- **Draw to Life System**: Create your own characters and villains with an intuitive drawing interface
- **Dynamic Team Building**: Defeat enemies to recruit new imaginary allies
- **RPG Progression**: Level up and expand your team of imaginary friends
- **Customization**: Name and customize your items, characters, and allies

## Installation

1. Download the latest release
2. Unzip the file
3. Run `LostAndFoundKingdom.exe`

## Project Structure

```
├── src/
│   ├── main.py              # Game entry point
│   ├── game/
│   │   ├── __init__.py
│   │   ├── game_engine.py   # Core game logic
│   │   ├── scenes.py        # Game scenes and transitions
│   │   ├── inventory.py     # Item management system
│   │   └── character.py     # Character and ally system
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── canvas.py        # Drawing interface
│   │   ├── drag_drop.py     # Drag and drop mechanics
│   │   └── menu.py          # UI menus
│   ├── assets/
│   │   ├── watercolor_filters.py
│   │   ├── fonts/
│   │   └── sounds/
│   └── utils/
│       └── config.py
├── requirements.txt
├── build.py                 # Script to build EXE
└── .gitignore
```

## Story

Sandy, a bored child, discovers a hidden kingdom in an old warehouse. Every item found becomes real in this imaginary world. Choose your allies, face villains, and uncover the truth across multiple endings—all leading back to the simple magic of childhood imagination.

## Development

This game is built with Python using Pygame and Pillow for graphics processing.

## Building the Game

To build the standalone EXE:

```bash
pip install -r requirements.txt
python build.py
```

The executable will be created in the `dist/` folder.
