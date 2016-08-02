# CVMazeRunner
A python program that uses OpenCV to process and solve an image of a maze

On long car trips as a kid I used to love to solve mazes to pass the time. Now, as a programmer, I'm hoping to give my laptop a similar experience. 

The program can solve the mazes in the test images folder. It uses opencv to run image processing to smooth out and threshold the image. Afterwards, a version of A* is used to compute the solution to the maze.

To improve performance, the algorithm first calculates the average width of the passages in the image. It then breaks the maze down ito blocks of nxn size where n is the width of the corridors. Although this approach may miss smaller passages or shortcuts, it allows the program to vastly improve performance, especially on mazes where passages are very wide. 

To try it out for yourself, simply run the setup.py file. You will be prompted for a png maze file. Feel free to try those test images folder, or try out your own images. From there, you can select your own start/end points. Alternately, you can let the program pick for you. It's default start points are either the first opening in the top and bottom of the maze or the midpoint of the top and bottom of the maze. 

I hope you enjoy trying out this program!


Sample Maze:
![Maze Sample Image](test images/Sample Maze 2.png)


