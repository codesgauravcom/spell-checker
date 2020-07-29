from spellchecker import SpellChecker
spell = SpellChecker()
misspelled = spell.unknown(['i', 'love', 'manchine', 'learneing'])

for word in misspelled:

    print(spell.correction(word))