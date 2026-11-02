# 今天第六天，先来复习下昨天学的
products = [
    {"name": "键盘", "price": 199},
    {"name": "鼠标", "price": 89},
    {"name": "显示器", "price": 999}
]
# 请定义一个函数 def get_expensive(item_list):：
# 要求： 结合 return 和 列表推导式，用一行代码返回 item_list 里所有价格（price）大于 100 的商品名字（name）列表。
# 思考附加问（一句话回答）： 如果我不用列表推导式，而是用 for 循环去查某个特定商品的价格，
# 兜底的 return "没找到" 应该跟 if 对齐，还是跟 for 对齐？为什么？
def get_expensive(item_list):
    return [m['name'] for m in item_list if m['price'] > 100]
#跟for对齐

