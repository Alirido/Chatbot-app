#Program BACKEND untuk membaca pertanyaan dari file eksternal.
import bmV2
from kmp_algo import KMP_algo


#Baca file eksternal pertanyaan.txt
file= open('pertanyaan.txt',"r")
db_question = []

#Setiap pertanyaan dimasukkan ke dalam list pertanyaan (db_question : database)
for question_line in file:
        question_line = question_line.strip() #Menghilangkan '\n'
        db_question.append(question_line)

file.close() #close file 



#Baca file eksternal jawaban.txt
file = open('jawaban.txt', "r")
db_answer = []

#Setiap jawaban dimasukkan ke dalam list jawaban (db_answer: database)
for answer_line in file:
        answer_line = answer_line.strip() #Menghilangkan '\n'
        db_answer.append(answer_line)

file.close()


#Dapatkan input user
input_user = input()

#Lanjutkan dengan string matching. Cari dengan KMP algorithm:
idx = 0
for question in db_question:
        is_found = KMP_algo(question, input_user)
        #Jika ditemukan
        if (is_found != -1):
                #Kalau tingkat kecocokan di atas 90%
                if ((len(input_user) / len(question) >= 0.9)):
                        print(db_answer[idx])
        idx += 1
