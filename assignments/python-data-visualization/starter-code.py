import pandas as pd


def main():
    # load data
    df = pd.read_csv('dataset.csv')
    print(df.head())
    print(df.describe())

    # TODO: create a plot using matplotlib or plotly
    # Example using matplotlib:
    # import matplotlib.pyplot as plt
    # plt.plot(df['x'], df['y'])
    # plt.title('Sample Data')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.show()


if __name__ == '__main__':
    main()
