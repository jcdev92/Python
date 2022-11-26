def make_repeater_of(n: int):
    def repeater(string: str) -> str:
        assert type(string) == str, 'only strings are valid, do not accept numbers'
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(int(input('introduzca el numero de veces a repetir: ')))
    print(repeat_5(input('ingrese una palabra o letra: ')))

if __name__ == '__main__':
    run()
