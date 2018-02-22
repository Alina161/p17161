import string
list=[]
answer=input("give a sentence: ")
for i in answer:
    if i in string.ascii_letters:
        if i in string.ascii_uppercase:
            if ord(i)>=ord('N'):
                y= chr(ord(i)-13)
            else:
                y= chr(ord(i)+13)
        else:
            if ord(i) >= ord('n'):
                y= chr(ord(i)-13)
            else:
                y= chr(ord(i)+13)
    else:
        y=i
    list.append(y)
print("".join(list))