#Program BACKEND untuk membaca pertanyaan dari file eksternal.
import bmV2

#Mendapat input pertanyaan dari pengguna
input_user = input()

#Baca file eksternal
file = open('pertanyaan.txt',"r")

#Membaca setiap pertanyaan di dalam pertanyaan.txt
#db = database
db_question = []
idx_question = 0
for question_line in file:
        question_line = question_line.strip() #Menghilangkan '\n'
        db_question.append(question_line)
        idx_question += 1

#Setiap pertanyaan dimasukkan ke dalam list pertanyaan (db_question)
#Lanjutkan dengan string matching.

#Cari dengan KMP algorithm:





'''
for c in q:
    found =bmV2.BM(c,input_user)
    if found:
        print(q[input_user])
        break
'''
#print ("Pattern \t:",input_user)



