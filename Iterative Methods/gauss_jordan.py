import get_coefficients_as_list
import check_diagonal_dominant

# function that computes in gauss jardon method
def gauss_jordan(no_of_unknowns):
  factors = [0]*no_of_unknowns
  coefficient_list = get_coefficients_as_list.get_coefficients_as_list(no_of_unknowns)
  if check_diagonal_dominant.is_diagonally_dominant(coefficient_list):
    print("Computing...")
  else:
    print("Matrix failed to be diagonally dominant\nExiting...")
    return
  for i in range(0,no_of_unknowns):
    if int(coefficient_list[i][i]) == 0:
      print('Divide by zero detected!')
      return
    for j in range(0,no_of_unknowns):
      if i != j:
        ratio = coefficient_list[j][i]/coefficient_list[i][i]
        for k in range(0,no_of_unknowns+1):
          coefficient_list[j][k] = coefficient_list[j][k] - ratio * coefficient_list[i][k]
  # Obtaining Solution
  for i in range(0,no_of_unknowns):
    factors[i] = coefficient_list[i][no_of_unknowns]/coefficient_list[i][i]
  print(factors)