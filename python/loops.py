n=4 #for loop
for i in range(0,n):
    print(i)

a=["geeks","for","geeks"] #Iteration by index of sequences
for idx in range(len(a)):
    print(a[idx])

cnt = 0 #While Loop
while (cnt < 3):
    cnt = cnt+1
    print("Hello geeks")

    for i in range (1,5):
        for j in range(i):
            print(i, end='')
            print()