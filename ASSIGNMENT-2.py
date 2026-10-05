# 1. List Creation:

# Create a list named age_list with five integer elements. For eg., [24, 25, 26, 27, 28]
age_list = [24, 25, 26, 27, 28]
print(age_list)

#Create a list named name_list with five string elements
name_list = ["Anu", "Rahul", "Priya", "Kiran", "Meera"]
print(name_list)



# 2. List Operations / Modifications:

#Append the string "Yazhini" to name_list.
name_list.append("Yazhini")
print(name_list)

# Insert the element 30 at index 2 in age_list.
    # 24, 25, 26, 27, 28
    #  0  1   2   3    4
age_list.insert(2, 30)
print(age_list)

# Remove the string "Yazhini" from name_list.
name_list.remove("Yazhini")
print(name_list)


# Pop the last element from age_list.
age_list.pop()
print(age_list)


# Extend the age_list with additional ages [29, 30, 26].
age_list.extend([29, 30, 26])
print(age_list)


# Sort age_list in descending order.
age_list.sort(reverse=True)
print(age_list)


# Find Max age, Min age and sum of all ages from age_list.
max_age = max(age_list)
min_age = min(age_list)
total_age = sum(age_list)

print("Maximum age:", max_age)
print("Minimum age:", min_age)
print("Sum of all ages:", total_age)



# 3. Accessing List Elements:

# Print the first element of name_list.
name_list = ["Anu", "Rahul", "Priya", "Kiran", "Meera"]
#             0        1        2        3        4
print(name_list[0])

# Print the last element of name_list.
print(name_list[-1])

# Print the elements from index 2 to index 4 in name_list.
print(name_list[2:5])

#Print the elements of name_list in reverse order.
print(name_list[::-1])


# 4_Dictionary
# Create a dictionary named student_marks that maps the names of five students to their marks (use scale of from 0 to 100).
student_marks = {
    "Anu": 75,
    "Rahul": 68,
    "Priya": 90,
    "Kiran": 82,
    "Meera": 77
}
print(student_marks)

# Access and print the mark of a specific student, of your choice.
print(student_marks["Priya"])

# Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80
print(student_marks)

# Update the mark of any one older student to 82
student_marks["Rahul"] = 82
print(student_marks)

# Use the keys(), values(), and items() methods to print all keys, values, and key-value pairs in the student_marks dictionary.
student_marks = {
    "Anu": 75,
    "Rahul": 82,
    "Priya": 90,
    "Kiran": 82,
    "Meera": 77,
    "Janani": 80
}
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())


# 5_Sets (Operations):
# Create a set called my_set with following values: ['a','e','i','o','u','a','a','i'] Analyse the output and provide explanation for the same.
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print(my_set)


# Attempt to change the value of my_set[4] = 's'. If code throws an error, provide an explanation.
my_list = ['a', 'e', 'i', 'o', 'u']
print(my_list[4])


# Create two sets: set1 with values: {1, 3, 5, 7, 9} set2 with values: {2, 3, 5, 8, 10}
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print("Set 1:", set1)
print("Set 2:", set2)

# Compute and print the union and intersection of set1 and set2.
union_set = set1.union(set2)
print("Union:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)


# 6_Operators & Conditional Statements : (IF, ELIF, ELSE)

# Performance Category Program:
# 1. Prompt user for Input. Score range should be from 0 to 10 (both inclusive).
score = float(input("Enter your score (0 to 10): "))

if score >= 0 and score <= 10:
    print("Valid score")
else:
    print("Invalid score. Please enter a score between 0 and 10.")


#2. Find the performance category based on the input score using following criteria:
    # a. Above Average: Score greater than 7
    # b. Average: Score between 4 and 7(both inclusive)
    # c. Below Average: Score lesser than 4

score = float(input("Enter your score (0 to 10): "))
if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average")

elif score >= 4:
    print("Average")

else:
    print("Below Average")
print(score)

#3 Output: Print the Performance category.
score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Performance Category: Above Average")

elif score >= 4:
    print("Performance Category: Average")

else:
    print("Performance Category: Below Average")


#4. Additional Step: You can give a prompt of your choice to each category.
#For eg: If score below average “Need to Improve your performance, consistent practice will lead to better results”.

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Performance Category: Above Average")
    print("Excellent work! Keep up the good performance.")

elif score >= 4:
    print("Performance Category: Average")
    print("Good effort! Keep practicing to improve further.")

else:
    print("Performance Category: Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")
