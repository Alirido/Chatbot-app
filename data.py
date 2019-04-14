import sqlite3

from questions import Questions
#import bmv2

#con = sqlite3.connect('question.db') # create file name question.db if not exist
con = sqlite3.connect(':memory:') #useful for testing
c = con.cursor()


c.execute("""CREATE TABLE questions (
    question text,
    answer text
)""")

def insert_q(qa):
    with con:
        c.execute("INSERT INTO questions VALUES (?,?)",(qa.q,qa.a))

def get_ans(q):
    c.execute("SELECT answer FROM questions WHERE question=:question",{'question':q})
    return c.fetchall()

def update_ans(ques,ans):
    with con:
        c.execute("""UPDATE questions SET answer =:answer
        WHERE question =:question""",{'question':ques.q,'answer':ans})

def remove_ques(qa):
    with con:
        c.execute("DELETE from questions WHERE question =:question AND answer = :answer",{'question':qa.q,'answer':qa.a})

# Create the questions (<question,answer>)       
q1 = Questions('Apa kabar','Baik.. Anda?')
q2 = Questions('Siapa nama anda','Nama saya xxx..Salam kenal')
q3 = Questions('Bagaimana saya bisa menjadi mahasiswa di ITB','Mulai tahun 2011, ITB menggunakan SNMPTN dan SBMPTN untuk melaksanakan seleksi mahasiswa baru program sarjana di semua Fakultas dan Sekolah di ITB. Selain dari pelaksanaan SNMPTN dan SBMPTN tersebut, ITB tidak menerima mahasiswa baru program sarjana melalui jalur seleksi lain. Sebagai informasi, silakan mengunjungi laman resmi SNMPTN 2016 (http://snmptn.ac.id/) atau laman resmi SBMPTN 2016 (http://sbmptn.ac.id/) untuk memperoleh gambaran mengenai pelaksanaan pendaftaran dan seleksi mahasiswa baru di Perguruan Tinggi Negeri di Indonesia, termasuk ITB.')
q4 = Questions('Apa Itu SBMPTN ?','SBMPTN merupakan singkatan dari Seleksi Bersama Masuk Perguruan Tinggi Negeri, merupakan suatu sistem seleksi mahasiswa baru program sarjana untuk seluruh Perguruan Tinggi Negeri di Indonesia termasuk ITB, yang dilaksanakan secara bersama dengan menggunakan pola seleksi berdasarkan hasil ujian tertulis. Sebagai informasi pelaksanaan SBMPTN 2016, silakan mengunjungi laman resmi SBMPTN 2016 (http://sbmptn.ac.id/).')
q5 = Questions('Bagaimana pola seleksi penerimaan mahasiswa baru melalui SBMPTN ?','SBMPTN merupakan sistem ujian saringan masuk perguruan tinggi negeri yang dilaksanakan secara nasional, oleh sebuah panitia terpusat yang ditunjuk oleh Majelis Rektor Perguruan Tinggi Negeri Indonesia (MRPTNI). Ujian tertulis SBMPTN dilaksanakan secara serentak dan terpadu pada jam dan hari yang sama, dengan soal yang sama di berbagai wilayah di Indonesia, sehingga peserta diharapkan dapat memilih lokasi yang terdekat dengan penyelenggaraan kegiatan seleksi tersebut. Tempat ujian tidak menjadi bahan pertimbangan dalam proses seleksi dan penentuan kelulusan seorang calon mahasiswa di perguruan tinggi negeri yang dipilihnya. Sebagai informasi pelaksanaan SBMPTN 2016, silakan mengunjungi laman resmi SBMPTN 2016 (http://sbmptn.ac.id/).')
q6 = Questions('Siapa saja yang boleh menjadi peserta SBMPTN ?','Peserta SBMPTN harus lulus dari Satuan Pendidikan dan Ujian Nasional SMA/MA/SMK/MAK atau yang setara dengan 3 tahun terakhir dan telah memiliki ijazah SMA/MA/SMK/MAK atau yang setara. Untuk lulusan tahun berjalan sekurang-kurangnya telah memiliki Surat Keterangan Hasil Ujian Nasional (SKHUN) dari Kepala Sekolah yang dilengkapi dengan pasfoto terbaru yang bersangkutan dan dibubuhi cap sekolah. Peserta yang bersangkutan juga harus memenuhi persyaratan yang berlaku di program studi tujuannya. Sebagai informasi pelaksanaan SBMPTN 2016, silakan mengunjungi laman resmi SBMPTN 2016 (http://sbmptn.ac.id/).')
q7 = Questions('Saya tidak memiliki nilai UN SLTA dan merupakan peserta Paket C. Namun demikian, pada saat pelaksanaan SBMPTN, nilai ujian Paket C yang saya ikuti belum terbit. Bisakah saya menjadi peserta SBMPTN ?','Peserta SBMPTN harus lulus dari Satuan Pendidikan dan Ujian Nasional SMA/MA/SMK/MAK atau yang setara dengan 3 tahun terakhir dan telah memiliki ijazah SMA/MA/SMK/MAK atau yang setara. Khusus bagi peserta Paket C, hanya dapat mengikuti SBMPTN bila telah memiliki Ijazah Paket C. Bila nilai Paket C belum terbit pada saat pelaksanaan SBMPTN tahun berjalan, silakan mengikuti SBMPTN pada tahun yang akan datang. Sebagai informasi pelaksanaan SBMPTN 2016, silakan mengunjungi laman resmi SBMPTN 2016 (http://sbmptn.ac.id/).')
q8 = Questions('Saya berasal dari luar Jawa dan berminat memilih ITB pada pelaksanaan SBMPTN. Apakah saya harus mendaftarkan diri dan mengikuti ujian di Bandung ?','Sesuai dengan informasi di laman resmi SBMPTN (http://sbmptn.ac.id), tempat pelaksanaan ujian tidak menjadi pertimbangan pada kelulusan SBMPTN. Dengan demikian saudara dapat mendaftar dan mengikuti SBMPTN di lokasi terdekat dengan tempat domisili anda.')
q9 = Questions('Materi apa saya yang diujikan pada pelaksanaan SBMPTN ?','SBMPTN terdiri atas kelompok ujian SAINTEK, kelompok ujian SOSHUM, dan kelompok ujian CAMPURAN (mengikuti ujian ujian SAINTEK dan SOSHUM). Informasi mengenai materi yang diujikan di masing-masing kelompok ujian dapat diperoleh di laman http://sbmptn.ac.id/.')
q10 =Questions(' Bisakah saya mengikuti ujian lintas bidang pada pelaksanaan SBMPTN ?','Peserta SBMPTN akan mengikuti kelompok ujian berdasar fakultas/sekolah/program studi yang dipilihnya, tanpa memperhatikan bidang studi asal SMA. Sebagai contoh, siswa yang berasal dari SMA IPA dapat memilih SBM ITB (kelompok ujian SOSHUM) serta harus mengikuti ujian dengan materi kelompok SOSHUM. Demikian pula sebaliknya, siswa SMA yang berasal dari IPS dapat memilih FTMD ITB (kelompok ujian SAINTEK) serta harus mengikuti ujian dengan materi kelompok SAINTEK. Informasi selengkapnya dapat diperoleh di laman http://sbmptn.ac.id/.')
q11=Questions('Apakah ITB membuka Program Peminatan pada pelaksanaan SBMPTN ?','Tidak, Program Peminatan ITB hanya ditawarkan pada pelaksanaan SNMPTN saja dan tidak dibuka pada pelaksanaan SBMPTN.')




#insert the questions
insert_q(q1)
insert_q(q2)
insert_q(q3)
insert_q(q4)
insert_q(q5)
insert_q(q6)
insert_q(q7)
insert_q(q8)
insert_q(q9)
insert_q(q10)
insert_q(q11)


v = 'Bagaimana saya bisa menjadi mahasiswa di ITB'
jb=get_ans(v)
print(jb)


#c.execute("SELECT answer FROM questions WHERE question=?",(q,))
# print(c.fetchone()) # get next row , and return that row, if none return none
# c.fetchmany(x) # x = number of row, return x as list, if no return empty list
# c.fetchall() # get the remaining row that are left and return as list
con.commit()

con.close()