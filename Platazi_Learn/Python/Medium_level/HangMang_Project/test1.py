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
    guion = ''
    for x in word:
        guion += '-' 
        
    while guion != word:
        print(guion, end=' ')
        enter = str(input('\nIngrese una letra: '))
        lista = []
        for r in word:
            lista += r.split()
        for i in lista:
            if i == enter:
                y = lista.find(i)
                w = lista.find(i, y+1)
                l = list(guion)
                l[y] = i
                l[w] = i
                guion = "".join(l)
            clear()      


    else:
        print(guion, end=' ')
        print('Felicidades Ganaste!!')


def run():
    words()

if __name__ == '__main__':
    run()