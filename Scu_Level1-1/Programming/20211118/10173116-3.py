x=input('請輸入公司名稱:')
if(x==""):
    print('你沒有輸入公司名稱!')
else:
    print('{:^35}'.format(x))
    print('{0:<12}{1:^12}{2:>12}'.format('年度','營業額','獲利率'))
    print('{0:<12}{1:^20,}{2:>11.2%}'.format(106,1550000,0.0309))
    print('{0:<12}{1:^20,}{2:>11.2%}'.format(107,2000000,0.0523))
    print('{0:<12}{1:^20,}{2:>11.2%}'.format(108,2234000,0.0547))