import math
from queue import PriorityQueue

def distance_calculator(start_coordinate,end_coordinate):
    x1,y1=start_coordinate
    x2,y2=end_coordinate
    return math.sqrt((x1-x2) ** 2 +(y1-y2)** 2)

def shortest_path(M,start,goal):
    frontier=PriorityQueue()
    visited=set()
    camefrom=[math.inf for _ in range (len(M.roads))]
    gscore=[math.inf for _ in range (len(M.roads))]
    fscore=[math.inf for _ in range (len(M.roads))]
    gscore[start]=0
    fscore[start]=distance_calculator(M.intersections[start],M.intersections[goal])
    frontier.put((0,start))
    while frontier:
        current_path=frontier.get()
        current_list=current_path
        current_node=current_list[-1]
        visited.add(current_node)
        
        if current_node==goal:
            return reconstruct_path(camefrom, current_node,start)
        
        for a in M.roads[current_node]:
            if a not in visited:
                total_distance=gscore[current_node]+distance_calculator(M.intersections[current_node],M.intersections[a])
                if total_distance>=gscore[a]:
                    continue
                gscore[a]=total_distance
                total_score=gscore[a]+distance_calculator(M.intersections[a],M.intersections[goal])
                camefrom[a] = current_node
                if total_score < fscore[a]:
                    fscore[a]=total_score
                    frontier.put((fscore[a],a))
                    
    return
def reconstruct_path(camefrom, current_node,start):
    total_path = [current_node]
    while current_node !=start:
        current_node= camefrom[current_node]
        total_path.append(current_node)
    total_path.reverse()
    return total_path
    
                  