from capitals import states
import random

print("Let's learn some capitals!!")
random.shuffle(states)
# print(states)
for state in states:
    question= "What is the capital of" + " " +state['name']
    print(question)
    answer= input()
    # print (state['capital'])
    if answer == state['capital']:
        print("You got it")
    else:
        print("You ain't got it")
    
   
   

    
    
    

    
   
#    for keys, values in state.items():
       



       


        
        

        
        
        
        



    