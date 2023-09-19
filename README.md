Nama : Dien Fitriani Azzahra

NPM : 2206828033

Kelas : PBP-F

# TUGAS 2
##  1. Apa perbedaan antara form POST dan form GET dalam Django?

Pada dasarnya form POST digunakan untuk mengirim data ke server, yang bila proses tersebut berhasil akan mengembalika kode status HTTp 201, sedangkan GET digunakan untuk membaca data dari server web, yang bila proses berhasil akan mengembalikan kode status HTTP 200. Namun, secara spesifik, form POST dan GET dalam Django dapat diklasifikasi dalam beberapa poin
- Tampilan Nilai Variabel di URL:

  POST: Nilai variabel tidak ditampilkan di URL, sehingga lebih aman karena data tidak terlihat secara terbuka di URL.

  GET: Nilai variabel ditampilkan di URL, sehingga pengguna dapat dengan mudah memasukkan nilai variabel baru. Ini kurang aman karena data terlihat dalam URL           dan dapat dengan mudah diakses atau dimodifikasi oleh pengguna lain.
- Panjang String:

  POST: Tidak ada pembatasan panjang string yang ditransmisikan melalui metode POST.

  GET: Panjang string yang dikirim melalui metode GET dibatasi sampai sekitar 2047 karakter karena keterbatasan URL.
- Pengambilan Variabel:

  POST: Variabel diambil menggunakan request.POST.get dalam Django. Ini biasanya digunakan untuk mengambil data yang dikirim melalui formulir.

  GET: Variabel diambil langsung dari URL menggunakan request.GET.get dalam Django. Ini biasanya digunakan untuk mengambil data yang dikirim melalui tautan atau query string.
- Tujuan Penggunaan:

  POST: Form POST biasanya digunakan untuk mengirim data-data penting seperti kata sandi atau data yang ingin disimpan di server.

  GET: Form GET biasanya digunakan untuk mengirim data-data tidak penting atau untuk membaca data dari server. Ini sering digunakan untuk pencarian atau filter.



## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
JSON vs XML
A syntax for storing and exchanging data
using XML
• Fetch an XML document
• Use the XML DOM to loop through the document
• Extract values and store in variables
using JSON
• Fetch a JSON string
• Use JSON.parse() to parse the JSON string
• is an easier to use alternative to XML.
• For AJAX applications, JSON is faster and easier than XML
SLIDE 30


## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
https://appkey.id/pembuatan-website/web-programming/json-adalah/


## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat input form untuk menambahkan objek model pada app sebelumnya.
### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

## 5.  Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

# TUGAS 1                      
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Sesuai dengan checklist pertama saya membuat proyek Django baru bernama CircleD. Namun, sebelum proyek dapat terbentuk, saya perlu melakukan beberapa tahapan awal terlebih dahulu seperti mensetup direktori dan repositori GitHub baru untuk proyek ini. Dari direktori yang sudah saya sesuaikan pada local laptop tersebut, saya melakukan instalasi Django dan inisiasi proyek Django yang akan dibuat, dengan menggunakan virtual environment. Cara membuat(line 1) dan mengaktifkan(line 2) virtual environment:
        
        python -m venv env  
        env\Scripts\activate.bat
        
Agar pengembangan aplikasi Circle D nantinya menjadi lebih mudah, perlu juga untuk disiapkan depedencies agar mudah dalam memanfaatkan library, framework, ataupun package, dengan membuat berkas requirements yang berisi

        
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        
penjelasan : `django` merupakan framework web Django, `gunicorn` server HTTP untuk menjalankan aplikasi Django, `whitenois` adalah middleware pengelola file statis di aplikasi, `psycopg2-binary` adalah adaptor PostgreSQL untuk Django, sedangkan `requests` dan `urllib3` adalah library yang digunakan untuk melakukan HTTP request. 

Setelah dependecies tersebut telah terpasang, saya membuat proyek Django CircleD dengan perintah di CLI
        
    django-admin startproject CircleD .
    
penjelasan: `django-admin` berarti penghubung dengan Django secara global sehingga dapat menjalankan tugas, seperti membuat proyek yang ingin saya lakukan saat itu. `startproject` berarti sub perintah agar django membuat proyek baru dan menyiapkan struktur awal dari proyek tersebut(seperti direktori atau file). `CircleD` adalah nama proyek saya, serta `.` di akhir command berarti proyek dibuat dalam direktori yang saat itu terbuka.

Checklist selanjutnya adalah membuat aplikasi dengan nama main pada proyek tersebut. Agar dapat membuat aplikasi baru saya menjalankan command pada CLI di direktori CircleD dengan perintah 
        
        python manage.py startapp <nama_app> 
Karena nama app yang diminta pada checklist adalah main sehingga saya menjalankan perintah di CLI 
        
        python manage.py startapp main
Setelah saya menjalankan perintah tersebut, secara otomatis direktori saya bertambah dengan nama "main". Agar nantinya peramban web aplikasi saya merouting pada proyek main, saya perlu memodifikasi berkas urls.py dalam direktori proyek CircleD agar sesuai. Poin yang saya modifikasi adalah, pertama menambahkan impor include. Fungsi ini untuk mengimpor rute URL dari aplikasi lain ke dalam berkas tersebut. Dengan begitu saya dapat menambahkan rute URL untuk mengarahkan ke tampilan main dengan menambahkan line:

       urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
        ]

Selanjutnya saya membuat model dengan nama item di aplikasi main yang akan distock pada CircleD. Tiap item yang dijual memiliki beberapa atribut seperti nama, kategori item, harga, jumlah stock, dan deskripsi itemnya. Karena masing masing atribut tersebut memiliki ketentuan tipe masing masingnya, sehingga saya buat untuk tiap atribut sebagai berikut 

        name = models.CharField(max_length=255)
        category = models.CharField(max_length=255)
        price = models.IntegerField()
        amount = models.IntegerField()
        description = models.TextField()

Penjelasan : nama item dan kategori bertipe charfield, kategori dan harga item bertipe integer serta deskripsi bertipe textfield. 

Karena pada tugas 2 ini menggunakan konsep MVT sehingga diterapkan komponen Template. Saya membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas saya. Pada file views.py tersebut saya membuat function berikut:
    
    def show_main(request):
        context = {
            'name': 'Dien',
            'class': 'F',
        }
        return render(request, "main.html", context)

penjelasan : view function show_main ini akan merender halaman "main.html" dengan menggunakan data yang didefinisikan dalam variable context, seperti nama ('Dien') dan kelas ('F'). Hasilnya akan menjadi halaman HTML yang ditampilkan kepada pengguna ketika mereka mengakses URL yang sesuai dengan view function tersebut. 

Selanjutnya saya melakukan sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py, dengan perintah:

        from django.urls import path
        from main.views import show_author

        app_name = 'main'
        
        urlpatterns = [
            path('', show_author, name='show_author'),
        ]
pembuatan berkas urls.py pada direktori aplikasi main untuk menjalankan aplikasi main. Dengan begitu mengonfigurasi satu URL dalam aplikasi "main" yang akan mengarahkan permintaan ke fungsi view show_author ketika URL diakses. Terakhir, agar laman aplikasi yang dikembangkan dapat diakses siapapun, saya melakukan deployment ke Adaptable. Agar dapat melakukan deployment saya perlu membuat akun adaptable yang terhubung dengan repositori CircleD yang tersimpan dalam github. Serta melakukan setup aplikasi agar Adaptable kompetibel digunakan. Proses deployment memakan waktu beberapa menit. Aplikasi CircleD dapat diakses melalui link [https://circled.adaptable.app](https://circled.adaptable.app/main/) .

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Alt text](bagan-tugas-2.png)
    Penjelasan :
    Dimulai dari request client pada halaman web ke server aplikasi berbasis django. Request tersebut akan dikonfigurasi yang telah didefinisikan dalam berkas 'urls.py' dengan tujuan agar terpetakan ke fungsi tampilan yang sesuai dengan request client. Jika URl telah berhasil dikonfigurasi, view function terkait akan dipanggil. Function ini terdapat pada views.py. Komponen View memutuskan tampilan untuk merespon request dari client. Karena komponen ini tidak memiliki kapabilitas untuk berinteraksi dengan database. Berkas models.py yang akan berinteraksi dengan database. Dalam models.py juga terdapat definisi model. Komponen ini berinteraksi dengan basis data, mengambil, menyimpan, atau memanipulasi data yang diperlukan oleh view function. Setelah proses selesai, dan mendapatkan hasil yang sesuai dengan request client, view function akan mereturn respon HTTP yang merupakan data yang akan dikirimkan ke halaman web client. Respon ini akan disesuaikan dengan komponen templates yang telah dibuat pada berkas html di direktori templates, sehingga tampilan akan sesuai dengan permintaan client. 

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan untuk mengisolasi package dan dependencies. Dependencies adalah modul yang digunakan agar software dapat berfungsi. Dengan virtual environment, depedencies dapat terisolasi dari proyek lainnya yang juga sedang dikembangkan sehingga tidak bertabrakan dengan versi lainnya. Namun, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Hanya saja pengembangan aplikasi akan lebih efisien dibanding membuat aplikasi web berbasis Django tanpa virtual environment, karena dapat mendukung dalam pengembangan proyek paralel. Jadi, virtual environment membantu menjaga proyek-proyek Python tetap terorganisir dan memudahkan manajemen pengembangan proyek. 

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC adalah konsep yang digunakan dalam pengembangan web yang terdiri dari beberapa komponen yakni Model, View, dan Controller. Model adalah komponen yang menyimpan data, logika dalam aplikasi, dan berinteraksi dengan database. Model tidak mencakup kemampuan dalam user interface. Sehingga, gap tersebut didukung dengan komponen View. Komponen ini bertanggung jawab dalam menampilkan user interface menggunakan data yang diberikan oleh controller. Komponen controller adalah berada di antara komponen Model dan View, seperti memproses input, ataupun mengubah model atau view sesuai dengan kebutuhan
- MVT adalah konsep yang digunakan dalam pengembangan web yang terdiri dari beberapa komponen yakni Model, View, dan Template. Komponen Model dan View pada MVT memiliki tugas yang sama dengan komponen MV di MVC. Hanya saja komponen View menampilkan dalam tampilan yang telah disediakan oleh komponen Template.Template adalah pengatur tampilan user interface.sehingga, komponen inilah yang mengatur ampilan HTML dan tampilan data dari Model.
- MVVM adalah konsep yang digunakan dalam pengembangan web yang terdiri dari beberapa komponen yakni Model. View, dan ViewModel. Komponen Model dan View pada MVVM memiliki tanggung jawab yang sama dengan komponen di MVC dan MVT, tetapi komponen View di MVVT cenderung lebih pasif karena terdapat komponen ViewModel. ViewModel adalah komponen yang bertanggung jawab dalam mengolah perubahan data antara Model dan View dengan tujuan data yang ditampilkan dapat sesuai dengan format.
- Perbedaan ketiganya terletak pada komponen-komponennya dalam menjalankan tanggung jawabnya. Secara keseluruhan komponen View dan Model memiliki tanggung jawab yang sama di antara ketiganya yakni Model bertugas menyimpan data dan logika aplikasi, View bertanggung jawab dalam menampilkan user interface. Tetapi ketiganya memiliki perbedaan pada salah satu komponennya. Seperti MVC karena memiliki komponen controller, maka komponen ini lebih mendukung dalam pengembangan yang terfokuskan pada pengendalian alur kedua komponen lainnya. MVT karena memiliki komponen Template maka lebih terfokuskan untuk pengembangan yang kode HTMLnya perlu dipisahkan dari logika aplikasi. Sedangkan, MVVM karena memiliki komponen ViewModel. sangat terfokus pada tampilan user interface sehingga konsep ini lebih sesuai digunakan untuk pegembangan yang terfokuskan pada tampilan user interface yang kompleks. 



