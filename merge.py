import pandas as pd
from extraction import y_bound_cal


filename_root_solution = "csv/websolutions$@b.csv"
filename_root_test = "csv/test20$@b.csv"
year_bound = y_bound_cal(20, 23)
question_number = []
solutions = []
questions = []
all_merged = pd.DataFrame()
print(year_bound)
for i in year_bound:
    solution_filename = filename_root_solution.replace('$@', str(i))
    test_filename = filename_root_test.replace('$@', str(i))
    solution_df = pd.read_csv(solution_filename)
    test_df = pd.read_csv(test_filename)
    question_number = []
    solutions = []
    questions = []
    paper_name = []
    for index, row in solution_df.iterrows():
        alphebet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        q = alphebet[int(index)]
        question_number = question_number + [q]
        solutions = solutions + [solution_df.loc[index, 'solution']]
        questions = questions + [test_df.loc[index, 'test']]
        paper_name = paper_name + [f'20{i}b']
    here = pd.DataFrame({'question_number': question_number, 'question': questions, 'solution': solutions, 'paper_name': paper_name})
    here.to_csv(f"csv/merged20{i}b.csv")
    all_merged = pd.concat([all_merged, here])
all_merged = all_merged.reset_index(drop=True)
all_merged.to_csv("csv/all_merged.csv")
