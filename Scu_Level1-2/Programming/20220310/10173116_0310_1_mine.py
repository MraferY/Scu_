def vip(id,name,tel='沒有號碼'):
    vip_dict={id:{'NAME':name,'TEL':tel}}
    return vip_dict 
def vip2(name,tel='沒有號碼'):
    vip_dict2={'NAME':name,'TEL':tel}
    return vip_dict2

v={}
while True:
    print('建立VIP資訊系統')
    id=input('請輸入ID:')
    name=input('請輸入姓名:')
    tel=input('請輸入電話號碼:')
    member=vip(id,name,tel)
    if v=={}:
        v.update(member)
        print(v)
    else:
        if id in v:
            a=vip2(name,tel)
            v[id]=dict(v[id]).update(a) #還在失敗狀態
            print(v)
        else:
            v.update(member)
            print(v)
    re=input('是否繼續?輸入非y字元結束:')
    if re !="y":
        break
