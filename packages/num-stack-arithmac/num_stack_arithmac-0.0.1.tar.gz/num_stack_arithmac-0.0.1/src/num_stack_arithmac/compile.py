def compilele(prog,start):
    num=start
    for x in prog:
        if x=="+":
            num+=1
        elif x=="-":
            num-=1
        elif x=="%":
            num=num%2
        elif x=="^":
            num=num**2
        elif x=="r":
            num=num**.5
        elif x=="p":
            print(num,end="")
        elif x=="q":
            print(chr(num),end="")
        elif x=="b":
            print(bin(num)[2:],end="")
        elif x=="x":
            print(hex(num)[2:],end="")
        elif x=="o":
            print(bool(num),end="")
        elif x=="s":
            break
def run():
    print("Welcome to Num Stack Arithmac!\n\n\n\n")
    inn=input("Enter the filepath or code you want to run:\n\n")
    if "." in inn or "\\" in inn:
        with open(inn) as c:
            code=c.read()
    else:
        code=inn
    stdin=input("Enter the starting number:\n\n")
    if stdin==None:
        stdin=0
    compilele(code,stdin)
    if input('Input "Q" if you want to stop the programme.')=="Q":
        quit()
    else:
        run()
run()