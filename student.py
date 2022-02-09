import pandas as pd
import plotly.express as px

file1 = pd.read_csv("data.csv")
fig = px.scatter(file1, x="student_id", y="level")
fig.show()