class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mlp = 1
        sm = 0
        while(n > 0):
            mlp = mlp * (n%10)
            sm = sm + (n%10)
            n //= 10
        return (mlp - sm)
