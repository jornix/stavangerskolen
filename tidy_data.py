import pandas as pd

df = pd.read_csv("nedlasting.csv", delimiter=";")

# Drop unnecessary columns
df = df.drop(
    ["Skoletype", "Vurderingsområde", "Eierform", "Måleenhet"], axis=1
).reset_index(drop=True)
# Tidy column names
df = df.rename(
    columns={
        "Enhetsnavn": "enhetsnavn",
        "Statistikk": "statistikk",
        "Indikator/delskår": "indikator_delskar",
        "Periode": "periode",
        "Trinn": "trinn",
        "Kjønn": "kjonn",
        "Verdi": "verdi",
    }
)
# Replace missing values
df = df.replace(".", "")

# Single out sex
gutter = df[df["kjonn"] == "Gutter"].reset_index(drop=True)
jenter = df[df["kjonn"] == "Jenter"].reset_index(drop=True)
begge_kjonn = df[df["kjonn"] == "Begge kjønn"].reset_index(drop=True)

b_trinn_5 = begge_kjonn[
    (begge_kjonn["trinn"] == "Trinn 5") & (begge_kjonn["verdi"] != "")
].reset_index(drop=True)
b_trinn_5_gutter = gutter[
    (gutter["trinn"] == "Trinn 5") & (gutter["verdi"] != "")
].reset_index(drop=True)
b_trinn_5_jenter = jenter[
    (jenter["trinn"] == "Trinn 5") & (jenter["verdi"] != "")
].reset_index(drop=True)


u_trinn_8 = begge_kjonn[
    (begge_kjonn["trinn"] == "Trinn 8")
    & (begge_kjonn["verdi"] != "")
    & (begge_kjonn["indikator_delskar"] != "Engelsk avgiverskole (Kun skolenivå)")
    & (begge_kjonn["indikator_delskar"] != "Lesing avgiverskole (Kun skolenivå)")
    & (begge_kjonn["indikator_delskar"] != "Regning avgiverskole (Kun skolenivå)")
].reset_index(drop=True)
u_trinn_8_gutter = gutter[
    (gutter["trinn"] == "Trinn 8")
    & (gutter["verdi"] != "")
    & (gutter["indikator_delskar"] != "Engelsk avgiverskole (Kun skolenivå)")
    & (gutter["indikator_delskar"] != "Lesing avgiverskole (Kun skolenivå)")
    & (gutter["indikator_delskar"] != "Regning avgiverskole (Kun skolenivå)")
].reset_index(drop=True)
u_trinn_8_jenter = jenter[
    (jenter["trinn"] == "Trinn 8")
    & (jenter["verdi"] != "")
    & (jenter["indikator_delskar"] != "Engelsk avgiverskole (Kun skolenivå)")
    & (jenter["indikator_delskar"] != "Lesing avgiverskole (Kun skolenivå)")
    & (jenter["indikator_delskar"] != "Regning avgiverskole (Kun skolenivå)")
].reset_index(drop=True)

u_trinn_9 = begge_kjonn[
    (begge_kjonn["trinn"] == "Trinn 9") & (begge_kjonn["verdi"] != "")
].reset_index(drop=True)
u_trinn_9_gutter = gutter[
    (gutter["trinn"] == "Trinn 9") & (gutter["verdi"] != "")
].reset_index(drop=True)
u_trinn_9_jenter = jenter[
    (jenter["trinn"] == "Trinn 9") & (jenter["verdi"] != "")
].reset_index(drop=True)

u_trinn_8.head()
u_trinn_8_gutter.head()
u_trinn_8_jenter.head()

# Write modified dataframe to file
df.to_csv("results.csv", index=False)
gutter.to_csv("gutter.csv", index=False)
jenter.to_csv("jenter.csv", index=False)
begge_kjonn.to_csv("begge_kjonn.csv", index=False)
b_trinn_5.to_csv("begge_kjonn_5.csv", index=False)
b_trinn_5_gutter.to_csv("gutter_5.csv", index=False)
b_trinn_5_jenter.to_csv("jenter_5.csv", index=False)
u_trinn_8.to_csv("begge_kjonn_8.csv", index=False)
u_trinn_8_gutter.to_csv("gutter_8.csv", index=False)
u_trinn_8_jenter.to_csv("jenter_8.csv", index=False)
u_trinn_9.to_csv("begge_kjonn_9.csv", index=False)
u_trinn_9_gutter.to_csv("gutter_9.csv", index=False)
u_trinn_9_jenter.to_csv("jenter_9.csv", index=False)
