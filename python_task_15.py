f=open("names.txt", "r")
names_count = {}
if f.mode == 'r':
  names = f.read().split("\n")

  for name in names:
      if name in names_count:
          names_count[name] += 1
      else:
          names_count[name] = 1

  for name in names_count:
      print(name, ": ", names_count[name])