#create a tuple corrdinate with 2 elements and calculate which are near the origin (0,0) and which are far away from the origin.
# Define a list of coordinates as tuples

import math
coordinates = [(1, 2), (3, 4), (0, 0), (-1, -1), (5, 5), (2, 1)]

#origin is (0, 0)

def origin_distance(coordinate):
    return math.sqrt(coordinate[0]**2 + coordinate[1]**2)



# Create two lists to store near and far coordinates
near_coordinates = []
far_coordinates = []

# Define a threshold distance to classify near and far coordinates
threshold_distance = 3

# Iterate through the list of coordinates and classify them based on their distance from the origin
for coordinate in coordinates:
    distance = origin_distance(coordinate)
    if distance <= threshold_distance:
        near_coordinates.append(coordinate)
    else:
        far_coordinates.append(coordinate)


# Print the results
print(f"Coordinates near the origin (within distance of {threshold_distance}): {near_coordinates}")
print(f"Coordinates far from the origin (beyond distance of {threshold_distance}): {far_coordinates}")

