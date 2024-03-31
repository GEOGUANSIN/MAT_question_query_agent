import pandas as pd


class Separation:
    def __init__(self, filename = None):
        self.filename_ = filename

    def separate_test(self):
        """
          This function reads a text file and separates its content based on newline characters
          followed by uppercase letters.

          Args:
              filename: The path to the text file.

          Returns:
              A dictionary where keys are sections identified by uppercase letters after newlines
              and values are lists containing the lines belonging to that section.
        """
        sections = {}
        current_section = None
        with open(self.filename_, 'r') as f:
            for line in f:
                # Check for newline followed by uppercase letter
                if len(line) > 2:#print(f'line[0]:{line[0]}')
                    if line[0].isupper() and line[1] == '.':
                        current_section = line[0]  # Extract the uppercase letter as section name
                        sections[current_section] = [line]  # Create a new list for the section
                    else:
                        # Append line to the current section (if any)
                        if current_section and line != "\\end{document}":
                            sections[current_section].append(line.strip())  # Remove trailing newline
        return sections

    def separate_solution(self):
        """
          This function reads a text file and separates its content based on newline characters
          followed by uppercase letters.

          Args:
              filename: The path to the text file.

          Returns:
              A dictionary where keys are sections identified by uppercase letters after newlines
              and values are lists containing the lines belonging to that section.
        """
        sections = {}
        current_section = None
        with open(self.filename_, 'r') as f:
            for line in f:
                # Check for newline followed by uppercase letter
                if len(line) > 2:#print(f'line[0]:{line[0]}')
                    if line[0].isupper() and line[1] == ' ':
                        current_section = line[0]  # Extract the uppercase letter as section name
                        sections[current_section] = [line]  # Create a new list for the section
                    else:
                        # Append line to the current section (if any)
                        if current_section and line != "\\end{document}":
                            sections[current_section].append(line.strip())  # Remove trailing newline
        return sections


def y_bound_cal(min_: int, max_: int):
    yb = [i for i in range(min_, max_ + 1)]
    return yb


def export_csv(filename_root_: str, target: str, y_bound: list):
    question = ''
    sections = {}
    for k in y_bound:
        filename = filename_root_.replace('$@', str(k))
        sol_sep = Separation(filename)
        if target == 'solution':
            sections = sol_sep.separate_solution()
            print(f"sections:{sections}")
        if target == 'test':
            sections = sol_sep.separate_test()
            print(f"sections:{sections}")
        key: str
        for key in sections.keys():
            print(f"key:{key}")
            question = ''
            for value in sections[key]:
                question = question + '\n' + value
            if target == 'solution':
                sections[key] = [question[2:]]
            elif target == 'test':
                sections[key] = [question[4:]]

        output = pd.DataFrame(sections).transpose()
        print(output)
        output.columns = [target]
        output['paper_name'] = f'20{k}b'
        output.to_csv(filename[:-4] + '.csv')


if __name__ == '__main__':
    filename_root = "websolutions$@b.tex"
    year_bound = y_bound_cal(20, 23)
    export_csv(filename_root, 'solution', year_bound)

    filename_root = "test20$@b.tex"
    year_bound = y_bound_cal(20, 23)
    export_csv(filename_root, 'test', year_bound)

