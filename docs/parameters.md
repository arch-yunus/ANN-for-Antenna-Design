# 📒 Parameter Selection & Material Guide

Anten tasarımında parametrelerin seçimi, sistemin performansını, verimliliğini ve uygulama alanını doğrudan belirler.

## 1. Fiziksel Boyutlar (W ve L)
- **Uzunluk (L):** Rezonans frekansının ana belirleyicisidir. L arttıkça frekans düşer. Genellikle $\lambda/2$ (dalga boyunun yarısı) olarak tasarlanır.
- **Genişlik (W):** Giriş empedansını ve radyasyon verimliliğini etkiler. Genişlik arttıkça bant genişliği de bir miktar artar.

## 2. Substrate (Taban Malzemesi) Seçimi
Antenin üzerine inşa edildiği yalıtkan tabaka (substrate), elektromanyetik dalgaların hızını belirler.

### Dielektrik Sabiti ($\epsilon_r$):
- **Düşük $\epsilon_r$ (2.2 - 3.5):** Daha yüksek verimlilik ve daha geniş bant genişliği sağlar. Ancak anten boyutları büyür. (Örn: Rogers RT/duroid)
- **Yüksek $\epsilon_r$ (4.4 - 10.2):** Anten boyutlarını küçültür (minyatürizasyon). Ancak verimlilik düşebilir ve yüzey dalgaları artabilir. (Örn: FR-4)

### Yükseklik (h):
- Kalın tabakalar (h > 1.6mm) bant genişliğini artırır ancak yüzey dalgası kayıplarına neden olabilir.
- İnce tabakalar (h < 0.8mm) düşük profil gerektiren uygulamalar (mobil cihazlar) için uygundur ancak dar bantlıdır.

## 3. Tasarım İpuçları (Best Practices)
1. **Önce L Değerini Belirleyin:** Hedef frekansınız için L parametresini optimize edin.
2. **Empedans Uyumlama:** Besleme hattının 50 Ohm veya 75 Ohm empedansa uyumlu olduğundan emin olun.
3. **Malzeme Kalitesi:** Yüksek frekanslarda (Ku ve Ka bandı) düşük kayıp tanjantına (Loss Tangent) sahip malzemeler (Teflon bazlı) seçilmelidir.

---
*Hazırlayan: Bahattin Yunus Çetin*
