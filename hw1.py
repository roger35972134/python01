def get_length(dna):
    
	lengh=len(dna)
	return lengh
def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1)>len(dna2):
        return True
    else:
        return False
def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    gan=dna.count(nucleotide)
    return gan
def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
	
    else:
        return False
def insert_sequence(dna1,dna2,index= 0):
	index= min(index, len(dna1))
	s= dna1[0:index]+dna2+dna1[index:]
	return s
def is_valid_sequence(dna):
    for x in dna:
        if x not in ['A','T','C','G']:
            return False
    return True
def get_complement(search,dna1,dna2,dna3,dna4):
	'''
		key what you want to search in search
		then this functhion will show what you find
	'''
	if search==dna1[0]:
		print(dna1)
	elif search==dna2[0]:
		print(dna2)
	elif search==dna3[0]:
		print(dna3)
	elif search==dna4[0]:
		print(dna4)
	else:
		print('你當我是白癡?')
def get_complementary_sequence(dna):
        return dna[::-1]
