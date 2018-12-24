# LEGO Brick Sorter
An automatic LEGO brick sorter created as a final project for our Principles of Engineering (POE) course in the Fall semester of 2018. The system has integrated mechanical, electrical and software components and uses computer vision to detect and classify the bricks.

![Roller](../photos/roller.jpg)

To start the sorter, you turn a crank at the top of the machine until it spits out one brick. This interactive component is in a similar style to the other exhibits in a LEGOLand Discovery Center. We built our machine for a LEGOLand to use to sort LEGOs in an interesting and visually compelling way.

![Roller](../photos/scanner.jpg)

Next, we scan the brick from two angles and use OpenCV to detect color and size of the brick. The OpenCV portion is computued in Python and can be run off of a Raspberry Pi. The output of the computer vision software then uses the serial input to communicate to an Arduino that controlls a stepper motor and a servo. 

![Disk](../newestSite/images/disk.jpg)

A motor shield attached to the Arduino then tells the stepper motor how much to turn so that it positions the disk to put the correct cup into place. Finally, after a delay, the Arduino then communicates to a servo to drop the brick onto the slide and into the cup.

I created a website to explain the functions and operations of our final product. Check it out at http://poe.olin.edu/2018/LEGpOe/

Anna Griffin worked on the OpenCV portion of the sorter. Check out more of her work at https://github.com/annagriffin
