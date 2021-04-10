# This is an example of a brute force search. It runs in linear time O(n). 
def find_max(list, max_val):
    max_val = list[0]
    for i in range(len(list)):
        if list[i] > max_val:
            max_val = list[i]
    return max_val

if __name__ =="__main__":
    key = 20
    list = [1,2,3,59,68,90,20,34,43,54]
    max_val = find_max(list, key)

    print(f"the maximum value in {list} was {max_val}")