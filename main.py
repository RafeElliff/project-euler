#moves right and down
#2 moves available as long as not on furthest right or furthest bottom tile
# Always takes exactly 40 moves to get to end
#therefore 40! possible routes
#as each set of moves has 20 rights and 20 downs, which can be in any order, there will be duplicated. These can be eliminated by dividing our answer(20!)*(20!)

import math
print(math.factorial(40)/math.factorial(20)**2)
#not a lot of code for this one, difficult part was working out the actual maths