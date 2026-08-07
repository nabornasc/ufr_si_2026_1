for cont in range(1,106):
    quad=cont**2
    print(f'{cont:>3}² = {quad:>6} ||', end='')
    if cont%7==0:
        print()