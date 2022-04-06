
a,b,c=map(str,input().split())
x,y,z=map(int,input().split())

if a==b:
  e=max(x,y,z)
  print("Max : ",e)
elif a==c:
  k=min(x,y,z)
  print("Min :",k)
else:
  print("None")