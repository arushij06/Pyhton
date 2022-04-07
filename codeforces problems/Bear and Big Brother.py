"""
Bear and Big Brother - https://codeforces.com/problemset/problem/791/A

Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.

Right now, Limak and Bob weigh a and b respectively. It's guaranteed that Limak's weight is smaller than or equal to his brother's weight.

Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.

After how many full years will Limak become strictly larger (strictly heavier) than Bob?
Input

The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight of Limak and the weight of Bob respectively.
Output

Print one integer, denoting the integer number of years after which Limak will become strictly larger than Bob.
Examples:

Input           Output
4 7             2

Input           Output
4 9             3

"""

def max_years(limak_wt, bob_wt):
    max_years = 0
    while(limak_wt <= bob_wt):
        limak_wt = limak_wt * 3
        bob_wt = bob_wt * 2
        max_years += 1 
    return max_years

limak_wt, bob_wt = map(int, input().split())
print(max_years(limak_wt, bob_wt))