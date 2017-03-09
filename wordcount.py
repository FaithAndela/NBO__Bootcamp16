def words(teststring):

  my_string = teststring.split()

  dict1 = {}

  for st in my_string:

      if st.isdigit() == True:

          st = int(st)

      dict1[st] = dict1.get(st, 0) + 1

  return dict1
print(words("testing 1 2 testing"))