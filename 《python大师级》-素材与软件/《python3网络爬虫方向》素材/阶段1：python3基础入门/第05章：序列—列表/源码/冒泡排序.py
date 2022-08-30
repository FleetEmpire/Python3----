number = [12,10,24,5,67,78,2,35,13,56,90,134,1,345,66,22,33,33,4,45,67,89,3,100]
for j in range(0,len(number)-1):
         for i in range(0,len(number)-1):
                 if number[i]<number[i+1]:
                         number[i],number[i+1] = number[i+1],number[i]
print (number)

