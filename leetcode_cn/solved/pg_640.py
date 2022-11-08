class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace("-", "+-").split("=")
        left = equation[0].split("+")
        right = equation[1].split("+")

        factor = 0
        val = 0
        for i in left:
            if not i:
                continue
            if "x" in i:
                factor_i = i.split("x")[0]
                if not factor_i:
                    factor_i = 1
                elif factor_i == "-":
                    factor_i = -1
                else:
                    factor_i = int(factor_i)
                factor += factor_i
            else:
                val += int(i)
        for i in right:
            if not i:
                continue
            if "x" in i:
                factor_i = i.split("x")[0]
                if not factor_i:
                    factor_i = 1
                elif factor_i == "-":
                    factor_i = -1
                else:
                    factor_i = int(factor_i)
                factor -= factor_i
            else:
                val -= int(i)
        if factor == 0:
            return "No solution" if val else "Infinite solutions"
        return "x=" + str(-val // factor)
