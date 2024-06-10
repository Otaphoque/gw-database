import pandas as pd
import json

df = pd.read_csv('/Users/constance/VisualStudioCode/CTF/Geekweek/Borealis1.csv')

df["stonewall_decision"] = ""
df["stonewall_reason"] = ""

df["neustar_proxy_anonymizer_status"] = ""
df["neustar_proxy_type"] = ""
df["neustar_proxy_level"] = ""
df["neustar_proxy_last_detected"] = ""
df["neustar_vpn_service"] = ""
df["neustar_hosting_facility"] = ""

df["virustotal_malicious"] = ""
df["virustotal_undetected"] = ""
df["virustotal_suspicious"] = ""
df["virustotal_harmless"] = ""
df["virustotal_timeout"] = ""

df["porcupince"] = ""

for index, row in df.iterrows():
# for index in range(0,10) :
    borealis = json.loads(df['Borealis'].iloc[index])

    df.at[index, "stonewall_decision"] = borealis["modules"]["STONEWALL"]["decision"]
    df.at[index, "stonewall_reason"] = borealis["modules"]["STONEWALL"]["reason"]
    df.at[index, "neustar_proxy_anonymizer_status"] = borealis["modules"]["NEUSTAR"][0]["proxy"]["anonymizer_status"]
    df.at[index, "neustar_proxy_type"] = borealis["modules"]["NEUSTAR"][0]["proxy"]["proxy_type"]
    df.at[index, "neustar_proxy_level"] = borealis["modules"]["NEUSTAR"][0]["proxy"]["proxy_level"]
    df.at[index, "neustar_proxy_last_detected"] = borealis["modules"]["NEUSTAR"][0]["proxy"].get("proxy_last_detected", "NA")
    df.at[index, "neustar_vpn_service"] = borealis["modules"]["NEUSTAR"][0]["proxy"]["vpn_service"]
    df.at[index, "neustar_hosting_facility"] = borealis["modules"]["NEUSTAR"][0]["proxy"]["hosting_facility"]
    df.at[index, "virustotal_malicious"] = borealis["modules"]["VIRUSTOTAL"]["avResults"]["malicious"]
    df.at[index, "virustotal_undetected"] = borealis["modules"]["VIRUSTOTAL"]["avResults"]["undetected"]
    df.at[index, "virustotal_suspicious"] = borealis["modules"]["VIRUSTOTAL"]["avResults"]["suspicious"]
    df.at[index, "virustotal_harmless"] = borealis["modules"]["VIRUSTOTAL"]["avResults"]["harmless"]
    df.at[index, "virustotal_timeout"] = borealis["modules"]["VIRUSTOTAL"]["avResults"]["timeout"]
    df.at[index, "porcupince"] = borealis["modules"]["PORCUPINE"]

print(df)

df.to_csv("constance.csv")