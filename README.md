# Customer-Insights-Dashboard-with-AI-Powered-Text-Generation-and-Sentiment-Analysis

This web application, built with Flask, enables users to input text for both sentiment evaluation and content generation. It utilizes NLTK’s Vader for sentiment analysis and employs the GPT-2 model from Hugging Face Transformers to generate additional related text.

## 🔍 Key Functionalities

- Submit text input (e.g., reviews, feedback, or open-ended responses).
- Instantly assess the sentiment using NLTK’s Vader SentimentIntensityAnalyzer.
- Generate additional AI-driven text aligned with the given input.
- Display sentiment results, input, and generated output in a clear layout.
- Quick access button to return and analyze new input data.

---

## 🛠️ Tech Stack

- **Python**: Handles backend logic and NLP processing.
- **Flask**: Lightweight framework used for routing and rendering the web app.
- **NLTK**: Natural language processing toolkit, used here for sentiment classification.
- **Transformers (by Hugging Face)**: For incorporating pre-trained GPT-2 models to generate text.
- **HTML & CSS**: Structure and basic styling of the web interface.
- **Bootstrap**: Ensures the interface is responsive and visually consistent.

---

## 🧪 Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/vinit714/AI-Powered-Text-Generation-and-Sentiment-Analysis-Dashboard.git
   
---   

### 2.🔧 Install Required Dependencies

   ```bash
   pip install -r requirements.txt
   ```
This will install Flask, NLTK, Transformers, and any other dependencies.
### 3. 📦 Download Required NLTK Data

Download the datasets required for Vader sentiment analysis:

```bash
python -m nltk.downloader vader_lexicon
python -m nltk.downloader reuters
```
 
### 4. ▶️ Run the Application

Launch the Flask app using:

```bash
python run.py
```
### 5. 🌐 Access the Application

Open your browser and go to:

```
http://localhost:5000
```

---



## **💡 How to Use**
Go to the homepage.
Enter any feedback or comment into the input field.
Click "Submit" to perform sentiment analysis and text generation.
Review the results displayed on the next page.
Click "Go Back" to try a new input.

----

## **🤝 Contributions**
We welcome your input! Whether it's a bug fix, feature suggestion, or enhancement, feel free to fork this repository and open a pull request or raise an issue.

---

## **📘 About This Project**
This application was created to analyze customer messages and generate meaningful AI responses. It’s ideal for exploring AI-powered customer insight tools and testing NLP techniques with real-time user input.

---
## 🏷️ Tags

`flask-app` `customer-insights` `sentiment-analysis` `nlp` `text-generation`
`gpt-2` `huggingface` `vader` `ai-dashboard` `python-project`

---

## 📊 Repository Insights

* **Languages Used**

  * Python – 45.5%
  * HTML – 32.0%
  * CSS – 22.5%

* **Stars**: ⭐ 0

* **Forks**: 🍴 0

* **Watchers**: 👀 1

---







   
