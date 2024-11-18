#1 create a list called number containing the numbers (1,5,3,8).Append the number 10 to the end of the list.
# Insert the number 2 at index 1. Remove the number 3 from the list.Print the final list.
number = [1, 5, 3, 8 ]
number.append(10)
number.insert(1, 2)
number.remove(3)
print(number)

#2 Create a list called colors containg (red, green, blue, purple) sort the list alphabetically.
# Reverse the sorted list.Print the final list
colours = [ 'yellow', 'red', 'green', 'blue', 'purple' ]
colours.sort()
colours.reverse()
print(colours)

#3 Create a list called temperature containing (25, 18, 32, 20, 28). find the minimun temp, 
# maximum print both values
temperature = [25, 18, 32, 20, 28 ]
min_temp = min(temperature)
max_temp = max(temperature)
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)

#4 Create a list called scores containing (85, 72, 90, 68, 80) calculate the total sum of the scores. 
# Print the total sum
scores = [85, 72, 90, 68, 80 ]
total_sum = sum(scores)
print("Total sum of the scores:", total_sum)

#5 CREATE A LIST CALLED ANIMALS CONTAINING (Cat, Dog Bird Fish)Remove the element at index 2. 
# Replace the element at index 1 with lizard. use pop to remove and return the last element.print the last element
animals = ['cat', 'dog', 'bird', 'fish' ]
animals.insert(1, 'lizard')
animals.remove('bird')
popped = animals.pop()
print(popped)
print(animals)

#5. create 2 lists, where list1 =[1,2,3] and list2 =[4,5,6]. combine list2 into list1 and print the final list
list1 = [1,2, 3 ]
list2 = [4, 5, 6 ]
list1.extend(list2)
print(list1)

#6. create a list called name containing [alice, bob, charlie, david]. find the index of bob and print it out.
name = ['alice', 'bob', 'charlie', ';david' ]
name.index('bob')
print(name.index('bob'))