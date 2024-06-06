a = int(input())
s = 0
temp = a
while temp > 0:
    b = temp&10
    s = s+b
    temp = temp//10
if (a%s==0):
    print("it is a jicky no.")
else:
    print("it is not a jicky no.")