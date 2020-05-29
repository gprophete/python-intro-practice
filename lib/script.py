from capitals import states
import random

score = {
    "correct":0,
    "incorrect":0
}

print('''
********************************
*                               *
*Let's learn some capitals!!    *
*                               *
********************************''')
# random.shuffle(states)
# print(states)
while True:
    random.shuffle(states)
    for state in states:
        question= "What is the capital of" + " " +state['name']
        print(question)
        answer= input()
        # print (state['capital'])

        if answer.lower() == state['capital'].lower():
            print("You got it")
            score['correct'] += 1
        else:
            print("You ain't got it")
            score['incorrect'] += 1

        right= score['correct']
        wrong= score['incorrect']
        print(f"you got {right} right")
        print(f"you got {wrong} wrong")
    
    print("End game(y/n)")
    choice = input()
    if choice.lower() == 'n' or choice == '':
        exit()
    
   
   

    
    
    

    
   
#    for keys, values in state.items():
       



       


        
        

        
        
        
        



    