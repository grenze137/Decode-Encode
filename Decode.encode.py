"""
nový typ přidat do:
seznam modes
def needKey
novou funkci
"""

"""
def name(t, k):
	global answer
	a= ""
	
	if m=="e": 
		...
	elif m=="d":
		...
	answer.set(a)
"""

import tkinter
import random

win = tkinter.Tk() 
win.geometry("400x350")
win.resizable (0,0)
win.title("Encode/Decode")
win.configure(bg='black')

#input od uživatele
text = tkinter.StringVar()
key = tkinter.StringVar()

modes=["substituce","sub. (postupně)","substituce(heslo)","ASCII", "pozpátku", "pozpátku (slova)", "odpředu a odzadu", "proložení textu", "písmena na čísla", "zlomky", "mobilní šifra", "tabulka", "obrácená abeceda", "morseovka", "morseovka(inverze)", "morseovka(změna)", "morseovka(čísla)", "šifrovací kříže", "číselný klíč"]

čárkyHáčky = {"á":"a", "é":"e", "ě":"e", "í":"i", "ó":"o", "ů":"u", "ú":"u","ý":"y", "č":"c", "ď":"d", "ň":"n", "ř":"r", "š":"s", "ť":"t", "ž":"z"}
abeceda= ["a","b", "c", "d", "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
answer= tkinter.StringVar()
mobil = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
morse= { 'a':'.-', 'b':'-...','c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-','l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-','r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--','x':'-..-', 'y':'-.--', 'z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ',':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
suda = ["0","2","4","6","8"]
licha = ["1","3","5","7","9"]
znaminka = ["+","-","*",":"]

#módy
def decodeScreen():
	global Listbox
	global m
	m="d"
	text.set("")
	key.set("")
	#tlačítka na přepínání módů
	tkinter.Button (win, text = "Dekódovat", command = decodeScreen, bg="black", fg = "green", activebackground="black", activeforeground ="green", cursor="hand2 ",).place(x=0,y=0)
	tkinter.Button (win, text = "Zakódovat", command = encodeScreen, bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2").place(x=65, y=0)
	
	#message
	tkinter.Label(win,text="Text", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 60)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=text, width =35,fg = "green").place(x=100, y=60)
	#zakrývač
	tkinter.Label(win,bg = "black", width=15).place (x=100, y=83)

	#key
	tkinter.Label(win,text="Klíč", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 110)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=key, width =35,fg = "green").place(x=100, y=110)

	#type
	tkinter.Label(win,text="Typ", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 160)
	tkinter.Label(win,bg = "black", width=40).place (x=100, y=132)
	Listbox=tkinter.Listbox (win,height=5, bg="green", fg="black", font="TkDefaultFont 10", cursor="hand2", selectbackground="black", relief="flat", highlightthickness="0",selectmode="single", width = 15, selectforeground="green", activestyle="none", justify="center",)
	pos=1
	for e in modes:
		Listbox.insert(pos, e)
		pos +=1
	Listbox.place(x=100, y=160)
	scrollbar = tkinter.Scrollbar(win, command = Listbox.yview,  )
	scrollbar.place(x=207,y=160, height=87)
	Listbox.config(yscrollcommand=scrollbar.set)
	#zakrývač
	tkinter.Label(win,bg = "black", width=13).place (x=225, y=160)

	#result
	tkinter.Button (win, text = "Výsledek",command = result,bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2", font="TkDefaultFont 10 bold").place(x=20, y=280)
	#zykrývač result
	tkinter.Label(win,bg="black", font="TkDefaultFont 10", width = 50, ).place(x=100, y=280)

def encodeScreen():
	global m
	m="e"
	global Listbox
	text.set("")
	key.set("")
	#tlačítka na přepínání módů
	tkinter.Button (win, text = "Dekódovat", command = decodeScreen, bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2 ",).place(x=0,y=0)
	tkinter.Button (win, text = "Zakódovat", command = encodeScreen, bg="black", fg = "green", activebackground="black", activeforeground ="green", cursor="hand2").place(x=65, y=0)
	
	#message
	tkinter.Label(win,text="Text", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 60)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=text, width =35,fg = "green").place(x=100, y=60)
	#zakrývač
	tkinter.Label(win,bg = "black", width=15).place (x=100, y=83)

	#key
	tkinter.Label(win,text="Klíč", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 110)
	tkinter.Entry(win, cursor = "xterm", font="TkDefaultFont 10", textvariable=key, width =35,fg = "green").place(x=100, y=110)

	#type
	tkinter.Label(win,text="Typ", bg = "black", bd=0, fg="green", font="TkDefaultFont 10 bold").place (x=20, y= 160)
	tkinter.Label(win,bg = "black", width=40).place (x=100, y=132)
	Listbox=tkinter.Listbox (win,height=5, bg="green", fg="black", font="TkDefaultFont 10", cursor="hand2", selectbackground="black", relief="flat", highlightthickness="0",highlightbackground="blue",selectmode="single", width = 15, selectforeground="green", activestyle="none", justify="center",)
	pos=1
	for e in modes:
		Listbox.insert(pos, e)
		pos +=1
	Listbox.place(x=100, y=160)
	scrollbar = tkinter.Scrollbar(win, command = Listbox.yview,  )
	scrollbar.place(x=207,y=160, height=87)
	Listbox.config(yscrollcommand=scrollbar.set)
	#zakrývač
	tkinter.Label(win,bg = "black", width=13).place (x=225, y=160)


	#result
	tkinter.Button (win, text = "Výsledek",command = result,bg="green", fg = "black", activebackground="black", activeforeground ="green", cursor="hand2", font="TkDefaultFont 10 bold").place(x=20, y=280)
	#zykrývač result
	tkinter.Label(win,bg="black", font="TkDefaultFont 10", width = 50, ).place(x=100, y=280)


def withoutDia(t):
	te = ""
	for letter in t:
		if letter in čárkyHáčky:
			te +=čárkyHáčky[letter]
		else:
			te += letter
	return te

#je potřeba klíč
def needKey(mode):
	global keyText
	k=key.get()
	te = text.get()
	try:
		k=int(k)
	except:
		"fucl"
	#různý typy
	if mode=="substituce":
		te=te.lower()
		keyText="*Povinné pole-libovolné celé číslo"
		if k=="":
			return True
		elif type(k)!=int:
			return True
		else:
			substituce(withoutDia(te),k)
			return False

	elif mode=="ASCII":
		ASCII(withoutDia(te))
		return False

	elif mode=="pozpátku":
		pozpatku(te)
		return False

	elif mode=="pozpátku (slova)":
		pozpatkuSlova(te)
		return False

	elif mode=="odpředu a odzadu":
		odpreduOdzadu(te)
		return False

	elif mode=="proložení textu":
		prolozeni(te)
		return False

	elif mode=="písmena na čísla":
		te = te.lower()
		pismenaNaCisla(withoutDia(te))
		return False

	elif mode=="zlomky":
		te.lower()
		zlomky(withoutDia(te))
		return False

	elif mode=="mobilní šifra":
		te.lower()
		mobilniSifra(withoutDia(te))

	elif mode=="tabulka":
		te=te.lower()
		keyText="*Povinné pole-libovolný pětimístný text"
		if k=="":
			return True
		elif len(k)!=5:
			return True
		else:
			tabulka(withoutDia(te),k)
			return False

	elif mode=="sub. (postupně)":
		te = te.lower()
		substitucePostupne(withoutDia(te))
		return False

	elif mode =="obrácená abeceda":
		te =te.lower()
		obracenaAbc(withoutDia(te))
		return False

	elif mode =="substituce(heslo)":
		notWord = False
		te= te.lower()
		k=k.lower()
		k=withoutDia(k)
		keyText = "*Povinné pole-libovolné slovo"

		for e in k:
			if e not in abeceda:
				notWord = True
		if k=="":
			return True
		elif notWord:
			return True
		else:
			substituceHeslo(withoutDia(te),k)
			return False
	
	elif mode=="morseovka":
		te=te.lower()
		morseovka(withoutDia(te))

	elif mode=="morseovka(inverze)":
		te=te.lower()
		morseovkaInverze(withoutDia(te))

	elif mode=="morseovka(změna)":
		morseovkaZmena(withoutDia(te))

	elif mode=="morseovka(čísla)":
		te=te.lower()
		morseovkaCisla(withoutDia(te))

	elif mode=="šifrovací kříže":
		sifrovaciKrize(te)

	elif mode=="číselný klíč":
		keyText = "*Povinné pole-libovolné součíslí, kde se neopakují čísla"
		repeat = False
		for e in str(k):
			r = 0
			for s in str(k):
				if s==e:
					r+=1
			if r>1:
				repeat = True
				break		

		if k=="":
			return True


		elif type(k)!=int:
			return True
		elif repeat:
			return True
		else:
			ciselnyKlic(te,k)
			return False



#po zmáčknutí result decode0
def result():
	global answer
	t=True
	l=True
	try:
		Listbox.get(Listbox.curselection())
		tkinter.Label(win,bg = "black", width=15).place (x=225, y=160)
	except:
		tkinter.Label(win,text="*Povinné pole", bg = "black", fg="red", font="TkDefaultFont 8").place (x=225, y=160)
		t=False
		l=False
	if text.get()=="":
		tkinter.Label(win,text="*Povinné pole", bg = "black", fg="red", font="TkDefaultFont 8").place (x=100, y=83)
		t=False
	else:
		tkinter.Label(win,bg = "black", width=15).place (x=100, y=83)
	if l:
		nK = needKey(Listbox.get(Listbox.curselection()))
		if nK:
			tkinter.Label(win,text=keyText, bg = "black", fg="red", font="TkDefaultFont 8").place (x=100, y=132)
			t=False
		else:
			tkinter.Label(win,bg = "black", width=40).place (x=100, y=132)
	else:
		tkinter.Label(win,bg = "black", width=40).place (x=100, y=132)



	if t==True:
		tkinter.Entry(win, cursor = "arrow", font="TkDefaultFont 10", textvariable=text, width = 35,fg = "green", state="readonly").place(x=100, y=60)
		tkinter.Entry(win, cursor = "arrow", font="TkDefaultFont 10", textvariable=answer, width = 35,fg = "green",state="readonly").place(x=100, y=280)
		tkinter.Entry(win, cursor = "arrow", font="TkDefaultFont 10", textvariable=key, width =35,fg = "green", state="readonly").place(x=100, y=110)
		tkinter.Label(win, bg = "black", width=20, height=6).place (x=100, y=160)
		tkinter.Label(win,text=Listbox.get(Listbox.curselection()), bg = "black", highlightbackground="green", highlightthickness=1,fg="green", font="TkDefaultFont 10", width=15).place (x=100, y=160)

		

#šifry
def substituce(t, k):
	global answer
	a= ""
	
	if m=="d":
		for l in t:
			try:
				index=abeceda.index(l)
				if index+k<=25:
					a += abeceda[index+k]
				else:
					while index+k>=26:
						index = index-26
					a += abeceda[index+k]
			except:
				a += l
	elif m=="e":
		for l in t:
			try:
				index=abeceda.index(l)
				if index-k>0:
					a += abeceda[index-k]
				else:
					while index-k<-26:
						index = index+26
					a += abeceda[index-k]
			except:
				a += l		

	answer.set(a)

def ASCII(t):
	global answer
	a= ""

	if m=="e":
		for e in t:
			a += str(ord(e))+" "
	elif m=="d":
		list = t.split()
		for e in list:
			e = int(e)
			a += chr(e)
	answer.set(a)

def pozpatku(t):
	global answer
	a= ""
	a = t[::-1]
	answer.set(a)

def pozpatkuSlova(t):
	global answer
	a= ""
	words = t.split()
	for e in words:
		a+= e[::-1]+" "
	answer.set(a)

def odpreduOdzadu(t):
	global answer
	a= ""
	
	if m=="e": 
		for e in range(len(t)):
			if e%2==0:
				a+=t[e]
		for e in reversed(range(len(t))):
			if e%2==1:
				a+=t[e]
	elif m=="d":
		pos = 0
		if len(t)%2==0:
			while pos<len(t)/2:
				if pos ==0:
					a+=t[pos]
				else:
					a+=t[-pos]+t[pos]
				pos +=1
			a+=t[pos]
		else:
			while pos<=len(t)/2:
				if pos ==0:
					a+=t[pos]
				else:
					a+=t[-pos]+t[pos]
				pos +=1
	answer.set(a)

def prolozeni(t):
	global answer
	a= ""
	if m=="e": 
		if len(t)%2==0:
			for e in range(int(len(t)/2)):
				a += t[e]+t[int(len(t)/2)+e]
		else:
			for e in range(int((len(t)+1)/2)):
				if e==int((len(t)-1)/2):
					a += t[e]
				else:
					a += t[e]+t[int((len(t)+1)/2)+e]
	elif m=="d":
		for e in range(len(t)):
			if e%2==0:
				a+=t[e]
		for e in range(len(t)):
			if e%2==1:
				a+=t[e]
	answer.set(a)	

def pismenaNaCisla(t):
	global answer
	a= ""
	
	if m=="e": 
		for e in t:
			if e==" ":
				a+="0 "
			else:
				try:
					a+=str(abeceda.index(e)+1)+" "
				except:
					a=a
	elif m=="d":
		letters = t.split()
		for e in letters:
			if e=="0":
				a+=" "
			else:
				try:
					a+=abeceda[int(e)-1]
				except:
					a=a
	answer.set(a)	

def zlomky(t):
	global answer
	a= ""
	abc = abeceda[:22]+abeceda[23:]
	if m=="e":
		for e in t:
			if e==" ":
				a+=" ;"
			elif e=="w":
				a+="2/5;2/5;"
			else:
				try:
					a+= str(abc.index(e)%5+1)+"/"
					if abc.index(e)<5:
						a+="1;"
					elif abc.index(e)<10:
						a+="2;"
					elif abc.index(e)<15:
						a+="3;"
					elif abc.index(e)<20:
						a+="4;"
					elif abc.index(e)<25:
						a+="5;"
				except:
					a=a

	elif m=="d":
		letters=t.split(";")
		for e in letters:
			if e==" ":
				a+=" "
			else:
				try:
					a+= abc[(int(e[2])-1)*5+int(e[:1])-1]
				except: 
					a=a
	answer.set(a)

def mobilniSifra(t):
	global answer
	a= ""
	
	if m=="e": 
		for e in t:#pímsena v textu
			if e!=" ":
				if e in abeceda:
					for n in mobil:#čísla v telefonu
						letters = mobil[n]
						if e in letters:
							a+=n*(letters.index(e)+1)+" "
	elif m=="d":
		letter=t.split()
		try:
			for e in letter:
				n=mobil[e[0]]
				a+=n[len(e)-1]
		except:
			a=a
	answer.set(a)

def tabulka(t, k):
	global answer
	a= ""
	abc = abeceda[:16]+abeceda[17:]
	if m=="e": 
		for e in t:

				if e=="q":
					a+="Q;"
				elif e==" ":
					a+=" ;"
				else:
					try:
						if abc.index(e)<5:
							a+=k[0]
						elif abc.index(e)<10:
							a+=k[1]
						elif abc.index(e)<15:
							a+=k[2]
						elif abc.index(e)<20:
							a+=k[3]
						elif abc.index(e)<25:
							a+=k[4]
					
						a+=str(abc.index(e)%5+1)+";"
					except:
						a=a

	elif m=="d":
		k=k.lower()
		letter = t.split(";")
		for e in letter:
			if e==" ":
				a+=" "
			elif e=="Q":
				a+="q"
			else:
				try:
					a+=abc[k.index(e[0])*5+int(e[1])-1]
				except:
					a=a
	answer.set(a)

def substitucePostupne(t):
	global answer
	a= ""
	pos = 0
	if m=="e": 
		for e in t:
			if e==" ":
				a+=" "
			else:
				try:
					index=abeceda.index(e)
					if index+pos<=25:
						a += abeceda[index+pos]
					else:
						while index+pos>=26:
							index = index-26
						a += abeceda[index+pos]
					pos += 1
				except:
					a =a
	elif m=="d":
		for e in t:
			if e==" ":
				a+=" "
			else:
				try:
					index=abeceda.index(e)

					if index-pos>0:
						a += abeceda[index-pos]
					else:
						while index-pos<-26:
							index = index+26
						a += abeceda[index-pos]
					pos += 1
				except:
					a = a

	answer.set(a)

def obracenaAbc(t):
	global answer
	a= ""
	
	if m=="e": 
		for e in t:
			try:
				index = abeceda.index(e)
				a+=abeceda[-index-1]
			except:
				a+= e
	if m=="d":
		for e in t:
			try:
				index = abeceda.index(e)
				a+=abeceda[-index-1]
			except:
				a+= e
	answer.set(a)

def substituceHeslo(t, k):
	global answer
	a= ""
	pos = 0
	
	if m=="e": 
		for l in t:
			if l==" ":
				a+=" "
			else:
				if pos>=len(k):
					pos=pos-len(k)
				try:
					index=abeceda.index(l)
					indexDva = abeceda.index(k[pos])
					if index+indexDva<=25:
						a += abeceda[index+indexDva]
					else:
						while index+indexDva>=26:
							index = index-26
						a += abeceda[index+indexDva]
					pos +=1
				except:
					a = a

	elif m=="d":
		for e in t:
			if e==" ":
				a+=" "
			else:
				if pos>=len(k):
					pos=pos-len(k)
				try:
					index=abeceda.index(e)
					indexDva = abeceda.index(k[pos])

					if index-indexDva>0:
						a += abeceda[index-indexDva]
					else:
						while index-indexDva<-26:
							index = index+26
						a += abeceda[index-indexDva]
					pos += 1
				except:
					a = a
	answer.set(a)

def morseovka(t):
	global answer
	a= ""
	
	if m=="e": 
		for e in t:
			try:
				if e==" ":
					a+="/"
				else:
					a+=morse[e]+"/"
			except:
				a=a

	elif m=="d":
		try:
			words= t.split("//")
			for e in words:
				letters=e.split("/")
				for s in letters:
					for j in morse:
						if morse[j]==s:
							a+=j
				a+=" "
		except:
			a=a


	answer.set(a)	

def morseovkaInverze(t):
	global answer
	a= ""
	
	if m=="e": 
		morseovka(t)
		s=answer.get()
		for e in s:
			try:
				if e=="/":
					a+="/"
				elif e==".":
					a+="-"
				elif e=="-":
					a+="."
			except:
				a=a

		answer.set(a)
	elif m=="d":
		for e in t:
			try:
				if e=="/":
					a+="/"
				elif e==".":
					a+="-"
				elif e=="-":
					a+="."
			except:
				a=a
		morseovka(a)

def morseovkaZmena(t):
	global answer
	a= ""
	
	if m=="e": 
		t=t.lower()
		morseovka(t)
		s=answer.get()
		for e in s:
			r=random.choice(abeceda)
			try:
				if e=="/":
					a+=" "
				elif e==".":
					a+=r.lower()
				elif e=="-":
					a+=r.upper()
			except:
				a=a

		answer.set(a)

	elif m=="d":
		for e in t:
			try:
				if e.islower():
					a+="."
				elif e.isupper():
					a+="-"
				elif e==" ":
					a+="/"
			except:
				a=a
		morseovka(a)

def morseovkaCisla(t):
	global answer
	a= ""
	if m=="e": 
		morseovka(t)
		s=answer.get()
		s=s.split("//")
		for j in s:
			for e in j:
				try:
					if e==".":
						a+=random.choice(licha)
					elif e=="-":
						a+=random.choice(suda)
					elif e=="/":
						a+=" "+random.choice(znaminka)+" "
				except:
					a=a
			a+=" "+random.choice(znaminka)+" "
		a=a[:-5]+"="

		answer.set(a)
	elif m=="d":
		for e in t:
			try:
				if e in suda:
					a+="-"
				elif e in licha:
					a+="."
				elif e in znaminka:
					a+="/"
			except:
				a=a
		morseovka(a)

def sifrovaciKrize(t):
	global answer
	a= ""
	
	if m=="e":
		while len(t)%4!=0:
			t+="-"
		n = 4
		part=[t[i:i+n] for i in range(0, len(t), n)]
		for e in part:
			a+=e[1]
		for e in part:
			a+=e[0]
			a+=e[2]
		for e in part:
			a+=e[3]

	elif m=="d":

		nula=""
		dva=""
		n=int(len(t)/4)
		p=t[n:-n]
		for e in range(len(p)):
			if e%2==0:
				nula+=p[e]
			else:
				dva+=p[e]
		jedna=t[:n]
		tri=t[-n:]
		pos=0
		while pos<n:
			a+=nula[pos]
			a+=jedna[pos]
			a+=dva[pos]
			a+=tri[pos]
			pos+=1

def ciselnyKlic(t, k):
	global answer
	a= ""
	k=str(k)
	x=0
	key = [] 
	for e in k:
		key.append(int(e))
	key = sorted(key)
	if m=="e":
		while x<=len(t):
			for e in key:
				index = k.index(str(e))
				try:
					a+=t[index+x]
				except:
					...
			x+=len(k)

	elif m=="d":
		while x<=len(t):
			for e in k:
				index = key.index(int(e))
				try:
					a+=t[index+x]
				except:
					...
			x+=len(k)



	answer.set(a)

#r,aj it íoaebz řjeipotb-a, mr m dm e l  oi re-
		
	answer.set(a)




#program 
decodeScreen()

win.mainloop()

