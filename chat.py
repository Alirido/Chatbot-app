# =============================================================
#Program BACKEND untuk membaca pertanyaan dari file eksternal.
# =============================================================

from bmV2 import BM
from kmp_algo import KMP_algo
from tesaurus import getSinonim
#from regex import Regex
import re

# global regexType

# =============================================================================
# Fungsi untuk mengatur confidence level pertanyaan dari sinonim maupun bukan.
# =============================================================================
def setConfValueSynonym(tipe, conf_value, question, input_user_byword, idx):
        #tipe = 1: KMP, tipe = 2: BoyerMoore, tipe = 3: Regex
       
        #Cari by_word, yaitu kata perkata dari input_user_byword.
        for byword in input_user_byword:
                conf_value_el_word = 0 ; conf_value_el_synonym = 0
                is_found_word = getAlgo(tipe,question,byword) #Panggil algo yang paling sesuai.
                #Ditemukan, maka conf_value diupdate.
                if (is_found_word != -1):
                        conf_value_el_word =  min(len(byword),len(question))/ max(len(byword),len(question))
                        
                synonym_list = getSinonim(byword)
                for synonym in synonym_list:
                        is_found_word = getAlgo(tipe,question,byword)
                        #Ditemukan
                        if (is_found_word != -1):
                                conf_value_el_synonym = max(min(len(synonym),len(question))/ max(len(synonym),len(question)),conf_value_el_synonym) 

                #Bandingkan confidence value kata asli vs synonym, lalu update confidence value.
                conf_value[idx] = conf_value[idx] + max(conf_value_el_word, conf_value_el_synonym)


# =============================================================================
# Fungsi untuk mendapat tipe algoritma yang diinginkan (KMP, BM, Regex)
# =============================================================================
def getAlgo(tipe, question, byword):
        if (tipe == 1):
                try:
                        return KMP_algo(max(question, byword), min (question,byword))
                except (IndexError):
                        print('???')
                        # break
        elif (tipe == 2):
                return BM(max(question, byword), min (question,byword))

def Regex(Text,Pattern):
        hasil =[]
        idx =0
        regexType = input('Masukkan regex : ')
        for ques in Text:
                match = re.search(regexType,ques)
                # print(match)
                if (match !=None):
                        # print(match.group())
                        hasil.append(ques)
                        print(db_answer[idx])
                idx+=1
        for a in hasil:
                print(a)



# =============================================================================
# PROGRAM UTAMA BERJALAN DARI SINI
# =============================================================================
        
file= open('pertanyaan.txt',"r") #Baca file eksternal pertanyaan.txt
db_question = []

# =============================================================================
#Setiap pertanyaan dimasukkan ke dalam list pertanyaan (db_question : database)
# =============================================================================
for question_line in file:
        question_line = question_line.replace(' ','') #Hapus semua space
        question_line = question_line.replace('?','') #Hapus semua question mark
        question_line = question_line.strip() #Hapus'\n'
        db_question.append(question_line)
file.close()
#print(db_question)


file = open('jawaban.txt', "r")  #Baca file eksternal jawaban.txt
db_answer = []

# =============================================================================
# Setiap jawaban dimasukkan ke dalam list jawaban (db_answer: database)
# =============================================================================
for answer_line in file:
        answer_line = answer_line.strip()
        db_answer.append(answer_line)
file.close()


file = open('stopword.txt', "r")  #Baca file eksternal stopword.txt
ds = []

# =============================================================================
# Setiap stopwords dimasukkan ke dalam list stopwords
# =============================================================================
for ds_line in file:
        ds_line = ds_line.strip()
        ds.append(ds_line)
file.close()

input_user = input('Masukkan pertanyaan yang Anda mau: ') #Dapatkan input user
for word in input_user: #delete stopword
        print(word)
        if word in ds:
                print("a")
                input_user=input_user.replace(word,'')
input_user = input_user.replace('?','') #Menghapus '?'



input_user_byword = input_user.split() #Menghapus space dari pertanyaan yang diinput oleh user, menjadi list of words.
input_user = input_user.replace(' ','')
print(input_user)
tipe_algo = int(input('Ketik 1 untuk KMP, 2 untuk BM, dan 3 untuk Regex: '))
#print(input_user_byword)
if (tipe_algo ==3):
        Regex(db_question,input_user)

# =============================================================================
# Lanjutkan dengan string matching. Cari dengan KMP algorithm:
# =============================================================================
idx = 0
conf_value = {key : 0 for key in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}

for question in db_question:
        is_found = getAlgo(tipe_algo, question, input_user)
        #Jika ditemukan
        if (is_found != -1):
                #Kalau tingkat kecocokan di atas 90%
                try:
                        if ((len(input_user) / len(question) >= 0.9)):
                                print(db_answer[idx])
                                break
                except(ZeroDivisionError):
                        print("I don't understand")
                
                            
        idx += 1

#Jika tidak ditemukan
idx = 0
if (is_found == -1):
        for question in db_question:
                setConfValueSynonym(tipe_algo, conf_value, question, input_user_byword,idx)
                idx += 1
        #Mencari key yang memiliki nilai maksimum dari dictionary
        print(conf_value)
        idx_value_max = max(conf_value, key = lambda x: conf_value.get(x) )
        if (conf_value[idx_value_max] > 0.5):
                idx = max(conf_value, key = lambda x: conf_value.get(x) )
                print(db_answer[idx])
        else:
                print("Rephrase the question!")


