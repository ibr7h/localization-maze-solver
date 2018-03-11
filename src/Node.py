class Node(object):
    HEURISTIC_DISTANCE_MULTIPLIER = 1;
    TRAVELLED_DISTANCE_MULTIPLIER = 1;

    def __init__(self,x,y):
        self.position = (x,y)

    def get_priority(self,end,length):
        return ( self.TRAVELLED_DISTANCE_MULTIPLIER*length +
               self.HEURISTIC_DISTANCE_MULTIPLIER+self.get_heuristic(end))

    def get_heuristic(self,end):
        return ((end.position[0]-self.position[0])
                + (end.position[1] - self.position[1]))