import os
import pandas as pd
import urllib.request
from ..config import DATASET_URL, DATASET_PATH


def download_dataset():
    os.makedirs(os.path.dirname(DATASET_PATH), exist_ok=True)
    print(f"Downloading dataset from {DATASET_URL}...")
    urllib.request.urlretrieve(DATASET_URL, DATASET_PATH)
    print(f"Dataset saved to {DATASET_PATH}")


def load_dataset() -> pd.DataFrame:
    if not os.path.exists(DATASET_PATH):
        download_dataset()

    df = pd.read_csv(DATASET_PATH, sep="\t", header=None, names=["label", "message"])
    df["label"] = df["label"].map({"ham": "ham", "spam": "spam"})
    df = df.dropna().reset_index(drop=True)
    print(f"Loaded dataset: {len(df)} samples ({df['label'].value_counts().to_dict()})")
    return df
