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

import math
## Hint: You may want to utilize the following hashDictionary structure in your implementation
## of augmented versions of Dijkstra's Algorithm and A*.
##
## There are 5 public functions in the structure.
##
## insert(vertex_id,cost,data) - inserts neuron vertex_id with a specified cost and
##    supplemental data into the structure
## decrease_key(vertex_id,cost,data) - once neuron vertex_id is inserted into the data
##    structure, you can call decrease_key to reduce the specified cost and replace the
##    supplemental data
## pop() - returns a (vertex_id,cost,data) tuple for the minimum cost neuron
## get_cost(vertex_id) - returns the cost associated with neuron vertex_id.  If vertex_id
##    does not exist in the data structure, this will return None
## is_empty() - returns if the data structure is currently storing any neurons

class hashDictionary():
    def __init__(self):
        self._hashtable = dict()
        self._heap = dict()
        self._numelements = 0

    def insert(self,vertex_id,cost,data):
        self._numelements += 1
        self._heap[self._numelements] = [vertex_id,cost,data]
        self._hashtable[vertex_id] = self._numelements
        self._decrease_key(self._numelements)

    def _min_heapify(self,heap_pos):
        left = 2*heap_pos
        right= 2*heap_pos+1
        cost = self._heap[heap_pos][1]

        swapper = heap_pos

        if((left <= self._numelements) and (self._heap[left][1] < cost)):
            swapper = left
        if((right <= self._numelements) and (self._heap[right][1] < self._heap[swapper][1])):
            swapper = right
        if(swapper != heap_pos):
            self._swap(heap_pos,swapper)
            self._min_heapify(swapper)

    def _swap(self,heap_pos,swapper):
        temp = self._heap[heap_pos]
        self._heap[heap_pos] = self._heap[swapper]
        self._heap[swapper] = temp
        self._hashtable[self._heap[heap_pos][0]] = heap_pos
        self._hashtable[self._heap[swapper][0]] = swapper


    def decrease_key(self,vertex_id,new_cost,new_data):
        old_cost = self._heap[self._hashtable[vertex_id]][1]
        if(old_cost < new_cost):
            raise Exception("Tried to decrease cost from " + old_cost + " to " + new_cost)
        self._heap[self._hashtable[vertex_id]][1] = new_cost
        self._heap[self._hashtable[vertex_id]][2] = new_data
        self._decrease_key(self._hashtable[vertex_id])

    def _decrease_key(self,heap_pos):
        while(heap_pos > 1):
            parent = heap_pos/2
            if(self._heap[heap_pos][1] < self._heap[parent][1]):
                self._swap(heap_pos,parent)
                heap_pos = parent
            else:
                break

    def pop(self):
        if(self._numelements == 0):
            raise Exception("Tried to pop from an empty heap")
        self._swap(1,self._numelements)
        ret = self._heap[self._numelements]
        self._numelements -= 1
        self._min_heapify(1)
        return tuple(ret)

    def get_cost(self,vertex_id):
        if(vertex_id in self._hashtable):
            return self._heap[self._hashtable[vertex_id]][1]
        return None

    def is_empty(self):
        return self._numelements == 0


## Blackbox function
## Set local_mode to True for local testing.  Set local_mode to False for online testing.
local_mode = False
if(local_mode):
  ## Feel free to put a custom local Blackbox function here.
  def Blackbox(signal,cc):
    return signal + cc
else:
  from BlackboxHolder import Blackbox

####################
### Problem 5-3a ###
####################

######################################################################################
## N will be a list of tuples describing neurons                                    ##
##   Each neuron is a list containing an integer ID and a 3D position               ##
##   e.g. (0, (23.949,28.8538,-92.85773))                                           ##
## A will be list describing axons                                                  ##
##   Each axon is a list containing the ID of the parent, the ID of the child,      ##
##   the travel time, and the cognitive coefficient, e.g. (3, 5, 12.948, -1.848)    ##
## Returned result should be a list of (ID, voltage, time) tuples, each             ##
##   representing the voltage and activation time of neuron ID.  You can order the  ##
##   list in any order.                                                             ##
##  e.g. ((0,1,0),(1,3.884,1.283),(2,-3.923,1.733))                                 ##
######################################################################################

def Compute_All_Voltages(N, A):
    # List of neurons to fire
    # Neuron, Voltage, Time
    hashD = hashDictionary()
    hashD.insert(N[0][0], 0, 1)
    # Neurons already activated
    activated_neurons = set()
    # Answer to return
    answer_list = []

    while not hashD.is_empty():
        neuron = hashD.pop()
        # Add activated neuron and append to answers list
        if neuron[0] not in activated_neurons:
            activated_neurons.add(neuron[0])
            answer_list.append(neuron)

            for axon in A:
                # If axon's parent is equal to neuron
                if axon[0] == neuron[0] and axon[1] not in activated_neurons:
                    # Check if it is in there already
                    cost = hashD.get_cost(axon[1])
                    if cost is not None and cost > neuron[1] + axon[2]:
                        hashD.decrease_key(axon[1], neuron[1] + axon[2], Blackbox(neuron[2], axon[3]))
                    else:
                        hashD.insert(axon[1], neuron[1] + axon[2], Blackbox(neuron[2],axon[3]))
    return sorted(answer_list)

####################
### Problem 5-3b ###
####################

######################################################################################
## N will be a list of tuples describing neurons as described previously            ##
## A will be list describing axons as described previously                          ##
## motor will be the ID of the motor neuron                                         ##
## Returned result should be a tuple (voltage, time) of the voltage and activation  ##
##   time of motor                                                                  ##
##  e.g. (23.958, 93.848)
######################################################################################

def Compute_Motor_Voltage(N, A, motor):
    # hashD = hashDictionary()
    # hashD.insert(N[0][0], 0, N[0][1])
    # # Neurons already activated
    # activated_neurons = set()
    # # Answer to return
    # answer_list = []

    # for i in N:
    #     if motor == i[0]:
    #         motor_location = i[1]

    # while !hashD.is_empty():
    #     neuron = hashD.pop()
    #     for i in N:
    #         if i[0] == neuron[0]:
    #             neuron_location = i[1]
    #     if neuron[0] not in activated_neurons:
    #         if neuron[0] == motor:
    #             return (neuron[2], neuron[1])
    #         activated_neurons.add(neuron[0])
    #         answer_list.append(neuron)

    #         for axon in A:
    #             # If axon's parent is equal to neuron
    #             if axon[0] == neuron[0] and axon[1] not in activated_neurons:
    #                 heuristic = math.sqrt((motor_location[1] - neuron_location[1]) * (motor_location[1] - neuron_location[1]) +
    #                                       (motor_location[0] - neuron_location[0]) * (motor_location[0] - neuron_location[0]) +
    #                                       (motor_location[2] - neuron_location[2]) * (motor_location[2] - neuron_location[2]))
    #                 # Check if it is in there already
    #                 cost = hashD.get_cost(axon[1])
    #                 if cost != None and cost < neuron[1] + axon[2]:
    #                     hashD.decrease_key(axon[1], neuron[1] + axon[2], Blackbox(neuron[2], axon[3]))
    #                 else:
    #                     hashD.insert((axon[1], neuron[1] + axon[2], Blackbox(neuron[2],axon[3])))
    # return answer_list

    #         for axon in A:
    #             # If axon's parent is equal to neuron
    #             if axon[0] == neuron[0] and axon[1] not in activated_neurons:
    #                 axon[1]
    #                 queue.append((axon[1], neuron[1] + axon[2], Blackbox(neuron[2],axon[3]), heuristic))
    #         queue = sorted(queue, key=lambda neuron:neuron[1] + neuron[3])
    # return answer_list

    initial_neuron = (N[0][0],0,1)
    queue = [initial_neuron]
    activated_neurons = set()
    answer_list = []
    for i in N:
        if motor == i[0]:
            motor_location = i[1]
    while len(queue) != 0:
        neuron = queue.pop(0)
        for i in N:
            if i[0] == neuron[0]:
                neuron_location = i[1]
        # Add activated neuron and append to answers list
        if neuron[0] not in activated_neurons:
            if neuron[0] == motor:
                return (neuron[2], neuron[1])
            activated_neurons.add(neuron[0])
            answer_list.append(neuron)

            for axon in A:
                # If axon's parent is equal to neuron
                if axon[0] == neuron[0] and axon[1] not in activated_neurons:
                    heuristic = math.sqrt((motor_location[1] - neuron_location[1]) * (motor_location[1] - neuron_location[1]) +
                                          (motor_location[0] - neuron_location[0]) * (motor_location[0] - neuron_location[0]) +
                                          (motor_location[2] - neuron_location[2]) * (motor_location[2] - neuron_location[2]))
                    queue.append((axon[1], neuron[1] + axon[2], Blackbox(neuron[2],axon[3]), heuristic))
            queue = sorted(queue, key=lambda neuron:neuron[1] + neuron[3])
    return sorted(answer_list)



####################
### Problem 5-3d ###
####################

######################################################################################
## N will be a list of tuples describing neurons as described previously            ##
## A will be list describing axons as described previously                          ##
## motor will be the ID of the motor neuron                                         ##
## Returned result should be a tuple (voltage, time) of the voltage and activation  ##
##   time of motor                                                                  ##
##  e.g. (23.958, 93.848)
######################################################################################

def Quick_Motor_Voltage(N, A, motor):
    pass
