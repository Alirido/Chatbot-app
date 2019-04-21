#booyer moore hoospol : bad match table 
def bad_match_table(pattern):
	# create set of last occurence table
	table={}
	default = len(pattern)
	i=0
	
	table['*']= default
	for char in pattern:
		#finding last occurence
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
	matched = -1
	i = m-1

	table = bad_match_table(P) # initialize the last occurence table
	shift = 0
	last_index = m - 1
	#loop while not found,place the pattern
	while shift <= n - m and matched ==-1:
		currpos = last_index
		num_matched_chars = 0
		#comparing pattern with current text positon
		while (currpos >= 0) and (P[currpos] == T[currpos + shift]):
			num_matched_chars+=1
			currpos-=1
		# if pattern ==text then, it's same
		if currpos < 0:
			matched =1
			break
		#if not, shift the pattern position
		else:
			bad_char =T[currpos+shift] # the mismatch char

			if bad_char not in table: # mismatch char not in the table,shift the pattern position = the length of pattern
				safe_shift_1=m
			else:
					safe_shift_1=min(table[bad_char]) # shift the pattern position as many as the last occurence in table
					if safe_shift_1 ==0:
						safe_shift_1=m
					else:
						safe_shift_1=min(table[bad_char])

			shift+=safe_shift_1
	
	return matched


