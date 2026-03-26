# 📖 Antenna Theory & Physical Fundamentals

Bu doküman, microstrip patch antenlerin çalışma prensiplerini ve bu projede kullanılan matematiksel modelleri açıklar.

## 1. Microstrip Patch Anten Nedir?
Microstrip patch anten, bir dielektrik katman (şu durumda substrate) üzerine yerleştirilmiş iletken bir yamadan (patch) oluşur. Alt kısım ise tamamen iletken bir yer düzlemi (ground plane) ile kaplıdır.

### Avantajları:
- Düşük profil ve hafiflik.
- Baskı devre (PCB) teknolojisi ile kolay üretim.
- Mekanik olarak dayanıklı.

## 2. Transmission Line Model (İletim Hattı Modeli)
Projedeki verilerin üretiminde kullanılan temel modeldir. Bu modelde, patch iki yuvadan (slot) oluşan bir iletim hattı olarak kabul edilir.

### Rezonans Frekansı (f_r) Formülü:
$$f_r = \frac{c_0}{2L \sqrt{\epsilon_{eff}}}$$

Burada:
- **$c_0$:** Işık hızı ($3 \times 10^8$ m/s).
- **$L$:** Patch uzunluğu.
- **$\epsilon_{eff}$:** Etkin dielektrik sabiti.

### Etkin Dielektrik Sabiti ($\epsilon_{eff}$):
Patch antenin üzerindeki hava ve altındaki dielektrik malzeme arasındaki etkileşim, dalgaların "etkin" bir ortamda hareket etmesine neden olur.
$$\epsilon_{eff} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[ 1 + 12\frac{h}{W} \right]^{-1/2}$$

## 3. Yapay Zekanın (ANN) Rolü
Geleneksel yöntemlerde, bu formüller her zaman çok hassas sonuçlar vermez (özellikle yüksek frekanslarda). EM simülatörleri (HFSS, CST) ise çok fazla işlemci gücü ve zaman gerektirir. 

**ANN (Artificial Neural Networks)**, bu karmaşık ilişkiyi büyük bir veri setinden öğrenerek:
1. **Hızlı Tahmin:** Saniyeler içinde sonuç üretir.
2. **Doğrusal Olmayan İlişkiler:** Karmaşık saçılma (fringing) etkilerini modeller.
3. **Optimizasyon:** İstenen frekans için en iyi boyutları saniyeler içinde bulabilir.

---
*Hazırlayan: Bahattin Yunus Çetin*
