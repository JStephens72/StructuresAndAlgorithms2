class SimplexSolver:
    def get_pivot_col(self):
        low = 0
        pivot_idx = -1
        for i in range(len(self.objective) - 1):
            if self.objective[i] < low:
                low = self.objective[i]
                pivot_idx = i
        return pivot_idx

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
