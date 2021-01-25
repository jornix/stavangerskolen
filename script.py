import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Read csv and store in dataframe df
df = pd.read_csv("results.csv")
df.drop(["index"], axis=1).reset_index(drop=True)


# Separate fifth grade tests
femte_trinn = df[
    (df["statistikk"] == "Nasjonale prøver 5. trinn") & (pd.isna(df["verdi"]) == False)
].reset_index(drop=True)

# Separate the different tests for fifth grade (engelsk, lesing, regning)
femte_trinn_engelsk = femte_trinn[
    (femte_trinn["indikator_delskar"] == "Engelsk")
    & (femte_trinn["kjonn"] == "Begge kjønn")
].reset_index(drop=True)
femte_trinn_lesing = femte_trinn[
    (femte_trinn["indikator_delskar"] == "Lesing")
    & (femte_trinn["kjonn"] == "Begge kjønn")
].reset_index(drop=True)
femte_trinn_regning = femte_trinn[
    (femte_trinn["indikator_delskar"] == "Regning")
    & (femte_trinn["kjonn"] == "Begge kjønn")
].reset_index(drop=True)

# Set some seaborn estethic variables
sns.set_theme(style="ticks", color_codes=True)
sns.set_style("darkgrid")
sns.set_context("paper")
sns.set_palette("PiYG")

# calculate and print boxplots to files
fig, axes = plt.subplots(figsize=(10, 15))
fig.suptitle("Nasjonale prøver 5. trinn, spredning i resultater")
sns.boxplot(data=femte_trinn_engelsk, x="verdi", y="enhetsnavn", palette="RdYlBu")
sns.stripplot(
    data=femte_trinn_engelsk,
    x="verdi",
    y="enhetsnavn",
    palette="PRGn",
    hue="periode",
)
axes.set_title("Engelsk")
plt.savefig("plots/boxplot_femte_trinn_engelsk.png")

fig, axes = plt.subplots(figsize=(10, 15))
fig.suptitle("Nasjonale prøver 5. trinn, spredning i resultater")
sns.boxplot(data=femte_trinn_lesing, x="verdi", y="enhetsnavn", palette="RdYlBu")
sns.stripplot(
    data=femte_trinn_lesing,
    x="verdi",
    y="enhetsnavn",
    palette="PRGn",
    hue="periode",
)
axes.set_title("Lesing")
plt.savefig("plots/boxplot_femte_trinn_lesing.png")

fig, axes = plt.subplots(figsize=(10, 15))
fig.suptitle("Nasjonale prøver 5. trinn, spredning i resultater")
sns.boxplot(data=femte_trinn_regning, x="verdi", y="enhetsnavn", palette="RdYlBu")
sns.stripplot(
    data=femte_trinn_regning,
    x="verdi",
    y="enhetsnavn",
    palette="PRGn",
    hue="periode",
)
axes.set_title("Regning")
plt.savefig("plots/boxplot_femte_trinn_regning.png")
# sns.despine(offset=10, trim=True)


plt.show()
