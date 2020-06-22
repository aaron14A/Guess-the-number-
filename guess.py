import random 
  
print("Number guessing game") 
  
number = random.randint(0, 9) 
chances = 0
  
print("Guess the number between 0 and 9")  
while chances < 5: 
      
    guess = int(input()) 
       
    if guess == number: 
        print("Congratulation YOU WON!!!") 
        break
          
    if guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 
              
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
             
    chances += 1
          
if not chances < 5: 
    print("YOU LOSE!!! The number is", number) 