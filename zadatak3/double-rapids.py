# podignuti cudf knjižnicu
import cudf
import numpy as np

def double(x, out):
    for i in range(len(x)):
        out[i] = x[i]*2
        
if __name__ == '__main__':

    # stvori cudf Dataframe i napravi stupac brojeva
    n = 10**8
    d = {'input' : list(range(0, n))}
    df = cudf.DataFrame(data=d)
    
    # stvori stupac udvostrucenih brojeva
    # incols - A list of names of input columns that match the function arguments
    # outcols - A dictionary of output column names and their dtype.
    dcudf = df.apply_rows(double, incols=['input'], outcols={'out' : np.int32}, kwargs={})

    # isprintaj prvih deset brojeva u DataFrameu
    print(dcudf[:10]) 
