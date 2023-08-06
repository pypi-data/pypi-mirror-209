import tkinter as tk
from tkinter import filedialog as fd
def compilele(prog,start,boole):
    comment=False
    num=float(start)
    s=""
    for x in prog:
            if comment and x!=">":
                pass
            elif x=="+":
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
                if num==int(num):
                    s+=str(int(num))
                else:
                    s+=str(num)
            elif x=="q":
                s+=chr(int(num))
            elif x=="b":
                s+=bin(int(num))[2:]
            elif x=="x":
                s+=hex(int(num))[2:]
            elif x=="o":
                s+=str(bool(num))
            elif x=="<":
                comment=True
            elif x==">":
                comment=False
            elif x=="s":
                break
    if boole:
        global out
        try:
            out.delete("1.0",tk.END)
            out.insert("1.0",s)
        except Exception as e:
            out=tk.Text(window)
            out.pack()
            out.insert("1.0",s)
    else:
        print("\n\n"+s)
def graphic():
    global window
    window=tk.Tk()
    window.title("Num Stack Arithmac")
    close=tk.Button(window,text="Exit",command=lambda:window.destroy())
    close.pack()
    labeli=tk.Label(window,text="Code:",font=("TkDefaultFont",15))
    labeli.pack()
    text=tk.Text(window)
    text.pack()
    labelii=tk.Label(window,text="Starting Number:",font=("TkDefaultFont",15))
    labelii.pack()
    number=tk.Entry(window)
    number.pack()
    filleri=tk.Label(window,text="")
    filleri.pack()
    def handle():
        p=text.get('1.0',tk.END)
        i=number.get()
        if i=="" or i==None:
            i=0
        compilele(p,i,True)
    button=tk.Button(window,text="Run",command=handle,width=20,height=2)
    button.pack()
    fillerii=tk.Label(window,text="")
    fillerii.pack()
    # def openfile():
        # types=(("Num Stack Arithmac Scripts","*.nsa"))
        # global filename
        # filename=fd.askopenfilename(title="Open Script",filetypes=types)
        # with open(filename) as file:
            # content=file.read()
        # text.delete("1.0",tk.END)
        # text.insert("1.0",content)
    # def savefile():
        # global filename
        # try:
            # with open(filename,'w') as file:
                # file.write(text.get("1.0",tk.END))
        # except:
            # filename=fd.asksavefile(initialfile="numstackarithmacscript.nsa",defaultextension=".nsa",filetypes=(("Num Stack Arithmac Scripts","*.nsa")))
    # openfile=tk.Button(window,text="Open",command=openfile,width=20,height=2)
    # openfile.pack(side="left")
    # savefile=tk.Button(window,text="Save",command=savefile,width=20,height=2)
    # savefile.pack(side="right")
    window.mainloop()
def run():
    print("\nWelcome to Num Stack Arithmac!\n\n\n\n")
    inn=input("Enter the filepath or code you want to run (or type \"g\" for a graphical editor with no support for saving and opening files):\n\n")
    if "." in inn or "\\" in inn:
        with open(inn) as c:
            code=c.read()
    elif inn=="g":
        graphic()
        run()
    else:
        code=inn
    stdin=input("\n\nEnter the starting number:\n\n")
    if stdin==None:
        stdin=0
    compilele(code,stdin,False)
    if input('\n\nInput "Q" or "q" if you want to stop the programme. ') in "Qq":
        quit()
    else:
        run()
run()