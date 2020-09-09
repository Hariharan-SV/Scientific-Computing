# Defining Function
def f(x):
  return x**3 - 5*x - 9

# Defining derivative of function
def g(x):
  return 3*x**2 - 5

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):
  step = 1
  flag = 1
  condition = True
  
  if g(x0) == 0.0:
    print('Divide by zero error!')
    return
  
  x1 = x0 - f(x0)/g(x0)
  print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
  
  if abs(f(x1)) > e:
    newtonRaphson(x1,e,step+1) 
  else:
    print('\nRequired root is: %0.8f' % x1)


x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))

# Starting Newton Raphson Method
print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
newtonRaphson(x0,e,1)