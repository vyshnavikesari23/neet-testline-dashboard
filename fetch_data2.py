import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Load Data
@st.cache_data
def load_data():
    with open(r"C:\Users\VYSHNAVI\desktop\APIEndpoint.json", "r") as file:
        api_data = json.load(file)
    with open(r"C:\Users\VYSHNAVI\desktop\QuizEndpoint.json", "r") as file:
        quiz_data = json.load(file)
    with open(r"C:\Users\VYSHNAVI\desktop\QuizSubmissionData.json", "r") as file:
        submission_data = json.load(file)
    return api_data, quiz_data, submission_data

api_data, quiz_data, submission_data = load_data()

# Convert API Data to DataFrame
df_api = pd.DataFrame(api_data)

# Ensure correct data types
df_api['user_id'] = df_api['user_id'].astype(str).str.strip()
df_api['accuracy'] = df_api['accuracy'].str.replace('%', '').astype(float)
df_api['final_score'] = df_api['final_score'].astype(float)
df_api['negative_score'] = df_api['negative_score'].astype(float)

df_api['date'] = pd.to_datetime(df_api['submitted_at']).dt.date
df_api = df_api[['date', 'score', 'accuracy', 'negative_score', 'final_score', 'correct_answers', 'incorrect_answers', 'quiz', 'user_id', 'quiz_id']]

# Extract quiz topics safely
df_api['topic'] = df_api['quiz'].apply(lambda x: x.get('topic', '') if isinstance(x, dict) else '')
df_api.drop(columns=['quiz'], inplace=True)

# Streamlit UI
st.title("📊 Student Performance Dashboard")

# Sidebar Filters
selected_user = st.sidebar.text_input("Enter User ID").strip()
selected_quiz_id = st.sidebar.text_input("Enter Quiz ID").strip()

# Display available User IDs and Quiz IDs in the sidebar
st.sidebar.subheader("Available User IDs")
st.sidebar.write(df_api['user_id'].unique())

st.sidebar.subheader("Available Quiz IDs")
st.sidebar.write(df_api['quiz_id'].unique())

# Validate User ID and Quiz ID
user_ids = df_api['user_id'].astype(str).str.strip().unique()
quiz_ids = df_api['quiz_id'].astype(str).str.strip().unique()

if selected_user and selected_user not in user_ids:
    st.error("User ID not found in the data. Please enter a valid User ID.")
    st.stop()

if selected_quiz_id and selected_quiz_id not in quiz_ids:
    st.error("Quiz ID not found in the data. Please enter a valid Quiz ID.")
    st.stop()

# Filter Data Based on User ID and Quiz ID
user_df = df_api[(df_api['user_id'] == selected_user) & (df_api['quiz_id'].astype(str) == selected_quiz_id)]

# Line Chart: Score Trends
graph = px.line(user_df, x='date', y='score', title=f'Score Trend for User {selected_user} in Quiz {selected_quiz_id}')
st.plotly_chart(graph)

# Bar Chart: Accuracy Comparison
bar_chart = px.bar(user_df, x='date', y='accuracy', title=f'Accuracy Over Time for User {selected_user} in Quiz {selected_quiz_id}')
st.plotly_chart(bar_chart)

# Summary Metrics
st.subheader("Performance Summary")
st.write(user_df[['date', 'score', 'accuracy', 'negative_score', 'final_score', 'correct_answers', 'incorrect_answers']])

# Generate Student Persona
def determine_student_persona(user_df):
    avg_accuracy = user_df['accuracy'].mean()
    if avg_accuracy > 90:
        return "🌟 High Performer: Consistently scoring well. Keep up the good work!"
    elif avg_accuracy > 70:
        return "📈 Improving Performer: Showing progress, focus on weak areas."
    elif avg_accuracy > 50:
        return "⚠️ Needs Improvement: Accuracy is moderate, practice more."
    else:
        return "❗ Struggling Student: Needs serious improvement and targeted practice."

st.subheader("🎭 Student Persona Analysis")
st.write(determine_student_persona(user_df))

# NEET Rank Prediction Model
def predict_neet_rank(user_df):
    avg_accuracy = user_df['accuracy'].mean()
    if avg_accuracy > 85:
        return "🏆 Estimated NEET Rank: Top 1000"
    elif avg_accuracy > 70:
        return "🥈 Estimated NEET Rank: 1000 - 5000"
    elif avg_accuracy > 50:
        return "🥉 Estimated NEET Rank: 5000 - 15000"
    else:
        return "📉 Estimated NEET Rank: Above 15000 (Needs Improvement)"

st.subheader("📊 NEET Rank Prediction")
st.write(predict_neet_rank(user_df))

# Generate Quiz-Level Personalized Recommendations
def generate_quiz_recommendations(user_df):
    avg_accuracy = user_df['accuracy'].mean()
    weak_topics = user_df[user_df['accuracy'] < 80]['topic'].unique()
    
    recommendations = []
    if avg_accuracy < 80:
        recommendations.append("Your accuracy in this quiz is low. Focus on reviewing mistakes.")
    if len(weak_topics) > 0:
        recommendations.append(f"Focus on improving these weak topics: {', '.join(weak_topics)}")
    
    if not recommendations:
        return "Great job! Maintain your accuracy for this quiz."
    return "\n".join(recommendations)

st.subheader("📌 Quiz-Level Personalized Recommendations")
st.write(generate_quiz_recommendations(user_df))

st.sidebar.write("👨‍💻 Developed with Streamlit & Plotly")
