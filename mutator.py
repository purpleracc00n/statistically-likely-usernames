import argparse

# masks
# {base_word}{special_character}{word}
# {word}{special_character}{base_word}

parser = argparse.ArgumentParser(description='Mutator for statistically likely usernames that uses prefixes and suffixes to create new likely users')
parser.add_argument("-f","--file",type=str,help="Wordlist to mutate")
args = parser.parse_args()


words = ["admin","adm","administrator","srv","serv","svc","service","backup"]
special_characters = ["_",".","-"]

with open(args.file, "r") as base_words:
        for base_word in base_words:
                base_word = base_word.rstrip()
                for word in words:
                        for special_character in special_characters:
                                print(base_word+special_character+word)
                                print(word+special_character+base_word)
