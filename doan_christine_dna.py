# Programmer: Christine Doan
# Prompt: Write a program that accepts input as strings of ACGT triples
# Produce a list of triples and corresponding amino acids, one set per line.


# The main function w/ input
def main():
    aminoAcids = {'TTT': 'Phe', 'TCT': 'Ser', 'TGT': 'Cys', 'TAT': 'Tyr','TTC': 'Phe', 
    'TCC': 'Ser', 'TGC': 'Cys', 'TAC': 'Tyr','TTG': 'Leu', 'TCG': 'Ser','TGG': 'Trp', 'TAG': '***','TTA': 'Leu', 
    'TCA': 'Ser', 'TGA': '***','TAA': '***','CTT': 'Leu', 'CCT': 'Pro', 'CGT': 'Arg', 'CAT': 'His','CTC': 'Leu', 
    'CCC': 'Pro', 'CGC': 'Arg', 'CAC': 'His','CTG': 'Leu', 'CCG': 'Pro', 'CGG': 'Arg', 'CAG': 'Gln','CTA': 'Leu', 
    'CCA': 'Pro', 'CGA': 'Arg', 'CAA': 'Gln','GTT': 'Val', 'GCT': 'Ala', 'GGT': 'Gly', 'GAT': 'Asp','GTC': 'Val','GCC': 'Ala', 'GGC': 'Gly', 
    'GAC': 'Asp','GTG': 'Val', 'GCG': 'Ala','GGG': 'Gly', 'GAG': 'Glu','GTA': 'Val', 'GCA': 'Ala', 'GGA': 'Gly','GAA': 'Glu','ATT': 'Ile', 'ACT': 'Thr', 'AGT': 'Ser', 
    'AAT': 'Asn','ATC': 'Ile', 'ACC': 'Thr', 'AGC': 'Ser', 'AAC': 'Asn','ATG': 'Met', 'ACG': 'Thr', 'AGG': 'Arg', 'AAG': 'Lys',
    'ATA': 'Ile', 'ACA': 'Thr', 'AGA': 'Arg', 'AAA': 'Lys'}
    
    asking = True
    while asking:
        writeNucleo = input('Enter a nucleotide sequence, or just press ENTER to quit: ')
        writeNucleo = writeNucleo.upper()

        if writeNucleo in aminoAcids:
            print(writeNucleo, aminoAcids[writeNucleo])

        elif writeNucleo == '':
            print('Quitting terminal.')
            asking = False
            exit()

        elif len(writeNucleo) % 3 != 0:
            print("You must give full triples.")

        else:
            print(writeNucleo, 'is invalid. Try again.')



main()