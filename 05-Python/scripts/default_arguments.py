# A q a 1 z Q
# default arguments = default value for certain parameters
# default is used where certain paramteres is omiited
# make your function more flexible, reduces # of arguments
# 1.positional 2.DEFAULT 3.keyword 4.arbitrary
def net_price(list_price, discount, tax):
    return list_price*(1 - discount)*(1 - tax)
#here cant give any argument currently as default not set
print(net_price(500,0,0.25))
#whatever passed in given more importance
def net_price(list_price, discount=0, tax=0.05):
    return list_price*(1 - discount)*(1 - tax)
print(net_price(500))
print(net_price(500, 0,0.5))