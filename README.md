# GridCellNeighborhoods
### Solution to the Counting Grid Cell Neighborhoods problem.

## My Initial Thoughts

My initial gut reaction is to just iterate over every cell in the 2D-grid and mark if it falls into the range of the positive number, but we can do better than that in terms of execution time. **O(w*h)** would be this solution's complexity, I believe.

With that said, I am not entirely sure it can get much better than **O(`total_area_of_neighborhoods`)**. *However*, in cases where there's many, many Neighborhoods and a ton of overlap, depending on how I implement it, this could become even more non-performant than iterating over every single index in the array. This leads me to the following approach:

1) Calculate the potential area of all Neighborhoods, assuming no cut-off or overlap just for simplicity's sake.
2) If the total area would be **MORE** than the area of the grid, we will **iterate over the entire grid**.
3) If the total area would be **LESS** than the area of the grid, we will **iterate over the range of the Neighborhoods only**.

I plan to output execution time to determine if this is *actually* true just out of my own curiosity. I also plan to use a `Set` as this inherently handles duplicates for me.
