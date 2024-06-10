
import pandas as pd
import requests
from tqdm import tqdm

# Read the CSV file
df = pd.read_csv('/Users/constance/VisualStudioCode/CTF/Geekweek/IPlistUnique.csv')
df["Borealis"] = ""

subscription_key = "57f42b675f36441da23cea8f90607280"

# Define constants
BOREALIS_HOST = "https://ingestion.collaboration.cyber.gc.ca/borealis"
modules = "SPUR,NEUSTAR,DEVICE,PORCUPINE,VIRUSTOTAL,STONEWALL"

# Add a loading bar to the loop
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing IPs"):
    try:
        request = row['clientIp']
        response = requests.get("{}/process/{}?modules={}&subscription-key={}".format(BOREALIS_HOST, request, modules, subscription_key))
        df.at[index, 'Borealis'] = response.text
    except Exception as e:
        print(e)
        df.to_csv('Borealis.csv', index=False)

# Save the final dataframe to a CSV file
df.to_csv('Borealis.csv', index=False)

print(df)


# import pandas as pd
# import requests

# subscription_key = "57f42b675f36441da23cea8f90607280"

# df = pd.read_csv('/Users/constance/VisualStudioCode/CTF/Geekweek/IPlistUnique.csv')
# df["Borealis"] = ""

# BOREALIS_HOST = "https://ingestion.collaboration.cyber.gc.ca/borealis"
# modules = "SPUR,NEUSTAR,DEVICE,PORCUPINE,VIRUSTOTAL,STONEWALL"
# for index, row in df.iterrows():
#     try:
#         request = row['clientIp']
#         response = requests.get("{}/process/{}?modules={}&subscription-key={}".format(BOREALIS_HOST,request,modules,subscription_key))

#         df.at[index, 'Borealis'] = response.text
#         print(index)
#     except Exception as e:
#         print(e)
#         df.to_csv('Borealis.csv', index=False)

# print(df)
# df.to_csv('Borealis.csv', index=False)