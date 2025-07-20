def simple_interest(ori, per, times):
    return ori * per * times

def simple_interest_amount(ori, per, times):
    return ori + simple_interest(ori, per, times)

print(simple_interest_amount(10000000, 0.03875, 5))
print(simple_interest_amount(1100000, 0.05, 5/12))