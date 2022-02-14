# Checker for Fibonacci
list=[0,1]
a=2
b=0
c=1
check= input ('Enter the number to be checked:')
def fibonacci (check,a,b,c): # function defined
  while a <=int (check):
   result= list[int (b)] +  list[int (c)]
   list.append(result)
   a=int (a) + 1
   b=int (b) + 1
   c=int (c) + 1
  if int(check) in list:
      print(' '+str (check) + ' ' + 'belongs to the fibonacci series')
  if int (check) not in list:
       print(' '+ str (check) + ' ' + 'does not belong to the fibonacci series') 
fibonacci(check,a,b,c) # function is called



