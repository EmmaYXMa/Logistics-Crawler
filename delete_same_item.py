'''rFile = open('58lease_warehouse_info2-70.txt', 'r')
wFile = open('58lease_warehouse_info_after_removal.txt','w')
allLine = rFile.readlines()
rFile.close()
h = {}
for i in allLine:
    if not h.has_key(i):
        h[i] = 1
        wFile.write(i)
wFile.close()


lines, sorted = open('58lease_warehouse_info2-70.txt', 'r').readlines(), lambda a, cmp: a.sort(cmp=cmp) or a
open('b.txt', 'w').write(''.join([i[0] for i in sorted([(j, lines.index(j)) for j in set(lines)], lambda a,b: a[1]-b[1]
    )]))
'''

h,r,w ={}, file('58lease_warehouse_info2-70.txt'), file('c.txt','w')
w.write(reduce(lambda x,y:x+y, [i for i in r if h.get(i)==None and h.setdefault(i, True)]))
