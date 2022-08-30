#函数的递归
'''
函数递归：一个函数内部调用它自己
递归调用的次数过多，会导致栈溢出
递归特征：
1、必须有一个明确的结束条件；
2、每次进入更深一层递归时，问题规模相比上次递归都应有所减少；
3、相邻两次重复之间有紧密的联系，前一次要为后一次做准备
（通常前一次的输出就作为后一次的输入）。





return的两个作用：
1.用来返回一个值给函数。
2.用来结束函数


'''
'''
def sum(num):
    print(num)
    if num == 1:
        return sum
        
    else:
        sum(num - 1)
        
print(sum(3))
'''


#递归求sum = n+(n-1)+(n-2)+(n-3)...1的和
#方式一：
'''
def sum(n):
    if n > 0:
        return n + sum(n-1)
    else:
        return 0

new_sum = sum(10)
print(new_sum)
'''
#方式2
'''
def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)

new_sum = sum(10)
print(new_sum)
'''

#递归求n!=1×2×3×...×(n-1)n阶乘


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

new_sum = factorial(10)
print(new_sum)













