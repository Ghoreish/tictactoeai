import random
def win(l):
    win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in win_list:
        m=0
        for j in i:
            if j not in l:
                m=1
        if m==0:
            return True
    return False
def willwin(a,l):
    for i in l:
        if win(a+[i]):
            return i
    return False
def show(x,o):
    print("=========")
    for i in range(1,10):
        if i in x:
            print("X ",end="")
        elif i in o:
            print("o ",end="")
        else:
            print(str(i)+" ",end="")
        if i%3==0:
            print()
    print("=========")
def getmax(x):
    dic={}
    for i in range(1,10):
        dic[i]=0
    for i in x:
        dic[i]+=1
    max=0
    nnn=0
    for i in dic:
        if dic[i]>max:
            max=dic[i]
            nnn=i
    return nnn
def getmin(x):
    dic = {}
    for i in range(1, 10):
        dic[i] = 0
    for i in x:
        dic[i] += 1
    min = 100000000000
    nnn = 0
    for i in dic:
        if dic[i] < min:
            min = dic[i]
            nnn = i
    return nnn
def check(a,b,k):
    yyy=0
    lll=[]
    lll2=[]
    p=0
    x=eval(str(a))
    o=eval(str(b))
    l=eval(str(k))
    while True:
        yyy+=1
        if l==[]:
            yyy =1
            p=0
            x = eval(str(a))
            o = eval(str(b))
            l = eval(str(k))
        c=l[random.randint(0,len(l)-1)]
        x.append(c)
        l.remove(c)
        if p==0:
            p=c
        if win(x)==True and win(o)==False:
            lll.append(int(p))
            l=[]
            if len(lll)>=1000:
                nnn=getmax(lll)
                return nnn
            continue
        if l==[]:
            continue
        c = l[random.randint(0, len(l)-1)]
        o.append(c)
        l.remove(c)
        if win(o)==True:
            lll2.append(int(p))
            l=[]
l=[1,2,3,4,5,6,7,8,9]
x=[]
o=[]
while True:
    ml=input("You first or PC? (1/2)(you are o):")
    if ml=="1":
        while True:
            show(x, o)
            cc = int(input("Enter a number: "))
            l.remove(cc)
            o.append(eval(str(cc)))
            if len(l)<3:
                if win(x) == True:
                    print("X win")
                    show(x, o)
                    break
                elif win(o) == True:
                    print("o win")
                    show(x, o)
                    break
                else:
                    print("DRAW!")
                    show(x, o)
                    break
            c = check(x, o, l)
            if win(o) == True:
                print("o win")
                show(x, o)
                break
            if willwin(x, l) != False:
                c = willwin(x, l)
            elif willwin(o, l) != False:
                c = willwin(o, l)
            x.append(eval(str(c)))
            l.remove(c)
            if win(x) == True:
                print("X win")
                show(x, o)
                break
    elif ml=="2":
        while True:
            if len(l)<3:
                if win(x) == True:
                    print("X win")
                    show(x, o)
                    break
                elif win(o) == True:
                    print("o win")
                    show(x, o)
                    break
                else:
                    print("DRAW!")
                    show(x, o)
                    break
            if win(o) == True:
                print("o win")
                show(x, o)
                break
            c=check(x,o,l)
            if willwin(x, l) != False:
                c=willwin(x,l)
            elif willwin(o,l)!=False:
                c=willwin(o,l)
            x.append(eval(str(c)))
            l.remove(c)
            if win(x)==True:
                print("X win")
                show(x, o)
                break
            show(x, o)
            cc = int(input("Enter a number: "))
            l.remove(cc)
            o.append(eval(str(cc)))
    else:
        print("ERROR!")
        continue