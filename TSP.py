# From The Algorithm Design Manual by Skiena
# Problem 1-26
#Implement the two TSP heuristics of section 1.1 (page 5).
#Which of them gives better-quality solutions in practice?
#Can you devise a heuristic that works better than both of
#them?
#
# Hueristic #1:  Nearest Neighbor
#NearestNeighbor(P)
#    Pick and visit an initial point p_0 from P
#    p = p_0
#    i = 0
#    While there are still unvisited points
#        i = i + 1
#        Select p_i to be the closest unvisited point to p_(i-1)
#        Visit p_i
#    Return to p_0 from p_(n-1)
#
#Heuristic #2:  ClosestPair(P)
#    Let n be the number of points in set P
#    For i=1 to n-1 do
#        d = inf
#        For each pair of endpoints (s,t) from distinct vertex chains
#            if dist(s,t) <= d then s_m = s, t_m = t, and d = dist(s,t)
#        Connect (s_m,t_m) by an edge
#    Connect the two endpoints by an edge
#
#
#  NOTE: ONLY IMPLEMENTED NEAREST NEIGHBOR

from matplotlib.pyplot import plot
from random import randint

def main():
    P = [-21, -5, -1, 0, 1, 3, 11]
    # The points to test the heuristics
    print NearestNeighbor(P)
    #ClosestPair(P)

def NearestNeighbor(P):
    if P is not None:
        lenP = len(P)
        ind_p = randint(0,lenP-1)
        p = P[ind_p]
        i = 0
        total_distance = 0
        while i <= lenP-1:
            print "We are at point", p
            print "P looks like ",P
            i = i + 1
            distance, nearestNeighborInd = NearestPoint(P,p)
            total_distance = total_distance + distance
            print "The index of nearest neighbor is ",nearestNeighborInd
            p = P[nearestNeighborInd]
            print "Its nearest neighbor is",p
            print "Distance to travel is ",distance
            P = pop_ind(ind_p,P)
            print "After popping the old point, P now looks like ",P
            print "len of P is ",len(P)
            ind_p = find(p,P)
            print "current index of p is ",ind_p
            if len(P) == 1:
                print "We are at the end, return to zero"
                total_distance = total_distance + abs(P)[0]
                break
        return total_distance

def NearestPoint(P,p):
    #find the nearest neighbor to p in P, then determine the distance
    #normalize P to p's coordinate
    normalized_distances = []
    for i in xrange(len(P)):
        element = P[i]
        normalized_distances.append(element - p)
    distance, ind = min_distance(normalized_distances)
    return distance, ind 

def testNearestPoint():
     P = [-21, -5, 3, 11]
     p = 3
     print NearestPoint(P,p)

     P = [-21, -5, 11]
     p = 11
     print NearestPoint(P,p)

def pop_ind(ind,list):
    list_new = list[:ind]
    list_new.extend(list[ind+1:])
    return list_new

def find(val, list):
    try:
        ind = []
        for i in xrange(len(list)):
            if val == list[i]:
                ind = i
                return ind
        if ind == []:
            print "Element not found"
            return []
    except:
        print "Error: check inputs"

def min_distance(list):
    if list == []:
        return []
    else:
        list = abs(list)
        #find first none zero element to initialize search
        for i in xrange(len(list)):
            if list[i] != 0:
                min = list[i]
                min_ind = i # in case min is indeed the minimum, we must return its index
        for i in xrange(len(list)):
            if list[i] < min and list[i] > 0: #greater than zero, otherwise closest point is itself! :)
                min = list[i]
                min_ind = i
        return min, min_ind
        
def abs(list):
    if list == []:
        return []
    else:
        for i in xrange(len(list)):
            if list[i] < 0:
                list[i] = -1*list[i]
        return list

def ClosestPair(P):
    return 1

if __name__ == "__main__":
    main()
    #testNearestPoint()
