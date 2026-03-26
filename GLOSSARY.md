# 📖 RF & Electronic Warfare (EW) Glossary / Terimler Sözlüğü

Bu sözlük, anten mühendisliği, yapay zeka ve elektronik harp teknolojilerindeki temel kavramları içerir.

## 1. Anten Mühendisliği ve RF
- **W (Width):** Microstrip patch antenin genişliği. Giriş empedansını ve bant genişliğini etkiler.
- **L (Length):** Antenin uzunluğu. Rezonans frekansını belirleyen en kritik parametredir (~λ/2).
- **h (Height):** Substrate (taban malzemesi) kalınlığı. Verimliliği ve bant genişliğini doğrudan etkiler.
- **er (Relative Permittivity):** Malzemenin dielektrik sabiti. Dalga boyunu ve anten boyutlarını belirler.
- **f_r (Resonant Frequency):** Antenin EM enerjisini en verimli şekilde yaydığı, geri dönüş kaybının (Return Loss) minimum olduğu frekans.
- **Bandwidth (Bant Genişliği):** Antenin belirli performans kriterlerini (örneğin VSWR < 2) karşıladığı frekans aralığı.

## 2. Yapay Zeka ve Optimizasyon
- **MLP (Multilayer Perceptron):** Girdiler (W, L, h, er) ile çıktı (f_r) arasındaki lineer olmayan ilişkiyi modelleyen çok katmanlı yapay sinir ağı.
- **Inverse Design (Ters Tasarım):** İstenen performans hedefine (f_r) ulaşmak için optimal tasarım parametrelerinin (W, L) yapay zeka veya optimizasyon ile bulunması.
- **Sensitivity Analysis (Duyarlılık Analizi):** Girdi değişkenlerindeki küçük değişimlerin çıktı (f_r) üzerindeki etkisini ölçme süreci.
- **L-BFGS-B:** Sınırlanmış (bounded) optimizasyon problemleri için kullanılan verimli bir quasi-Newton algoritması.

## 3. Elektronik Harp (EW/EH) ve Taktiksel Boyut
- **Signal Intelligence (SIGINT):** Düşman anten sistemlerinin frekans ve konum tespiti.
- **Jamming (Karıştırma):** Düşman haberleşme frekanslarına yüksek enerjili EM dalgası göndererek iletişimi koparma.
- **Stealth (Düşük Görünürlük):** Anten tasarımının Radar Kesit Alanını (RCS) minimize ederek radar sistemlerinden kaçma yeteneği.
- **Spread Spectrum:** Sinyalin geniş bir frekans bandına yayılarak tespiti ve karıştırmayı zorlaştırdığı teknik.

---
**Hazırlayan:** [Bahattin Yunus Çetin](https://github.com/bahattinyunus)
