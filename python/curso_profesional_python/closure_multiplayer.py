def make_multiplayer(x):
    def multiplayer(n):
        return x*n
    
    return multiplayer

times10 = make_multiplayer(10)
times40 = make_multiplayer(4)

print(times10(3))
print(times40(5))
print(times10(times40(2)))
