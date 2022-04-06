"""
n
Di
Fi
"""

def max_production(farmers, diet, food_prod):
    profit = 0
    max_profit = 0
    start = 0
    end = 0
    j = 0
    for i in range(farmers):
        profit += food_prod[i] - diet[i]
        if profit < 0:
            profit = 0
            j = i + 1
        elif max_profit < profit:
            max_profit = profit
            start = j
            end = i
    return max_profit, (start, end)
    
num_farmers = int(input())
farmers_diet = list(map(int,input().split()))
food_produce = list(map(int, input().split()))
print(max_production(num_farmers,farmers_diet, food_produce))

