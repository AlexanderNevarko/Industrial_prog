def hash_table(words, hash_func):
    table = {}
    max_hash = 1023
    for word in words:
        hash_ = hash_func(word) % max_hash
        if hash_ in table:
            table[hash_].append(word)
        else:
            table[hash_] = [word]
    return table


def hash_func(word):
    hash_ = 5381
    step = 31
    for char in word:
        hash_ = (hash_ + ord(char)) * step
    return hash_


def table_search(table, size, hash_func, word):
    hash_ = hash_func(word) % size
    if word in table[hash_]:
        return True
    else:
        return False


def prepare_table(filename):
    with open(filename, 'r') as file:
        list_ = file.read().split()
    table = hash_table(list_, hash_func)
    return table


def main():
    table = prepare_table('textfile.txt')
    print(table_search(table, 1023, hash_func, 'I'))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()