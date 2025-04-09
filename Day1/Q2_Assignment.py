d1 = {"ok" : 1, "nok" : 2 }
d2 = {"ok" : 2, "new" : 3}
union_dict = d1 | d2 # we can also use "or" #union
print(union_dict)
for i in dict.keys(d1): #intersection
    for j in dict.keys(d2):
        if i ==j:
            common = {i : d1[i]}
            print(common)
for key in dict.keys(d1 | d2):  #merge
    merge = {key: d1.get(key,0) + d2.get(key,0)}
    print(merge)
for k in d1.keys():
    if k == d1.keys() and k!= d2.keys():
        minus = {k: d1.get(k,0) }
        print(minus)    