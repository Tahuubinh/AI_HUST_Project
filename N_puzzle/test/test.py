from time import sleep
import copy

# delay = 0.1
# print('Go to sleep…')
# sleep(delay)
# print('Back to work…')
# sleep(10)
# print("go jogging")

list1 = [ 1, 2, 3, 4, 5, 6 ]
 
# Pops and removes the last element from the list
# print(list1.pop())
 
# # Print list after removing last element
# print("New List after pop : ", list1, "\n")
 
# list2 = [1, 2, 3, ('cat', 'bat'), 4]
 
# # Pop last three element
# print(list2.pop())
# print(list2.pop())
# print(list2.pop())
 
# # Print list
# print("New List after pop : ", list2, "\n")
# a = "D"
# print(a == 'D')

list2 = list1.copy()
list1[2] = 100
print(list1)
print(list2)