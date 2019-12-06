from first_class_function import double, square

def process(title, lists, func):
    print(f'Processing... {title}')
    for i in lists:
        print(f'{i} => {func(i)}')


if __name__ == '__main__':
    process(f'Double between 1 and 10: ', range(1, 11), double)
    process(f'Square between 1 and 10: ', range(1, 11), square)
