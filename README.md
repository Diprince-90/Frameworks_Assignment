# Frameworks_Assignment
📊 CORD-19 Data Explorer
A Streamlit-powered web application for exploring COVID-19 research metadata from the CORD-19 dataset. This project walks through the full data science workflow—from loading and cleaning data to analysis, visualization, and interactive presentation.

🚀 Features
- Load and clean the metadata.csv file from the CORD-19 dataset
- Explore publication trends by year, journal, and source
- Generate visualizations including bar charts and word clouds
- Filter data interactively by year range and journal
- Display sample data and summary statistics
- Built entirely with Python, Pandas, Matplotlib, and Streamlit

📁 Dataset
This app uses the metadata.csv file from the CORD-19 Research Challenge. Please download and place the file in the root directory of this project.

🛠️ Installation
- Clone this repository or download the script.
- Install required packages:
pip install pandas matplotlib wordcloud streamlit
- Place metadata.csv in the same folder as the script.

▶️ Running the App
Launch the Streamlit app from your terminal:
streamlit run app.py


Then open the provided local URL in your browser to interact with the app.

📊 Visualizations
- Publications Over Time: Bar chart showing number of papers per year
- Top Journals: Bar chart of the most prolific journals
- Word Cloud: Most frequent words in paper titles
- Source Distribution: Bar chart of top data sources

📌 Project Structure
- app.py: Main Streamlit application
- metadata.csv: Dataset file (not included—download separately)
- README.md: Project documentation

🧠 Learning Outcomes
By completing this project, you’ll gain experience in:
- Data loading and cleaning with Pandas
- Exploratory data analysis (EDA)
- Visualization with Matplotlib and WordCloud
- Building interactive apps with Streamlit
- Documenting and presenting data science work

📝 License
This project is for educational purposes and is not affiliated with the Allen Institute for AI or Kaggle.

