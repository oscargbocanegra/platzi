# hola 3 -> holaholahola

def make_repeater_of(n):
    def repeter(string):
        assert type(string) == str, "Solo puedes usar cadenas"
        return string * n
    return repeter

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_5("platzi"))

if __name__ == '__main__':
    run()