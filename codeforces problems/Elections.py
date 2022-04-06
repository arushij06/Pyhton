"""
Elections - https://codeforces.com/contest/570/problem/A
The country of Byalechinsk is running elections involving n candidates. The country consists of m cities. We know how many people in each city voted for each candidate.

The electoral system in the country is pretty unusual. At the first stage of elections the votes are counted for each city: it is assumed that in each city won the candidate who got the highest number of votes in this city, and if several candidates got the maximum number of votes, then the max_winner is the one with a smaller index.

At the second stage of elections the max_winner is determined by the same principle over the cities: the max_winner of the elections is the candidate who won in the maximum number of cities, and among those who got the maximum number of cities the max_winner is the one with a smaller index.

Determine who will win the elections.
Input

The first line of the input contains two integers n, m (1 ≤ n, m ≤ 100) — the number of candidates and of cities, respectively.

Each of the next m lines contains n non-negative integers, the j-th number in the i-th line aij (1 ≤ j ≤ n, 1 ≤ i ≤ m, 0 ≤ aij ≤ 109) denotes the number of votes for candidate j in city i.

It is guaranteed that the total number of people in all the cities does not exceed 109.
Output

Print a single number — the index of the candidate who won the elections. The candidates are indexed starting from one.
Examples
Input:
3 3
1 2 3
2 3 1
1 2 1

Output:
2
"""
def city_elections(city):
    city_winner = 0
    max_votes = -1
    for candidate in range(len(city)):
        if max_votes < city[candidate]:
            city_winner = candidate + 1
            max_votes = city[candidate]
    return city_winner
    
def elections_winner(voting_list):
    cities_won = {}
    max_winner = 0
    for city in voting_list:
        city_winner = city_elections(city)
        cities_won[city_winner] = cities_won.get(city_winner, 0) + 1
        if cities_won.get(max_winner, 0) < cities_won[city_winner]:
            max_winner = city_winner
        elif cities_won.get(max_winner, 0) == cities_won[city_winner]:
            if city_winner < max_winner:
                max_winner = city_winner
    return max_winner


num_candidates, num_cities = map(int,input().split())
num_votes = []
for i in range(num_cities):
    num_votes.append(list(map(int, input().split())))
print(elections_winner(num_votes))