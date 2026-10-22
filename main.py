import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("matches.csv")

wins = df[df["Result"] == "W"]
draws = df[df["Result"] == "D"]
losses = df[df["Result"] == "L"]

total_matches = len(df)
total_wins = len(wins)
total_losses = len(losses)
total_draws = len(draws)

win_percentage = (total_wins / total_matches) * 100

loss_percentage = (total_losses / total_matches) * 100

draw_percentage = (total_draws / total_matches) * 100


labels = ["Wins", "Draws", "Losses"]
colors = ["c", "y", "b"]

percentage = [
    win_percentage,
    draw_percentage,
    loss_percentage
]

plt.pie(percentage, labels=labels, autopct="%1.1f%%", startangle=90, shadow=True, colors=colors)
plt.title("Real Madrid match results")

plt.show()