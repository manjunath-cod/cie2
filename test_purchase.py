from purchases import customer_purchases

def test_customer_zero():
    assert customer_purchases(15000, 50000, 0) == 65000

def test_customer_total():
    assert customer_purchases(15000, 50000, 20000) == 85000
