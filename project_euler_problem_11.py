'''
Largest product in a grid
Problem 11 
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 [26] 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 [63] 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 [78] 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 [14] 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?
'''

def generate_grid():
    grid_string = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

    grid = grid_string.split('\n')
    grid = [row.lstrip() for row in grid]
    grid = [row.split() for row in grid]

    return grid

def compute_vertical_product(grid, row_index, col_index):
    vertical_product = 1
    for offset in range(0, 4):
        vertical_element = (int(grid[row_index + offset][col_index]))
        vertical_product = vertical_product * vertical_element

    return vertical_product

def compute_horizontal_product(grid, row_index, col_index):
    horizontal_product = 1
    for offset in range(0, 4):
        horizontal_element = (int(grid[row_index][col_index + offset]))
        horizontal_product = horizontal_product * horizontal_element

    return horizontal_product

def compute_left_diagonal_product(grid, row_index, col_index):
    left_diagonal_product = 1
    for offset in range(0, 4):
        diagonal_element = (int(grid[row_index + offset][col_index + offset]))
        left_diagonal_product = left_diagonal_product * diagonal_element

    return left_diagonal_product

def compute_right_diagonal_product(grid, row_index, col_index):
    right_diagonal_product = 1
    for offset in range(0, 4):
        diagonal_element = (int(grid[row_index + 3 - offset][col_index + offset]))
        right_diagonal_product = right_diagonal_product * diagonal_element

    return right_diagonal_product

def main(grid):
    products = []
    #Calculate all vertical products and find the max vertical product
    vertical_product_row_end = 16
    vertical_product_column_end = 20
    max_vertical_product = 0
    for vertical_product_row_index in range(vertical_product_row_end):
        for vertical_product_column_index in range(vertical_product_column_end):
            vertical_product = compute_vertical_product(grid,
                                                        vertical_product_row_index,
                                                        vertical_product_column_index)

            if vertical_product > max_vertical_product:
                max_vertical_product = vertical_product

    products.append(max_vertical_product)        
    
    #Calculate all horizontal products and find the max horizontal product
    horizontal_product_row_end = 20
    horizontal_product_column_end = 16
    max_horizontal_product = 0
    for horizontal_product_row_index in range(horizontal_product_row_end):
        for horizontal_product_column_index in range(horizontal_product_column_end):
            horizontal_product = compute_horizontal_product(grid,
                                                            horizontal_product_row_index,
                                                            horizontal_product_column_index)

            if horizontal_product > max_horizontal_product:
                max_horizontal_product = horizontal_product

    products.append(max_horizontal_product)

    #Calculate all left diagonal products and find the left max diagonal product
    left_diagonal_product_row_end = 16
    left_diagonal_product_column_end = 16
    max_left_diagonal_product = 0
    for left_diagonal_product_row_index in range(left_diagonal_product_row_end):
        for left_diagonal_product_column_index in range(left_diagonal_product_column_end):
            left_diagonal_product = compute_left_diagonal_product(grid,
                                                                  left_diagonal_product_row_index,
                                                                  left_diagonal_product_column_index)

            if left_diagonal_product > max_left_diagonal_product:
                max_left_diagonal_product = left_diagonal_product

    products.append(max_left_diagonal_product)

    #Calculate all right diagonal products and find the right max diagonal product
    right_diagonal_product_row_end = 16
    right_diagonal_product_column_end = 16
    max_right_diagonal_product = 0
    for right_diagonal_product_row_index in range(right_diagonal_product_row_end):
        for right_diagonal_product_column_index in range(right_diagonal_product_column_end):
            right_diagonal_product = compute_right_diagonal_product(grid,
                                                        right_diagonal_product_row_index,
                                                        right_diagonal_product_column_index)

            if right_diagonal_product > max_right_diagonal_product:
                max_right_diagonal_product = right_diagonal_product

    products.append(max_right_diagonal_product)

    max_product = max(products)
    return products, max_product

if __name__ == "__main__":
    print(main(generate_grid()))
