def pattern(n):
    for i in range(n-1):
        for j in range(i+1):
            print("",end="")
        for k in range(n-i-1):
            print("*",end="")
        print()
n=int(input("\n Enter Your Row Number:-"))
pattern(n)
