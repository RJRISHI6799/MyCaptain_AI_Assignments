# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Perform set operations
union = E | N
intersection = E & N
difference = E - N
symmetric_difference = E ^ N

# Print the results
print("Union of E and N is", union)
print("Intersection of E and N is", intersection)
print("Difference of E and N is", difference)
print("Symmetric difference of E and N is", symmetric_difference)