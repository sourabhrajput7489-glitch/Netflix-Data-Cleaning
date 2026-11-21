
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Netflix Data Dashboard",
    layout="wide"
)

# Load cleaned dataset
df = pd.read_csv("data/Cleaned_Netflix.csv")

st.title("Netflix Data Analytics Dashboard")
st.write("Netflix Data Cleaning & Preparation - Task 1")

# Sidebar filter
st.sidebar.header("Filters")

content_type = st.sidebar.selectbox(
    "Select Content Type",
    ["All"] + df["type"].dropna().unique().tolist()
)

if content_type != "All":
    df = df[df["type"] == content_type]

# KPI Cards
total = len(df)
movies = (df["type"] == "Movie").sum()
tv_shows = (df["type"] == "TV Show").sum()

c1, c2, c3 = st.columns(3)

c1.metric("Total Titles", total)
c2.metric("Movies", movies)
c3.metric("TV Shows", tv_shows)

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head(20))

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")

type_count = df["type"].value_counts()

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(type_count.index, type_count.values)
ax.set_xlabel("Content Type")
ax.set_ylabel("Number of Titles")
ax.set_title("Netflix Content Distribution")

st.pyplot(fig)
plt.close(fig)

# Rating distribution
st.subheader("Rating Distribution")

rating_count = df["rating"].value_counts()

fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(rating_count.index, rating_count.values)
ax.set_xlabel("Rating")
ax.set_ylabel("Number of Titles")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)
plt.close(fig)

# Release year histogram
st.subheader("Release Year Distribution")

fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(df["release_year"].dropna(), bins=30)
ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")

st.pyplot(fig)
plt.close(fig)

# Download cleaned dataset
st.subheader("Download Cleaned Dataset")

csv = df.to_csv(index=False)

st.download_button(
    "Download CSV",
    data=csv,
    file_name="Netflix_Cleaned.csv",
    mime="text/csv"
)