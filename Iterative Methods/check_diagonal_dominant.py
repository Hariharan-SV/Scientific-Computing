def is_diagonally_dominant(coefficient_list):
  for i in range(0,len(coefficient_list)):
    row_sum = 0
    for j in range(0,len(coefficient_list[i])):
      row_sum = row_sum + abs(coefficient_list[i][j])
    row_sum = row_sum - abs(coefficient_list[i][i])
    if(abs(coefficient_list[i][i]) < row_sum):
      return False
  return True