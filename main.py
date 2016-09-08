from itertools import chain
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
    'ue': 't',
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
    'l': 'l',
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
    'ian': 'm',
    "*": 'o',
}


class TrieTree(dict):
    def put(self, key):
        current = self
        key = list(key)
        while key:
            letter = key.pop(0)
            current.setdefault(letter, {})
            current = current[letter]
        current.setdefault("_end")

    def search(self, key):
        current = self
        for letter in key:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False


def main():
    trie = TrieTree()
    for k in mapping:
        trie.put(k)
    # with open('resource.txt', 'rb') as f:
    #     for line in f:
    #         txt = line.decode('utf8')
    #         a, b = txt.split()
    #         p, q = 0, 1
    #         parsed = []
    #         while q <= len(a):
    #             if not trie.search(a[p:q]):
    #                 parsed.append(a[p:q-1])
    #                 q -= 1
    #                 p = q
    #             q += 1
    #         parsed += [a[p:q-1]]
    #         print(parsed)
    wf = open('dest.txt', 'w')
    with open('resource2.txt', 'rb') as f:
        x = 0
        for line in f:
            a, b, _ = line.decode("utf8").split()
            splited = b.split('|')
            print(splited)
            collected = []
            for i in splited:
                p = 1
                while p <= len(i) and trie.search(i[:p]):
                    p += 1
                print(i[:p-1], i[p-1:])

                if not i[p-1:]:
                    collected.append(['*'])

                collected.append([i[:p-1]])

                if i[p-1:]:
                    collected.append([i[p-1:]])

            print(a, collected)
            translated = "".join([mapping[i] for i in chain(*collected)])
            print(translated)
            wf.write("{} {}\n".format(translated, a))

    wf.close()
if __name__ == '__main__':
    main()

