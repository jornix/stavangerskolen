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

# Save tables to excel file
begge_kjonn_9 = pd.read_csv("begge_kjonn_9.csv")
gutter_9 = pd.read_csv("gutter_9.csv")
jenter_9 = pd.read_csv("jenter_9.csv")
jenter_gutter_9 = pd.concat([gutter_9, jenter_9]).reset_index(drop=True)
jenter_gutter_9

income_sheets = {
    "5. trinn, begge kjønn": begge_kjonn_5,
    "5. trinn, gutter og jenter": jenter_gutter_5,
    "8. trinn, begge kjønn": begge_kjonn_8,
    "8. trinn, gutter og jenter": jenter_gutter_8,
    "9. trinn, begge kjønn": begge_kjonn_9,
    "9. trinn, gutter og jenter": jenter_gutter_9,
}
writer = pd.ExcelWriter("./tabeller.xlsx", engine="xlsxwriter")

for sheet_name in income_sheets.keys():
    income_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
writer.save()

# Set some seaborn estethic variables
sns.set_theme(style="ticks", color_codes=True)
sns.set_style("darkgrid")
sns.set_context("paper")
sns.set_palette("PiYG", 2)

# Plot it
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Nasjonale prøver 5. trinn, 2014-2020")
sns.violinplot(ax=axes[0], data=begge_kjonn_5, x="verdi", y="indikator_delskar")
axes[0].set_title("Alle")
axes[0].set_xlabel("Verdi")
axes[0].set_ylabel("")
sns.violinplot(
    ax=axes[1],
    data=jenter_gutter_5,
    x="verdi",
    y="indikator_delskar",
    hue="kjonn",
    split=True,
    inner="quart",
    linewidth=1,
)
axes[1].set_title("Gutter og jenter")
axes[1].set_xlabel("Verdi")
axes[1].set_ylabel("")
axes[1].legend().texts[0].set_text("Gutter")
plt.tight_layout()
plt.savefig("plots/5_trinn_resultater_fordeling_etter_kjønn.png")
plt.show()

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Nasjonale prøver 8. trinn, 2014-2020")
sns.violinplot(ax=axes[0], data=begge_kjonn_8, x="verdi", y="indikator_delskar")
axes[0].set_title("Alle")
axes[0].set_xlabel("Verdi")
axes[0].set_ylabel("")
sns.violinplot(
    ax=axes[1],
    data=jenter_gutter_8,
    x="verdi",
    y="indikator_delskar",
    hue="kjonn",
    split=True,
    inner="quart",
    linewidth=1,
)
axes[1].set_title("Gutter og jenter")
axes[1].set_xlabel("Verdi")
axes[1].set_ylabel("")
axes[1].legend().texts[0].set_text("Gutter")
plt.tight_layout()
plt.savefig("plots/8_trinn_resultater_fordeling_etter_kjønn.png")
plt.show()

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Nasjonale prøver 9. trinn, 2014-2020")
sns.violinplot(ax=axes[0], data=begge_kjonn_9, x="verdi", y="indikator_delskar")
axes[0].set_title("Alle")
axes[0].set_xlabel("Verdi")
axes[0].set_ylabel("")
sns.violinplot(
    ax=axes[1],
    data=jenter_gutter_9,
    x="verdi",
    y="indikator_delskar",
    hue="kjonn",
    split=True,
    inner="quart",
    linewidth=1,
)
axes[1].set_title("Gutter og jenter")
axes[1].set_xlabel("Verdi")
axes[1].set_ylabel("")
axes[1].legend().texts[0].set_text("Gutter")
plt.tight_layout()
plt.savefig("plots/9_trinn_resultater_fordeling_etter_kjønn.png")
plt.show()
