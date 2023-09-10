# Scientific Paper Recommendation System

![Scientific Papers](https://www.fondation-cdf.fr/wp-content/uploads/2021/01/Articles-scientifiques.jpg)
_Image source: [Fondation CDF](https://www.fondation-cdf.fr/2021/01/12/lenvolee-des-publications-scientifiques-en-temps-de-covid-19/)_

## Objectives

The Scientific Paper Recommendation System project aims to provide an pplication that suggests relevant scientific papers to users based on their input text, such as abstracts or keywords or titles. This system assists researchers in discovering pertinent research papers more efficiently.

## Advantages of Our App Compared to Google Scholar

Our app has distinct benefits:

1. **Personalized Suggestions:** We tailor recommendations to your specific criteria.

2. **More Relevant Results:** We consider title, keywords, and other factors to ensure papers align with your interests.

3. **Easy to Use:** Our user-friendly interface makes finding papers straightforward.

4. **Directly Aligned Recommendations:** Unlike Google Scholar's undisclosed algorithms, our system sorts articles based on your criteria. This saves time and provides more focused results.


## Guidelines

1. **Model Selection:** The project utilizes a pretrained model (model_name = "sentence-transformers/all-MiniLM-L6-v2") from Hugging Face, thanks to its advanced language understanding capabilities as the foundation for the recommendation system.

2. **Model Customization:** The pretrained model undergoes fine-tuning for adaptation to the specific recommendation criteria. This includes attributes such as title, keywords, laboratory name, institute name, and publication year. The customization enhances the relevance of the paper recommendations.

3. **Source of Recommendations:** The recommendations are generated from a selection of articles on Google Scholar. The system extracts article titles and links from Google Scholar.

4. **Streamlit Application:** The development of a Streamlit application (`streamlit_app.py`) provides users with the ability to input abstracts, keywords, titles, or other text and subsequently receive a list of recommended scientific papers. The application's interface offers interactivity and user-friendliness for seamless access to the recommendation system.

5. **Deployment with Hugging Face:** To enhance accessibility, the Streamlit application is deployed on Hugging Face's infrastructure. This deployment simplifies the usage of the recommendation system for researchers and individuals in search of pertinent scientific papers.


