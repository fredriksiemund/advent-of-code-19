from intcode2 import calcThruster

a = [9,7,8,5,6]
highest_value = 0
def permutation(start, end):
  global highest_value
  if end==start:
    return_value = int(calcThruster("input.txt", a))
    if return_value > highest_value:
      highest_value = return_value
    return
  for i in range(start, end+1):
    a[i],a[start] = a[start],a[i]
    permutation(start+1, end)
    a[i],a[start] = a[start],a[i]
permutation(0,len(a)-1)

print(highest_value)

