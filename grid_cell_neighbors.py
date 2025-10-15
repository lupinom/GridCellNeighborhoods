'''
This module provides a function to count unique neighboring cells in a 2D grid
within a specified Manhattan distance from cells containing positive integers.
'''

'''
:param grid: 2D list of integers
:param neighborhood_range: non-negative integer defining the Manhattan distance
:return: integer count of unique neighboring cells within neighborhood_range of any positive integer cell
'''
def count_neighbors(grid, neighborhood_range):
    # Check for valid neighborhood_range
    if neighborhood_range < 0:
        raise ValueError("Neighborhood range must be non-negative")
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
   
    # Handle empty grid case
    if rows == 0 or cols == 0:
        return 0  

    positive_coords = []

    # Find all coordinates with positive integers and add to list
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                positive_coords.append((r, c))
    
    # Skip processing if neighborhood_range is greater than grid dimensions (no need to check each cell)
    if neighborhood_range >= rows + cols - 2 and positive_coords:  # A positive cell has to exist as well
        return rows * cols

    neighbor_set = set()

    # For each positive coordinate, find its neighbors
    for (row, col) in positive_coords:
        for n_row in range(-neighborhood_range, neighborhood_range + 1):
            for n_col in range(-neighborhood_range, neighborhood_range + 1):
                if abs(n_row) + abs(n_col) <= neighborhood_range:  # Manhattan distance
                    x, y = row + n_row, col + n_col  # Get neighbor coordinates
                    if 0 <= x < rows and 0 <= y < cols:  # Check bounds
                        neighbor_set.add((x, y))

    # Return the size of the Set
    return len(neighbor_set)


if __name__ == "__main__":
    # Example usage
    rows, cols = 10, 25
    example_grid = [[0] * cols for _ in range(rows)]
    example_grid[0][0] = 1
    example_grid[2][7] = 2
    example_grid[4][24] = 3
    example_grid[5][3] = 4
    example_grid[8][20] = 5
    example_grid[9][12] = 6
    neighborhood_range = 8
    print(f"Number of neighbors: {count_neighbors(example_grid, neighborhood_range)}")
