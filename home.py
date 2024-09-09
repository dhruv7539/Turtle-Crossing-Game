import random

list=['banana','apple']
word=input("enter a word: ").lower()
display=[]

chosen_word=random.choice(list)
print(chosen_word)

for let in chosen_word:
    display.append("_")

count=0
for let in chosen_word:
    if let==word:
        display[count]=let
    count+=1    

print(display)

end_game=False
lives=2
while not end_game:
    word=input("enter a word: ").lower()

    count=0
    for let in chosen_word:
        if let==word:
            display[count]=let 
        count+=1

    if word not in chosen_word:
        lives-=1
        if lives==0:
            end_game=True

    print(display)

    if "_" not in display:
        end_game=True
    
    
