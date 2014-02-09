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

from matplotlib.pyplot import plot
from random import randint

def main():
    # The points to test the heuristics
    P = [-21, -5, -1, 0, 1, 3, 11]
    NearestNeighbor(P)
    ClosestPair(P)

def NearestNeighbor(P):
    if P is not None:
        lenP = len(P)
        ind_p_0 = randint(0,lenP-1)
        p_0 = P[ind_p_0]
        i = 0
        while i <= lenP-1:
            i = i + 1
            # Which is nearest point?  Add current points value to all elements
            # The smallest element of the result will be closest

def ClosestPair(P):
    return 1

if __name__ == "__main__":
    main()
