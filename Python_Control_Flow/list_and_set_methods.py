# Demonstrating list methods
# Creating a list with 5 elements
my_list = [5, 3, 8, 1, 4]

my_list.append(7)
print("After append(7):", my_list)  

my_list.remove(3)
print("After remove(3):", my_list)  

popped = my_list.pop()
print(popped)  
print("popped", my_list)       

my_list.sort()
print(my_list)      

my_list.reverse()
print(my_list)    

my_list.extend([10, 12])
print(my_list)  


# Creating two sets with at least 4 elements each
seta = {1, 2, 3, 4}
setb = {3, 4, 5, 6}

seta.add(5)
print("After add(5) to seta:", seta)  

seta.remove(2)
print("After remove(2) from seta:", seta)  

union_set = seta.union(setb)
print("Union of seta and setb:", union_set)  

intersection_set = seta.intersection(setb)
print("Intersection of seta and setb:", intersection_set)  

difference_set = seta.difference(setb)
print("Difference of seta from setb:", difference_set)  
