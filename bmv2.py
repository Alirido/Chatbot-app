#booyer moore hoospol : bad match table dan good match table
def bad_match_table(pattern):
	table={}
	default = len(pattern)
	i=0
	
	table['*']= default
	for char in pattern:
		if char not in table:
			table[char]=[default-i-1]
		else:
			table[char]=[default-i-1]
		i+=1
	return table
	


def good_match_table(pattern):
	
	last_char = pattern[-1]
	last_index = len(pattern)-1
	
	shifts = {}
	shifts[0] = 1					
	last_shift = 1
	max_suffix_match_length = 0
	
	p = last_index-1
	while (p >= 0) and (pattern[p] != last_char):
		p -= 1

	if p > 0:
		shifts[1] = last_index - p
		i = 1
		max_suffix_match_length = 1
		last_shift = shifts[1]
		while p > 0:
			q = p-1
			matched = 1
			while (q >= 0) and (pattern[last_index-matched] == pattern[q]):
				q -= 1
				matched += 1
			if matched < max_suffix_match_length:
				p -= 1
				while (p >= 0) and (pattern[p] != last_char):
					p -= 1

			else:
				for j in range(i+1,matched+1):
					shifts[j] = last_index - p
				max_suffix_match_length = matched
				i = matched
				last_shift = last_index - p
	else:
		for i in range(1,len(pattern)):
			shifts[i] = len(pattern)
		
	
	while (len(shifts) <= len(pattern)):
		try:
			i += 1
			shifts[i] = last_shift
		except(UnboundLocalError) :
			break
			
	
	return shifts



def BM(T,P):
	n = len(T)
	m = len(P)
	matched = False
	i = m-1

	if (m>n-1):
		return matched
	else:
		suffix_match_shifts = good_match_table(P)
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
					safe_shift_1=currpos+1
				else:
					safe_shift_1=min(table[bad_char])

				
				safe_shift_2 =suffix_match_shifts[num_matched_chars]
				shift+=max(safe_shift_1,safe_shift_2)
	
	return matched






# T = input()
# P = input()
# print ("T  \t:",T)
# print ("Pattern \t:",P)

# found =BM(T,P)
# print(found)






