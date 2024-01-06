'''
# Square Hollow Pattern
n=int(input())
for i in range(n):
  for j in range(n-1):
    if ((i==0) or (i==(n-1)) or (j==0) or (j==n-2)):
      print('* ',end='')
    else:
      print('  ',end='')
  print('\n')

# Number Triangular
n = int(input())
for i in range(n):
  for k in range(n-i+1):
    print(" ",end='')
  for j in range(i+1):
    print(i+1,end=' ')
  print('\n')

# Number Increasing Pyramid
n = int(input())
for i in range(n):
  for j in range(i+1):
    print(i+1,end=' ')
  print('\n')

# Number Increasing Reverse Pyramid
n = int(input())
for i in range(n):
  for j in range(n-i):
    print(j+1,end=' ')
  print('\n')

# Number Changing Pyramid
n = int(input())
num=0
for i in range(n):
  for j in range(i+1):
    num+=1
    print(num,end=' ')
  print('\n')

# Palindrome Triangular
n = int(input())

for i in range(n+1):
  for k in range(n-i+1):
    print(" ",end='')
  x=i
  for j in range(i):
    print(x,end='')
    x-=1
  for l in range(i):
    if l+1==1:
      continue
    else:  
      print(l+1,end='')
  print('\n')

# Diamond Pattern
n = int(input())
for i in range(1,n+1):
  for k in range(n-i):
    print(" ",end='')
  for j in range(i):
    print('*',end=' ')
  print('\n')  
for i in range(n-1,0,-1):
  for k in range(n-i):
    print(" ",end='')
  for j in range(i):
    print('*',end=' ')
  print('\n')

# Hellow Triangle Pattern
n = int(input())
for i in range(1,n+1):
  for k in range(n-i):
    print(" ",end='')
  for j in range(1,i*2):
    if((i==1) or(i==n) or (j==1) or(j==i*2-1)):
      print("*",end='')
    else:
      print(" ",end='')
  print('\n')

#Hellow Reverse Triangle Pattern
n= int(input())
for i in range(n,0,-1):
  for k in range(n-i):
    print("  ",end='')
  for j in range(2*i-1):
    if((i==0)  or (j==0) or(j==i*2-2)):
      print("* ",end='')
    else:
      print("  ",end='')
  print(' \n')

# Hollow Diamond Pyramid
n =int(input())
for i in range(1,n):
  for k in range(n-i):
    print("  ",end='')
  for j in range(1,i*2):
    if((i==1)  or (j==1) or(j==i*2-1)):
      print("* ",end='')
    else:
      print("  ",end='')
  print(' \n')
for i in range(n,0,-1):
  for k in range(n-i):
    print("  ",end='')
  for j in range(2*i-1):
    if((i==0)  or (j==0) or(j==i*2-2)):
      print("* ",end='')
    else:
      print("  ",end='')
  print(' \n')

#  Pascal's Triangle 
n = int(input())
for i in range(1, n+1):
  for j in range(0, n-i+1):
    print(' ', end='')
  C = 1
  for j in range(1, i+1):
    print(' ', C, sep='', end='')
    C = C * (i - j) // j
  print()

#Zero-One Triangle
n=int(input())
for i in range(1,n+1):
  num=0
  for j in range(1,i+1):
    if ((j==1) and(i%2==0)):
      num=1
    num=(1 if num==0 else 0)
    print(num,end='')
  print()
'''
