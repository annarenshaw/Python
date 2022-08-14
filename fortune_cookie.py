import random

lucky_number = random.randint(1,100)

fortune = random.randint(1,3)

fortune_text = ()

if fortune == 1:
    fortune_text = 'You will come upon a lot of money!'

if fortune == 2:
    fortune_text = 'Today will be tough... but worth it!'

if fortune == 3:
    fortune_text = 'You will get married this year!'

print(f'{fortune_text} Your Lucky Number Is {lucky_number}')