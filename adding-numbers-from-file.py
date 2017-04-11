print 'now adding via loop\n'
f = open('numbers.txt','r')
s = 0
for line in f:
	s=s+int(line)
print 'sum is ',s
	
