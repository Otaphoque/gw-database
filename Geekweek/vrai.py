import pandas as pd
import requests
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import signal
import sys

df = pd.read_csv('/Users/constance/VisualStudioCode/CTF/Geekweek/IPlistUnique.csv')
# df = pd.read_csv('/Users/constance/VisualStudioCode/CTF/Geekweek/unique1.csv')
df["Borealis"] = ""

BOREALIS_HOST = "https://ingestion.collaboration.cyber.gc.ca/borealis"
modules = "SPUR,NEUSTAR,DEVICE,PORCUPINE,VIRUSTOTAL,STONEWALL"
subscription_key = "57f42b675f36441da23cea8f90607280"

session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def process_row(row):
    try:
        request = row['clientIp']
        response = session.get(f"{BOREALIS_HOST}/process/{request}?modules={modules}&subscription-key={subscription_key}")
        return response.text
    except Exception as e:
        print(f"Error processing IP {row['clientIp']}: {e}")
        return None

def save_and_exit(signal, frame):
    print("Saving DataFrame and exiting...")
    df.to_csv('Borealis.csv', index=False)
    sys.exit(0)

signal.signal(signal.SIGINT, save_and_exit)

tqdm.pandas(desc="Processing IPs")

df['Borealis'] = df.iloc[35000:].progress_apply(process_row, axis=1)
# df['Borealis'] = df.progress_apply(process_row, axis=1)

df.to_csv('/Users/constance/Downloads/Borealis/Borealis20.csv', index=False)
print(df)
