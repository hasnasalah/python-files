def make_multiplier(factor):
    def times(x):
        return x*factor
    
    return times


times3 = make_multiplier(3)
times7 = make_multiplier(7)


print(times3(5))
print(times7(5))
