from itertools import permutations, combinations

def friends_teams(friends,team_size=2,order_does_matter=False):
    if order_does_matter:
        return list(permutations(friends, team_size))
    else:
        return list(combinations(friends, team_size))

friends = friends = 'Bob Dante Julian Martin'.split()

print(friends_teams(friends, 2, True))
print(friends_teams(friends))