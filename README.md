 🔬 Biometric-Based Blood Group Detection Using Fingerprint Analysis

---

📌 Overview

This project presents an intelligent biometric system that predicts **ABO** and **Rh** blood groups using **fingerprint features**. Traditional blood testing methods require invasive procedures, skilled technicians, and laboratory infrastructure. This system offers an alternative:
✔️ **Non-invasive**
✔️ **Fast & automated**
✔️ **Cost-efficient**
✔️ **Scalable for healthcare screening**

The model analyzes dermatoglyphic patterns extracted from fingerprints and uses machine learning to classify blood groups with high accuracy.

---
 🧠 Key Features

* **Fingerprint Preprocessing**
  – Noise reduction, ridge enhancement, binarization, and segmentation.
* **Feature Extraction**
  – Minutiae (ridge endings, bifurcations)
  – Pore-level geometry
  – Ridge texture and orientation fields
* **Genetic Algorithm Optimization**
  – Selects the most discriminative fingerprint features.
* **CNN Classification Model**
  – Predicts both **ABO** and **Rh** blood groups.
* **End-to-End Pipeline**
  – Input image → Preprocessing → Feature Extraction → GA Optimization → CNN Prediction.

---
 🏗️ System Architecture

```
Fingerprint Image  
        │
        ▼
Preprocessing (enhancement, segmentation)
        │
        ▼
Feature Extraction (minutiae + pores + texture)
        │
        ▼
Genetic Algorithm (feature optimization)
        │
        ▼
CNN Model (ABO + Rh classification)
        │
        ▼
Predicted Blood Group
```

---

 🛠️ Tech Stack

* **Python 3.x**
* **TensorFlow / Keras** – CNN classification
* **OpenCV** – preprocessing & feature extraction
* **NumPy, Pandas** – data handling
* **Matplotlib / Seaborn** – visualization

---

 📂 Project Structure


---

 🚀 How to Run

1. **Clone the repository**

```
git clone https://github.com/your_username/your_repo.git
```

2. **Install dependencies**

```
pip install -r requirements.txt
```

3. **Run the main program**

```
python main.py
```


 📊 Results

* High classification accuracy for both **ABO and Rh** systems.
* Genetic Algorithm improved feature relevance and model performance.

*(Add accuracy numbers once training is complete.)*

---

📈 Future Enhancements

* Support for multiple fingerprints to improve accuracy
* Real-time mobile app version
* Integration with hospital management systems
* Larger dataset expansion

---

 📜 License

This project is released under the **MIT License**.

---





