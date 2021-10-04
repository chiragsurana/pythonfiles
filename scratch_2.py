import  string
import  random
s=0
flag=0
choice=['r','p','s']
while True:
    c = input("enter r ,p,s")
    ch = c[0]
    generator = int(random.random() * 3)
    t = choice[generator]
    print(t, ch, generator)
    if ch == 'r' or ch == 'p' or ch == 's':
        if t == ch:
            print("play next")
        elif (ch == 'r' and t == 's') or (ch == 'p' and t == 'r') or (ch == "s" and t == 'p'):
            print("win")
            s = s + 1
        else:
            print("lost")
            k= input("enter your name")
            flag = 1
        if flag == 1:
            print(k,"your score", s)
            print("")
            break



