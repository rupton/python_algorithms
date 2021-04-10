# This is an example of a brute force search. It runs in linear time O(n). 
def find_min(list, min_val):
    min_val = list[0]
    for i in range(len(list)):
        if list[i] < min_val:
            min_val = list[i]
    return min_val

if __name__ =="__main__":
    key = 20
    list = [10,2,3,59,68,90,20,34,43,54]
    min_val = find_min(list, key)

    print(f"the maximum value in {list} was {min_val}")