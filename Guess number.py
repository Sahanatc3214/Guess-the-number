import random , time , sys
import playsound as ps
magic = random.randint(1,100)

s = time.perf_counter()
print('Guess number within 1-100 ')

while time.perf_counter() - s <= 15:
    guess = int(input('Guess = '))
    if guess == magic:
        print('You won 10k cash price')
        ps.playsound('clapping.mp3')
        sys.exit(0)
    
    elif guess > magic:
        print('Try lesser number')
    else:
        print('Some greater number')
        
                
print('Hard luck try next time,correct number is ',magic)

