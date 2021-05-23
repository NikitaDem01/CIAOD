s1 = "abe"
s2 = "acd"
s3 = "aboba"
s4 = "asawadadwadawddawdawdaw"

def firstTask(s1, s2):
    shelp1 = sorted(s1)
    shelp_1 = ''.join(shelp1)
    shelp2 = sorted(s2)
    shelp_2 = ''.join(shelp2)
    x = 0
    for i in range(len(s1)):
        if (shelp_1[i] <= shelp_2[i]):
            x = x + 1
    if x == len(s1):
        return True
    else:
        return False

def secondTask(s):
    if s == "":
        return None
    max = 0
    for i in range(len(s)):
        x = s[i]
        for j in range(i + 1,len(s)):
            x = x + s[j]
            if x == x[::-1]:
                if len(x) > max:
                    max = len(x)
                    returnx = x
    if max == 0:
        return None
    return returnx

def thirdTask(s):
    l = len(s)/2
    counter = 0
    part_list = []
    for i in range(1,int(l)+1):
        st = s
        while len(st) > 1:
            if st[:i] == st[i:2*i]:
                if st[:i] in part_list:
                    pass
                else:
                    part_list.append(st[:i])
                    counter += 1
            st = st[1:]
    return counter
  
print(firstTask(s1, s2))
print(secondTask(s3))
print(thirdTask(s4))
