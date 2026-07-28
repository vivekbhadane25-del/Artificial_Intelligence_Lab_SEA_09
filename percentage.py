n=int(input("enter student marks"))
total_marks=500
percentage=(n/total_marks)*100
print(percentage,"%")
if(percentage>=90):
 print("first class student")
elif (90>percentage>=75):
 print("second class")
elif (75>percentage>=33):
 print("third class student")
else:
 print("student is fail")
