lih=['H','e','l','l','o']
liw=['W','o','r','l','d']
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=''
for i in range(len(lih)):
    for a in alp:
        if lih[i].lower()==a:
            s=s+a
s1=''
s2=' '
for i in range(len(liw)):
    for a in alp:
        if liw[i].lower()==a:
            s1=s1+a

print(s.title()+s2+s1.title())
            
