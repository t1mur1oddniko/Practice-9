old = []
I4 = str()
for I in range (100000,999999):
    N = I
    I1 = str(I)[1:]
    I2 = N+1
    I2_= str(I2)[1:]
    I3 = N + 2
    I3_= str(I3)[1:][:-1]
    I4 = N + 3
    I4_= str(I4)
    if (I1 == I1[::-1]) and (I2_ == I2_[::-1]) and (I3_ == I3_[::-1]) and (I4_ == I4_[::-1]):
        old.append(N)
print (old)
