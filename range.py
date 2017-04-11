f = open('line-program-textread','r')
s= f.readline()
print "my line is-",s
p= f.readline()
print "my line is-",p
q= f.readline()
print "my line is-",q
m= f.readline()
print "my line is-",m
n= f.readline()
print "my line is-",n

print 'now printing via loop\n'
f = open('line-program-textread','r')
for myvar in f:
        print 'my line is- ', myvar,

print 'now printing via readlines\n'

f = open('line-program-textread','r')
s = f.readlines()
print 'value of f.readlines() is ', s





