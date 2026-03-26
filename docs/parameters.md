# ?? Parameter Selection & Material Guide

Anten tasarımında parametrelerin seçimi, sistemin performans?n?, verimlili?ini ve uygulama alan?n? do?rudan belirler.

## 1. Fiziksel Boyutlar (W ve L)
- **Uzunluk (L):** Rezonans frekans?n?n ana belirleyicisidir. L artt?kça frekans dü?er. Genellikle $\lambda/2$ (dalga boyunun yar?s?) olarak tasarlan?r.
- **Geni?lik (W):** Giri? empedans?n? ve radyasyon verimlili?ini etkiler. Geni?lik artt?kça bant geni?li?i de bir miktar artar.

## 2. Substrate (Taban Malzemesi) Seçimi
Antenin üzerine in?a edildi?i yal?tkan tabaka (substrate), elektromanyetik dalgalar?n hız?n? belirler.

### Dielektrik Sabiti ($\epsilon_r$):
- **Dü?ük $\epsilon_r$ (2.2 - 3.5):** Daha yüksek verimlilik ve daha geni? bant geni?li?i sa?lar. Ancak anten boyutlar? büyür. (Örn: Rogers RT/duroid)
- **Yüksek $\epsilon_r$ (4.4 - 10.2):** Anten boyutlarını küçültür (minyatürizasyon). Ancak verimlilik dü?ebilir ve yüzey dalgalar? artabilir. (Örn: FR-4)

### Yükseklik (h):
- Kal?n tabakalar (h > 1.6mm) bant geni?li?ini art?r?r ancak yüzey dalgas? kay?plar?na neden olabilir.
- ince tabakalar (h < 0.8mm) dü?ük profil gerektiren uygulamalar (mobil cihazlar) için uygundur ancak dar bantl?d?r.

## 3. Tasar?m İpuçlar? (Best Practices)
1. **Önce L De?erini Belirleyin:** Hedef frekans?n?z için L parametresini optimize edin.
2. **Empedans Uyumlama:** Besleme hatt?n?n 50 Ohm veya 75 Ohm empedansa uyumlu oldu?undan emin olun.
3. **Malzeme Kalitesi:** Yüksek frekanslarda (Ku ve Ka band?) dü?ük kay?p tanjant?na (Loss Tangent) sahip malzemeler (Teflon bazl?) seçilmelidir.

---
*Haz?rlayan: Bahattin Yunus Çetin*
