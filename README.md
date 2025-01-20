
# Recommendation System

## 📖 Overview
The **Recommendation System** is a Python-based application designed to recommend mobile devices based on user input. Leveraging natural language processing (NLP) techniques and cosine similarity, the system identifies matching products and provides relevant recommendations for users.

---

## 🚀 Features
- Search for mobile devices using keywords.
- Provides matching products based on the search term.
- Recommends related products using content-based filtering.
- Includes a database of real-world mobile devices, including flagship smartphones and budget-friendly options.

---

## 🛠️ Technologies Used
- **Python**: Programming language for implementation.
- **Pandas**: To manage and process tabular data.
- **Numpy**: To handle array and numerical operations.
- **Scikit-learn**: For TF-IDF vectorization and cosine similarity calculations.

---

## 📂 Project Structure
```
recommendation-system/
│
├── database.py          # Creates the product database
├── similarity.py        # Prepares the TF-IDF matrix and cosine similarity
├── recommendation.py       # Recommendation logic implementation
├── main.py              # Entry point for the application
├── README.md            # Project documentation
├── requirements.txt     # Required Python libraries
```

---

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DeathCore0607/recommendation-system.git
   cd recommendation-system
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage
1. Run the application:
   ```bash
   python main.py
   ```

2. Enter a keyword (e.g., "iPhone") to search for mobile devices and receive recommendations.

---

## 🗂️ Example Output
```plaintext
==================================================
Mobile Device Recommendation System
==================================================

Enter a keyword to search (or 'quit' to exit): iPhone

Matching Products for "iPhone":
1. iPhone 15 Pro Max (Smartphone)
   The latest flagship with exceptional camera capabilities and A17 Bionic chip.

Recommended Products Related to "iPhone":
1. iPhone 14 Pro (Smartphone)
   Powerful performance with advanced display features.
2. Samsung Galaxy S24 Ultra (Smartphone)
   A premium alternative with top-notch features.
```

---

## 🔧 Customization
To update or expand the product database:
1. Open `database.py`.
2. Modify the `data` dictionary to add or update products.

---

