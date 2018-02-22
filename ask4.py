roman={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IV",5:"V",4:"IV",1:"I"}
convert = []
reply = int(input("enter a number to convert: "))
for item in roman:
    phliko,upoloipo=divmod(reply,item)
    convert.append(phliko*roman[item])
    reply = upoloipo
print("".join(convert))