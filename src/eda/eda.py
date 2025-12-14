import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main(csv_path=None, out_dir='reports'):
    if csv_path is None:
        csv_path = os.path.join(os.getcwd(), 'Heart_Disease_Prediction.csv')
    df = pd.read_csv(csv_path)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, 'eda_summary.txt'), 'w') as f:
        f.write('Shape: %s\n' % (df.shape,))
        f.write('\nColumns and dtypes:\n')
        f.write(str(df.dtypes))
        f.write('\n\nMissing values:\n')
        f.write(str(df.isnull().sum()))
        f.write('\n\nDescriptive statistics:\n')
        f.write(str(df.describe(include='all')))
        f.write('\n\nTarget distribution:\n')
        if 'Heart Disease' in df.columns:
            f.write(str(df['Heart Disease'].value_counts()))
        elif 'HeartDisease' in df.columns:
            f.write(str(df['HeartDisease'].value_counts()))

    # Correlation heatmap for numeric features
    num = df.select_dtypes(include=['number'])
    if not num.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(num.corr(), annot=True, fmt='.2f', cmap='coolwarm')
        plt.title('Correlation heatmap')
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, 'correlation_heatmap.png'))

    print('EDA complete — reports saved to', out_dir)


if __name__ == '__main__':
    main()
