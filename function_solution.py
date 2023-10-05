# func sol

def flatten_and_sort(arr):
    return sorted ([ elem for sublist in arr for elem in sublist ])

# func test

input_list = [[ 3, 2, 1 ], [7, 8, 9 ], [ 4, 5, 6 ]]
result = flatten_and_sort( input_list )


print( result )