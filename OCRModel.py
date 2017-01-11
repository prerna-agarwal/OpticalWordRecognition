import itertools
import math
count1=0
total=0
count2=0
characters=['d','o','i','r','a','h','t','n','s','e']
with open("C:\Users\Adarsh Agarwal\Downloads\hw2\ocr.dat", "r") as f:
	lines=f.readlines()
with open("C:\Users\Adarsh Agarwal\Downloads\hw2\data.dat", "r") as f,open("C:\Users\Adarsh Agarwal\Downloads\hw2\otruth.dat", "r") as f1:
	words=f.readlines()
	original=f1.readlines()
	for j in range(0,len(words)):
		new_word=''
		word=words[j]
		org=original[j]
		org=org[:-1]
		orig=list(original[j])
		word=word.split()
		for k in range(0,len(word)):
			max=0
			char=''
			for i in range(0,10):
				line=lines[int(word[k])*10+i]
				line=line.split()
				if max<float(line[2]):
					max=float(line[2])
					char=line[1]
			new_word=new_word+char
			total=total+1
			if char==orig[k]:
				count1=count1+1
		if new_word==org:
				count2=count2+1
print "Character Wise: "+`float(count1)/float(total)*100.0`
print "Word Wise: "+`float(count2)/float(len(words))*100.0`
#Exhaustive inference
loglike=0.0
count1=count2=0
for i in range(0,len(words)):
	permute=[]
	z=0.0
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
		z=z+value
		for c in element:
			string=string+c
		if max<value:
			max=value
			new_word=string
		if string==org[:-1]:
			temp=value
	print z
	loglike=loglike+math.log10(float(temp)/float(z))
	for x in range(0,len(new_word)):
		if new_word[x]==org[x]:
			count1=count1+1
	if new_word==org[:-1]:
		count2=count2+1
print "Exhaustive"
print count1,count2
print "Average Log likelihood: "+`float(loglike)/float(len(words))`