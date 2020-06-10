this_set = {1,2,3}
this_set.add(1)         #Cannot duplicate items
this_set.add(4)
this_set.discard(5)     #If 5 not found, discard does not raise error
x = this_set.pop()
print(this_set)
print("Pop item is {}".format(x))

if (4 in this_set):
    print("Yes")
else:
    print("No")


set1 = {1,2,3}
set2 = {'a', 'b', 'c', 1}
set1.update(set2)          #Union set1, set2, remove duplication
print (set1)