'''flag = True
while flag:
    li = ["手机","电脑","鼠标垫","游艇"]

    for i in li:
        print('{}\t\t{}'.format(li.index(i)+1,i))

    num_of_choice = input('请输入选择的商品序号/输入Q&q退出：')
    if num_of_choice.isdigit():
        num_of_choice = int(num_of_choice)
        if num_of_choice > 0 and num_of_choice <= len(li):
            print(li[num_of_choice-1])
        else:print('请输入有效数字')
    elif num_of_choice.upper() =='q':break
    else:print('请输入数字！')'''

li = [
    {'name': '苹果', 'price': 10},
    {'name': '香蕉', 'price': 20},
    {'name': '西瓜', 'price': 30},

]
#把货物放在货架上
shopping_car ={}
print('欢迎光临！')
money = input('让我看看你的钱！')
if money.isdigit() and int(money) >0:
    for i,k in enumerate(li):
        print('序号{}，商品{}，价格{}'.format(i,k['name'],k['price']))
    choose = input ('请输入您要购买的序号')
    if choose.isdigit() and int(choose) < len(li):
        num = input('您要购买的商品数量：')
        if num.isdigit():
            if int(money) > li[int(choose)]['price']*int(num):
                money = int(money) - li[int(choose)]['price']*int(num)


    else:
        print('都说了是序号，你傻啊 ！')