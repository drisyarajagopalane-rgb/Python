#String Concatenation:

string1 = "Hello "
name = input("Enter your Name: ")
string2 = string1 + name

print(string2)

string3 = ", welcome to Python programming"
string2 = string2 + string3

print(string2)

#String Slicing and Indexing:

#  Character: H e l l o   Z a r a ,     w   e  l  c  o  m  e     t o      P  y  t  h  o n      p  r  o  g  r  a  m  m  i  n  g
#      Index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40            
# Print the fi rst character of the string
print(string2[0])
# Print the last character of the string.
print(string2[-1])
# Print the first 5 characters of the string.
print(string2[:5])
# Print the last 11 characters of the string.
print(string2[-11:])
# Print the string in reverse.
print(string2[::-1])
# Use slicing and print the word “Python” from the existing string.
print(string2[23:29])




strM = "Python beginner tutorial"
# Convert the sentence to uppercase
print(strM.upper())
#Convert the sentence to lowercase.
print(strM.lower())
# Use Capitalize and return the sentence to the original input form.
print(strM.capitalize())
# Count the total number of occurrences of character ‘t’ in the string.
print(strM.count("t"))
# Replace all occurrences of “Python” with “Machine Learning” in the input string strM = “Python beginner tutorial”
print(strM.replace("Python", "Machine Learning"))

# Tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)
# Concatenate the two tuples and store it in “t_combine”
t_combine = t1 + t2
print(t_combine)
# Repeat the elements of “t_combine” 3 times
print(t_combine * 3)
# Access the 3rd element from “t_combine”
print(t_combine[2])
# Access the first three elements from “t_combine”
print(t_combine[:3])
# Access the last three elements from “t_combine”
print(t_combine[-3:])