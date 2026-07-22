GUI_Labels_Buttons_Combobox

# GUI, labels, buttons, combobox

```python
fromtkinterimport*
fromtkinterimportttk


Class chooseBuild:

	def __init__(self,master):
		frame=Frame(master,width=300,height=250)
		frame.pack()
		
		label_1=Label(frame,text='Firstlabel:')
		label_2=Label(frame,text='Secondlabel:')
		label_3=Label(frame,text='Thirdlabel:')
		button_1=Button(frame,text='Hey!',command=self.but1)
		button_2=Button(frame,text='Hoy!',command=self.but2)
		button_3=Button(frame,text='!STOP!',command=frame.quit)
		self.combo1=ttk.Combobox(frame,textvariable=varCombo)
		self.combo1.bind('<Return>',self.combo1_onEnter)
		self.combo1.bind('<<ComboboxSelected>>',self.combo1_onEnter)
		self.combo1['values']=('Abcd','Bcde','Cdef','Defg','Demo','Efgh','Fghi')
		self.combo1.current(2)
		
		
		#<Button-1>(minus1)=Leftbutton,<Button-2>=Scrollwheel,<Button-3>=RightClick
		#button_1.bind('<Button-1>',self.but1)
		#button_2.bind('<Button-1>',self.but2)
	
		#stickyN=North,E=East,S=South,W=West
		label_1.grid(row=0,sticky=W)
		label_2.grid(row=1,sticky=W)
		label_3.grid(row=0,column=1,sticky=W)
		button_1.grid(row=2,columnspan=2)
		button_2.grid(row=3,columnspan=2)
		button_3.grid(row=4,columnspan=3)
		self.combo1.grid(row=5,sticky=W)
	
	def combo1_onEnter(self,event):
		tempVar=varCombo.get()
		print('tempVar:',tempVar)
	
	
	def but1(self):
		self.getTreeList('Heyyourself')
		getTreeList2('Heyyourself')
	
	
	
	def but2(self):
		self.getTreeList('Hoyyourself')
		getTreeList2('Hoyyourself')

	def getTreeList(self,param):
		print(param)


def getTreeList2(param):
	print(param,param,param)


main =Tk()
main.title('Sample test window')
main.geometry('640x480')
varCombo=StringVar(main,value='Demo')
mainWindow=chooseBuild(main)
main.mainloop()
```

