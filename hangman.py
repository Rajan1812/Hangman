import os
import random
star_string = ''
star_list = []

def select(word_file):
  global star_list
  word_list=[]
  f=open(word_file,'r')
  for i in f:
    word_list.append(i)
  #print word_list
  word_list_size=len(word_list)
#  print word_list_size
  word=random.choice(word_list)
  #print word
  word_size=len(word)-1
  print word
  print("*"*word_size)
  star_list = ["*"] * word_size
  return word


def guess(attempts,word):
  #print word
  global star_string
  global star_list
  
  if attempts == 0 or  "".join(str(x) for x in star_list)+'\n'== word:
    print "Game Over"
    exit(0)
  
  letter=raw_input("enter the one char of the word\n")
  letter_count=len(word)-1
  
  if letter in word:
    letter_number=word.find(letter)
    star_list[letter_number] = letter
    print star_list
    
    
    guess(attempts,word)

  else:
    attempts -= 1
    print"wrong guess try again"
    print "attempts left =",attempts
    guess(attempts,word)
  

if __name__ == '__main__':
  attempts=input("number of attempts you want 1-10\n")
  if attempts > 10 or attempts < 1:
    for i in range(3):
      if attempts > 10 or attempts < 1:
        print "wrong range. Please try again\n"
        attempts=input()
        if attempts > 10 or attempts < 1:
          continue
        else:
          break
      if i == 2:
        print "too many wrong attempts Bye :)"
        exit(0)
  #print attempts  

  #select('./test')
  guess(attempts,select('./test'))
