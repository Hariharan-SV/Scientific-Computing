"""
To-Do
[ ] - Gauss elimination
[ ] - Gauss jordan
[ ] - Gauss jacobi
[ ] - Gauss Seidel
"""
# print_rules will print a general rule to not to use cases where number of equations != no of unknowns
def print_rules():
  print("Rule:\nThe program is designed to handle only when number of unknowns and number of equations are equal\nEnter a number,n which denotes number of unknowns,")

# print_rules will print all available options to compute
def print_options():
  print("\n1.Gauss elimination\n2.Gauss Jordan\n3.Gauss Jacobi\n4.Gauss Seidel")

# For example if user wants to input two equations like
# x1 + 2x2 = 3
# 2x1 + x2 = 3
# it will return a list like [[1,2,3],[2,1,3]]
def get_coefficients_as_list(no_of_unknowns):
  all_coefficients = []
  for i in range(1,no_of_unknowns+1):
    coefficient = []
    print("Enter the coefficients for equation ",i)
    for j in range(1,no_of_unknowns+1):
      num = int(input("Enter the coefficient of x"+str(j)+":- "))
      coefficient.append(num)
    coefficient.append(int(input("Enter the RHS constant :- ")))
    all_coefficients.append(coefficient)
  return all_coefficients

# function that computes in gauss elimination method
def gauss_elimination(no_of_unknowns):
  coefficient_list = get_coefficients_as_list(no_of_unknowns)
  print(no_of_unknowns,coefficient_list)

# function that computes in gauss jardon method
def gauss_jardon(no_of_unknowns):
  coefficient_list = get_coefficients_as_list(no_of_unknowns)
  print(no_of_unknowns,coefficient_list)

# function that computes in gauss jacobi method
def gauss_jacobi(no_of_unknowns):
  coefficient_list = get_coefficients_as_list(no_of_unknowns)
  print(no_of_unknowns,coefficient_list) 

# function that computes in gauss seidall method
def gauss_seidall(no_of_unknowns):
  coefficient_list = get_coefficients_as_list(no_of_unknowns)
  print(no_of_unknowns,coefficient_list)

# here our program gets executed
if __name__ == "__main__":
  print_rules()  
  no_of_unknowns = int(input("Enter n : "))
  print_options()
  choice = int(input("Enter choice: "))
  if(choice == 1):
    gauss_elimination(no_of_unknowns)
  elif(choice == 2):
    gauss_jordan(no_of_unknowns)
  elif(choice == 3):
    gauss_jacobi(no_of_unknowns)
  elif(choice == 4):
    gauss_seidall(no_of_unknowns)
  else:
    print("No option selected !")