def greedy_iterative(coin_values, total_amount):
    change = []
    for coin in coin_values:
        while total_amount >= coin:
            total_amount -= coin
            change.append(coin)
    return change



def greedy_recursive(coin_values, total_amount):
    if total_amount == 0:
        return []
    
    suitable_coins = [coin for coin in coin_values if coin <= total_amount]
    if not suitable_coins:
        return []
    
    max_coin = max(suitable_coins)
    remaining_amount = total_amount - max_coin

    return [max_coin] + greedy_recursive(coin_values, remaining_amount)


L = [5, 2, 1, 0.5, 0.2, 0.1, 0.05]
m = 12.35

greedy_iterative_change = greedy_iterative(L, m)
print("Greedy Iterative Change:", greedy_iterative_change)

greedy_recursive_change = greedy_recursive(L, m)
print("Greedy Recursive Change:", greedy_recursive_change)