import math

#Function defining false position method
def false_position(lower_x,upper_x,error_allowed):
  print("\nLower x : ",lower_x)
  print("Higher x : ",upper_x)
  print("Error e : ",error_allowed)
  middle_x = float(upper_x - (( ( f(upper_x) * (lower_x-upper_x) ) / ( f(lower_x) - f(upper_x) )   )))
  if abs(f(middle_x)) < error_allowed:
    return middle_x
  elif f(lower_x) * f(middle_x) < 0:
    return false_position(lower_x,middle_x,error_allowed)
  else:
    return false_position(middle_x,upper_x,error_allowed)

#Define the function whose roots are to be found
def f(x):
  return x* math.exp(x) - 1

#Function to get inputs
def get_inputs():
  lower_x = int(input("Enter first guess: "))
  upper_x = int(input("Enter second guess: "))
  error_allowed = float(input("Enter error value allowed (epsilon): "))
  if f(lower_x) * f(upper_x) < 0:
    a = false_position(lower_x,upper_x,error_allowed)
    print("Root is : " + str(a))
    exit()
  else:
    print("f(lower_x)*f(higher_x) = ",f(lower_x)*f(upper_x))
    print("Not possible...\nEnter inputs")
    get_inputs()

#Calling input function
get_inputs()