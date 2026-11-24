from purchases import customer_purchases

def customer_zero(15000,50000,0):
    assert customer_purchases(15000, 50000, 0) == 65000

def customer_total(15000,50000,20000):
    assert customer_purchases(1500, 50000, 20000) == 71500