# when digesting a whole genome sequence of a lambda phage completely with ecoRI, how long can each fragment be obtained. also look at hindiii, bamhi, noti. 

#input:lambda phage genomic sequence 
#output: length of digested fragments when digested by 4 enzymes respectively (ecoRI, hindIII, bamhI, notI)

#RE sites for own reference
# enzymedict =  'ecoRI': 'GAATTC', 
#               'HindIII': 'AAGCTT', 
#               'BamHI': 'GGATCC', 
#               'NotI': 'GCGGCCGC',

import re

#Import file as a string
f = open('lambdaphageseq.fasta', 'r')
dna_seq = f.read().replace("\n", "")

restrictionsite = 'GAATTC'

#Check if restriction site is present in DNA sequence
if restrictionsite not in dna_seq:
    print('The restriction site ' + restrictionsite + ' is not present in the current DNA sequence. Please input another sequence.')
else:
#Scan entire string for instances of restriction site and splice them out
    fragwithoutsites = re.split(restrictionsite, dna_seq)    #['AATTC', 'GCGT', 'TAAGCT', 'ACGTAAGCGT'] - output of fragwithoutsites if GAATTC

# for each fragment except for the first one, they should start with AATTC. for each fragment except the last, they should end with G.

#Manually add the restriction sites back in to each fragment 
    finaloutput = []
    for index in range(len(fragwithoutsites)):                                      #by using range function for len of list, it will return 0, 1, 2, 3 as the indices
        if restrictionsite != 'GCGGCCGC':
            if index == 0:                                                          #condition for first index                                                        
                finaloutput.append(fragwithoutsites[index] + restrictionsite[0]) 
            elif index == len(fragwithoutsites) - 1:                                #condition for last index
                finaloutput.append(restrictionsite[1:] + fragwithoutsites[index]) 
            else:                                                                   #condition for middle indices (not first nor last)           
                finaloutput.append(restrictionsite[1:] + fragwithoutsites[index] + restrictionsite[0])
        elif restrictionsite == 'GCGGCCGC':
            if not restrictionsite:
                break
            if index == 0:                                                          #condition for first index                                                        
                finaloutput.append(fragwithoutsites[index] + restrictionsite[0:2]) 
            elif index == len(fragwithoutsites) - 1:                                #condition for last index
                finaloutput.append(restrictionsite[2:] + fragwithoutsites[index]) 
            else:                                                                   #condition for middle indices (not first nor last)           
                finaloutput.append(restrictionsite[2:] + fragwithoutsites[index] + restrictionsite[0:2])

#Count the length of each returned fragment
    print('The digested fragments are:' + str(finaloutput))
    for fragment in finaloutput:
        print(len(fragment))

#Test sequence
# dna_seq = 'AATTCGAATTCGCGTGAATTCTAAGCTGAATTCACGTAAGCGT'  #test random dna sequence for GAATTC
#dna_seq = 'AATTCGAATTCGCGGCGGCCGCTGAATTCTAAGCTGAATTCGCGGCCGCACGTAAGCGT' #dna seq w NotI restriction sites
# # expected output = AATTCG AATTCGCGTG AATTCTAAGCTG AATTCACGTAAGCGT
    




































