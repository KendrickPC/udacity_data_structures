# -*- coding: utf-8 -*-
# PEP8 Verified


def hamming_distance(str1, str2):
    if len(str1) == len(str2):
        count = 0
        for char in range(len(str1)):
            if str1[char] != str2[char]:
                count += 1
        return count


# Test Cases
print ("Pass" if (10 == hamming_distance('ACTTGACCGGG',
                                         'GATCCGGTACA')) else "Fail")
print ("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
print ("Pass" if (None == hamming_distance('Slot machines',
                                           'Cash lost in me')) else "Fail")
print ("Pass" if (9 == hamming_distance('A gentleman',
                                        'Elegant men')) else "Fail")
print ("Pass" if (2 == hamming_distance('0101010100011101',
                                        '0101010100010001')) else "Fail")
