import streamlit as st
import joblib
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

from recommend import recommend_songs

st.set_page_config(page_title="🎵 Song Recommender", layout="wide")
st.title("🎵 Spotify Song Recommender")

st.write("Enter a song name to get personalized recommendations!")

song_name = st.text_input("Enter a song name:", placeholder="e.g., Shape of You")

top_n = st.slider("Number of recommendations:", min_value=1, max_value=20, value=10)

if st.button("Get Recommendations"):
    if song_name.strip():
        with st.spinner("Finding recommendations..."):
            recommendations = recommend_songs(song_name, top_n=top_n)
        
        if recommendations is not None:
            st.success(f"✅ Found {len(recommendations)} recommendations!")
            st.dataframe(
                recommendations,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.error(f"❌ Song '{song_name}' not found in database. Try another song!")
    else:
        st.warning("⚠️ Please enter a song name")