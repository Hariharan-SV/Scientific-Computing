# Defining Function
def f(x):
  return x**3 - 5*x - 9

# Implementing Secant Method

def secant(x0,x1,e,step): 
  if f(x0) == f(x1):
    print('Divide by zero error!')
    return
  
  x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
  abs(f(x2)) > e

  print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
  
  if abs(f(x2)) > e:
    secant(x1,x2,e,step+1)
  else:
    print('\n Required root is: %0.8f' % x2)
    return

x0 = float(input('Enter First Guess: '))
x1 = float(input('Enter Second Guess: '))
e = float(input('Tolerable Error: '))

# Starting Secant Method
print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
secant(x0,x1,e,1)
