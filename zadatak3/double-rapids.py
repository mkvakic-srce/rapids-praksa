# podignuti cudf knjižnicu
import cudf

# pomnozi listu brojeva s dva
def double(x):
    return x*2

if __name__ == '__main__':

    # stvori cudf Dataframe i napravi stupac brojeva
    n = 10**8
    df = cudf.DataFrame(list(range(0, n)))

    # stvori stupac udvostrucenih brojeva
    # incols - A list of names of input columns that match the function arguments
    # outcols - A dictionary of output column names and their dtype.
    dcudf = df.apply_rows(double, incols=[df], outcols=dict(o1=np.int32))

    # isprintaj prvih deset brojeva u DataFrameu
    print(dcudf[:10]) # cudf varijanta
