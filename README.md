\# Snake Game (Python)

\## Project Description This is a classic \*\*Snake Game\*\* implemented
in Python using the \`turtle\` library. The player controls the snake to
collect red food on the screen, grow in length, and avoid collisions
with the walls or its own tail.

\## Technologies Used - Python 3.x  - \`turtle\` library (for graphics
and user input)  - \`time\` library (to control game loop speed)  -
\`random\` library (for random food placement)

\## Features - Keyboard controls: \*\*W, A, S, D\*\*  - Snake grows as
it eats food  - Real-time score display  - Game ends when the snake hits
the wall or itself  - Food spawns at random positions

\## Installation and Running 1. Make sure Python 3 is installed on your
machine. 2. Place the following files in the same directory:  -
\`main.py\` (main game loop)  - \`snake.py\` (snake class)  -
\`food.py\` (food class)  - \`score_board.py\` (scoreboard class) 3. Run
the game using your terminal or IDE: \`\`\`bash python main.py \`\`\` 4.
Control the snake using the \*\*W, A, S, D\*\* keys and enjoy the game.

\## Code Structure - \*\*main.py\*\*: Initializes the game screen,
snake, food, and scoreboard. Contains the main game loop.  -
\*\*snake.py\*\*: Defines the snake class, including movement, direction
control, segment addition, and tail collision detection.  -
\*\*food.py\*\*: Creates the food object and randomly spawns it on the
screen.  - \*\*score_board.py\*\*: Manages the score display and the
\"Game Over\" message.

\## Game Mechanics 1. The snake starts with 3 segments. 2. Eating food
increases the snake length by one segment and increases the score by 1.
3. The game ends if the snake hits the wall or its own tail, displaying
a \"Game Over\" message.

\## Development Notes - The \`turtle\` library is used for simple
graphics and animation.  - The game speed can be adjusted with
\`time.sleep()\`.  - Future enhancements could include score saving,
level progression, and more advanced graphics.
