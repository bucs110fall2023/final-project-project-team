[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803402&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Space Invaders
## CS110 Final Project  << Fall, 2023 >>

## Project Team

Nicholas Gonzalez, Amadou Barrie
***

## Project Description

We plan on making a game based on "Space Invaders". We want to implement a movable character, enemies and a level system. The basics of what we want to do is control a player that can shoot, and have increasing enemies that move around avoiding the lasers.
***    

## GUI Design

### Initial Design

![initial gui](assets/gui.png)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Levels
2. Increasing Difficulty
3. Shootable laser
4. Moveable player
5. Enemies

### Classes

- Controller
- Alien
- Player
- Laser

## ATP
Test Case 1: Player Movement
Test description: The player moves in the desired direction(s)
Test steps:
1. Press and hold left key
2. Player moves left
3. Press and hold right key
4. Player moves right
Expected outcome: Player should only move left and right when the left or right keys are pressed.
Test Case 2: Collision Detection
Test description: Verify that when the player's laser hits an alien, the alien is removed
Test steps:
1. Fire a laser in the direction of an alien
2. See if the alien is gone
3. Fire a laser and miss an alien
4. See if the alien is still there
Expected outcome: An alien should be removed from the screen when a laser makes contact with it.
Test Case 3: Player's laser
Test description: Verify that the laser correctly fires
Test steps:
1. Press space
2. See if a red laser fires from the player ship
3. Press and hold space
4. See if laser only shoots once
Expected outcome: A red laser fires once every time spacebar is pressed.
Test Case 4: Level increase
Test description: Verify that when all aliens are gone, more appear.
Test steps:
1. Hit all aliens on the screen
2. See if more appear on the screen for a maximum of 5 times(5 levels)
3. Game closes after 5 levels
Expected outcome: User is able to play 5 levels of reappearing aliens
Test Case 5: Laser Collision
Test description: Verify that when a laser hits an alien, it does not hit other aliens
Test steps:
1. Shoot a laser in the direction of an alien
2. See if when the laser makes contact with an alien, it stops and doesn't go through. 
Expected outcome: The laser stops once it makes contact with an alien

