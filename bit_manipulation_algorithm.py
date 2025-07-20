import random
from sklearn.cluster import KMeans
from math import sqrt
def split_two_digit_number(number):
    # Extract the tens digit
    tens_digit = number // 10

    # Extract the ones digit
    ones_digit = number % 10

    return tens_digit, ones_digit

def flip_last_and_before_rightmost_1(decimal_number):
    binary_number = list(bin(decimal_number)[2:].zfill(3))  # Convert to 3-bit binary
    # Flip the last bit and the bit before the last
    for i in range(1, 4):
        if i == 2 or i == 1 or i == 3:
            binary_number[-i] = '1' if binary_number[-i] == '0' else '0'
    decimal_output = int(''.join(binary_number), 2)
    return decimal_output
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2)

def analyze_clusters(data, modified_data, n_clusters):
    """Analyze clusters for a given number of clusters."""
    # Apply K-means clustering to the original numbers
    kmeans_original = KMeans(n_clusters=n_clusters, random_state=0).fit([[num] for num in data])
    original_labels = kmeans_original.labels_
    original_centers = kmeans_original.cluster_centers_

    # Apply K-means clustering to the altered numbers
    kmeans_altered = KMeans(n_clusters=n_clusters, random_state=0).fit([[num] for num in modified_data])
    altered_labels = kmeans_altered.labels_
    altered_centers = kmeans_altered.cluster_centers_

    # Find the closest original center for each altered center
    cluster_mapping = [-1] * len(original_centers)
    for i, orig_center in enumerate(original_centers):
        min_distance = float('inf')
        closest_cluster = -1
        for j, alt_center in enumerate(altered_centers):
            distance = euclidean_distance(orig_center, alt_center)
            if distance < min_distance:
                min_distance = distance
                closest_cluster = j
        cluster_mapping[i] = closest_cluster

    # Print cluster centers for original numbers
    print(f"n_clusters = {n_clusters}")
    print("Original cluster centers:", original_centers)

    # Print cluster centers for altered numbers
    print("Altered cluster centers:", altered_centers)

    # Compare the clusters to find how many altered numbers have changed clusters
    changed_count = 0
    misclassified_numbers = []

    for i in range(len(data)):
        original_cluster = original_labels[i]
        altered_cluster = altered_labels[i]
        mapped_altered_cluster = cluster_mapping[original_cluster]

        if altered_cluster != mapped_altered_cluster:
            changed_count += 1
            misclassified_numbers.append(modified_data[i])

    # Calculate and print the percentage of changed numbers
    total_numbers = len(data)
    percentage_changed = (changed_count / total_numbers) * 100

    print(f"Number of altered numbers that changed clusters: {changed_count}")
    print(f"Percentage of altered numbers that changed clusters: {percentage_changed:.2f}%")
    print(f"Misclassified numbers: {misclassified_numbers}")
    print()
# Initialize variables

number = [58, 91, 87, 25, 44, 38, 37, 68, 11, 83, 12, 50, 73, 44, 70, 19, 32, 31, 48, 34, 96, 48, 44, 87, 91, 98, 82, 98, 75, 7, 94, 64, 5, 33, 2, 92, 95, 10, 54, 89, 36, 36, 24, 46, 81, 17, 34, 12, 86, 29, 54, 42, 60, 70, 14, 48, 94, 11, 37, 8, 78, 99, 96, 91, 93, 47, 23, 3, 53, 98, 12, 4, 47, 84, 85, 43, 41, 63, 95, 9, 80, 31, 65, 40, 93, 32, 66, 81, 58, 83, 61, 37, 49, 37, 25, 47, 90, 34, 31, 66]  # List from 1 to 99
n = len(number)
total=[]
type1=[]
for i in range(n):
    tens_digit, ones_digit = split_two_digit_number(number[i])
    total.append(tens_digit+ones_digit)
    if(tens_digit%2==0):
        type1.append(1)
    else:
        type1.append(2)
print(type1)
flipped_decimal_number = []
type_result = []  # Changed from type to avoid conflict

def case3(i):
    t = flip_last_and_before_rightmost_1(total[i])
    if t == 0:
        flipped_decimal_number.append(number[i] + total[i])
        type_result.append(4)
    else:
        if type1[i] == 1:
            flipped_decimal_number.append(number[i] + t - total[i])
            type_result.append(1.1)
        else:
            flipped_decimal_number.append(number[i] - t + total[i])
            type_result.append(1.2)

# Process each number using case3
for i in range(n):
    case3(i)

# Calculate deviation
deviation = []
for i in range(n):
    t = flipped_decimal_number[i] - number[i]
    deviation.append(t)

# Print results
print("Number:", number)
print("Flipped Decimal Numbers:", flipped_decimal_number)
print("Deviation:", deviation)

for n_clusters in [2, 3, 4, 5]:
    analyze_clusters(number, flipped_decimal_number, n_clusters)
