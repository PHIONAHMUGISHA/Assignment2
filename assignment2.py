#lists are mutable, it has also work with index
#item stored should be same 
#lists are arrays like stracture(using indexing)
studentNames=['sandra', 'patricia', 'phionah' ,'anitah'] #strings
studentMarks=[80, 56, 78, 98] #intergers
data=['sandra',90,'kamyokya'] #mixed types

#Access the whole list
print(studentNames, type(studentNames))

#Acessing list items
#indexes(positive indexing)
print(studentNames[0]) #first item
print(studentNames[1]) #second item
print(studentNames[2]) #third item
print(studentNames[4]) #last item

#indexes (negative indexing)
print(studentNames[-4]) #first item
print(studentNames[-3]) #second item

#qn 1
#print from patricia, anitah,faith,phionah, excluding the last and first using slicing.
studentNames.insert(2,"faith")
studentNames.remove("sandra") 
print(studentNames)

#QN 2
#Add the name masha at the fourth position
studentNames.insert(3 ,"masha")
print(studentNames)

#Qn3
#Update the name phionah phionah aladinah
studentNames[studentNames.index("phionah")]="phionah aladinah"
print(studentNames)

#QN 4
#Display the length of student list
print(f"the length of the student list is :{len(studentNames)}")

#QN 5
#print all the student names using a 4loop
for names in studentNames:
    print(names)

#QN 6
#calculate the total marks for student marks variable
totalMarks=sum(studentMarks)
print(totalMarks)





