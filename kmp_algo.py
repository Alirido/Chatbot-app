#Fungsi algoritma KMP, diambil dari slide kuliah.
#Mengembalikan indeks ditemukannya pattern.
def KMP_algo(text, pattern):
    #Cari panjang dari text dan pattern, biasanya panjang pattern < text.
    text_len = text.len()
    pattern_len = pattern.len()
    #Menghitung fungsi pinggiran dari KMP.
    func = computeFunc(pattern)
    i = 0 ; j = 0
    while (i < text_len):
        if (pattern[j] == text[i]):
            #Kalau panjang j sudah mencapai panjang pattern. Berarti sudah ditemukan.
            if (j == pattern_len - 1):
                return i - pattern_len + 1
            i += 1
            j += 1
        elif (j > 0):
            j = func[j-1] #Panggil fungsi pinggiran. Geser sebanyak nilai dari func, cek pattern dari indeks ke j.
        else:
            i += 1
    #Kalau tidak ada yang match, fungsi mengembalikan -1
    return -1


#Fungsi pinggiran dari KMP, pre-processor dari Pattern.
#Mengembalikan array yang berisi nilai indeks jika terjadi mismatch.
def computeFunc(pattern):
    #Array fungsi tersebut, memiliki panjang sebanyak panjang pattern.
    func = []
    func[0] = 0 #sudah pasti 0

    #Hitung func untuk indeks >=1
    pattern_len = pattern.len()
    j = 0 ; func_idx = 1
    while (func_idx < pattern_len):
        #Kasus prefix dan suffix sama.
        if(pattern[j] == pattern[func_idx]):
            func[func_idx] = j+1
            func_idx += 1
            j += 1
        #Kasus prefix dan suffix tidak sama, namun mungkin sama untuk panjang yang lebih kecil.
        elif(j > 0):
            j = func[j-1]
        #Prefix dan suffix pada panjang berapapun tidak ada yang sama.
        else:
            func[func_idx] = 0
            func_idx += 1
    return func

    

