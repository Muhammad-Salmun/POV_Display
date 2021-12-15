# POV_Display

Turtle is used to simulate the moving hand of the pov display
For installing in Ubuntu Linux, use:
  'sudo apt-get install -y python3-wxgtk4.0'
  
```
function test() {
  console.log("notice the blank line before this function?");
}
```

30 turtles travelling in a circle of radius ranging from 0 to number to turtles
they move at 1 degree per move while up() is employed
turtle uses polar coordinates for navigation
hence the algorithm returns a list of all the points to activate the led in cartesian cordinate system

The algoirthm takes starting and ending points of line to be drawn
fomulates a vector equation of the line
finds the collission point of this line and circle with provided radius
parameters of line and circle is collected mandaterly using classes
for more details refer: https://codereview.stackexchange.com/questions/86421/line-segment-to-circle-collision-algorithm
the radius of circle is iterated from 0 to total number of leds
later the points are converted to polar using cart2pol code file

cart2pol uses the basic equation r(rho) = √ ( x2 + y2 ) | θ = tan-1 ( y / x )
from numpy library 'pip install numpy' makes use of arctan() function
the output is in radians which is converted to degrees using rad2deg()



