import pandas as pd
from extraction import y_bound_cal


filename_root_solution = "csv/websolutions$@b.csv"
filename_root_test = "csv/test20$@b.csv"
year_bound = y_bound_cal(20, 23)
print(year_bound)
for i in year_bound:
    solution_filename = filename_root_solution.replace('$@', str(i))
    test_filename = filename_root_test.replace('$@', str(i))
    solution_df = pd.read_csv(solution_filename)
    test_df = pd.read_csv(test_filename)
    for index, row in solution_df.iterrows():
        print(index)
        print(solution_df.loc[index, 'solution'])
        print(test_df.loc[index, 'test'])

