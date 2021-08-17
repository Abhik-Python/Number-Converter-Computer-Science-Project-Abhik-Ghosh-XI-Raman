import os
import tkinter
import tkinter.font
import tkinter.messagebox
from tkinter import *


class Conversions:

    def bintodec(self, b):
        s = b[::-1]
        out = 0
        for x in range(0, len(s)):
            out += int(s[x]) * (2 ** x)
        return str(out)

    def octtodec(self, o):
        s = o[::-1]
        out = 0
        for x in range(0, len(s)):
            out += int(s[x]) * (8 ** x)
        return str(out)

    def hextodec(self, h):
        s = h[::-1]
        l = []
        out = 0

        for x in s:
            if x == "A":
                l.append("10")
            elif x == "B":
                l.append("11")
            elif x == "C":
                l.append("12")
            elif x == "D":
                l.append("13")
            elif x == "E":
                l.append("14")
            elif x == "F":
                l.append("15")
            else:
                l.append(x)

        for i in l:
            out += int(i) * (16 ** l.index(i))

        return out

    def dectobin(self, d):
        b = 0
        m = 1
        while int(d) > 0:
            b = b + ((int(d) % 2) * m)
            m = m * 10
            d = int(int(d) / 2)
        return b

    def dectooct(self, o):
        b = 0
        m = 1
        d = int(o)
        while d > 0:
            b = b + ((d % 8) * m)
            m = m * 10
            d = int(d / 8)
        return b

    def dectohex(self, h):
        i = 0
        s = ""
        decnum = int(h)
        hexdecnum = []
        while decnum != 0:
            rem = decnum % 16
            if rem < 10:
                rem = rem + 48  # ASCII Values Defines here for chr() refered https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
            else:
                rem = rem + 55  # ASCII Values Defines here for chr() refered https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
            rem = chr(rem)
            hexdecnum.insert(i, rem)
            i = i + 1
            decnum = int(decnum / 16)
        for x in hexdecnum:
            s = s + str(x)
        return s[::-1]


def Main(c):
    root = Tk()
    root.config(bg="#F0EEDC")
    root.resizable(width=False, height=False)
    root.title("Number Converter | By Abhik Ghosh | XI Raman")
    root.geometry("790x550")

    if os.path.isfile("icon.png"):
        root.iconphoto(True, tkinter.PhotoImage(file='icon.png'))

    lblt = Label(root, text="NUMBER CONVERTER", font=("", 32), bg="#F0EEDC")
    llpl = Label(root, text="                                                         ", bg="#F0EEDC")
    llpl75 = Label(root, text="                                                        ", bg="#F0EEDC").grid(row=0,
                                                                                                             column=2)
    llpl.grid(row=0, column=0)
    lblt.grid(row=0, column=1)
    label1 = Label(root, text=" ", bg="#F0EEDC").grid(row=1, column=0, columnspan=3)
    llpl2 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=2,
                                                                                                             column=0)
    label2 = Label(root, text="Enter number to convert:", bg="#F0EEDC").grid(row=2, column=1)

    llpl3 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=3,
                                                                                                             column=0)
    val_var = tkinter.StringVar()
    inp = Entry(root, width=25, textvariable=val_var, relief=tkinter.constants.GROOVE).grid(row=3, column=1)

    llpl5 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=4,
                                                                                                             column=0,
                                                                                                             columnspan=3)

    llpl6 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=5,
                                                                                                             column=0)
    llpl44 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=6,
                                                                                                              column=0)
    label3 = Label(root, text="Convert From: ", font=("", 12), bg="#F0EEDC").grid(row=7, column=0)

    options = ["Binary", "Decimal", "Octal", "Hexadecimal"]
    clicked1 = StringVar()
    clicked1.set("Decimal")

    drop1 = OptionMenu(root, clicked1, *options)
    drop1.grid(row=7, column=1)

    llpl275 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=8,
                                                                                                               column=0)

    label4 = Label(root, text="Convert to: ", font=("", 12), bg="#F0EEDC").grid(row=9, column=0)

    clicked2 = StringVar()
    clicked2.set("Binary")

    drop2 = OptionMenu(root, clicked2, *options).grid(row=9, column=1)

    llpl4 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=11,
                                                                                                             column=0)

    bt = Button(root, text="CONVERT", command=lambda: {onclick()}).grid(row=12, column=1)

    llpl4 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=13,
                                                                                                             column=0)

    llpl4 = Label(root, text="                                                         ", bg="#F0EEDC").grid(row=14,
                                                                                                             column=0)
    llpl4 = Label(root, text="ANSWER", font=("", 15), bg="#F0EEDC").grid(row=14, column=1)

    T = Text(root, width=50, relief=tkinter.constants.GROOVE)
    T.grid(row=15, column=1)

    def onclick():
        box1 = clicked1.get()
        box2 = clicked2.get()
        ein = val_var.get()

        decnum = 0
        ans = 0

        if ein.find(".") != -1:
            tkinter.messagebox.showerror("Value Error",
                                         "This Converter Does Not Support Decimal Numbers Please Enter Whole Numbers Only",
                                         parent=root)
            val_var.set("")
            T.delete(1.0, "end")
            return
        l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z', " "]

        for x in l:
            if ein.find(x) != -1:
                tkinter.messagebox.showerror("Value Error",
                                             "Please Enter only Valid Numbers i.e : 0 - 9 , A , B , C , D , E ,F ",
                                             parent=root)
                val_var.set("")
                T.delete(1.0, "end")
                return

        binl = ["2", "3", "4", "5", "6", "7", "8", "9"]
        octl = ["8", "9"]

        if box1 != "Decimal":
            if box1 == "Binary":
                for x in binl:
                    if ein.find(x) != -1:
                        tkinter.messagebox.showerror("Value Error",
                                                     "Please enter a valid Binary Number",
                                                     parent=root)
                        val_var.set("")
                        T.delete(1.0, "end")
                        return
                else:
                    decnum = c.bintodec(ein)
            elif box1 == "Octal":
                for x in octl:
                    if ein.find(x) != -1:
                        tkinter.messagebox.showerror("Value Error",
                                                     "Please enter a valid Octal Number",
                                                     parent=root)
                        val_var.set("")
                        T.delete(1.0, "end")
                        return
                    else:
                        decnum = c.octtodec(ein)
            elif box1 == "Hexadecimal":
                for x in l:
                    if ein.find(x) != -1:
                        tkinter.messagebox.showerror("Value Error",
                                                     "Please enter a valid Hexadecimal Number ( eg 18A case sensitive)",
                                                     parent=root)
                        val_var.set("")
                        T.delete(1.0, "end")
                        return
                    else:
                        decnum = c.hextodec(ein)
        else:
            if ein.isdecimal():
                decnum = int(ein)
            else:
                tkinter.messagebox.showerror("Value Error",
                                             "Please Input a Valid Decimal Value",
                                             parent=root)
                val_var.set("")
                T.delete(1.0, "end")
                return

        if box2 == "Binary":
            ans = c.dectobin(decnum)
        elif box2 == "Octal":
            ans = c.dectooct(decnum)
        elif box2 == "Hexadecimal":
            ans = c.dectohex(decnum)
        else:
            ans = decnum

        T.delete(1.0, "end")
        T.insert(1.0, ans)

    root.mainloop()


if __name__ == "__main__":
    con = Conversions()
    Main(con)
