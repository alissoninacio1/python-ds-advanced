grade: dict = {
    "Alice": [85, 70, 80],
    "Bob": [90, 89, 92],
    "Charlie": [75, 80, 60],
    "Diana": [95, 90, 98],
    "Anna": [89, 99, 100],
    "Luis": [73, 82, 61],
    "Peter": [100, 100, 90]
}


# By using .items(), you can check the current value but use the key to modify the dictionary
for key, value in grade.items():
    average = round(sum(value) / len(value))
    #add the average as a new key-value pair in the dictionary
    grade[key] = average

print(grade)

highest_average = max(grade.values())
print(f"The highest average score is: {highest_average}")





