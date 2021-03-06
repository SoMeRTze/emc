#!/usr/bin/python
#/usr/sbin/env python
from tkinter import *
from tkinter import filedialog
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
from tkinter.ttk import *

from Crypto.Cipher import AES
from Crypto import Random




def encrypt_files():
	key = s_key.get()
	in_filename = fileLocation.get()
	out_filename = dfileLocation.get()
	
	obj = AES.new(key, AES.MODE_CBC)
	obj2 = AES.new(key, AES.MODE_CBC)
	f = open(in_filename, 'r')
	o = open(out_filename, 'w')
	
	while True:
		msg = f.read(AES.block_size)
		if len(msg) == 0:
			break
		elif len(msg) % 16 != 0:
			msg += ' ' * (16 - len(msg) % 16)
		
		ciphertext = obj.encrypt(msg)
		
		o.write(ciphertext)
		
	original_msg = obj2.decrypt(ciphertext)
	cip = ciphertext
		
	f.close()
	o.close()
		
	return cip
		
		
def decrypt_files():
	key = s_key.get()
	in_filename = fileLocation.get()
	out_filename = dfileLocation.get()
	
	obj = AES.new(key, AES.MODE_CBC)
	obj2 = AES.new(key, AES.MODE_CBC)
	f = open(in_filename, 'r')
	o = open(out_filename, 'w')
	
	while True:
		msg = f.read(AES.block_size)
		if len(msg) == 0:
			break
		elif len(msg) % 16 != 0:
			msg += ' ' * (16 - len(msg) % 16)
		
		original_msg = obj2.decrypt(msg)
		
		
		o.write(original_msg)
		
	
	originl = original_msg
		
	f.close()
	o.close()
		
	return originl


CLS = ""
done = "Successfully completed Encryption/Decryption of your data!"


def clear():
	dstate.set(CLS)
	fileLocation.set(CLS)
	dfileLocation.set(CLS)
	s_key.set(CLS)
	dcrypto.set(CLS)
	
	
def doCrypto():
	choice = ""
	choice = dcrypto.get()
	if choice == 'encrypT':
		encrypt_files()
	elif choice == 'dencrypT':
		decrypt_files()
	else:
		encrypt_files()
	
	dstate.get()
	dstate.set(done)
	return

	
def openFile():
	filename = filedialog.askopenfilename()
	fileLocation.get()
	fileLocation.set(filename)
	return

	
def saveFile():
	dfilename = filedialog.askopenfilename()
	dfileLocation.get()
	dfileLocation.set(dfilename)
	return

	
app = Tk()
app.title("Encrypt")
app.geometry('1000x700+200+200')
app.maxsize(1100,700)

dcrypto = StringVar()
encrypt_it = Radiobutton(app, text='encrypt data', variable=dcrypto, value='encrypT').pack(side="top", pady=5)
decrypt_it = Radiobutton(app, text='decrypt data', variable=dcrypto, value='dencrypT').pack(side="top", pady=5)


B1 = Button(app, text="choose file to encrypt or decrypt", width=40, command=openFile).pack(side="top", padx=15, pady=20)

fileLocation = StringVar()
fileLocation.set("")
f_location = Entry(app, textvariable=fileLocation, width=40).pack(side="top", pady=20)

labelText = StringVar()
labelText.set("Enter a 16 or 32 digits key")
label2 = Label(app, textvariable=labelText).pack(side="top", pady=20)

s_key = StringVar()
f_key = Entry(app, textvariable=s_key, width=32).pack(side="top", pady=20)

B2 = Button(app, text="save data to file", width=20, command=saveFile).pack(side="top", padx=15, pady=20)

dfileLocation = StringVar()
dfileLocation.set("")
df_location = Entry(app, textvariable=dfileLocation, width=40).pack(side="top", pady=20)

B3 = Button(app, text="Encrypt or Decrypt Data", width=20, command=doCrypto).pack(side="top", padx=15, pady=20)

dstate = StringVar()
dstate.set("")
state = Entry(app, textvariable=dstate, width=50).pack(side="top", pady=20)

B4 = Button(app, text="clear", width=10, command=clear).pack(side="top", padx=15, pady=20)

output = StringVar()
output.set("v0.0.8. Python 2.7					@copyrights 2020 Imena Labs Ltd.")
S_out = Entry(app, textvariable=output, width="150").pack(side="bottom", padx=15, pady=15)

app.mainloop()



	
