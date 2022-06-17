cells = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

i, num_cells = 0, len(cells)
for i, v in enumerate(cells, 1):
    if (i != v):
        break

if (i == num_cells):
    print("Win")
else:
    print(i)

a = set()
a.add(str([1,2,3]))
a.add(str([1,2,3]))
print(a)

# if i + 1 == num_cells:
#     return True
# return False