'''
Created on Dec 9, 2013

@author: grmsjac6
'''
im_table_file = open('integer_mass_table.txt')

im_table = {s.split(' ')[0]:int(s.split(' ')[1])  for s in im_table_file }



rev_table = dict()
for v in im_table.values():
    rev_table[v]= {a for a in im_table.keys() if im_table[a] == v}




integer_dict = {im_table[x]:x for x in im_table}
i_set = set(integer_dict.values())



    