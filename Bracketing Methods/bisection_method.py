#Function defining bisection method
def bisection_method(lower_x,upper_x,error_allowed):
  print("\nLower x : ",lower_x)
  print("Higher x : ",upper_x)
  print("Error e : ",error_allowed)
  middle_x = float((lower_x+upper_x)/2)
  if abs(f(middle_x)) < error_allowed:
      return middle_x
  elif f(lower_x) * f(middle_x) < 0:
      return bisection_method(lower_x,middle_x,error_allowed)
  else:
      return bisection_method(middle_x,upper_x,error_allowed)

#Define the function whose roots are to be found
def f(x):
  return x**3-5*x-9

#Function to get inputs
def get_inputs():
  lower_x = int(input("Enter first guess: "))
  upper_x = int(input("Enter second guess: "))
  error_allowed = float(input("Enter error value allowed (epsilon): "))
  if f(lower_x) * f(upper_x) < 0:
    answer = bisection_method(lower_x,upper_x,error_allowed)
    print("Root is : " + str(answer))
    exit()
  else:
    print("f(lower_x)*f(upper_x) = ",f(lower_x)*f(upper_x))
    print("Not possible...\nEnter inputs")
    get_inputs()

#Calling input function
get_inputs()