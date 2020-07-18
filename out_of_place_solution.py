import copy

#Function to rotate a 2D Array 90 degrees Clockwise out-of-place.
#By "put-of-place", we are creating a separate variable/array to print the output.
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    x, y = (0, 0)
    for j in range(n):
        for i in range((n - 1), -1, -1):
            #print("{} {} {} {}".format(x, y, i, j))
            rotated[x][y] = given_array[i][j]
            y = ((y + 1) % n)
        x = ((x + 1) % n)
    return rotated


# Converts the 2D-Array into a readable matrix format for printing
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# rotate(a1, 3) should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# rotate(a2, 4) should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
