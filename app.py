import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Music Recommender", page_icon="🎵", layout="wide")

# ---------------- CUSTOM BACKGROUND + COLORS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* Select a song label color */
    label {
        color: #ffffff !important;
        font-weight: 600;
        font-size: 16px;
    }

    /* Button color */
    div.stButton > button {
        background-color: #ffffff;
        color: #000000;
        font-weight: 700;
        border-radius: 8px;
        padding: 6px 16px;
    }

    /* Song card */
    .card {
        background: linear-gradient(135deg, #020024, #090979, #020024);
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        color: white;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.6);
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset.csv")

    # Rename columns to simple names
    df = df.rename(columns={
        "Song-Name": "song",
        "Singer/Artists": "artist"
    })

    df = df[["song", "artist"]].dropna()
    return df

df = load_data()

# ---------------- ML MODEL ----------------
tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["song"] + " " + df["artist"])
similarity = cosine_similarity(X)

def recommend(song_name, n=5):
    idx = df[df["song"] == song_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:n+1]
    return df.iloc[[i[0] for i in scores]]

# ---------------- UI ----------------
st.title("🎵 Music Recommender System")
st.caption("ML-based recommendations using TF-IDF + Cosine Similarity")

song = st.selectbox("🎧 Select a song", df["song"].values)

if st.button("Show Recommendation"):
    recs = recommend(song)

    cols = st.columns(5)
    for col, (_, row) in zip(cols, recs.iterrows()):
        with col:
            st.markdown(
                f"""
                <div class="card">
                    {row['song']}<br><br>
                    <span style="font-size:14px; font-weight:400;">
                        {row['artist']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
