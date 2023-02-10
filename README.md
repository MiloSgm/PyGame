# PyGame

## Task 00 -Instalation
    The very first step is to import the pygame lib in your .py file  and to install it (don't forget to give the rights to your .py file (chmod +x)).
    
    pip install pygame

## Task 01 -Create a window:
    The very first step is to import the pygame lib in your .py file and to install it (don't forget to give the rights to your .py file (chmod +x)). 
    Then just open your window.
    
## Task 02 -Event close:
    After that you can now create a function Def game_loop() with the opening of your window.
    You can now manage the envent to close your window but also be able to close your window with the escape key.
    
## Task 04 -Event escape 
     Now, let's add a new event
     your game has to close when you press the escape button
     
## Task 05 -Background
    you will now learn how to draw some things on the window
    First, let's draw a background
    Create a function draw_game() that will draw your all the stuff you need on your screen
    For now, just make it draw a blue rectangle on the entire screen 

## Task 06 -Pads
    Let's get started for real now and start coding the game
    create a class Pad() that will have
    -the following variables:
    x, y -> position
    width, height -> shape
    speed -> movement speed
    score -> (no comments)
    k_up, k_down -> bool that will be usefull for the inputs
    -and the method draw() that will draw himself, you can just draw a white rectangle

## Task 07 -Move
    Create a new function called get_inputs() that will set the k_up to True when you are pressing the up key and false when you are not
    (you can do the same for k_down)
    Now, add a new method to your Pad() class: move().
    the move() method will just move the pad depending on the variables k_up and k_down
    
## Task 08 -Ball
    What would Pong be without a ball ?
    You guess it, it's now time to add a ball to your game !
    Create a class Ball() with the following variables:
    x, y -> position
    radius -> shape
    speed -> movement speed (that will increases)
    hspeed, vspeed -> vertival / horzontal speed
    -and the method draw() that will draw the ball, you can just draw a white circle
    
## Task 09 -Move_Ball
    Add a move() method to the class Ball()
    This method will just move the ball depending on its horizontal speed (hspeed * speed) and its vertical speed (vspeed * speed)
    Upgrade the get_inputs() function to move the ball when you press the space key (only when the ball is not moving)
    
## Task 10 -Collision
    Your ball should now move but pass through the pads and walls. Too bad, this game is no fun, let's ass collisions.
    In the move() method of your class Ball(), add the collisions.
    If the ball is about collide with the walls up and down, reverse its vspeed
    If the ball is about collide with one of the pads, reverse its hspeed
    Add the reset() method to your class Ball(), when you call it, it should stop the ball and put it back to the middle of the screen
    When the ball pass get out of the screen, call its reset() method
    
## Task 11 -Acceleration
    Let's add some fun to this poor game.
    When the ball collide with a pad increase its speed, that way, the game will surely become harder?
    
## Task 12 -Score
    If there is no score, there is no competition. If there is no competition, there is no fight. If there is no fight, there is no fun.
    You guessed it right, you will have to implement the score
    When the ball get out of the screen by the right, the left player should get a point, when it get out by the left, the right player should get the point
    For now, print on the terminal when a player score a point.
    
## Task 13 -Draw_Score
    Who look at the terminal playing pong ?
    Let's draw the score on the screen.
    When the ball is not moving, draw the score of each player on their side.

## Task 14 -Win
    This game is becoming more and more boring, the score is 56 to 0 but i didn't win yet ???
    You should add a win / lose system: when a player come to score 3 points, he wins.
    Add an endscreen, when a player won you should display it to make his pride grow.
    
## Task 15 -Restart
    When you get to your end screen you should be able to start a new game.
    In you end screen add a button or just a key binding to restart your game.
    Here you are your pong is finish, now you can play continually and destroy your
    friends again and again to make the jealous of your innate talent.

