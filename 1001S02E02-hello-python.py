def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

    print('输入数字开始进行计算')
    a=int(input(''))
    print('请选择：=，-，*，/')
     c=input('')
    print('请继续输入数字')
    b=int(input(''))
    if c=='+':
       print(add(a,b))
    elif c=='-':
       print(subtract(a,b))
    elif c=='*':
       print(multiply(a,b))
    elif c=='/':
       print(divide(a,b))
    else:
       print('输入错误')
       
i=0
j=0
while i<9:
     j+=1
     if condition:i%2 !=0 orj%2 !=0 :
         pass
   else:
     print(f'i*j=i*j',end='\t')
     j=j+1
    print()
    i=i+1
    