#Author: Jacob Noethiger jln5438@psu.edu
firstGrade=input("Enter your course 1 letter grade: ")
firstCredit=input("Enter your course 1 credit: ")
firstGPA=0.0
if(firstGrade=='A'):
  firstGPA=4.0
elif(firstGrade=='A-'):
  firstGPA=3.67
elif(firstGrade=='B+'):
  firstGPA=3.33
elif(firstGrade=='B'):
  firstGPA=3.0
elif(firstGrade=='B-'):
  firstGPA=2.67
elif(firstGrade=='C+'):
  firstGPA=2.33
elif(firstGrade=='C'):
  firstGPA=2.0
elif(firstGrade=='D'):
  firstGPA=1.0
print("Grade point for course 1 is: "+str(firstGPA))
secondGrade=input("Enter your course 2 letter grade: ")
secondCredit=input("Enter your course 2 credit: ")
secondGPA=0.0
if(secondGrade=='A'):
  secondGPA=4.0
elif(secondGrade=='A-'):
  secondGPA=3.67
elif(secondGrade=='B+'):
  secondGPA=3.33
elif(secondGrade=='B'):
  secondGPA=3.0
elif(secondGrade=='B-'):
  secondGPA=2.67
elif(secondGrade=='C+'):
  secondGPA=2.33
elif(secondGrade=='C'):
  secondGPA=2.0
elif(secondGrade=='D'):
  secondGPA=1.0
print("Grade point for course 2 is: "+str(secondGPA))
thirdGrade=input("Enter your course 3 letter grade: ")
thirdCredit=input("Enter your course 3 credit: ")
thirdGPA=0.0
if(thirdGrade=='A'):
  firstGPA=4.0
elif(thirdGrade=='A-'):
  thirdGPA=3.67
elif(thirdGrade=='B+'):
  thirdGPA=3.33
elif(thirdGrade=='B'):
  thirdGPA=3.0
elif(firstGrade=='B-'):
  thirdGPA=2.67
elif(thirdGrade=='C+'):
  thirdGPA=2.33
elif(thirdGrade=='C'):
  thirdGPA=2.0
elif(thirdGrade=='D'):
  thirdGPA=1.0
print("Grade point for course 3 is: "+str(thirdGPA))
totalCredits=(int(firstCredit)+int(secondCredit)+int(thirdCredit))

GPA=((int(firstGPA)*int(firstCredit))+(int(secondGPA)*int(secondCredit))+(int(thirdGPA)*int(thirdCredit))/totalCredits)

print("Your GPA is: "+str(GPA))