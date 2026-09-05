rna = input("Input RNA sequence: ").upper()

# Input validation is delegated to the user by design.


codons = {"AUG": "Met", "GCA": "Ala", "CCA": "Pro", "GGG": "Gly"}

proteins = [codons.get(rna[i:i+3], "FCK") for i in range(0, len(rna), 3)]

print("Peptide sequence: " + '-'.join(proteins))
