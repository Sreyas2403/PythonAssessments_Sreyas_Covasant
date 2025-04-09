def convert(x):
    flatten_list = [[[[int(n) for n in s.strip("()").split(",")] for s in sub_list] for sub_list in out_list]for out_list in x]
    return flatten_list            
x = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]   
output = convert(x)
print(output)