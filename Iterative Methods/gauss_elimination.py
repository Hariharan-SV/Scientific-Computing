import get_coefficients_as_list

# function that computes in gauss elimination method
# coefficient_list=[[3,-2,5,0,2],[4,5,8,1,4],[1,1,2,1,5],[2,7,6,5,7]]
# factors = [28.7777777777778, 2.1666666666666683, -16.00000000000001, 6.055555555555558]
def gauss_elimination(no_of_unknowns):
  coefficient_list = get_coefficients_as_list.get_coefficients_as_list(no_of_unknowns)
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