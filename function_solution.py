# Func Solution
def flatten_and_sort(arr):
    return sorted([elem for sublist in arr for elem in sublist])

# Test the function
input_list = [[3, 2, 1], [7, 8, 9], [4, 5, 6]]
result = flatten_and_sort(input_list)
print(result)

# Functional Prompt
# How does this solution ensure data immutability?
# This will ensures data immutability because it doesn't modify the original input list. It creates a new list without changing the og data.

# Is this solution a pure function? Why or why not?
# Pure function because it only depends on its input.

# Is this solution a higher order function? Why or why not?
# Not a higher-order function because it doesn't take arguments or return functions.

# Would it have been easier to solve this problem using a different programming style?
# No, since this simplifies the process and won't alter the og data.

# Why is functional programming a helpful paradigm when solving this problem?
# It keeps data safe and use pure functions, same presented to this problem.