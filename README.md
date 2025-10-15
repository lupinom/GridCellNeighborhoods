# GridCellNeighborhoods
### Solution to the Counting Grid Cell Neighborhoods problem.

## My Initial Thoughts

My initial gut reaction is to just iterate over every cell in the 2D-grid and mark if it falls into the range of the positive number, but we can do better than that in terms of execution time. **O(w*h)** would be this solution's complexity, I believe. And then there's additional complexity because for each index, I would need to check if it falls into the range of *any* Neighborhood, which means iterating over every Neighborhood origin per square on the grid until you've exhausted the origins or until you've found an origin that's in range of the current index on the grid.

With that said, I am not entirely sure it can get much better than **O(`total_area_of_neighborhoods`)**, so I will be mapping out the Neighborhoods as I find them in the array and adding the indices to a `Set` so it auto-handles duplicates.

This also would be a good opportunity for me to try **Test-Driven Development (TDD)**, so the test cases for this project are going to be written before the actual solution.
