import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    data = pd.read_csv('unprocessed_data/csgo_round_snapshots.csv')

    train, test = train_test_split(data, test_size=0.15)

    train.to_csv('data/csgo_round_train.csv', index=False)
    test.to_csv('data/csgo_round_test.csv', index=False)


if __name__ == '__main__':
    main()
