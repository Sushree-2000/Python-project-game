STEPS TO DEVELOP TETRIS:
1) Install PyGame
2) Setup the Game loop
3) Creating the Grid
4) Create the blocks
5) Move the blocks
6) Rotate the blocks
7) Checking for collisions
8) Check for completed rows
9) Game Over
10) Create User Interface
11) Add Score
12) Add next block
13) Add Sounds


Game Structure:
- Definitions:
  - Defining the variables needed
  - Creating the game objects
- Game Loop:
  - Updating the positions of the game objects
    - Event Handling
    - Updating Positions
    - Drawing Objects
  - Checking for collisions
- Create Grid:
  - How pygame draws:
      1) Display surface: It's like a blank Canvas. We can only have one per game.
          -> Created by: "screen = pygame.display.set_mode((300, 600))"
          -> Used as: "pygame.display.update()"
      2) Surface: Another type of blank canvas. We can have many surfaces per game.
      3) Rect: Rectangles are used for positioning, collision detection and for drawing objects.
- Create blocks:
  - L, J, I, O, T, S, Z blocks, with their middle point as rotating block
  - Their rotation logic:
      -> For ex: T => (0,1), (1,0), (1,1), (1,2)
          => rotate right: (0,1), (1,1), (1,2), (2,1)
          => rotate down: (1,0), (1,1), (1,2), (2,1)
          => rotate left: (0,1), (1,0), (1,1), (2,1)
  - Colors represent as tuple
- Move the blocks:
  - Change the block poisitions to move them from the initial position (0,0) to different.
- Rotate the blocks:
  - Add rotation and undo_rotation functionalities
- Checking for collisions:
- Checking for completed rows:
  



Game Class
===========
- It will be a container for all the elements of our game. 
- It will also hold all the game logics. So that the codes will be easier to understand maintain, expand.
- Codes will be easier to read and reduce the risk of bugs.