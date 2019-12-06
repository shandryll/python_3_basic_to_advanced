shopping = (
    {'quantity': 2, 'price': 10},
    {'quantity': 3, 'price': 20},
    {'quantity': 5, 'price': 14}
)

total = tuple(map(lambda buy: buy['quantity'] * buy['price'], shopping))

print(f'Total price: {total}')
print(f'Total: {sum(total)}')

def calc_total_price(shopping):
    return shopping['quantity'] * shopping['price']

total_2 = tuple(map(calc_total_price, shopping))

print(f'Total price: {total_2}')
print(f'Total: {sum(total_2)}')
