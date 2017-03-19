#!/usr/bin/python
from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        print('init State(...)')
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:] #copy list value
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
            # self.solver = parent.solver
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
            # self.solver = solver

    def GetDist(self):
        pass
    def createchildren(self):
        pass

class State_String(State):
    """docstring for ClassName"""
    def __init__(self, value, parent, start=0, goal=0):
        # ClassName is supposed
        #super(State_String, self).__init__(value, parent, start, goal)
        super().__init__(value, parent, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        print('state_strign.getdis')
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def createchildren(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2]
                child = State_String(val, self)
                self.children.append(child)

class AStart_Solver:
    """docstring for ClassName"""
    def __init__(self, start, goal):
        print("Initializing AStarat_Solver")
        self.path = []
        self.visitedqueue = [] # prevent visiting children twice
        self.priorityqueue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        startstate = State_String(self.start, 0, self.start, self.goal)
        count = 0
        print('pushing to priorityqueue')
        self.priorityqueue.put((0, count, startstate))
        print('pushed to priorityqueue')
        # while self.path is not null and priorityqueue has size
        while not self.path and self.priorityqueue.qsize():
            closestchild = self.priorityqueue.get()[2]
            closestchild = startstate.createchildren()
            self.visitedqueue.append(closestchild.value)
            for child in closestchild.children:
                if child.value not in self.visitedqueue:
                    count += 1
                    if not child.dist:
                         # solution found
                        self.path = child.path
                        break
                    self.priorityqueue.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible")
        return self.path

"""
class ClassName(object):
    #docstring for ClassName
    def __init__(self, start, goal):
        self.path = []
        self.visitedQueue = []
        self.priorityqueue = priorityqueue()
        self.start = start
        self.goal = goal
    def Solve(self):
        startstate = State_String(self.start, 0, self.start, self.goal, self)
        count = 0
        self.priorityqueue.put((o, count, startstate))
        while(not self.path and self.priorityqueue.qsize):
"""
##==============================================
## Main

if __name__ == '__main__':
    start1 = "hma"
    goal1 = "ham"
    print("starting...")
    a = AStart_Solver(start1, goal1)
    print('about to call a.solve()')
    a.solve()
    for i in range(len(a.path)):
        print("{0}) {1}".format(i, a.path[i]))
