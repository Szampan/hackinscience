import collections
import unicodedata

def remove_accents(text):
    if isinstance(text, bytes):
        text = text.decode('ascii')

    category = unicodedata.category  # this gives a small (~10%) speedup
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if category(c) != 'Mn')

def uni(word):
    return remove_accents(word.lower().replace(" ", "").replace("-", ""))

def is_anagram(left, right):
    left = uni(left)
    right = uni(right)

    if collections.Counter(uni(left)) == collections.Counter(uni(right)):
        return True
    else:
        return False
    
is_anagram("anagrą m ", "Margana")