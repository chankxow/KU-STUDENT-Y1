def countConsec(lst):


  max_count = 0
  max_elem = None
  curr_count = 0
  curr_elem = None

  for elem in lst:
    if elem == curr_elem:
      curr_count += 1
    else:
      if curr_count > max_count:
        max_count = curr_count
        max_elem = curr_elem
      curr_count = 1
      curr_elem = elem

  if curr_count > max_count:
    max_count = curr_count
    max_elem = curr_elem

  return max_elem, max_count

lst = eval(input('Enter a list of objects: '))

result = countConsec(lst)

if result[1] > 1:
  print(result[0])
  print(result[1])
else:
  print("Nothing to do.")