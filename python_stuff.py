#complimenting a strand of DNA
st = "AAAACCCGGT"
st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(st)

#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
#Given a DNA string tt corresponding to a coding strand, its transcribed RNA string uu is formed by replacing all occurrences of 'T' in tt with 'U' in uu.
#Given: A DNA string tt having length at most 1000 nt.
#Return: The transcribed RNA string of tt.

s = input()
print(s.replace("T", "U"))

#Translating RNA into Protein
# Sample input: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Corresponding output: MAMAPRTEINSTRING

string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]]

print(decoded)

#Hamming distance 
s1 = 'GAGCCTACTAACGGGAT'
s2 = 'CATCGTAATGACGGCCT'
print([ a!=b for (a, b) in zip(s1, s2)].count(True))

#Fibonacci rabbits sequence (immortal)
#n = number of months
#k = number of pairs

n = 28
k = 3

rabbits = [0,1]
for i in range(n-1):
    rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

rabbits[n % 2]
