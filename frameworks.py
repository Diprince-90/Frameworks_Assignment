# CORD-19 Data Explorer Streamlit App

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# App title and description
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("📊 CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata from the CORD-19 dataset.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna('')
    df['title'] = df['title'].fillna('')
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
year_range = st.sidebar.slider("Select publication year range", 2019, 2025, (2020, 2021))
selected_journals = st.sidebar.multiselect(
    "Select journals (optional)",
    options=df['journal'].dropna().unique(),
    default=[]
)

# Filter data
filtered_df = df[df['year'].between(year_range[0], year_range[1])]
if selected_journals:
    filtered_df = filtered_df[filtered_df['journal'].isin(selected_journals)]

# Show sample data
st.subheader("📄 Sample of Filtered Data")
st.dataframe(filtered_df[['title', 'journal', 'publish_time', 'abstract_word_count']].head(10))

# Publications by year
st.subheader("📅 Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values, color='skyblue')
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Publications")
ax1.set_title("Publications by Year")
st.pyplot(fig1)

# Top journals
st.subheader("🏛️ Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals.plot(kind='bar', ax=ax2, color='orange')
ax2.set_ylabel("Number of Papers")
ax2.set_title("Top Journals")
st.pyplot(fig2)

# Word cloud of titles
st.subheader("🧠 Word Cloud of Paper Titles")
title_words = ' '.join(filtered_df['title'].dropna()).lower()
tokens = re.findall(r'\b\w+\b', title_words)
common_words = Counter(tokens).most_common(100)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(common_words))
fig3, ax3 = plt.subplots()
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Source distribution
st.subheader("📚 Distribution by Source")
source_counts = filtered_df['source_x'].value_counts().head(10)
fig4, ax4 = plt.subplots()
source_counts.plot(kind='bar', ax=ax4, color='green')
ax4.set_ylabel("Number of Papers")
ax4.set_title("Top Sources")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("✅ **Tips:** Use the filters to explore trends by year or journal. Try adjusting the year range or selecting specific journals to see how the data changes.")