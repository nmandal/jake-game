print('Welcome to the Jake show - wanna play a game?')
answer=input('Are you ready to play?: ')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Where does Jake like to eat when drunk? ')
    if answer.lower()=='taco bell':
        score += 1
        print('Correct... #bajablasted')
    else:
        print('No Crunchwrap for you')
 
 
    answer=input('How many times has Jake seen Top Gun? ')
    if answer.lower()== '3':
        score += 1
        print('Correct')
    else:
        print('You are in the danger zone')
 
    answer=input('How many bing bongs can a bing bong bing if a bong bing could bing bongs? ')
    if answer.lower()=='a lot':
        score += 1
        print('Ariana I miss you')
    else:
        print('no, a lot')
 
print('Thank you for playing - you scored',score,"questions correctly!")
mark=(score/total_questions)*100
print('Percentage obtained:',mark)
restart=input('Want to play again? ')

if restart.lower()=='yes':
    print('Not sure how to code this yet... stay tuned')
else:
        print('Good choice')
