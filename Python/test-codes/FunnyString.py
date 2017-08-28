T = input()
str = []
for i in range(T): 
    char = raw_input()
    str.append(char)
# T = 2
# str = ['acxz','bcxz']
for i in range(T):
    S = str[i]
    R = S[::-1]
    flag = 0
    for j in range(1,len(S)):
        temp_S = abs(ord(S[j])-ord(S[j-1]))
        temp_R = abs(ord(R[j])-ord(R[j-1]))
        if temp_S is not temp_R:
            flag = 1
    if flag:
        print 'Not Funny'
    else:
        print 'Funny'
