def mainFunction():
  fname=input("Enter file name:")
  total=0
  count=0
  with open(fname,'r') as f:
    for line in f:
      for num in line.strip().split():
        total=total+float(num)
        count=count+1
  print ('\n The Avarage is:',total/count)
mainFunction()
