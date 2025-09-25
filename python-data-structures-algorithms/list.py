"""
    Lists are used to store multiple items in a single variable.

    Lists are ORDERED - CHANGEABLE(MUTABLE) - ALLOW DUPLICATES
    
    INDEX 0.

    *A list can contain different data types, but it's not recommended to use them.
    *Negative indexing means start from the end (similar to slicing as seen in strings)

    *We can add items referring to the index or range, to add more items dynamically or replace them.

    *Complete list methods in https://www.w3schools.com/python/python_lists_methods.asp


    *Sorting is ascending, by default.  To sort descending, use the keyword argument reverse = True
        thislist.sort(reverse = True)

    *You can also make a copy of a list by using the : (slice) operator
        thislist = ["apple", "banana", "cherry"]
        mylist = thislist[:]

        You cannot copy a list simply by typing list2 = list1, 
        because: list2 will only be a reference to list1, 
        and changes made in list1 will automatically also be made in list2.

    
    * + operator can be used to concatenate (or "join") two lists, 
        creating a new list containing all elements from both original lists.
        joined_list = list1 + list2
"""


list = [1, 2, 3, 4]

print(f"The list size or length is {len(list)}")

print(list[1])

#looping in a list

for i in list:
    print(i)


#looping indexes
for i in range(len(list)):
    print(f"printing indexes {i}")

# using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#using list comprehension
fruits = ["apple", "banana", "cherry"]
[print(x) for x in fruits]
