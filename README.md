# Mini-project description - Pong

In this project, we will build a version of Pong, one of the first arcade video games (1972). While Pong is not particularly exciting compared to today's video games, Pong is relatively simple to build and provides a nice opportunity to work on the skills that you will need to build a game like Asteroids. As usual, we have provided a program template that can be used to guide your development of Pong.

Mini-project development process
Add code to the program template that draws a ball moving across the Pong table. We recommend that you add the positional update for the ball to the draw handler as shown in the second part of the "Motion" video.

Add code to the function $$\color{red}{\verb|spawn_ball|}$$ that spawns a ball in the middle of the table and assigns the ball a fixed velocity (for now). Ignore the parameter $$\color{red}{\verb|direction|}$$ at this point.

Add a call to $$\color{red}{\verb|spawn_ball|}$$ in the function $$\color{red}{\verb|new_game|}$$ which starts a game of Pong. Note that the program template also includes an initial call to $$\color{red}{\verb|new_game|}$$ in the main body of your program to get a game going immediately.

Modify your code such that the ball collides with and bounces off of the top and bottom walls. Experiment with different hard-coded initial velocities to test your code.

Add randomization to the velocity in $$\color{red}{\verb|spawn_ball(direction)|}$$ The velocity of the ball should be upwards and towards the right if $$\color{red}{\verb|direction == RIGHT|}$$ and upwards and towards the left if $$\color{red}{\verb|direction == LEFT|}$$. The exact values for the horizontal and vertical components of this velocity should be generated using $$\color{red}{\verb|random.randrange()|}$$. For the horizontal velocity, we suggest a speed of around $$\color{red}{\verb|random.randrange(120, 240)|}$$ pixels per second. For the vertical velocity, we suggest a speed of around $$\color{red}{\verb|random.randrange(60, 180)|}$$ pixels per second. (You will need to set the signs of velocities appropriately.)

Add code to the draw handler that tests whether the ball touches/collides with the left and right gutters. (Remember that the gutters are offset from the left and right edges of the canvas by the width of the paddle as described in the "Pong" video.) When the ball touches a gutter, use either $$\color{red}{\verb|spawn_ball(LEFT)|}$$ or $$\color{red}{\verb|spawn_ball(RIGHT)|}$$ to respawn the ball in the center of the table headed towards the opposite gutter.

Next, add code that draws the left and right paddles in their respective gutters. The vertical positions of these two paddles should depend on two global variables. (In the template, the variables were $$\color{red}{\verb|paddle1_pos|}$$ and $$\color{red}{\verb|paddle2_pos|}$$.)

Add code that modifies the values of these vertical positions via an update in the draw handler.  The update should reference two global variables that contain the vertical velocities of the paddles. (In the template, the variables were $$\color{red}{\verb|paddle1_vel|}$$ and $$\color{red}{\verb|paddle2_vel|}$$.)

Update the values of these two vertical velocities using key handlers. The "w" and "s" keys should control the vertical velocity of the left paddle while the "Up arrow" and "Down arrow" key should control the velocity of the right paddle. In our version of Pong, the left paddle moves up at a constant velocity if the "w" key is pressed and moves down at a constant velocity if the "s" is pressed and is motionless if neither is pressed. (The motion if both are pressed is up to you.) To achieve this effect, you will need to use both a keydown and a keyup handler to increase/decrease the vertical velocity in an appropriate manner.

Restrict your paddles to stay entirely on the canvas by adding a check before you update the paddles' vertical positions in the draw handler. In particular, test whether the current update for a paddle's position will move part of the paddle off of the screen. If it does, don't allow the update.

Modify your collision code for the left and right gutters in step 6 to check whether the ball is actually striking a paddle when it touches a gutter. If so, reflect the ball back into play. This collision model eliminates the possibility of the ball striking the edge of the paddle and greatly simplifies your collision/reflection code.

To moderately increase the difficulty of your game, increase the velocity of the ball by 10% each time it strikes a paddle.

Add scoring to the game as shown in the Pong video lecture. Each time the ball strikes the left or right gutter (but not a paddle), the opposite player receives a point and ball is respawned appropriately.

Finally, add code to $$\color{red}{\verb|new_game|}$$ which resets the score before calling $$\color{red}{\verb|spawn_ball|}$$. Add a "Restart" button that calls $$\color{red}{\verb|new_game|}$$ to reset the score and relaunch the ball.

Your final version of Pong should be remarkably similar to the original arcade Pong game. Our full implementation of Pong took a little more than 100 lines of code with comments. For more helpful tips on implementing this mini-project, please visit the Code Clinic Tips page for this mini-project.
