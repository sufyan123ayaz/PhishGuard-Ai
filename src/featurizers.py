# src/featurizers.py
import pandas as pd
from .features import extra_security_features

def security_features_df(texts):
    rows = [extra_security_features(t) for t in texts]
    return pd.DataFrame(rows)
