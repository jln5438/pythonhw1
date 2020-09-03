#Author: Jacob Noethiger jln5438@psu.edu
firstGrade=input("Enter your course 1 letter grade: ")
firstCredit=input("Enter your course 1 credit: ")
firstGPA=0.0
if(firstGrade=='A' or firstGrade=='a'):
  firstGPA=4.0
elif(firstGrade=='A-' or firstGrade=='a-'):
  firstGPA=3.67
elif(firstGrade=='B+' or firstGrade=='b+'):
  firstGPA=3.33
elif(firstGrade=='B' or firstGrade=='b'):
  firstGPA=3.0
elif(firstGrade=='B-' or firstGrade=='b-'):
  firstGPA=2.67
elif(firstGrade=='C+' or firstGrade=='c+'):
  firstGPA=2.33
elif(firstGrade=='C' or firstGrade=='c'):
  firstGPA=2.0
elif(firstGrade=='D' or firstGrade=='d'):
  firstGPA=1.0
print("Grade point for course 1 is: "+str(firstGPA))
secondGrade=input("Enter your course 2 letter grade: ")
secondCredit=input("Enter your course 2 credit: ")
secondGPA=0.0
if(secondGrade=='A' or secondGrade=='a'):
  secondGPA=4.0
elif(secondGrade=='A-' or secondGrade=='a-'):
  secondGPA=3.67
elif(secondGrade=='B+' or secondGrade=='b+'):
  secondGPA=3.33
elif(secondGrade=='B' or secondGrade=='b'):
  secondGPA=3.0
elif(secondGrade=='B-' or secondGrade=='b-'):
  secondGPA=2.67
elif(secondGrade=='C+' or secondGrade=='c+'):
  secondGPA=2.33
elif(secondGrade=='C' or secondGrade=='c'):
  secondGPA=2.0
elif(secondGrade=='D' or secondGrade=='d'):
  secondGPA=1.0
print("Grade point for course 2 is: "+str(secondGPA))
thirdGrade=input("Enter your course 3 letter grade: ")
thirdCredit=input("Enter your course 3 credit: ")
thirdGPA=0.0
if(thirdGrade=='A' or thirdGrade=='a'):
  firstGPA=4.0
elif(thirdGrade=='A-' or thirdGrade=='a-'):
  thirdGPA=3.67
elif(thirdGrade=='B+' or thirdGrade=='b+'):
  thirdGPA=3.33
elif(thirdGrade=='B' or thirdGrade=='b'):
  thirdGPA=3.0
elif(firstGrade=='B-' or thirdGrade=='b-'):
  thirdGPA=2.67
elif(thirdGrade=='C+' or thirdGrade=='c+'):
  thirdGPA=2.33
elif(thirdGrade=='C' or thirdGrade=='c'):
  thirdGPA=2.0
elif(thirdGrade=='D' or thirdGrade=='d'):
  thirdGPA=1.0
print("Grade point for course 3 is: "+str(thirdGPA))
totalCredits=(int(firstCredit)+int(secondCredit)+int(thirdCredit))

GPA=((int(firstGPA)*int(firstCredit))+(int(secondGPA)*int(secondCredit))+(int(thirdGPA)*int(thirdCredit))/totalCredits)

print("Your GPA is: "+str(GPA))