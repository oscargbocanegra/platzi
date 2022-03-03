def make_division_by(n: int) -> int:
    """
    This closure returns a function that returns the division of an x number by n
    """
    def repeter(m: int):
        return int(m/n)
    return repeter

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # Return 6
    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # Return 20
    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # Return 3

if __name__ == '__main__':
    run()