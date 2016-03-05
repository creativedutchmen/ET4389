import pandas as pd


def datafile_to_dataframe(datafile):
    data = []
    with open(datafile) as f:
        for line in f:
            first = line.split(" ").pop(0)
            last = line.split(" ").pop().strip()
            data.append([first, last])
    df = pd.DataFrame(data, columns=['node_1', 'node_2'])
    return df


def concatenate_nodes(df):
    return pd.concat([df['node_1'], df['node_2']])


def count_nodes(df):
    return concatenate_nodes(df).nunique()


def count_edges(df):
    return df['node_1'].count()


def average_degree(df):
    return 2 * count_edges(df) / count_nodes(df)


def link_density(df):
    num_nodes = count_nodes(df)
    potential_links = num_nodes * (num_nodes - 1)
    return count_edges(df) / potential_links


if __name__ == "__main__":
    file = 'dataset.txt'
    df = datafile_to_dataframe(file)

    print(count_edges(df))
    print(count_nodes(df))
    print(average_degree(df))
    print("%2.2f%%" % (link_density(df) * 100))
