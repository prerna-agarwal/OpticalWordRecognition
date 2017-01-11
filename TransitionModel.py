import itertools
import math
count1=0
count2=0
total=0
index={'letter':{'char':'prob'}};
characters=['d','o','i','r','a','h','t','n','s','e']
with open("C:\Users\Adarsh Agarwal\Downloads\hw2\otrans.dat", "r") as fi:
	for line in fi:
		line=line.split()
		if line[0] in index:
			temp=index[line[0]]
			if line[1] not in temp:
				temp[line[1]]=float(line[2])
				index[line[0]]=temp
		else:
			index[line[0]]={line[1]:float(line[2])}
with open("C:\Users\Adarsh Agarwal\Downloads\hw2\data.dat", "r") as f1,open("C:\Users\Adarsh Agarwal\Downloads\hw2\otruth.dat", "r") as f2,open("C:\Users\Adarsh Agarwal\Downloads\hw2\ocr.dat", "r") as f:
	words=f1.readlines()
	original=f2.readlines()
	lines=f.readlines()
	for k in range(0,len(words)):
		new_word=''
		word=words[k]
		word=word.split()
		orig=original[k]
		org=orig[:-1]
		max=0
		char=''
		for i in range(0,10):
			line=lines[int(word[0])*10+i]
			line=line.split()
			if max<float(line[2]):
				max=float(line[2])
				char=line[1]
		new_word=new_word+char
		total=total+1
		if char==org[0]:
			count1=count1+1
		for i in range(1,len(list(word))):
			values=list()
			line=lines[int(word[i])*10]
			line=line.split()
			values.append(float(line[2]))
			for j in range(1,10):
				line=lines[int(word[i])*10+j]
				line=line.split()
				values.append(float(line[2]))
			temp=index[char]
			for j in range(0,10):
				values[j]=values[j]*temp[characters[j]]
			temp=list(values)
			temp.sort()
			char=characters[values.index(temp[-1])]
			new_word=new_word+char
			total=total+1
			if char==org[i]:
				count1=count1+1
		if new_word==org:
			count2=count2+1
print "Character Wise: "+`float(count1)/float(total)*100.0`
print "Word Wise: "+`float(count2)/float(len(words))*100.0`
#Exhaustive inference
loglike=0
count1=0
count2=0
for i in range(0,len(words)):
	permute=[]
	z=0
	max=0
	new_word=''
	word=words[i].split()
	org=original[i]
	for j in range(0,len(word)):
		permute.append(characters)
	for element in itertools.product(*permute):
		value=1.0
		string=''
		for j in range(0,len(element)):
			#value=value+math.log10(float(lines[int(word[j])*10+characters.index(element[j])].split()[2]))
			value=value*float(lines[int(word[j])*10+characters.index(element[j])].split()[2])
			if j>0:
				temp=index[element[j-1]]
				value=value*temp[element[j]]
		z=z+value
		for c in element:
			string=string+c
		if max<value:
			max=value
			new_word=string
		if string==org[:-1]:
			t=value
	print z
	loglike=loglike+math.log10(float(t)/float(z))
	for x in range(0,len(new_word)):
		if new_word[x]==org[x]:
			count1=count1+1
	if new_word==org[:-1]:
		count2=count2+1
print count1,count2
print "Average Log likelihood: "+`float(loglike)/float(len(words))`