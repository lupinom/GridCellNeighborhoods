# GridCellNeighborhoods
### Solution to the Counting Grid Cell Neighborhoods problem.

## My Initial Thoughts

My initial gut reaction is to just iterate over every cell in the 2D-grid and mark if it falls into the range of the positive number, but we can do better than that in terms of execution time. **O(w*h)** would be this solution's complexity, I believe.

With that said, I am not entirely sure it can get much better than **O(`total_area_of_neighborhoods`)**, so I will be mapping out the Neighborhoods as I find them in the array and adding the indices to a `Set` so it auto-handles duplication.

This also would be a good opportunity for me to try Test-Driven Development (TDD), so the test cases for this project are going to be written before the actual solution.