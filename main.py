mapping = {
    'q': 'q',
    'w': 'w',
    'iu': 'q',
    'ia': 'w',
    'ua': 'w',
    'e': 'e',
    'r': 'r',
    'uan': 'r',
    'er': 'r',
    't': 't',
    've': 't',
    'y': 'y',
    'uai': 'y',
    'v': 'y',
    'u': 'u',
    'sh': 'u',
    'i': 'i',
    'ch': 'i',
    'o': 'o',
    'uo': 'o',
    'p': 'p',
    'un': 'p',
    'a': 'a',
    's': 's',
    'ong': 's',
    'iong': 's',
    'd': 'd',
    'uang': 'd',
    'iang': 'd',
    'f': 'f',
    'en': 'f',
    'g': 'g',
    'eng': 'g',
    'h': 'h',
    'ang': 'h',
    'j': 'j',
    'an': 'j',
    'k': 'k',
    'ao': 'k',
    'ai': 'l',
    'ing': ';',
    'z': 'z',
    'ei': 'z',
    'x': 'x',
    'ie': 'x',
    'c': 'c',
    'iao': 'c',
    'zh': 'v',
    'ui': 'v',
    # 've': 'v',
    'b': 'b',
    'ou': 'b',
    'n': 'n',
    'in': 'n',
    'm': 'm',
    'ian': 'm'
}


class TrieTree(dict):
    def put(self, key):
        current = self
        for letter in key:
            current.setdefault(letter, {})
            current = current[letter]

    def search(self, key):
        current = self
        for letter in key:
            if letter not in current:
                return False
            current = current[letter]
        if not current:
            return True
        return False


def main():
    trie = TrieTree()
    for k in mapping:
        trie.put(k)

if __name__ == '__main__':
    main()

