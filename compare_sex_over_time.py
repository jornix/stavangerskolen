import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

begge_kjonn_5 = pd.read_csv("begge_kjonn_5.csv")
gutter_5 = pd.read_csv("gutter_5.csv")
jenter_5 = pd.read_csv("jenter_5.csv")
jenter_gutter_5 = pd.concat([gutter_5, jenter_5]).reset_index(drop=True)

begge_kjonn_8 = pd.read_csv("begge_kjonn_8.csv")
gutter_8 = pd.read_csv("gutter_8.csv")
jenter_8 = pd.read_csv("jenter_8.csv")
jenter_gutter_8 = pd.concat([gutter_8, jenter_8]).reset_index(drop=True)

# Save tables to excel file, for the heck of it
begge_kjonn_9 = pd.read_csv("begge_kjonn_9.csv")
gutter_9 = pd.read_csv("gutter_9.csv")
jenter_9 = pd.read_csv("jenter_9.csv")
jenter_gutter_9 = pd.concat([gutter_9, jenter_9]).reset_index(drop=True)

# Set some seaborn estethic variables
sns.set_theme(style="ticks", color_codes=True)
sns.set_style("darkgrid")
sns.set_context("paper")
sns.set_palette("Dark2", 3)

fig, axes = plt.subplots(3, 1, figsize=(10, 10))
fig.suptitle("Nasjonale prøver 5. trinn, 2014-2020")
sns.lineplot(ax=axes[0],data=begge_kjonn_5, x="periode", y="verdi", hue="indikator_delskar", legend="brief")
axes[0].set_title("Begge kjønn")
sns.lineplot(ax=axes[1],data=gutter_5, x="periode", y="verdi", hue="indikator_delskar")
axes[1].set_title("Gutter")
sns.lineplot(ax=axes[2],data=jenter_5, x="periode", y="verdi", hue="indikator_delskar")
axes[2].set_title("Jenter")
for i in range(3):
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Poeng")
    axes[i].legend().texts[0].set_text("Engelsk")
plt.tight_layout()
plt.savefig('plots/5_trinn_2014_2020.png')
plt.show()

fig, axes = plt.subplots(3, 1, figsize=(10, 10))
fig.suptitle("Nasjonale prøver 8. trinn, 2014-2020")
sns.lineplot(ax=axes[0],data=begge_kjonn_8, x="periode", y="verdi", hue="indikator_delskar", legend="brief")
axes[0].set_title("Begge kjønn")
sns.lineplot(ax=axes[1],data=gutter_8, x="periode", y="verdi", hue="indikator_delskar")
axes[1].set_title("Gutter")
sns.lineplot(ax=axes[2],data=jenter_8, x="periode", y="verdi", hue="indikator_delskar")
axes[2].set_title("Jenter")
for i in range(3):
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Poeng")
    axes[i].legend().texts[0].set_text("Engelsk")
plt.tight_layout()
plt.savefig('plots/8_trinn_2014_2020.png')
plt.show()

fig, axes = plt.subplots(3, 1, figsize=(10, 10))
fig.suptitle("Nasjonale prøver 9. trinn, 2014-2020")
sns.lineplot(ax=axes[0],data=begge_kjonn_9, x="periode", y="verdi", hue="indikator_delskar", legend="brief")
axes[0].set_title("Begge kjønn")
sns.lineplot(ax=axes[1],data=gutter_9, x="periode", y="verdi", hue="indikator_delskar")
axes[1].set_title("Gutter")
sns.lineplot(ax=axes[2],data=jenter_9, x="periode", y="verdi", hue="indikator_delskar")
axes[2].set_title("Jenter")
for i in range(3):
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Poeng")
    axes[i].legend().texts[0].set_text("Engelsk")
plt.tight_layout()
plt.savefig('plots/9_trinn_2014_2020.png')
plt.show()
