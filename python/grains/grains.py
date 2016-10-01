def on_square(num):
    return 2**(num-1)

def total_after(num):
    return sum(on_square(n) for n in range(1, num+1))
