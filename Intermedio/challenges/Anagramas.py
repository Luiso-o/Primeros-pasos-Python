print("\n***Es un anagrama?***\n")

"""
Escribe una funcion que reciba dos palabras (String) y retorne verdadero
o falso según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS las letras
de otra palabra inicial.
- No hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("amor", "roma"))
print(is_anagram("cara", "rara"))
print(is_anagram("Cara", "Arca"))
print(is_anagram("camion", "camilo"))
print(is_anagram("cAstOr", "CaSTro"))
print(is_anagram("soya", "soja"))
print(is_anagram("nido", "ODIN"))

print("\n")

#sorted(ordenará las letras de una palabra en orden alfabetico)
#lower(convierte todas las letras de la palabra a minusculas)
