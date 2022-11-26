### same remover ###

def remove_same(same):
    remover = list(set(same))
    print(remover)

def run():
    remove_same([0, 1, 4, 5, 4, 1, True, False])

if __name__ == "__main__":
    run()