# words.py
# 

def points_for_letter(letter):
    """Return the points as an integer for a given letter according to Scrabble
    letter frequency tables.
    """  
    
    # Dictionary to look up the point value for each letter. In the dictionary,
    # the key is the letter and the value is the point value
    tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
    
    return tile_score[letter]
    