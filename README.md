# Twitter Veri Seti Üzerinden Duygu Analizi (Sentiment Analysis)

Bu proje, Twitter verileri üzerinden kullanıcıların duygu durumunu otomatik olarak sınıflandırmak amacıyla geliştirilmiştir.

##  Veri Ön İşleme (Pre-processing)
Veri madenciliği süreçlerinde, ham verinin doğrudan modele verilmesi başarı oranını düşüren en büyük etkendir. Twitter verileri; reklamlar, bağlantılar ve özel karakterler içerdiği için yüksek oranda gürültü barındırır. Bu projede modelin sadece anlam taşıyan kelimelere odaklanması için şu adımlar uygulanmıştır:

*   **Küçük Harfe Dönüştürme:** "Happy" ve "happy" gibi kelimelerin farklı algılanmaması için tüm metin normalize edilmiştir.
*   **Kullanıcı Etiketlerinin (@mention) Kaldırılması:** Regex kullanılarak tüm @kullanıcı ifadeleri temizlenmiştir.
*   **Bağlantıların (URL) Temizlenmesi:** http ve https ile başlayan adresler ayıklanmıştır.
*   **Noktalama İşaretleri ve Sayıların Atılması:** Sadece alfabetik karakterlerin kalması sağlanmıştır.
*   **Boşluk Temizliği:** Metinlerin başındaki ve sonundaki gereksiz boşluklar silinmiştir.

### Örnek Dönüşüm
**Ham Tweet:** `@Onur http://bit.ly/123 Amazing day! 10/10 :)`  
**İşlenmiş Tweet:** `amazing day`

---

##  Metodoloji
*   **Vektörleştirme:** Metinleri sayısal verilere dönüştürmek için **TF-IDF** (Term Frequency-Inverse Document Frequency) yöntemi kullanılmıştır.
*   **Model:** 1.6 milyonluk büyük veri setlerinde hızlı ve yüksek performanslı sonuç verdiği için **Lojistik Regresyon** algoritması seçilmiştir.

---

##  Performans Analizi
*   **Doğruluk (Accuracy):** Modelim **%75.0** başarıyla çalışmaktadır.
*   **Özet:** Model hem pozitif hem de negatif tweetleri dengeli bir şekilde ayırabilmektedir (Tarafsız öğrenme).

![Hata Matrisi](Veri%20matrisi%202.png)

---

## 💡 Sonuç ve Değerlendirme
*   **Gözetim Kapitalizmi:** Bu sistemler, sosyal medyadaki "davranışsal artıklarımızı" işleyerek ruh halimizi tahmin eder. Şirketler bu sayede modumuza uygun manipülatif reklamlar sunabilmektedir.
*   **Eksiklikler:** Başarının %100 olmamasının sebebi; makinenin insanların yaptığı şakaları, mecazları ve ironileri henüz tam olarak anlayamamasıdır. Bu, gözetim kapitalizminin hala aşamadığı o "insan ruhu" boşluğunu temsil eder.
*   **Gelecek:** Bir sonraki aşamada **BERT** veya **Transformers** gibi derin öğrenme modelleri kullanılarak bağlamsal analiz geliştirilebilir.
