#EVAL 1 Wednesday 9-11
s="Refer"
s2="Regfree"
s3=[]
s4=[]
s5=[]
j=0
m=0
k=0
f=0
Test= True
for i in s:
    j+=1
for d in s2:
    m+=1
if (j<m):
    for item in range(0,j):
        if (s[item]==s2[item]):
          s3.append(s[item])
        else :
          s4.append(s[item])
          s5.append(s2[item])
          Test = False
    for lm in range(j,m):
        s5.append(s2[lm])
else:
    for item in range(0,j):
        if (s[item]==s2[item]):
          s3.append(s[item])
        else :
          s4.append(s[item])
          s5.append(s2[item])
          Test = False
    for lm in range(m,j):
        s5.append(s2[lm])


if Test :
    print("Both of these strings are same ")
else:
    print("The strings are not same")
s3="".join(s3)
s4.append(",")
for ite in range(0,len(s5)):
    s4.append(s5[ite])
s4="".join(s4)
print(f'The Common String is {s3}')

print(f'The String with all uncommon values is {s4}')
