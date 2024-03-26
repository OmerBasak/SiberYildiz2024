2024 SiberYıldız Çözümlerim
	Siber güvenlik üzerinde çok fazla uğraşmamış birisi olarak, yazılım ve az miktardaki siber güvenlik bilgimle çözebildiğim soruları paylaşacağım;

  **1) Nyan Cat:**
		Soruda bir alışveriş sitesi vardı ve sitede bir hesap oluşturdum. 

  <img src="/img/img1.png" width="500"/>

  Kullanıcı profili sayfasında ekranda gözükmeyen bir flag alanı vardı fakat içi boştu. Anlaşılan eğer doğru kullanıcı ile giriş yaparsam, flag alanı dolacaktı ve soruyu cevaplayabilecektim. 
  
  <img src="/img/img2.png" width="900"/>

  Profile sayfasının requestlerini networks kısmından incelediğimde userID çerezi ilgimi çekti. ='den dolayı base64 olduğunu düşündüm. 3 kez art arda base64 decoderden geçirdikten sonra değerin 5'e eşit olduğunu fark ettim. Yani "Sistemin 5. kullanıcısı ben olmalıydım. 1. kullanıcı ise admindir ve flag'ı görüntüleme yetkisine sahip olmalıdır." şeklinde bir düşünceyle 1 sayısını 3 kez base64'den geçirip sunucuya gönderdim. "ali123" kullanıcı adlı bir hesaba erişmiştim ve flag'ı görüntüleme yetkisine sahip değildi. Aynı işlemi 6 sayısı için de yaptım. Şaşırtıcı bir şekilde benim id değerimden sonra da hesaplar vardı. Flag'ı görme yetkisi olan hesap 100. kullanıcı bile olabilirdi. Bu sebepten basit bir python scripti yazdım.

  [Yazdığım Script: siber.py](https://github.com/OmerBasak/SiberYildiz2024/blob/main/NyanCat/siber.py)

  Ve sonuç: 

  <img src="/img/img3.png" width="700"/>

  Python flag'ı içeren html'i flag.data olarak kayıt etmişti. 

  **2) Bedavadan Biraz Pahalı:**
		  Karşıma bir alışveriş sitesi çıkmıştı ve web script zaafiyetleriyle alakalı olduğunu, yüksek ihtimalle çözemeyeceğimi düşünmüştüm.

  
  <img src="/img/img4.png" width="700"/>

  Sitedeki ürünlerin satın alma bağlantısı "https://ba9d8e09f7de04af.siberyildiz.com/?qq=87495:86107" bu tarz yerlere yönlendiriyordu. Buna kısaca x:y diyeceğim. Sol taraftaki x ilan numarasına eşit olduğundan bunun ürün id'si olduğunu anladım. Sağdaki değeri ise her değiştirdiğimde mevcut görünen bakiyem değişiyordu. Fakat orantılı bir artış veya azalma değildi.

  <img src="/img/img5.png" width="700"/>

  x ve y'ye aynı değeri girdiğimde yukarıdaki hatayı aldım. Bu sefer de fiyatın x ve y'nin farkı olduğunu düşündüm fakat değildi. Yine de y'nin x'e yakın değerleri olması gerekiyordu. İki seçeneğim vardı. Ya bunun algoritmasını öğrenmek için denemeler yapacaktım ya da tekrardan Python'dan yardım alacaktım ve cevabı benim için bulacaktı. Tabii ki ikinci seçeneği seçtim.

  <img src="/img/img6.png" width="500"/>

  [9 satırlık kod](https://github.com/OmerBasak/SiberYildiz2024/blob/main/BedavadanBirazPahali/please.py) bana uyarı mesajı vermeyen y değerini söylemişti: 81576. https://ba9d8e09f7de04af.siberyildiz.com/?qq=81223:81576 sayfasına girdiğimde bir fotoğraf seçilme sayfasına yönlendirdi ve ekranda mili saniyeler içerisinde kaybolan bir kısım vardı.

  <img src="/img/img7.png" width="500"/>

  [aaa.js kodu](https://github.com/OmerBasak/SiberYildiz2024/blob/main/BedavadanBirazPahali/aaa.js) ilgimi çekti fakat JavaScript bilmediğimden bununla uğraşmak yerine ChatGPT'den Python için çevirmesini istedim. [GPT'nin verdiği kodu](https://github.com/OmerBasak/SiberYildiz2024/blob/main/BedavadanBirazPahali/gpt.py) çalıştırdığımda sonuç karşımdaydı.

  <img src="/img/img8.png" width="500"/>

  (Karşımdaydı sanmıştım...) Verdiği url'ye girdiğimde Unauthorized access sonucu alıyordum ve headers'de değişiklikler yaparak, referer vs ekleyerek flag.txt'ye girmeye çalıştım. Başarılı olamadım. Sanırım siber güvenlik bilmeyen yazılımcıların ilk elendiği soru oldu ):

  **3) SertKod:**
  Basit bir soruydu.

  <img src="/img/img9.png" width="600"/>

  Verilen .apk dosyasını JadX ile açtığımızda bir kullanıcı adı ve şifre görüyordunuz. 

  <img src="/img/img10.png" width="200"/>
  
  Verilen mobil uygulamayı çalıştırıp bu kullanıcı adı ve şifreyle giriş yaptığınızda Accounts sayfasında flag çıkıyordu.

  **5) 01 Adana:**

  <img src="/img/img11.png" width="600"/>
    
  Site 10.zip içerisinde bir dosya indirtiyor. Zip'i açıp sqlite ile sql dosyalarının içeriğini incelemeye başladım. 10\Profiles\ki9j95dt.default-release\places.sql içerisinde moz_places tablosunda "http://4ps41ropumyebbsa.siberyildiz.com/a1bb2ccc3dddd4a13fedxx277tr5tr1.php" dikkatimi çekmişti. Siteye girdiğimde "66fnn3222o1o1235ggtr1.rar" adında bir dosya indirdi. Rarı açtığımda içi boş olan ama hiç de boş olmadığı belli olan [01 adında](https://github.com/OmerBasak/SiberYildiz2024/blob/main/01Adana/66fnn3222o1o1235ggtr1.rar) bir dosya çıkıyordu. Her yerinde tab boşlukları ve normal boşluklar vardı. İlk aklıma mors alfabesi alfabesi geldi. "Tablar uzun, boşluklar kısa çizgi :D" ama değilmiş, binary imiş. 

  <img src="/img/img12.png" width="800"/>

  Python'da basit bir replace işlemi ile tabları 1, boşlukları 0 olarak değiştirdikten sonra çıktıyı herhangi bir binary to text sitesine atmak çözüm için yeterliydi. Çıkan php dosyasını url'mizin sonuna eklediğimizde flag'ı görüyorduk.

  **6) Atların Efendisi:**
		En basit soruydu. Site "d41e73281c1dfb45af6bcf362afbc53a.py" adında bir Python scripti indirtiyordu. Kodların içerisinde bir value değeri vardı. Bu değer dosyayı indirdiğimiz siteye girildiğinde flag'ı veriyordu.


