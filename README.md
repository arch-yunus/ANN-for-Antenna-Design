# 📡 ANN for Antenna Design: Geleceğin Elektromanyetik Mühendisliği

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Architecture: MLP](https://img.shields.io/badge/Architecture-MLP-red.svg)](#)
[![Status: Masterclass](https://img.shields.io/badge/Status-Masterclass-brightgreen.svg)](#)

> **"Mühendislik, doğanın dizginlenemez ve çoğu zaman kaotik güçlerini insan zekasının analitik süzgecinden geçirerek profesyonel çözümlere dönüştürme sanatıdır. Yapay Zeka ise bu metodolojiyi, sadece tahmin edilebilirliğin ötesine taşıyarak, henüz keşfedilmemiş olasılıklar uzayında teknik mükemmelliği arayan dijital bir mimari disiplindir."**

---

## 👨‍💻 Yazar Hakkında (About the Author)

**Bahattin Yunus Çetin**  
*Teknoloji Mimarı & Yazılım Mühendisi (Technology Architect & Software Engineer)*  

[![GitHub](https://img.shields.io/badge/GitHub-BahattinYunus-181717?style=for-the-badge&logo=github)](https://github.com/bahattinyunus)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bahattin%20Yunus%20Çetin-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/bahattinyunus)

---

## 🛠 Mühendislik Metodolojisi (Engineering Methodology)

Bu proje, bir "Yapay Sinir Ağı" (ANN) kullanarak Microstrip Patch Anten tasarımını modernize eden profesyonel bir mühendislik aracıdır. Geleneksel Maxwell denklemi simülasyonlarının aksine, bu sistem çok boyutlu parametre uzayındaki gizli ilişkileri öğrenerek milisaniyeler içinde yüksek hassasiyetli tahminler sunar.

### Temel Özellikler
- **Forward Design:** Fiziksel boyutlardan (W, L, h, er) rezonans frekansı (fr) tahmini.
- **Inverse Design:** Hedef frekans için optimal boyutların (L-BFGS-B optimizasyonu ile) otomatik belirlenmesi.
- **Sensitivity Analysis:** Hangi parametrenin (örneğin uzunluk mu, dielektrik sabit mi?) sistemi ne kadar değiştirdiğinin analizi.
- **3D Topology Visualization:** Parametre ilişkilerinin profesyonel 3D haritaları.

---

## 🚀 Kurulum ve Kullanım (Installation & Usage)

### 1. Ortamı Hazırlama
```bash
git clone https://github.com/bahattinyunus/ANN-for-Antenna-Design.git
cd ANN-for-Antenna-Design
pip install -r requirements.txt
```

### 2. Model Eğitimi (Training)
```bash
python main.py --train --cv
```

### 3. Tasarım Tahmini (Forward Prediction)
```bash
python main.py --predict --W 45.0 --L 40.0 --H 1.6 --ER 4.4
```

### 4. Tersine Tasarım (Inverse Design)
```bash
python main.py --inverse --target_f 2.45
```

### 5. Duyarlılık Analizi (NEW)
```bash
python sensitivity.py
```

---

---

## 📂 Proje Yapısı (Project Hierarchy)

```text
ANN-for-Antenna-Design/
├── docs/                   # 📚 Akademik ve Teknik Dokümantasyon
│   ├── theory.md           # Maxwell Denklemleri & İletim Hattı Teorisi
│   └── parameters.md       # Malzeme ve Boyut Seçim Kılavuzu
├── assets/                 # 🎨 Görsel Materyaller ve Bannerlar
├── config.py               # ⚙️ Merkezi Hiperparametre ve Yol Yönetimi
├── generator.py            # 🧪 Veri Üretim Motoru (Transmission Line Model)
├── model.py                # 🧠 Yapay Sinir Ağı Mimarisi (MLP)
├── optimizer.py            # 🎯 Tersine Tasarım Optimizasyon Motoru
├── sensitivity.py          # 📊 Tasarım Duyarlılık Analizi
├── visualizer.py           # 📈 3D Topoloji ve Performans Görselleştirme
├── main.py                 # 🚀 Ana Kontrol Ünitesi (CLI)
├── GLOSSARY.md             # 📜 RF & EW Terimler Sözlüğü
└── requirements.txt        # 📦 Gerekli Kütüphaneler
```

---

## 🧠 Teknik Derin Bakış (Technical Deep Dive)

### 📊 Veri Seti ve Gürültü Modeli
Eğitim verileri, **Transmission Line Model** kullanılarak üretilir. Gerçek dünya RF ortamlarını simüle etmek için verilere `%2 % Gaussian Noise` eklenmiştir. Bu, modelin EM çözücü (HFSS/CST) varyasyonlarına karşı dayanıklılığını artırır.

### 🧠 Model Mimarisi
Sistem, `scikit-learn` tabanlı bir **Multilayer Perceptron (MLP)** kullanır:
- **Giriş Katmanı:** 4 Nöron ($W, L, h, \epsilon_r$)
- **Gizli Katmanlar:** [128, 64, 32] (ReLU aktivasyonu ile)
- **Çıkış Katmanı:** 1 Nöron ($f_r$ - GHz)
- **Regülarizasyon:** Overfitting'i önlemek için L2 Adam optimizer entegre edilmiştir.

### 🎯 Tersine Tasarım Stratejisi
Inverse design aşamasında, eğitilmiş model dondurulur ve **L-BFGS-B (Limited-memory Broyden–Fletcher–Goldfarb–Shanno with Boundaries)** algoritması kullanılarak hedef frekansa en yakın $W$ ve $L$ değerleri iteratif olarak bulunur.

---

## 🗺️ Gelecek Yol Haritası (Future Roadmap)

- [ ] **Full-Wave Integration:** Üretilen tasarımları otomatik olarak `.aedt` veya `.cst` formatında dışa aktarma.
- [ ] **Swarm Intelligence:** Optimizasyon motoruna PSO (Particle Swarm Optimization) desteği ekleme.
- [ ] **Complex Patch Shapes:** Dairesel ve üçgen yamalar için model desteği.
- [ ] **Gain Prediction:** Sadece rezonans değil, anten kazancı (Gain) tahmini ekleme.

---

## 📚 Teknik Dokümantasyon (Technical Curriculum)

Proje hakkında daha derinlemesine bilgi için aşağıdaki dokümanları inceleyin:

- [📖 Teori ve Fiziksel Temeller](docs/theory.md): Maxwell denklemleri ve Transmission Line Model.
- [📒 Parametre Kılavuzu](docs/parameters.md): Anten boyutları ve malzeme seçiminin etkileri.
- [📜 Terimler Sözlüğü](GLOSSARY.md): RF ve AW alanındaki anahtar kavramlar.

---

## 📄 Lisans (License)
Bu proje MIT lisansı altında sunulmaktadır.
