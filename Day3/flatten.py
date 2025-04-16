#Flattens the list 
                    # ie input = [1,2,3, [1,2,3,[3,4],2]]
                    # output = [1,2,3,1,2,3,3,4,2]
def flatten(input_list):
    flat_list = []
    for item in input_list:
        if type(item) == list:
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
            
    return flat_list
    
input_list =  [1,2,3, [1,2,3,[3,4],2]]
output_list = flatten(input_list)
print(output_list)