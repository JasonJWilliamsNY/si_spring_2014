
def melting_temp_small(DNA):
    """This function takes a DNA strand of less than 14
        nucleotides and returns a Tm(oC)"""
    countA = DNA.count('a')
    countT = DNA.count('t')
    countG = DNA.count('g')
    countC = DNA.count('c')
    
    Tm = (countA+countT) * 2 + (countG+countC) * 4
    print "Short strand: Tm is %.2f oC" %Tm


def melting_temp_large(DNA):
    """This function takes a DNA strand of less than 14
        nucleotides and returns a Tm(oC)"""
    countA = DNA.count('a')
    countT = DNA.count('t')
    countG = DNA.count('g')
    countC = DNA.count('c')
    
    Tm = 64.9 + 41*((countG+countC)-16.4) / (countA+countT+countC+countG)
    print "Long strand: Tm is %.2f oC" %Tm 

DNA = raw_input("Please enter a DNA strand\n ")
DNA = DNA.lower()



if len(DNA) < 14:
    melting_temp_small(DNA)
elif len(DNA) >= 14:
    melting_temp_large(DNA)
    


