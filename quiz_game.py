print("HI welcome to my Quiz game")
playing = input("Do you wanna play? ")
if playing.lower() != "yes":
    quit()
print("Okay lets play :)")
score =0
question1 = input("what does cpu stand for ? ") 
if question1.lower() == "central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")
question2 = input("what does GPU stand for ? ")
if question2.lower() == "graphics processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")
question3 = input("what does RAM stand for ? ")
if question3.lower() == "random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")
question4 = input("what does PSU stand for ? ")
if question4.lower() == "power supply unit":
    print("correct")
    score +=1
else:
    print("incorrect")
question5 = input("what does SSD stand for?" )
if question5.lower() == "solid state device":
    print("correct")
    score +=1
else:
    print("incorrect")
print((" you got " + str(score) + " questions correct"))
print("you got " + str((score/5)*100) + "%")
print("Thanxs for playing :)")
