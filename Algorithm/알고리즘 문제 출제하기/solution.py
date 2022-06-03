import sys
sys.stdin = open('input.txt')


def is_correct_order(order):
    if sum(order) > total_limit:
        return False

    for i in range(len(order)):
        if order[i] > each_limits[i]:
            return False

    return True


def is_in_stock_order(order):
    for i in range(len(order)):
        if order[i] > stocks[i]:
            return False

    return True


def sell_pokemon_bread(order):
    global stocks

    for i in range(len(stocks)):
        stocks[i] -= order[i]


T = int(input())

for tc in range(T):
    answers = []
    total_limit = int(input())
    stocks = list(map(int, input().split()))
    each_limits = list(map(int, input().split()))
    order_count = int(input())
    orders = [list(map(int, input().split())) for _ in range(order_count)]

    for order in orders:
        if not is_correct_order(order):
            answers.append("TOO MUCH ORDER!")

        elif not is_in_stock_order(order):
            answers.append("OUT OF STOCK!")

        else:
            sell_pokemon_bread(order)
            answers.append("THANK YOU!")

    print(f'#{tc+1}', end=' ')
    print(*answers, sep=' ')
