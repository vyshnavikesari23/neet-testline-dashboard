# 📊 NEET Testline - Personalized Student Recommendation System

## 🚀 Overview
This project is a **Python-based dashboard** built using **Streamlit** to analyze student quiz performance and provide **personalized recommendations**. The system extracts insights from quiz data, identifies weak areas, generates recommendations, and even predicts a **probable NEET rank** based on performance trends.

## 🎯 Features
- **Performance Analysis**: Identify quiz trends, weak topics, and accuracy rates.
- **Student Persona Analysis**: Categorizes students as **High Performer, Improving, Needs Improvement, or Struggling**.
- **Personalized Recommendations**: Suggests **topics and strategies** to improve quiz performance.
- **NEET Rank Prediction Model**: Estimates a student’s potential **NEET rank** based on past quiz performance.
- **Interactive Dashboard**: Allows users to input **User ID and Quiz ID** to view insights.

---

## 🛠️ Installation & Setup

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.8+** installed. Then, install required packages:
```bash
pip install -r requirements.txt
```

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/vyshnavikesari23/neet-testline-dashboard.git
cd neet-testline-dashboard
```

### **3️⃣ Add Data Files**
Ensure that the following JSON files are placed in the **same directory** as the script:
- `APIEndpoint.json`
- `QuizEndpoint.json`
- `QuizSubmissionData.json`

### **4️⃣ Run the Dashboard Locally**
```bash
streamlit run fetch_data.py
```
This will open an interactive **web-based dashboard** in your browser.

---

## 🚀 Deploy on Streamlit Cloud
You can deploy this app for free using **Streamlit Community Cloud**:
1. Go to **[Streamlit Cloud](https://share.streamlit.io/)** and sign in with GitHub.
2. Click **New App** → Select your GitHub repository.
3. Choose the **main** branch and enter:
   ```
   fetch_data.py
   ```
   in the **Main file path** field.
4. Click **Deploy** 🚀
5. Once deployed, Streamlit will generate a **public link** like:
   ```
   https://yourappname.streamlit.app/
   ```
   Share this link so others can access your dashboard without running code.

---

## 📊 How to Use

### **1️⃣ Enter User ID and Quiz ID**
- The sidebar allows input for **User ID** and **Quiz ID**.
- If a **valid User ID and Quiz ID** are provided, performance metrics are displayed.

### **2️⃣ View Performance Metrics**
- **Score Trends**: Line chart showing score improvement over time.
- **Accuracy Trends**: Bar chart displaying accuracy across quizzes.
- **Summary Table**: Detailed quiz statistics.

### **3️⃣ Get Personalized Recommendations**
- **Quiz-Level Insights**: Highlights **weak topics** and improvement areas.
- **Student Persona**: Categorizes users into **High Performer, Improving, Needs Improvement, or Struggling**.
- **NEET Rank Prediction**: Estimates a probable **rank range** based on accuracy.

## 📌 To-Do / Future Enhancements
- Add **AI-driven recommendations** for question types and difficulty levels.
- Enhance **NEET rank prediction** with **historical student data trends**.
- Implement a **backend API** for real-time data updates.

---

## 💡 Contributing
Pull requests are welcome! If you’d like to enhance the project, submit an issue or PR on **GitHub**.

---

## 🏆 Credits
Developed by **Vyshnavi** as part of the **NEET Testline Student Recommendation System** project.

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify as needed.
