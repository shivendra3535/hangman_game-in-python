import random
stages=['''
+---+
|   |
0   |
    |
    |
    |''',
    
    '''
+---+
|   |
0   |
|   |
    |
    |''',
    
    '''
 +---+
 |   |
 0   |
/|   |
     |
     |''',
     
     '''
 +----+
 |    |
 0    |
/|\   |
      |
      |''',
      
      '''
 +-----+
 |     |
 0     |
/|\    |
/      |
       |''',
       
       '''
  +------+
  |      |
  0      |
 /|\     |
 / \     |
         |'''
]
word_list= ["apple","potato","mango","beautiful","blessing","aviator"]
chosen_word= random.choice(word_list)
display=[ ]
for i in range(len(chosen_word)):
  display += '_'
  
print(display)
lives=0
matches=0;
for i in range(len(chosen_word)):
  guessed_letter= input("enter letter you want to guess : ")
  if(chosen_word[i]== guessed_letter):
    print("match")
    matches=matches+1
    if(matches==len(chosen_word)) :
        print("you won")
    display[i]=guessed_letter
    print(display)
  else :
    print("not match")
    print(display)
    lives=lives+1;
    print(stages[lives-1])
    if((lives==6) or (i==len(chosen_word))) :
        print("you loose")
        break
    
        
    
          