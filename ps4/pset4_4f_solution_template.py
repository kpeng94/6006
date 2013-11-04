# This solution template should be turned in through our submission site, at
# https://alg.csail.mit.edu

######################################################################################
### WARNING:                                                                       ###
### Be sure to write the Python code yourself!  We do run sophisticated automated  ###
### comparisons between each pair of programs turned in.  We are saddened and      ###
### troubled each year when a few studentsturn in nearly identical programs, and   ###
### we have to administer appropriate consequences.  It is better to turn in a     ###
### statement that you didn't have time to complete the assignment than to turn in ###
### the same code as someone else.                                                 ###
######################################################################################


####################
### Problem 4-4f ###
####################

######################################################################################
## N will be an integer, e.g. 4                                                     ##
## B will be a tuple of tuples rep'ing boulder locations, e.g. ((1,1),(2,2))        ##
## C will be a tuple of tuples rep'ing car locations, e.g. ((0,0),(0,3),(2,1),(3,2))##
## Returned result should be a list of tuples of tuples each rep'ing a move         ##
## e.g. [((0,3), (0,2)), ((3,2), (3,1)), ((3,1), (2,1)), ((0,2), (0,1)),            ##
##       ((0,1), (0,0)), ((0,0), (1,0)), ((1,0), (2,0)), ((2,0), (2,1))]            ##
######################################################################################

class DemoDerbyState:
  def __init__(self, car_locations, moves_set, move, parent):
    self.car_locations = car_locations
    self.moves_set = moves_set
    self.move = move
    self.parent = parent

### Implement me! ###
def DemoDerby(N, B, C):
  possible_locations_to_go_to = set()
  car_locations = set()
  # Map all points to a N + 2 by N + 2 grid
  # The padding is for the movement later
  # We add (1,1) so that the grid is centered properly
  for i in xrange(N):
    for j in xrange(N):
      possible_locations_to_go_to.add((N + 2) * (i + 1) + (j + 1))
  for boulder in B:
    boulder_loc = (N + 2) * (boulder[0] + 1) + (boulder[1] + 1)
    possible_locations_to_go_to.remove(boulder_loc)
  for car in C:
    car_location = (N + 2) * (car[0] + 1) + (car[1] + 1)
    car_locations.add(car_location)
  # States needs to be a list for BFS
  queue = []
  moves_set = set()
  visited_car_locations = set()
  # State is a board + moves made so far
  queue.append(DemoDerbyState(car_locations, moves_set, None, None))
  while len(queue) > 0:
    currentState = queue.pop(0)
    current_car_locations = currentState.car_locations
    current_moves_set = currentState.moves_set
    for car_location in current_car_locations:
      # Get the new car locations for each car_location
      new_car_location_tuples = [car_location - (N + 2),
                                 car_location + (N + 2),
                                 car_location - 1,
                                 car_location + 1]
      for new_car_location in new_car_location_tuples:
        # Create a new move
        move = (car_location, new_car_location)
        # DP for checking whether this is already in the current_move_set
        # and whether it is valid
        if move not in current_moves_set and new_car_location in possible_locations_to_go_to:
          # modify new car locations to contain the right locations for the
          # cars
          new_car_locations = current_car_locations.copy()
          new_car_locations.remove(car_location)
          new_car_locations.add(new_car_location)
          if new_car_locations not in visited_car_locations:
            new_moves_set = current_moves_set.copy()
            new_moves_set.add(move)
            if (len(new_car_locations) == 1):
              moves_list = []
              moves_list.append(move)
              state = currentState
              while state.move != None:
                moves_list.append(state.move)
                state = state.parent
              moves_list.reverse()
              return moves_list
            queue.append(DemoDerbyState(new_car_locations, new_moves_set, move, currentState))
            visited_car_locations.add(new_car_locations)
  return None


N=2
B=()
C=((0, 0), (1, 1))
print DemoDerby(N, B, C)

N=3
B=((1, 1), (1, 0))
C=((0, 0), (0, 2), (2, 0), (2, 2))
print DemoDerby(N, B, C)

N=4
B=((1, 1), (2, 2))
C=((0, 0), (0, 3), (2, 1))
print DemoDerby(N, B, C)

N=4
B=()
C=((0, 0), (0, 3), (1, 2))
print DemoDerby(N, B, C)

N=4
B=((1, 1), (2, 2))
C=((0, 0), (0, 3), (2, 1), (3, 2))
print DemoDerby(N, B, C)

# N=5
# B=((1, 1), (2, 2), (3, 3))
# C=((0, 0), (4, 4), (1, 2), (3, 2))
# print DemoDerby(N, B, C)
