#booyer moore hoospol : bad match table 
def bad_match_table(pattern):
	table={}
	default = len(pattern)
	i=0
	
	table['*']= default
	for char in pattern:
		if char not in table:
			table[char]=[default-i-1]
		else:
			if i != default-1:
				table[char]=[default-i-1]
			else:
				table[char]=[default]
		i+=1

	return table
	


def BM(T,P):
	n = len(T)
	m = len(P)
	matched = False
	i = m-1

	if (i>n-1):
		return matched
	else:

		table = bad_match_table(P)
		shift = 0
		last_index = m - 1

		while shift <= n - m and not matched:
			currpos = last_index
			num_matched_chars = 0
			while (currpos >= 0) and (P[currpos] == T[currpos + shift]):
				num_matched_chars+=1
				currpos-=1

			if currpos < 0:
				matched =True
				break
			else:
				bad_char =T[currpos+shift]

				if bad_char not in table:
					safe_shift_1=m
				else:
						safe_shift_1=min(table[bad_char])
						if safe_shift_1 ==0:
							safe_shift_1=m
						else:
							safe_shift_1=min(table[bad_char])

				shift+=safe_shift_1
	
	return matched


