class SimplexSolver:
    def get_pivot_row(self, col_idx):
        last_col = [self.rows[i][-1] for i in range(len(self.rows))]
        pivot_col = [self.rows[i][col_idx] for i in range(len(self.rows))]
        min_ratio = float("inf")
        min_ratio_idx = -1
        for i in range(len(last_col)):
            ratio = float("inf")
            if pivot_col[i] != 0:
                ratio = last_col[i] / pivot_col[i]
            if ratio < 0:
                continue
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_idx = i
        if min_ratio_idx == -1:
            raise Exception("no non-negative ratios, problem doesn't have a solution")
        return min_ratio_idx

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

    def get_pivot_col(self):
        low = 0
        pivot_idx = -1
        for i in range(len(self.objective) - 1):
            if self.objective[i] < low:
                low = self.objective[i]
                pivot_idx = i
        return pivot_idx

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)
