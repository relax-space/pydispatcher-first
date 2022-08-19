from pydispatch import dispatcher

ORDER_CREATE = 'order.created'
ORDER_EDIT = 'order.edit'


def create(sender, **kwargs):
    print(f'保存订单: 将订单保存到数据库. {kwargs}')


def edit(sender, **kwargs):
    print(f'修改订单: 修改数据库中的订单信息. {kwargs}')


def log(sender, **kwargs):
    print(f'打印日志 {kwargs}')


# 为ORDER_CREATE事件 订阅两个接收者:create和log
dispatcher.connect(create, signal=ORDER_CREATE)
dispatcher.connect(log, signal=ORDER_CREATE)
dispatcher.send(ORDER_CREATE, order={'name': '球鞋', 'price': 800})

# 为ORDER_EDIT事件 订阅两个接收者:edit和log
dispatcher.connect(edit, signal=ORDER_EDIT)
dispatcher.connect(log, signal=ORDER_EDIT)
dispatcher.send(ORDER_EDIT, order={'name': '球鞋', 'price': 600, 'desc': '打折'})
