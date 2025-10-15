# GridCellNeighborhoods
### Solution to the Counting Grid Cell Neighborhoods problem.

## My Initial Thoughts

My initial gut reaction is to just iterate over every cell in the 2D-grid and mark if it falls into the range of the positive number, but we can do better than that in terms of execution time. **O(w*h)** would be this solution's complexity, I believe. And then there's additional complexity because for each index, I would need to check if it falls into the range of *any* Neighborhood, which means iterating over every Neighborhood origin per square on the grid until you've exhausted the origins or until you've found an origin that's in range of the current index on the grid.

With that said, I am not entirely sure it can get much better than **O(`total_area_of_neighborhoods`)**, so I will be mapping out the Neighborhoods as I find them in the array and adding the indices to a `Set` so it auto-handles duplicates.

This also would be a good opportunity for me to try **Test-Driven Development (TDD)**, so the test cases for this project are going to be written before the actual solution.


## Final Implementation Comments

I did end up taking the TDD approach with this one, and it worked out fine, but I ended up having to implement more test cases after finishing my implementation to fill out a few more edge cases.

The steps for implementation are as follows:

1) Check for valid `neighborhood_range` and then return a `ValueError` if not valid
2) Check if the grid is empty and return `0` if so
3) Find all the coordinates with positive integers and add it to a list
4) Skip further processing if `neighborhood_range` is greater than (grid dimensions - 2) and return the size of the grid
5) Find each neighbor for each positive coordinate using the [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html) formula
6) Return the size of the set
