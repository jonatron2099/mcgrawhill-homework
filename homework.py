#plus(postive) margin
def plus_m(one,two):
    if one > two:
        return one-two
    else:
        return two-one

i1 = float(input("Enter Income:"))
s1 = float(input("Enter Saving:"))

#for APC,APS,MPC,and MPS
i2 = float(input("Enter 2nd Income:"))
s2 = float(input("Enter 2nd Saving:"))

c1 = i1-s1
c2 = i2-s2

apc1 = c1/i1
apc2 = c2/i2
aps1 = s1/i1
aps2 = s2/i2

mpc = plus_m(c1,c2)/plus_m(i1,i2)
mps = plus_m(s1,s2)/plus_m(i1,i2)

print("Consumption1:	",c1)
print("Consumption2:	",c2)
print("APC1:		",apc1)
print("APC2:		",apc2)
print("APS1:		",aps1)
print("APS2:		",aps2)
print("MPC:		",mpc)
print("MPS:		",mps)