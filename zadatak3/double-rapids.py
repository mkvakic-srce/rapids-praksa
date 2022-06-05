import cudf

# pomnozi listu brojeva s dva pomocu CUDAe
def double(numbers, doubled):
    for i, number in enumerate(numbers):
        doubled[i] = number*2

if __name__ == '__main__':

    # stvori cudf Dataframe i napravi stupac brojeva
    n = 10**8
    df = cudf.DataFrame()
    df['numbers'] = list(range(n))

    # stvori stupac udvostrucenih brojeva
    df = df.apply_rows(
        double,
        incols=['numbers'],
        outcols=dict(doubled=int),
        kwargs=dict(),
    )

    # isprintaj prvih deset brojeva
    print(df.iloc[:10])
