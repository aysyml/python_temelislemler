#a,b,ad,soyad değişkenlerimiz (Bir nesneye verilen isme değişken denir)
#20,3,ayl,yml ise değişkenlere atadığımız değerler

a = 20
b = 3
ad="ayl"
soyad="yml"

#Birden fazla değişkeni aynı anda tanımlayabiliriz.Örn:
x,y,z=2.1,3,7

print("Değişkenimiz :" ,a)
print("Değişkenimiz :" ,b)
#Bir değişkeni bir kez tanımlayıp birden fazla yerde tanımlayabiliriz.

print("Üs alma        : a**2  :", (a**2))
print("Toplama işlemi : a + b :", (a+b))
print("Çıkarma işlemi : a - b :", (a-b))
print("Bölme işlemi   : a/b   :", (a/b))
print("Çarpma işlemi  : a*b   :", (a*b))
print("Tam sayı bölme işlemi: a//b :",(a//b)) # tam kısmını verir.
print("Mod alma işlemi:       a%b  :",(a%b))
print("x değeri :", x)
print("y değeri :", y)
print("z değeri :", z)
print("ad:",ad)
print("soyad:",soyad)

#Notlar...
 #print() i konsolda yaptoğımız işlemin sonucunu görmek için yazdık.
 #Yazmasakta run işlemini gerçekleştirdiğimizde çalışır ama biz görmeyiz.
 #Bu işaretler(#,""" """) yorum  yapmak için kullanılır hiç bir şekilde derlenmez yani program bunu dikkate almaz.
 #Yazdığımız kodlar için küçük,anlaşılır notlar yazmak herzaman iyidir bunlar için yorum işareti kullanırız.
 #Python'da tanımlanmış anahtar kelimeleri değişken ismi olarak kullanırsak hata alırız.
#

#VERİ TİPLERİ
"""
    int : ( integer:tam sayı )
    float : (gerçel sayı )
    bool : (true yada false alır )
    None : Bir değeri yok yer tutucu görevi var.
    complex :Karmaşık sayıları belirtmek için
"""
#Bazı fonkisyonların özellikleri

#int() fonksiyonu
"""Metin olarak verilen sayıyı tam sayıya çevirebiliriz.Örn:"""
sayi1 = '1290'  #metin olarak verilmiş
print("Sayı1'in değeri :" , int(sayi1)) #tam sayıya çevirdik.

"""Gerçel sayıyı tam sayıya çevirmek içinde kullanabiliriz."""
sayi2=2.12
print("Sayı2'nin değeri :", int(sayi2)) #tam kısmı olan 2 sonucumuz olacak.

"""Yine int() fonksiyonunu kullanırken,ikinci argüman verip sayının hangi sayma sisteminde olduğunu belirtebiliriz."""
print("Sistem(Sayma sistemi) :" , int('1010',2))

#Verinin türünü öğrenmek için type() fonksiyonu kullanırız.
print("Verinin türü :" , type(2))  #int
print("Verinin türü :" , type('ayl')) #string
print("Verinin türü :" , type(2.15)) #float
print("Verinin türü :" , type(2+5j)) #complex

#Verinin bit büyüklüğünü öğrenmek için .bit_length()
print("25 sayısının büyüklüğü : " , (25).bit_length())

#Bool : True yada False değerini döndüren mantıksal veri türüdür.
# ==> 0 False , diğer tüm sayılar True
print("0' ın değeri nedir? Cevap :",bool(0))
print("2' nin değeri nedir ? Cevap :",bool(2))
print("1.7 'nin  değeri nedir ? Cevap :",bool(1.7))

#list,dictinory,tuple veri yapılarında hiç bir eleman yoksa bool karşılığı False olur.(ileriki konular olocak)
#None için hiç bir değer yada özellik olmadığı için False olacak.
print("None değeri :",bool(None))

#Bool için bazı işlemler:
"""Bool 0 ve 1 değer aldığı için yapılacak işlemlerde de 1 yada 0 değerini alırlar."""
print("True ve True toplamaı :" , (True + True)) #True değeri 1 olduğu için 1+1
print("True ve False toplamı :" , (True + False)) #1+0
print("False ve False toplamı :" ,(False + False)) # 0+0
print("True-False :",(True-False))
print("(True+True+True)*12 işleminin sonucu :",((True+True+True)*12)) # 3*12

#String(Metin Veri Tipi)
# String için "...." yada '...' tırnak işaretlerinden biri kullanılır.
print("Bu bir String veri Tipidir")
print('Burasıda String Veri Tipidir.')

string_ornek="Şelale"
print("String veri türünde türkçe karakter sıkıntısı yaşanmaz.Örneğin;",string_ornek)

#Bir metindeki karakteri almak için [] kullanılır.Örneğin;
karakterAl = "Merhaba, Python ve Java"
print("karakterAl' ın 0. değeri :" ,karakterAl[0])
print("karakterAl' ın 1. değeri :" ,karakterAl[1])
print("karakterAl' ın 5. değeri :" ,karakterAl[5])
#print("karakterAl' ın 100. değeri :",karakterAl[100]) #Burada bir sonuç alamayız.Çünkü 100. değeri yoktur.

#Bir veriyi metne çevirmek için str kullanılır.
veri_tipi=9875
print("veri_tipi type :" ,type(veri_tipi))  #int çıkar
veri_tipi_donusumu=str(veri_tipi)
print("Dönüştürülmüş halinin type ' ı:",type(veri_tipi_donusumu)) # str çıkar

# \n karakteri alt satıra geçmek için kullanılır.Örneğin:
print("Karakteri kullanmadan :" , "Python öğreniyorum")
print("Karakteri kullanarak :" , "Python\n öğreniyorum")
print("Karakteri kullanarak :" , "Python \nöğreniyorum")
print("Karakteri kullanarak :" , "Python öğreni\nyorum")

#Metin içinde tab kullanmak için
tabKullan="Java'yı \t biliyorum \t Python \t öğreniyorum...."
print("Tab kullanınca tab boşluğu oluyor :Örneğin ;",tabKullan) # Java'yı 	 biliyorum 	 Python 	 öğreniyorum.... sonucu alınacak.
#Metin içinde tırnak veya kesme işareti kullanmak için \" , \' kullanılır.

#Dosya ve klasor adreslerini yazmak için önemli detay!!!
dosya_yolu=r"C:\PythonCalismalari\python_notlar1"
print("dosya yolu için \"r\" kullanalım :" ,dosya_yolu)

#Metin veri tipinde toplama,çarpmada yapabiliriz.
meyve="elma "
renk=" kırmızı"
meyvenin_rengi= renk + meyve
meyve_carp = meyve*5
print("Meyvenin rengi :", meyvenin_rengi) #kırmızıelma
print("Meyveyi 5 ile çarp:",meyve_carp) #elma elma elma elma elma

#Bazı metotlar :
cumle="java ve python güzel'dir :)"
#upper() metnin tamamını büyük harf yapar,lower() küçük yapar.
print("cümledeki her harf büyük oldu :", cumle.upper())
#capitalize() Cümlenin ilk harfini büyük diğerlerini küçük yapmak için
print("ilk harf büyük olacak :",cumle.capitalize())
#title() metindeki her kelimenin ilk harfi büyük olur.
print("Her kelimenin ilk harfi büyük olacak :",cumle.title())

#Metindeki boşlukları kaldırmak için.Örenğin;
cumle2="    java      Python merhaba     ........"
print("Sağ ve soldaki tüm boşlukları kaldırır:",cumle2.rstrip())
print("Sağ ve soldaki tüm boşlukları kaldırır.:",cumle2.lstrip())
print("Metindeki tüm boşlukları kaldırır.:",cumle2.strip())
print("Metni kelimelere ayırmak için:",cumle2.split()) #['java', 'Python', 'merhaba', '........']

#Metnin herhangi bir bölümünü değiştirmek için replace()
cumle3="Mavi,Kırmızı,Sarı,Beyaz"                                                        #Mavi,Kırmızı,Sarı,Beyaz
print("Metnin herhangi bir yerini değiştirmek için)" ,cumle3.replace("Kırmızı","Beyaz")) #Mavi,Beyaz,Sarı,Beyaz

#Metnin belirtilen bir karakter ya da karakter dizisi ile başlayıp başlamadığını startswith() ile bitip bitmadiğini endswith() ile
print("Ma ile başlıyormu :",cumle3.startswith("Ma")) #True
print("xy ile başlıyormu :",cumle3.startswith("xy")) #False
print("Yaz ile bitiyormu :",cumle3.endswith("yaz")) #true

#Metinde bir karakter yada karakter sırasını bulmak için find() kullanılır.
    #ilgili harfin metinde ilk görüldüğü yeri verir.O harf yoksa -1 değer gelir.
cumle4="JavaPython"
print("Sırası :",cumle4.find('a'))
print("va nın sırası :",cumle4.find("va"))
print("x varmı ? :",cumle4.find("x")) #-1 olacak

#Bir metnin belirtilen formatta olup olmadığını kontrol etmek için,
"""
isupper()
isdigit()
isdecimal()
istitle()
isspace()
islower()
isspace()  kullanılır.
    
"""
formatKontrolu="Antalya"
print("isupper :",formatKontrolu.isupper()) #False
print("isdigit :",formatKontrolu.isdigit())
print("isdecimal :",formatKontrolu.isdecimal())
print("istitle:",formatKontrolu.istitle())
print("isspace :",formatKontrolu.isspace())
print("islower :",formatKontrolu.islower())

#bytes veri tipi
#Metinlerden farklı olarak verinin başına b getirilir.
cumle5=b"Java ve Python"
print("Type :" ,type(cumle5))

#Metin veri tipini byte veri tipine çevirmek için encode(),byte veri tipini metin tipine çevirmek için decode()
byte_veritipi=cumle5.encode("utf-8")
print(byte_veritipi)






