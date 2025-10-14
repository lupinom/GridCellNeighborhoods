'''
PSEUDOCODE:

Parameters given: N range, 2D grid
Logical steps to take:
1) Iterate over the grid
2) Add coordinates of positive integers to a list
3) For each coordinate in the list, iterate over its neighborhood range
4) Add each coordinate in the neighborhood to a Set (to avoid duplicates)
5) Return the size of the Set

'''