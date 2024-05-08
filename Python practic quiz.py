score=0
#ask user their name and save it
name=input ("What's your name? ") 
#Greet the user and introduce the quiz
print ("Welcome to my quiz,",name)
print ("This quiz is about Animals")
#Question1
answer=input ("Whats the animal with the longest life span?").lower()
#Answer 1
if answer=="the immortal jellyfish".lower() or "immortal jellyfish".lower():
    print("correct")
    score+=10
elif answer==(""):
    print("I see you didn't write anything")
else :
    print("Incorrect")
    print ("The answer was The Immortal Jellyfish")
    score-=5
#Question2
answer=input ("Whats the heaviest animal?").lower()
#Answer 2
if answer=="Blue Whale".lower() or "blue whale".lower():
    print("correct")
    score+=10
elif answer==(""):
    print("I see you didn't write anything")
else :
    print("Incorrect")
    print ("The answer was Blue Whale")
    score-=5
#Question3
answer=input ("Whats the oldest animal species?").lower()
#Answer 3
if answer=="Horseshoe Crab".lower() or "horseshoe crab".lower():
    print("correct")
    score+=10
elif answer==(""):
    print("I see you didn't write anything")
else :
    print("Incorrect")
    print ("The answer was Horseshoe Crab")
    score-=5
#Question4
answer=input ("Whats the most dangerous animal?").lower()
#Answer 4
if answer=="Mosquito".lower() or "mosquito".lower():
    print("correct")
    score+=10
elif answer==(""):
    print("I see you didn't write anything")
else :
    print("Incorrect")
    print ("The answer was Mosquito")
    score-=5
print("your final score is",score)
#End the quiz
print ("This is the end Thank you for participating in my quiz")

