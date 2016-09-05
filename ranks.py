import fpdf
class data:
	rank=0
	cgpa=0
	name=''
	#branch=''
	group=''
	roll=''
	def __init__(self,rank,roll='',group='',name='',cgpa=0):
		self.rank=rank
		self.cgpa=cgpa
		self.name=name
		#self.branch=branch
		self.roll=roll
		self.group=group
	def display(self):
		#print(str(self.rank), end="", flush=True)
		print(str(self.rank)+'     '+self.roll+'    '+self.group+'      '+self.name+'     '+str(self.cgpa))
li=[]
f=open('paper.txt')
lines_count=0
it=0
for line in f:
	string=line.split('\n')[0].split('\x0c')[0]
	ifdata=False
	for i in string:
		if i==' ':
			pass
		else:
			ifdata=True
	
	if ifdata==True:
		lines_count=lines_count+1
		rank=int((lines_count-1)/172)*43+(lines_count-1)%43+1-it
		#print(str(lines_count)+'  S->'+string+str(ifdata)+' -->' + str(rank))
		div=(int((lines_count-1)/43))%4
		if div==1:
			if '@' in string:
				#print("Hey")
				
				pass
			else:
				newdata=data(int(rank),string,string.split('2K15/')[-1].split('/')[0])
				li=li+[newdata]
		if div==2:
			if not '@' in string:
				try:
					li[rank-1].name=string
				except:
					pass
					#print("Error-->"+str(rank)+'   '+string+'   '+str(lines_count))
				#li[rank-1].display()
		if div==3:
			if not '@' in string:
				li[rank-1].cgpa=float(string)
				#li[rank-1].display()
			else:
				it=it+1
#gr=input("Enter the group")
def new_page(pdf,gr):
	pdf.add_page()
	pdf.set_font('Arial',size=12)
	pdf.set_fill_color(211,211,211)
	pdf.cell(40,10,'',0,0,'C')
	pdf.cell(130,10,gr,0,1,'C')
	pdf.cell(40,10,'',0,0,'C')
	pdf.cell(20,10,'RANK',1,0,'C',True)
	pdf.cell(40,10,'ROLL',1,0,'C')
	pdf.cell(45,10,'NAME',1,0,'C',True)
	pdf.cell(25,10,'CGPA',1,0,'C')
	pdf.cell(0,10,'',0,1,'C')
	pdf.set_font('Arial',size=8)
	
def cell_print(pdf,count,i):
	pdf.cell(40,7,'',0,0,'C')
	pdf.cell(20,7,str(count),1,0,'C',True)
	pdf.cell(40,7,str(i.roll),1,0,'C')
	pdf.cell(45,7,str(i.name),1,0,'C',True)
	pdf.cell(25,7,str(i.cgpa),1,0,'C')
	pdf.cell(0,7,'',0,1)


'''
pdf=fpdf.FPDF(format='letter')
pdf.set_author('PradyumnSinha')
for j in range (1,11):
	for k in range (ord('A'),ord('B')+1):
		gr=str(chr(k))+str(j)		
		new_page(pdf,gr)
		pdf.set_font('Arial',size=8)
		count=0
		cells=0
		print('\n'+"_______  "+gr+"  _______"+'\n')
		for i in li:
			if i.group ==gr:
				count=count+1
				print(str(count)+' . '+ i.name +'  '+ str(i.cgpa))
				cells=cells+1
				if cells>32:
					cells=1
					new_page(pdf,gr)
				cell_print(pdf,count,i)		
pdf.close()
pdf.output('group_wise_ranks.pdf')
'''

pdf1=fpdf.FPDF(format='letter')
pdf1.set_author('PradyumnSinha')
di={'COMP_DEPARTMENT':range(1,345),'COE':range(1,148),'Information Technology':range(148,247),'Software Engineering':range(247,345),'Electrical Department Ranks':range(538,781),'EE _Ranks':range(538,683),'EEE _Ranks':range(683,781) }
for group in di:
	new_page(pdf1,str(group))
	pdf1.set_font('Arial',size=8)
	count=0
	cells=0
	print('\n'+"_______  "+str(group)+"  _______"+'\n')
	for i in li:
		roll=int(i.roll.split('/')[-1])
		if roll in di[group]:
			count=count+1
			print(str(count)+' . '+ i.name +'  '+ str(i.cgpa))
			cells=cells+1
			if cells>32:
				cells=1
				new_page(pdf1,str(group))
			cell_print(pdf1,count,i)
pdf1.close()
pdf1.output('ranks.pdf')










