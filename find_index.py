# This is an example of a brute force search. It runs in linear time O(n). 
def find_index(list, key):
    for i in range(len(list)):
        print(i)
        if list[i] == key:
            return i
    return -1 

if __name__ =="__main__":
    key = 20
    list = [1,2,3,59,68,90,20,34,43,54]
    index = find_index(list, key)

    print(f"the key {key} was located at {index}")