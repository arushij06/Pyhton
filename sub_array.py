# Print all possible sub-arrays of a given array.

def sub_list(ls):
    result = [[]]
    for i in range(len(ls)):
        for j in range(i+1, len(ls)+1):
            result.append(ls[i:j])
    return result

inp_list = list(input().split())
print(sub_list(inp_list))