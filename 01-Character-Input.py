"http://www.practicepython.org/exercise/2014/01/29/01-character-input.html"

import datetime

i = datetime.datetime.now()



name = raw_input('type your name ')
age = raw_input('enter your age ')
curent_year = i.year
time = int (i.year) + (100 - int(age) )

print ("so if your name is " + name + " and your age is " + str(age) + " that means you will be 100 years old in " + str(time))



#print ("your name is ") + name
