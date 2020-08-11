"""
To-Do
[x] - Gauss elimination
[ ] - Gauss jordan
[ ] - Gauss jacobi
[x] - Gauss Seidel
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
# coefficient_list=[[3,-2,5,0,2],[4,5,8,1,4],[1,1,2,1,5],[2,7,6,5,7]]
# factors = [28.7777777777778, 2.1666666666666683, -16.00000000000001, 6.055555555555558]
def gauss_elimination(no_of_unknowns):
  coefficient_list = get_coefficients_as_list(no_of_unknowns)
  for i in range(0,no_of_unknowns-1):
    for j in range(i+1,no_of_unknowns):
      for k in range(no_of_unknowns,-1,-1):
        coefficient_list[j][k] = coefficient_list[i][i]*(coefficient_list[j][k]/coefficient_list[j][i])
    for j in range(i+1,no_of_unknowns):
      for k in range(0,no_of_unknowns+1):
        coefficient_list[j][k] = coefficient_list[i][k] - coefficient_list[j][k]
  factors = [0.0]*no_of_unknowns
  for i in range(no_of_unknowns-1,-1,-1):
    diff = 0
    for j in range(i+1,no_of_unknowns): 
      diff = diff + coefficient_list[i][j]*factors[j]
    #print(coefficient_list[i][no_of_unknowns],"-",diff,"/",coefficient_list[i][i])
    temp = (coefficient_list[i][no_of_unknowns]-diff)/coefficient_list[i][i]
    factors = factors[0:i]+ [temp]+factors[i+1:]
    #print(factors)
    #print("\n")
  print("Factors are listed in order as ",factors)

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
  factors = [1]+[0]*(no_of_unknowns-2)+[1]
  sample_factors = [1]+[0]*(no_of_unknowns-2)+[1]
  for i in range(0,6):
    for j in range(0,no_of_unknowns):
      diff = 0
      for k in range(0,j):
        diff = diff + coefficient_list[j][k]*sample_factors[k]
      for k in range(j+1,no_of_unknowns):
        diff = diff + coefficient_list[j][k]*sample_factors[k]
      diff = (coefficient_list[j][no_of_unknowns]-diff)/coefficient_list[j][j]
      sample_factors = sample_factors[0:j]+[diff]+sample_factors[j+1:]
      print("Error % is ",abs(100*(factors[j]-sample_factors[j])/sample_factors[j]))
    factors = sample_factors
    print("At iteration ",i+1," factors are ",sample_factors)

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