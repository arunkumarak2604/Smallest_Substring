str=input()
List=[]
for i in range(len(str)):
    for j in range(len(str),i,-1):
        List.append(str[i:j])
List.sort(reverse=True,key=len)
for i in List:
    if(len(i)==len(set(i))):
        print(len(i))
        break
