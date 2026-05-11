# Sentiment Analysis Virtual Bot (Tweetler) 🐦🤖

A machine learning and NLP-based virtual bot designed to analyze sentiments from Twitter in real time. **Tweetler** classifies tweets as **Positive**, **Negative**, or **Neutral** using Natural Language Processing (NLP) and Support Vector Machine (SVM) algorithms.

---

## 📌 Project Overview

The **Sentiment Analysis Virtual Bot (Tweetler)** is developed to understand human emotions and opinions expressed on Twitter. By using machine learning and NLP techniques, the system analyzes tweets and identifies their sentiment polarity.

The project helps businesses, researchers, and individuals monitor public opinions, customer feedback, brand reputation, and social media engagement effectively.

Tweetler also supports advanced features like sarcasm detection, emoji interpretation, and real-time tweet extraction through a Chrome extension.

---

## 🚀 Features

* 😊 **Sentiment Classification**

  * Positive
  * Negative
  * Neutral

* ⚡ **Real-time Tweet Analysis**

* 🧠 **Natural Language Processing**

  * Tokenization
  * Stemming
  * Stop-word removal
  * Entity recognition
  * Speech tagging

* 🌐 **Chrome Extension Integration**

  * Extracts tweets directly from Twitter homepage

* 📊 **Machine Learning-Based Predictions**

  * Uses Support Vector Machine (SVM)

* 😄 **Sarcasm & Emoji Detection**

* 🖥️ **User-Friendly Interface**

* 📈 **Scalable & Accurate System**

---

## 🛠️ Technologies Used

| Technology          | Purpose                     |
| ------------------- | --------------------------- |
| Python              | Core Programming Language   |
| Flask               | Web Framework               |
| Selenium            | Tweet Extraction Automation |
| NLP                 | Text Processing             |
| Scikit-learn        | Machine Learning            |
| SVM Algorithm       | Sentiment Classification    |
| HTML/CSS/JavaScript | Frontend Development        |
| Chrome Extension    | Twitter Data Extraction     |

---

## ⚙️ Workflow

### 1️⃣ Data Extraction

Tweets are extracted from Twitter using a Chrome extension powered by Selenium automation.

### 2️⃣ Preprocessing

The extracted text undergoes:

* Segmentation
* Tokenization
* Stop-word removal
* Stemming
* Speech tagging

### 3️⃣ Feature Extraction

Important sentiment-related features are identified for analysis.

### 4️⃣ Model Training

The Support Vector Machine (SVM) model is trained using labeled datasets.

### 5️⃣ Real-time Analysis

Tweets and replies are analyzed dynamically for sentiment prediction.

### 6️⃣ Output Presentation

Sentiment labels are displayed beside tweets for easy understanding.

---

## 📂 Project Structure

```plaintext
Tweetler/
│
├── app.py
├── model/
├── dataset/
├── templates/
├── static/
├── chrome_extension/
├── sentiment_model.pkl
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Tweetler.git
```

### 2. Navigate to Project Folder

```bash
cd Tweetler
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📋 Requirements

Add these libraries inside `requirements.txt`:

```txt
flask
selenium
scikit-learn
nltk
pandas
numpy
beautifulsoup4
```

---

## ▶️ Run the Project

```bash
python app.py
```

Open in browser:

```plaintext
http://127.0.0.1:5000/
```

---

## 🖥️ Project Demonstration

The Tweetler system works in real time by extracting tweets from Twitter and performing sentiment analysis dynamically.

The Chrome extension retrieves tweets from the Twitter homepage, after which NLP preprocessing techniques are applied. The trained SVM model predicts sentiments, and the output is displayed beside tweets instantly.

The project demonstrates the integration of:

* Machine Learning
* Natural Language Processing
* Browser Automation
* Real-time Data Analysis

---

## 🌟 Advantages

* Real-time sentiment monitoring
* Accurate sentiment prediction
* Helps analyze customer opinions
* Useful for brand reputation tracking
* Scalable and customizable system
* Supports sarcasm and emoji understanding

---

## 🔮 Future Enhancements

* Deep Learning integration (LSTM/BERT)
* Multi-language sentiment analysis
* Advanced visualization dashboard
* Voice sentiment analysis
* Social media analytics integration
* User authentication system
* Cloud deployment support

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes. Twitter data extraction should comply with Twitter/X platform policies and API guidelines.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make changes
4. Commit your updates
5. Submit a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Rutvij A & Team**

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
