#!/usr/bin/python3
from random import choice

# Generate a random peopm based on set of nouns, verbs, adjuctive, prepositions and adverbs

def make_poem():
    nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adj = ["furrv", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "within"]
    adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    # randomly select three nouns
    noun1 = choice(nouns)
    noun2 = choice(nouns)
    noun3 = choice(nouns)

    # make randolmly selected nouns are different
    while (noun1 == noun2):
        noun2 = choice(nouns)
    while (noun3 == noun1) or (noun3 == noun2):
        noun3 = choice(nouns)

    # randomly select three verbs
    verb1 = choice(verbs)
    verb2 = choice(verbs)
    verb3 = choice(verbs)

    while verb1 == verb2:
        verb2 = choice(verbs)
    while verb3 == verb1 or verb3 == verb2:
        verb3 = choice(verbs) 

    # randomly select three adjectives
    adj1 = choice(adj) 
    adj2 = choice(adj)
    adj3 = choice(adj)

    while adj1 == adj2:
        adj2 = choice(adj)
    while adj3 == adj1 or adj3 == adj2:
        adj3 = choice(adj)

    # randomly select two prepositions
    prepos1 = choice(prepositions)
    prepos2 = choice(prepositions)

    while prepos2 == prepos1:
        prepos2 = choice(prepositions)
    
    # randomly select one adverb 
    adv1 = choice(adverbs)

    # Check if the adjctive starts with vowel 
    if adj1[0] in "aeiou":
        article = "An"
    else:
        article = "A"

    poem = (
        # display peom with {A/An} {adj1} {noun1}
        f"{article} {adj1} {noun1}\n"
        # {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
        f"{article} {adj1} {noun1} {verb1} {prepos1} the {adj2} {noun2}\n"
        # {adverb2}, the {noun1} {verb2}
        f"{adv1}, the {noun1} {verb2}\n"
        # the {noun} {verb3} {prep2} a {adj3} {noun3}
        f"the {noun2} {verb3} {prepos2} a {adj3} {noun3}\n"
    )
    return poem

poem = make_poem()
print(poem)
    