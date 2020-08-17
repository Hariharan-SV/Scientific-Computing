import get_coefficients_as_list
import check_diagonal_dominant

# function that computes in gauss seidall method
def gauss_seidall(no_of_unknowns):
  coefficient_list = get_coefficients_as_list.get_coefficients_as_list(no_of_unknowns)
  if check_diagonal_dominant.is_diagonally_dominant(coefficient_list):
    print("Computing...")
  else:
    print("Matrix failed to be diagonally dominant\nExiting...")
    return
  factors = [1]+[0]*(no_of_unknowns-2)+[1]
  sample_factors = [1]+[0]*(no_of_unknowns-2)+[1]
  for i in range(0,6):
    for j in range(0,no_of_unknowns):
      diff = 0
      for k in range(0,j):
        diff = diff + coefficient_list[j][k]*sample_factors[k]
      for k in range(j+1,no_of_unknowns):
        diff = diff + coefficient_list[j][k]*sample_factors[k]
      #print(coefficient_list[j][no_of_unknowns],"-",diff,"/",coefficient_list[j][j])
      diff = (coefficient_list[j][no_of_unknowns]-diff)/coefficient_list[j][j]
      sample_factors = sample_factors[0:j]+[diff]+sample_factors[j+1:]
      print("Error % is ",abs(100*(factors[j]-sample_factors[j])/sample_factors[j]))
    factors = sample_factors
    print("At iteration ",i+1," factors are ",sample_factors)