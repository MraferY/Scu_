x0=input('請輸入這個月的利潤:')
x=int(x0)
a=x*0.1
b=(x-100000)*0.075+(100000*0.1)
c=(x-200000)*0.05+(100000*0.1)+(100000*0.075)
d=(x-400000)*0.03+(100000*0.1)+(100000*0.075)+(200000*0.05)
e=(x-600000)*0.015+(100000*0.1)+(100000*0.075)+(200000*0.05)+(200000*0.03)
f=(x-1000000)*0.01+(100000*0.1)+(100000*0.075)+(200000*0.05)+(200000*0.03)+(400000*0.015)
if x<=100000:
    print('您的利潤是%d元，這個月的獎金是%f'%(x,a))
elif(x<=200000):
    print('您的利潤是%d元，這個月的獎金是%f'%(x,b))
elif(x<=400000):
    print('您的利潤是%d元，這個月的獎金是%f'%(x,c))
elif(x<=600000):
    print('您的利潤是%d元，這個月的獎金是%f'%(x,d))
elif(x<=1000000):
    print('您的利潤是%d元，這個月的獎金是%f'%(x,e))
else:
    print('您的利潤是%d元，這個月的獎金是%f'%(x,f))