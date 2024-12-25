import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path
import zipfile

# Setup paths
user_docs = Path.home() / 'Documents'
extract_path = user_docs / 'kaggle_analysis'
viz_path = extract_path / 'visualizations'
zip_path = Path(r'C:\Users\thoma\Downloads\archive (2).zip')

# Create directories
os.makedirs(extract_path, exist_ok=True)
os.makedirs(viz_path, exist_ok=True)

try:
    # Extract zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    
    # Load and analyze data
    file_path = extract_path / 'multipleChoiceResponses.csv'
    df = pd.read_csv(file_path, low_memory=False)
    
    # Generate plots
    plt.figure(figsize=(12, 6))
    df['Q3'].value_counts().head(10).plot(kind='bar')
    plt.title('Top 10 Countries of Respondents')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(viz_path / 'demographics.png')
    plt.close()
    
    print(f"\nAnalysis complete! Check {viz_path} for visualizations.")
except Exception as e:
    print(f"Error: {e}")