def ms(n):
 s=[False]*2+[True]*(n\
-1)
 for x in range(2,n+1):
  if s[x]:
   m=2*x
   while m<=n:
    s[m]=\
False;m+=x
 return s
def lis(n):
 v = ms(n);                                                           p=[];
 for x in range(0,len(v)):
  if v[x]:p.\
append(x)
 return p
def r():
 print("enter a number:"),
 while True: 
  s=input()
  try:
   n=int(s)
   if n < 2:print("error:")
   else:return n
  except ValueError:print("error:")
def m():
 n=r();xs=\
lis(n)
 print(len(xs),"answers:")
 for x in xs:print(x)
 print("end of program")
m()
