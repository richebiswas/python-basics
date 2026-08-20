import math

n = int(input("Enter the number of training points: "))

# Dimension of each training point
dimension = int(input("Enter the dimension of each training point: "))

training_points = []

print("Enter the training points:")

for i in range(n):
    point = tuple(map(float, input(f"P{i + 1}: ").split()))
    training_points.append(point)

labels = []

print("Enter the class labels:")

for i in range(n):
    label = int(input(f"Class of P{i + 1}: "))
    labels.append(label)

print("Enter the test point:")
test_point = tuple(map(float, input().split()))

k = int(input("Enter the value of k: "))

distances = []

for i in range(n):
    distance = 0

    for j in range(dimension):
        distance += (training_points[i][j] - test_point[j]) ** 2

    distance = math.sqrt(distance)

    distances.append((distance, i))

distances.sort()

print("\nDistances from test point:")

for distance, index in distances:
    print(f"P{index + 1}: {distance:.4f}  Class: {labels[index]}")

nearest_neighbors = distances[:k]

print(f"\n{k} Nearest Neighbors:")

for distance, index in nearest_neighbors:
    print(f"P{index + 1}: Distance = {distance:.4f}, Class = {labels[index]}")

class_0 = 0
class_1 = 0

for distance, index in nearest_neighbors:
    if labels[index] == 0:
        class_0 += 1
    else:
        class_1 += 1

if class_0 > class_1:
    predicted_class = 0
else:
    predicted_class = 1

print("\nPredicted Class:", predicted_class)