class SimplexSolver:
    def get_solution_from_tableau(self):
        cols = []
        for colI in range(len(self.rows[0])):
            col = [0] * len(self.rows)
            for rowI in range(len(self.rows)):
                col[rowI] = self.rows[rowI][colI]
            cols.append(col)

        results = []
        for i in range(len(cols) - 1):
            if cols[i].count(0) == len(cols[i]) - 1 and 1 in cols[i]:
                results.append(cols[-1][cols[i].index(1)])
            else:
                results.append(0)
        return results, self.objective[-1]
    # Don't touch below this line

    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)
