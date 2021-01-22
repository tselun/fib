# merge and sort lists

def merge(o,a,d):
    s1 = set(o+a) # sets are unique
    s2 = s1.difference(set(d))
    n = list(s2)
    n.sort(reverse=True)
    n.sort(key=len, reverse=True)
    return n

if __name__ == "__main__":
    print("Enter list of elements seperated by SPACE ")
    o = input("Original list: ").split()
    a = input("To be added: ").split()
    d = input("To be removed: ").split()
    print(merge(o,a,d))