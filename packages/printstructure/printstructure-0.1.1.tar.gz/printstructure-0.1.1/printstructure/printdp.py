from tabulate import tabulate


class DPTable:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("invalid argument type: {}".format(type(data)))
        if not (
            all(isinstance(row, list) for row in data)
            or all(not isinstance(item, list) for item in data)
        ):
            raise TypeError("invalid DP table structure")
        if isinstance(data[0], list):
            for row in data:
                if len(row) != len(data[0]):
                    raise ValueError(
                        "invalid DP table structure, length of each row in the dp table is different"
                    )

        self.dp = data

    def print_dp(self):
        if isinstance(self.dp[0], list):
            headers = ["col#\nrow#"] + [i for i in range(len(self.dp[0]))]
            dp_with_row_idx = [[i] + row for i, row in enumerate(self.dp)]
            print(tabulate(dp_with_row_idx, tablefmt="grid", headers=headers))

        else:
            headers = ["col#"] + [i for i in range(len(self.dp))]
            tmp = [[""] + self.dp]
            print(tabulate(tmp, tablefmt="grid", headers=headers))
