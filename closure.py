def multiplier(n):
    def times(a):
        return a * n
    return times

times5 = multiplier(5)
times7 = multiplier(7)
del multiplier
print(times5(10))
print(times7(100))