import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Read csv and store in dataframe df
df = pd.read_csv("femte_trinn_begge_kjonn_2020_2021.csv")


# Set some seaborn estethic variables
sns.set_theme(style="ticks", color_codes=True)
sns.set_style("darkgrid")
sns.set_context("paper")
sns.set_palette("PiYG")
