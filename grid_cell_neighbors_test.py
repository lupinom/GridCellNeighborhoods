'''
These are the test cases for the grid_cell_neighbors module.
Below are various scenarios to ensure the correctness of the count_neighbors function.
'''
import grid_cell_neighbors
import unittest

class TestGridCellNeighbors(unittest.TestCase):

    def test_single_neighborhood_no_cutoff(self):
        neighborhood_range = 1
        grid = [
            [0, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 5)

    def test_single_neighborhood_with_cutoff(self):
        neighborhood_range = 2
        grid = [
            [0, 2, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 7)

    def test_single_neighborhood_with_multiple_cutoffs(self):
        neighborhood_range = 2
        grid = [
            [0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 11)

    def test_multiple_neighborhoods_no_cutoff_or_overlap(self):
        neighborhood_range = 1
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 10)

    def test_multiple_neighborhoods_with_cutoff_and_overlap(self):
        neighborhood_range = 2
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 17)
    
    def test_no_positive_integers_in_grid(self):
        neighborhood_range = 1
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 0)

    def test_range_of_zero(self):
        neighborhood_range = 0
        grid = [
            [0, 0, 0],
            [0, 3, 0],
            [0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 1)
    
    def test_odd_height_and_width_of_grid(self):
        neighborhood_range = 2
        grid = [
            [0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 7)

    def test_negative_integers_in_grid(self):
        neighborhood_range = 1
        grid = [
            [0, -1, 0],
            [0, 5, 0],
            [0, 0, -3]
        ]
        self.assertEqual(grid_cell_neighbors.count_neighbors(grid, neighborhood_range), 5)

if __name__ == '__main__':
    print("Running tests for grid_cell_neighbors module...")
    unittest.main()