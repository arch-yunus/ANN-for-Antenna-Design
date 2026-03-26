# ?? Antenna Theory & Physical Fundamentals

Bu doküman, microstrip patch antenlerin çal??ma prensiplerini ve bu projede kullan?lan matematiksel modelleri aç?klar.

## 1. Microstrip Patch Anten Nedir?
Microstrip patch anten, bir dielektrik katman (?u durumda substrate) üzerine yerle?tirilmi? iletken bir yamadan (patch) olu?ur. Alt k?s?m ise tamamen iletken bir yer düzlemi (ground plane) ile kapl?d?r.

### Avantajlar?:
- Dü?ük profil ve hafiflik.
- Bask? devre (PCB) teknolojisi ile kolay üretim.
- Mekanik olarak dayan?kl?.

## 2. Transmission Line Model (?letim Hatt? Modeli)
Projedeki verilerin üretiminde kullan?lan temel modeldir. Bu modelde, patch iki yuvadan (slot) olu?an bir iletim hatt? olarak kabul edilir.

### Rezonans Frekans? (f_r) Formülü:
$$f_r = \frac{c_0}{2L \sqrt{\epsilon_{eff}}}$$

Burada:
- **$c_0$:** I??k h?z? ($3 \times 10^8$ m/s).
- **$L$:** Patch uzunlu?u.
- **$\epsilon_{eff}$:** Etkin dielektrik sabiti.

### Etkin Dielektrik Sabiti ($\epsilon_{eff}$):
Patch antenin üzerindeki hava ve alt?ndaki dielektrik malzeme aras?ndaki etkile?im, dalgalar?n "etkin" bir ortamda hareket etmesine neden olur.
$$\epsilon_{eff} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[ 1 + 12\frac{h}{W} \right]^{-1/2}$$

## 3. Yapay Zekann (ANN) Rolü
Geleneksel yöntemlerde, bu formüller her zaman çok hassas sonuçlar vermez (özellikle yüksek frekanslarda). EM simülatörleri (HFSS, CST) ise çok fazla i?lemci gücü ve zaman gerektirir. 

**ANN (Artificial Neural Networks)**, bu karma??k ili?kiyi büyük bir veri setinden ö?renerek:
1. **H?zl? Tahmin:** Saniyeler içinde sonuç üretir.
2. **Do?rusal Olmayan ili?kiler:** Karma??k saç?l?m (fringing) etkilerini modeller.
3. **Optimizasyon:** İstenen frekans için en iyi boyutlar? saniyeler içinde bulabilir.

---
*Haz?rlayan: Bahattin Yunus Çetin*
