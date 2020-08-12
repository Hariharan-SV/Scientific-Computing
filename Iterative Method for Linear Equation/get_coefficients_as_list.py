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