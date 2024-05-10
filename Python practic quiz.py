play="yes"
while play == "yes":
    QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
    score=0
    #ask user their name and save it
    name=input ("What's your name? ") 
    #Greet the user and introduce the quiz
    print ("Welcome to my quiz,",name)
    print ("This quiz is about Animals")
    #Question1
    question = "Whats the animal with the longest life span?".lower()
    a = "Galapagos Tortoise".lower()
    b = "The Immortal Jellyfih".lower()
    c = "Glass sponge".lower()
    d = "tubeworm".lower()
    answer=input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    #Answer 1
    if answer==b.lower() or answer=="b".lower() or answer=="the immortal jellyfish".lower():
        print("correct")
        score+=10
    elif answer==(""):
        print("I see you didn't write anything")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d" and answer != "the immortal jellyfish":
        print ("That was not a choice")
    else :
        print("Incorrect")
        print ("The answer was The Immortal Jellyfish")
        score-=5
    #Question2
    answer=input ("Whats the heaviest animal?").lower()
    #Answer 2
    if answer=="Blue Whale".lower() or answer=="blue whale".lower():
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
    if answer=="Horseshoe Crab".lower() or answer=="horseshoe crab".lower():
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
    if answer=="Mosquito".lower() or answer=="mosquito".lower():
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
    print ("This is the end Thank you {} for participating in my quiz and Good job for getting the score of {}".format(name,score))
    play = input("Do you want another chance and play again")
print("Well then thank you for playing my quiz")
