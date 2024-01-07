import streamlit as st
import pandas as pd

st.title('Basketball Stats Explorer')

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2023,2025))))

@st.cache_data # once data has been loaded (ex. from year 2024), then it will be cached so it wont have to be loaded again
def load_data(year):
    file_path = "Data/basketball" + str(year) + ".csv"
    df = pd.read_csv(file_path)
    return df
playerstats = load_data(selected_year)

# sidebar team selection
# how to use: multiselect(title, all values possible, default values to be displayed)
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect("Team", sorted_unique_team, sorted_unique_team)

# sidebar position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data into new df based on input selection
# selecting data: df[(condition 1) & (condition 2)]
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)



