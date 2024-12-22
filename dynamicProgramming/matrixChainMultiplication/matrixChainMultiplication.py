
class MatrixChainMultiplication:

    def __init__(self, p: list):
        self.p = p
        self.n = len(p) - 1
        self.m = [[0] * self.n for _ in range(self.n)]
        self.s = [[0] * self.n for _ in range(self.n)]
        self.matrix_chain_order = ""

    def computeSMMatrices(self):
        if self.n < 0:
            raise ValueError("Empty list or matrices.")

        for length in range(2, self.n + 1):
            for i in range(self.n - length + 1):
                j = i + length - 1
                self.m[i][j] = float('inf')

                for k in range(i, j):
                    m_i_j = self.m[i][k] + self.m[k+1][j] + self.p[i]*self.p[k+1]*self.p[j+1]
                    if m_i_j < self.m[i][j]:
                        self.m[i][j] = m_i_j
                        self.s[i][j] = k

        self.constructParentheses(0, self.n - 1)

    def constructParentheses(self, i, j):
        if i == j:
            self.matrix_chain_order += f"A{i+1}"
        else:
            self.matrix_chain_order += "("
            self.constructParentheses(i, self.s[i][j])
            self.constructParentheses(self.s[i][j] + 1, j)
            self.matrix_chain_order += ")"

    def getOptimalStructure(self):
        self.computeSMMatrices()
        output = f"Minimum Scalar Multiplications: {self.m[0][self.n - 1]}\n"
        output += f"Optimal Parathenses: {self.matrix_chain_order}"
        return output
