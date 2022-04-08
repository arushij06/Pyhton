"""
Insomnia cure - https://codeforces.com/problemset/problem/148/A

«One dragon. Two dragon. Three dragon», — the princess was counting. She had trouble falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?
Input

Input data contains integer numbers k, l, m, n and d, each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).
Output

Output the number of damaged dragons.
Examples:

Input       Output
1           12
2
3
4
12

Input       Output
2           17
3
4
5
24

"""

def num_DragonsDamaged(dragons_position, total_dragons):
    harmed_dragons = []
    for position in range(1, total_dragons+1):
        for dragon in dragons_position:
            if position % dragon == 0:
                harmed_dragons.append(position)
                break
    return len(harmed_dragons)

dragons_position = []
for dragon in range(4):
    dragons_position.append(int(input()))
total_dragons = int(input())
print(num_DragonsDamaged(dragons_position, total_dragons))
