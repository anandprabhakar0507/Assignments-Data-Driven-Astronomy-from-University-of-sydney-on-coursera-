# Write your list_stats function here.
def list_stats(arr_list):
  sum_list = 0
  length = len(arr_list)
  for item in arr_list:
    sum_list = sum_list + item
  mean = sum_list/length
  mid = len(arr_list)
  arr_list.sort()
  if mid%2 == 0:
    mid1 = mid/2
    mid2 = mid1+1
    mid1 = mid1 - 1
    mid2 = mid2 - 1
    median = 0.5*(arr_list[int(mid1)]+arr_list[int(mid2)])
  else:
    median = arr_list[int(((mid+1)/2))-1]
  return (median,mean)
  



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)