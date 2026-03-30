# SnakeGame-py-

🐍 Snake Game (Python - Tkinter)

A classic Snake Game built using Python, Tkinter, and PIL (Pillow).
This project demonstrates GUI development, event handling, and basic game logic.

🎮 Features
Smooth snake movement
Score tracking system
Random food generation
Collision detection:
Wall collision
Self collision
Restart option after Game Over
Loading screen animation
Fullscreen gameplay
Simple and interactive UI
🛠️ Technologies Used
Python 🐍
Tkinter (GUI)
PIL (Pillow) for image handling
Random module
📂 Project Structure
snake-game/
│
├── main.py              # Main game file
├── snake_game.png      # Start button image
├── cross.png           # Close button image
├── cross11.jpg         # Exit icon (inside game)
└── README.md

▶️ How to Run
Clone the repository
git clone https://github.com/your-username/snake-game.git
cd snake-game

Install dependencies
pip install pillow

Run the game
python main.py

🎯 Controls
Key	Action
↑ Arrow	Move Up
↓ Arrow	Move Down
← Arrow	Move Left
→ Arrow	Move Right
🧠 Game Logic Overview
The snake moves in a grid of fixed size.
Food is generated randomly on the canvas.
When the snake eats food:
Score increases by 10
Snake grows longer
Game ends if:
Snake hits the wall
Snake collides with itself
🔄 Restart Feature

After Game Over, a Restart button appears:

Resets score
Restarts the game loop
⚙️ Customization

You can easily tweak the game:


SIZE = 30          # Size of snake block
SPEED = 100        # Speed of snake
GAME_WIDTH = 700
GAME_HEIGHT = 650

////////////////////////////////////////////////////////////////////////////////////////////////

🤝 Contributing

Feel free to fork this repo and improve the game!

📜 License

This project is open-source and free to use.

👨‍💻 Author

Harsh Tomar
