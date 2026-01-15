import pandas as pd

def load_dataset(path: str, text_col="text", label_col="label"):
    df = pd.read_csv(path)
    df = df.dropna(subset=[text_col, label_col]).copy()
    df[text_col] = df[text_col].astype(str)
    df[label_col] = df[label_col].astype(int)
    return df[[text_col, label_col]]
