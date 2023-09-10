import streamlit as st
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

def generate_recommendations(query, data, model, num_recommendations=10):
    embeddings = model.encode(data) 
    query_embedding = model.encode([query])  
    similarities = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    sorted_indices = similarities.argsort(descending=True)
    recommendations = [data[i] for i in sorted_indices[:num_recommendations]]
    return recommendations

def get_google_scholar_titles(query):
    url = f"https://scholar.google.com/scholar?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = []

    for result in soup.find_all("h3", class_="gs_rt"):
        title = result.get_text()
        link = result.find("a")["href"]
        articles.append((title, link))

    return articles

st.sidebar.write("Owner of this app: EMNA BAHRI, 2023")
input_type = st.sidebar.selectbox("Select input type:", ["Abstract", "Keywords", "Title"])
num_of_recommendations = st.sidebar.number_input("Number of Recommendations", min_value=1, max_value=50, value=10)

if st.sidebar.button("Recommend"):
    pass

st.title("Scientific Paper Recommendation System")
user_input = st.text_area(f"Enter the {input_type.lower()} of the paper")

if st.button("Get Recommendations"):
    google_scholar_titles_and_links = get_google_scholar_titles(user_input)  # Extrait les titres et les liens d'articles de Google Scholar
    recommendations = generate_recommendations(user_input, [title for title, _ in google_scholar_titles_and_links], model, num_recommendations=num_of_recommendations)
    if len(recommendations) == 0:
        st.write("Oops! We couldn't find any recommendations for you. Try different input!")
        st.image("https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif")
    else:
        st.write("Recommended Papers:")
        for i, rec in enumerate(recommendations):
            st.write(f"**{i+1}. Title:** {rec}")
            st.write("---------------")
            
google_scholar_titles_and_links = get_google_scholar_titles(user_input)

st.title("Google Scholar Article Source")
for i, (title, link) in enumerate(google_scholar_titles_and_links, start=1):
    st.subheader(f"Article {i}:")
    st.write("Title:", title)
    st.write("Link:", link)
    st.write("=" * 30)

st.write("Thank you for exploring our app! Feel free to come back whenever you're ready to dive into the world of scientific discoveries again!")