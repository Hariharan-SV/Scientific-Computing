# Importing math to use sqrt function
import math

# Let f(x) = x^3+x^2-1
def f(x):
	return x*x*x + x*x -1

# Re-writing f(x)=0 to x = g(x)
def g(x):
	return 1/math.sqrt(1+x)

# Implementing Fixed Point Iteration Method
def fixed_point_iteration(initial_guess, error,step):	
	x1 = g(initial_guess)
	initial_guess = x1
	print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
	if abs(f(x1)) > error:
		fixed_point_iteration(x1,error,step+1)
	else:
		print('\nRequired root is: %0.8f' % x1)


initial_guess = float(input('Enter Guess: '))
error = float(input('Tolerable Error: '))

print('\n\n*** FIXED POINT ITERATION ***')

fixed_point_iteration(initial_guess,error,1)
