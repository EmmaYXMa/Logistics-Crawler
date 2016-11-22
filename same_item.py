d = {}
for line in open('58lease_warehouse_info_after_removal.txt'):
    d[line] = d.get(line,0)+1
fd = open('same_item.txt','w')
for k,v in d.items():
    if v > 1:
        fd.write(k)
fd.close()

