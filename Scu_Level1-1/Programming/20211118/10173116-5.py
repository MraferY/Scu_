i=int(input('請輸入您的所得:'))
x1=1500*0.03
x2=3000*0.1+x1
x3=4500*0.2+x2
x4=26000*0.25+x3
x5=20000*0.3+x4
x6=25000*0.35+x5
if(i<=1500):
    x=i*0.03
elif(i<=4500):
    x=(i-1500)*0.1+x1
elif(i<=9000):
    x=(i-4500)*0.2+x2
elif(i<=35000):
    x=(i-9000)*0.25+x3
elif(i<=55000):
    x=(i-35000)*0.3+x4
elif(i<=80000):
    x=(i-55000)*0.35+x5
else:
    x=(i-80000)*0.45+x6
print('您的所得是{:,}元，應納稅額是{:,}元'.format(i,x))