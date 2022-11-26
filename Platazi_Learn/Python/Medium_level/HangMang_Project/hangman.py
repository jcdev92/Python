import random
import os

def clear():                                       #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")    


def words():
    with open('./WORDS/words.txt', 'r') as f:
        palabras = list(map(lambda w: w.rstrip('\n'), f))
    word = random.choice(palabras)
    pista = ["-"]*len(word)
    guion = ''.join(pista)
    while guion != word:
        print(guion, end=' ')
        while True:
            enter = str(input('\nIngrese una letra: '))
            if len(enter) == 1:
                break
            else: 
                print('\nsolo se puede ingresar una letra por intento, intentelo de nuevo\n')
        for i, l in enumerate(word):
            if l.lower() == enter.lower():
                pista[i] = l
                guion = ''.join(pista)
        clear()
    else:
        print(guion, end=' ')
        print('Felicidades Ganaste!!')

def run():
    words()

if __name__ == '__main__':
    run()