print("========>Quiz Application<========")
print("Total Questions 5 each carry 2 marks.")
print("You have to give 3 correct answer to pass.")
b=input("Do you want to start the test? Y/N:")
print(" ")
print(" ")
if b=='y' or b=='Y':
 
 with open("Questions.txt") as file:
   data=file.readlines()

 userAnswer=[]

 for i in range(0,10,2):
    question=data[i]
    print(question)

    options=data[i+1]
    print(options)

    a=input("Select an answer a,b,c,d : ")
    userAnswer.append(a)

 with open("Answers.txt") as file2:
   fileAnswers=file2.readlines()
 count=0

 for i in range(0,5):
   if(str(fileAnswers[i][0])==str(userAnswer[i])):
     count=count+2
   else:print('')


 result=(count/10)*100
 if result>60:
     f = open("Result.txt", "w")
     f.writelines(["=====>Report Card<=====\n","Result is ",str(result)," %","\n","Congratulations!! you are pass."])
     print("=====>Report Card<=====\n","Result is ",str(result)," %","\n","Congratulations!! you are pass.")
 else:
     f = open("Result.txt", "w")
     f.writelines(["=====>Report Card<=====\n","Result is ",str(result)," %","\n","Please try again"])
     print("=====>Report Card<=====\n","Result is ",str(result)," %","\n","Please try again")


else:print('')

