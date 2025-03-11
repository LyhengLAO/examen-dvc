import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess():

    df = pd.read_csv('./data/raw/raw.csv')
    print(f"on a {df.isna().sum().sum()} valeur manquant et {df.duplicated().sum().sum()} valeur duplicate")

    X = df.drop(['silica_concentrate','date'],axis = 1)
    y = df['silica_concentrate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

    X_train.to_csv("data/processed_data/X_train.csv", index=False)
    X_test.to_csv("data/processed_data/X_test.csv", index=False)
    y_train.to_csv("data/processed_data/y_train.csv", index=False)
    y_test.to_csv("data/processed_data/y_test.csv", index=False)

    print('split ok')

    sc = StandardScaler()

    X_train_scaled = pd.DataFrame(sc.fit_transform(X_train))
    X_test_sclaed = pd.DataFrame(sc.transform(X_test))

    X_train_scaled.to_csv("data/processed_data/X_train_scaled.csv", index=False)
    X_test_sclaed.to_csv("data/processed_data/X_test_scaled.csv", index=False)

    print('normalize ok')
    

if __name__ == '__main__':
    preprocess()