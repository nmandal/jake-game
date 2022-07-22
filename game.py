def main():
    print('Welcome to the Jake show - wanna play a game?')
    
    score = 0
    total_questions = 3
    game_count = 1
    game_responses = {} # {1: ['yes', 3, 'a lot', 3], 2: ['n', 2, 'bing bong', 0]}
    is_playing = True

    while is_playing:

        game_responses[game_count] = []
    
        answer=input('Are you ready to play? (y/n): ')
        if answer.lower().strip() in ('yes', 'y'):
            answer=input('Where does Jake like to eat when drunk? ')
            game_responses[game_count].append(answer)

            if answer.lower()=='taco bell':
                score += 1
                print('Correct... #bajablasted')
            else:
                print('No Crunchwrap for you')
        
        
            answer=input('How many times has Jake seen Top Gun? ')
            game_responses[game_count].append(answer)
            if answer.lower().strip() == '3':
                score += 1
                print("Correct - I carried that movie in the box office.")
            else:
                print('You are in the danger zone')
        
            answer=input('How many bing bongs can a bing bong bing if a bong bing could bing bongs? ')
            game_responses[game_count].append(answer)
            if answer.lower().strip() == 'a lot':
                score += 1
                print('Ariana I miss you')
            else:
                print('no, a lot')
        
            print(f'Thank you for playing - you scored {score} questions correctly!')
            mark = (score*100) // total_questions
            print(f'Score: {mark}%')

            restart=input('Want to play again? (y/n) ')

            if restart.lower().strip() in ('yes', 'y'):
                print('I just learned how to do a while loop!!')
            else:
                is_playing = False
                print('Good choice - goodbye!')
                print(f"Session responses: {game_responses}")

            score = 0
            game_count += 1                
        else:
            is_playing = False
            print('lolwtf - why did you run the program??')
    


if __name__ == '__main__':
    main()