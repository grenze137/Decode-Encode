import tkinter

win = tkinter.Tk() 
win.geometry("480x700")
win.resizable (0,0)
win.title("Encode/Decode")
win.configure(bg='black')

#input od uživatele
text= tkinter.StringVar()
result = text

modes=["morse", "reverse"]
mode = tkinter.StringVar()


#módy
def decodeScreen():
	text.set("")
	mode.set("")
	#tlačítka na přepínání módů
	tkinter.Button (win, text = "Decode", command = decodeScreen, bg="black", fg = "green", activebackground="black", activeforeground ="green", cursor="hand2 ").place(x=0,y=0)
	tkinter.Button (win, text = "Encode", command = encodeScreen, bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2").place(x=51, y=0)
	
	#message
	tkinter.Label(win,text="Message", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 60)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=text, width = 50,fg = "green").place(x=100, y=60)

	#type
	tkinter.Label(win,text="Type", bg = "black", bd=0, fg="black", font="TkDefaultFont 10 bold").place (x=20, y= 110)
	#result
	tkinter.Button (win, text = "Result",command = decode,bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2", font="TkDefaultFont 10 bold").place(x=20, y=170)
	#zykrývač result
	tkinter.Label(win,bg="black", font="TkDefaultFont 10", width = 50, ).place(x=100, y=170)


def encodeScreen():
	text.set("")
	mode.set("")
	#tlačítka na přepínání módů
	tkinter.Button (win, text = "Decode", command = decodeScreen, bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2").place(x=0,y=0)
	tkinter.Button (win, text = "Encode", command = encodeScreen, bg="black", fg = "green", activebackground="black", activeforeground ="green", cursor="hand2" ).place(x=51, y=0)
	
	#message
	tkinter.Label(win,text="Message", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 60)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=text, width = 50,fg = "green").place(x=100, y=60)

	#type
	tkinter.Label(win,text="Type", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 110)
	Listbox=tkinter.Listbox (win,height=3)
	pos = 1
	for e in modes:
		Listbox.insert(pos, e)
		pos +=1
	Listbox.place(x=100, y=110)

	#result
	tkinter.Button (win, text = "Result",command = decode,bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2", font="TkDefaultFont 10 bold").place(x=20, y=170)
	#zakrývač result
	tkinter.Label(win,bg="black", font="TkDefaultFont 10", width = 50, ).place(x=100, y=170)





#po zmáčknutí result decode
def decode():
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=text, width = 50,fg = "green", state="readonly").place(x=100, y=60)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=result, width = 50,fg = "green", state="readonly").place(x=100, y=170)

#po zmáčknutí result encode
def encode():
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=text, width = 50,fg = "green", state="readonly").place(x=100, y=60)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=result+"fuck", width = 50,fg = "green", state="readonly").place(x=100, y=170)




#program
decodeScreen()

win.mainloop()