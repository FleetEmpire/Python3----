#比较大小
def max(a,b):
    if a > b:
        return a
    else:
        return b
#排序
def maopao(number):
    for j in range(0,len(number)-1):
        for i in range(0,len(number)-1):
            if number[i]<number[i+1]:
                number[i],number[i+1] = number[i+1],number[i]
    return number
