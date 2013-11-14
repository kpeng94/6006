## You are NOT required to use this file to solve problem set 5, but we thought that
## these supplemental functions may help you with testing.



## You can use generate_graph to generate visualizations of neural networks.
## 
## Run generate_graph(N,A,filename) where N is a list of neurons and A is a list of axons.
## The function will output a png visualization of the neural network named filename
## Example: generate_graph([(0,(1.18,0.27,0.35)),(1,(0.84,2.17,-0.11)),(2,(2.88,1.89,0.84)),(3,(0.35,4.87,-0.48)),(4,(1.55,6.15,0.33))],[(0,1,2.13,1.21),(1,3,3.78,1.86),(3,4,2.98,2.14),(0,2,3.51,2.05),(2,4,5.93,1.21)],'outputgraph.png')    
##
## This file uses dot, which is an executable associated with graphviz.  You can manually
## set up graphviz, or you can use an Athena workstation which has graphviz already installed.
import os

def generate_graph(N,A,filename):
    gvfile = open('temp.gv','w')
    gvfile.write("digraph G {\n")
    for neuron in N:
        neuron[0]
        line = "  " + str(neuron[0]) + " [label = \"" + str(neuron[0]) + ": " + str(neuron[1]) + "\"];\n"
        gvfile.write(line)
    for axon in A:
        line = "  " + str(axon[0]) + " -> " + str(axon[1]) + " [label = \"TT: " + str(axon[2]) + "\\nCC: " + str(axon[3]) + "\"];\n"
        gvfile.write(line)
    gvfile.write('}\n')
    gvfile.close()
    os.system("dot -o" + filename + " -Tpng temp.gv")
    
## You can use create_random_graph to create a random neural network
## n is the number of neurons
## e is the (rough) number of axons per neuron
## motor is the ID of the motor neuron
##
## This function will return a random neural network in which there is a guaranteed path from neuron 0 to motor

import random
import math
def calculate_distance(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2 + (pos1[2]-pos2[2])**2)

def create_random_graph(n,e,motor):
  random.seed()
  N = []
  A = []
  marked = dict()
  for i in xrange(n):
    marked[i] = dict()
    marked[i][i] = True
    
  for i in xrange(n):
    N.append((i,(random.uniform(-10,10),random.uniform(-10,10),random.uniform(-10,10))))
  
  for i in xrange(n):
    dist = dict()
    for j in xrange(n):
      if(not(j in marked[i])):
          dist[j] = calculate_distance(N[i][1],N[j][1])
    sorteddist = sorted(dist.items(),key=lambda x:x[1])
    ##Add e-1 edges
    for j in xrange(e-1):
      minvert = sorteddist[0][0]
      sorteddist.pop(0)
      if(not(minvert in marked[i])):
        A.append((i,minvert,random.uniform(1.0,1.3)*calculate_distance(N[i][1],N[minvert][1]),random.random()+1))
        marked[i][minvert] = True
      
    ##Add another random edge to prevent local cliques    
    randvert = random.randint(0,n-1)
    if(not(randvert in marked[i])):
      A.append((i,randvert,random.uniform(1.0,1.3)*calculate_distance(N[i][1],N[randvert][1]),random.random()+1))
      marked[i][randvert] = True
  
  ## create a path that starts from neuron 0, goes through every node and ends with motor
  mchoices = range(n)
  mchoices.remove(0)
  mchoices.remove(motor)
  curNode = 0
  while(len(mchoices) > 0):
    ind = random.choice(mchoices)
    mchoices.remove(ind)
    if(not (ind in marked[curNode])):
      A.append((curNode,ind,random.uniform(1.0,1.3)*calculate_distance(N[curNode][1],N[ind][1]),random.random()+1))
    curNode = ind
  A.append((curNode,motor,random.uniform(1.0,1.3)*calculate_distance(N[curNode][1],N[motor][1]),random.random()+1))
  return (N,A)

