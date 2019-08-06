students=[]
stu=[]
nombre=[]
students=[["Rachel", -50], ["Mawer", -50], ["sheen", -50],["shaheen", 51]]

students=sorted(students,key=lambda students: students[1],reverse= False)

mini=students[0][1]

stu=students 
for i in range(0,len(students)-1):
    if students[0][1]==mini:
        students.remove(students[0])
        i =i-1

mini=students[0][1]

for i in range(len(students)):
    print(students[i][1])
    if (students[i][1]==mini):
        print(mini)
        nombre.append(students[i][0])
nombre=sorted(nombre,reverse= False)
for i in nombre:
    print (i) 
    print ("{0:.2f}".format(5.1234554321))