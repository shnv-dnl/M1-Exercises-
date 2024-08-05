#List all possible RNA sequence patterns coding this amino acid sequence pattern LFPWM. Genetic code shall conform to Universal genetic code. Program has to be suitable for ALL possible amino acid sequences
#To list all possible codons for the amino acid sequence pattern

#------------------
#input: amino acid sequence 
#output: ALL possible rna sequence patterns

#List down a dictionary of all AA and their corresponding tRNA codons

codondict = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'], #ALANINE, ala
    'R': ['CGU','CGC','CGA', 'CGG', 'AGA', 'AGG'], #ARGININE, arg
    'N': ['AAU', 'AAC'], #ASPARAGINE, asn
    'D': ['GAU', 'GAC'], #ASPARTIC ACID, asp
    'C': ['UGU', 'UGC'], #CYSTEINE, cys
    'Q': ['CAA', 'CAG'],#GLUTAMINE, gln
    'E': ['GAA', 'GAG'], #glutamic acid, glu
    'G': ['GGU', 'GGC', 'GGA', 'GGG'], #glycine, gly
    'H': ['CAU', 'CAC'], #histidine, his
    'I': ['AUU', 'AUC', 'AUA'], #isoleucine, ile
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], #leucine, leu
    'K': ['AAA', 'AAG'], #lysine, lys
    'M': ['AUG'], #methionine, met
    'F': ['UUU', 'UUC'], #phenylalanine, p
    'P': ['CCU', 'CCC', 'CCA', 'CCG'], #proline, pro
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], #serine, ser
    'T': ['ACU', 'ACC', 'ACA', 'ACG'], #threonine, thr
    'W': ['UGG'], #tryptophan, trp
    'Y': ['UAU', 'UAC'], #tyrosine, tyr
    'V': ['GUU', 'GUC', 'GUA', 'GUG'], #valine, val
    'STOP': ['UAA', 'UAG', 'UGA']
}

#We need the itertools module 
import itertools


#Define the whole function of reverse translation. 
def revtrans(protseq):
    codoncombos = [] #to store all possible codon sequences during output.
    for aa in protseq:  
        codoncombos.append(codondict[aa]) #iterate thru each aa from protseq and check if its in the dictionary and return a list with all codon options in sublists


# #All possible RNA sequences generated with itertools.product
    all_combinations = itertools.product(*codoncombos) #The asterisk, *, or unpacking operator, unpacks list, and passes the values, or elements, of list as separate arguments to the product function.
    #Essentially, itertools.product(*codon_combinations) is the same as itertools.product(codon_combinations[0], codon_combinations[1], ..., codon_combinations[n]).


# #Join the tuples into strings representing RNA sequences
    # all_rna_sequences = [''.join(codon_sequence) for codon_sequence in all_combinations] #list comprehension
    # return all_rna_sequences

    all_rna_sequences = []
    for codon_sequences in all_combinations:
        all_rna_sequences.append(''.join(codon_sequences)) #remove tuples and join each codon to the other one to create the final rna sequence
    return all_rna_sequences 

# #Input Sequence
protseq = 'LFPWM'
rna_sequences = revtrans(protseq)
for rna_seq in rna_sequences:
    print(rna_seq)

    
    

    








        



    

    









    


