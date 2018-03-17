t=int(input())
a=[]
b=[]
c=[]
d=[]
k=0
cnt=0
for i in range(0,t):
    m,p=input().strip().split(' ')
    m,p=[int(m),int(p)]
    a.append(m)
    b.append(p)
for g in range(t):
  for i in a:
    while (1):
      r=i%2
      i=i/2
      c.append(r)
      if i is 1:
         break
    if(1):
      break
  for j in b:
      while(1):
        r1=j%2
        j=j/2
        d.append(r1)
        if j is 1:
           break
      if len(c) > len(d):
        while(1):
           d.insert(0)
           if len(c) == len(d):
              break
      elif len(c)< len(d):
        while(1):
             c.insert(0)
             if len(c) == len(d):
                break
      for s in c:
         if s is not d[:k]:
           cnt+=cnt
           k=k+1
      print(cnt)
      c.clear()
      d.clear()
