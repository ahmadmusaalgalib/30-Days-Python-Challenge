marks=[98,27,29]
marks2=[99,23,66,67,70]
#for insert at the last
marks.append(33)
marks.insert(1 ,40)

print(23 in marks)
print(23 in marks2)
print(len(marks))
print(*marks)
print(marks[1])
print(*marks[0:2])
print(*marks2[0:4])

for Score in marks:
    print(Score)

print(*marks)
i=0

while i<len(marks):
    print(marks[i])
    i+=1

marks.clear()
print(marks)