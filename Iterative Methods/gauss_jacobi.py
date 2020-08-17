import get_coefficients_as_list
import check_diagonal_dominant

# function that computes in gauss jacobi method
def gauss_jacobi(no_of_unknowns):
  coefficient_list = get_coefficients_as_list.get_coefficients_as_list(no_of_unknowns)
  if check_diagonal_dominant.is_diagonally_dominant(coefficient_list):
    print("Computing...")
  else:
    print("Matrix failed to be diagonally dominant\nExiting...")
    return
  factors = [0]*(no_of_unknowns)
  sample_factors = [0]*(no_of_unknowns)
  for i in range(0,6):
    for j in range(0,no_of_unknowns):
      diff = 0
      for k in range(0,j):
        diff = diff + coefficient_list[j][k]*factors[k]
      for k in range(j+1,no_of_unknowns):
        diff = diff + coefficient_list[j][k]*factors[k]
      #print(coefficient_list[j][no_of_unknowns],"-",diff,"/",coefficient_list[j][j])
      diff = (coefficient_list[j][no_of_unknowns]-diff)/coefficient_list[j][j]
      sample_factors = sample_factors[0:j]+[diff]+sample_factors[j+1:]
    factors = sample_factors
    print("At iteration ",i+1," factors are ",factors)