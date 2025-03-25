import argparse

# masks
# {base_word}{special_character}{word}
# {word}{special_character}{base_word}

parser = argparse.ArgumentParser(description='Mutator for statistically likely usernames that uses prefixes and suffixes to create new likely users')
parser.add_argument("-f","--file",type=str,help="Wordlist to mutate")
parser.add_argument("-n","--org-names",type=str,help="Organisation names to mutate into given wordlists")
args = parser.parse_args()


words = ["admin","adm","administrator","srv","serv","svc","service","backup"]
special_characters = ["_",".","-"]

with open(args.file, "r") as base_words:
	# if organisation names were provided, it will mutate using those values instead of the default wordlist
	if args.org_names:
		words = args.org_names.split(",")
	for base_word in base_words:
		base_word = base_word.rstrip()
		for word in words:
			for special_character in special_characters:
				print(base_word+special_character+word)
				print(word+special_character+base_word)
