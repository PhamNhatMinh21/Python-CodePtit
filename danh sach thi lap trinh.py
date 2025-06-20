class Team:
    def __init__(self, ma, ten, truong):
        self.ma = ma
        self.ten = ten
        self.truong = truong
class ThiSinh:
    def __init__(self, ma1, ten1, team_code):
        self.ma1 = ma1
        self.ten1 = ten1
        self.team_code = team_code
    def __str__(self):
        team = res[self.team_code]
        return f'{self.ma1} {self.ten1} {team.ten} {team.truong}'
n = int(input())
res = {}
for i in range(1, n + 1):
    ten = input().strip()
    truong = input().strip()
    team = 'Team{0:0>2}'.format(i)
    res[team] = Team(team, ten, truong)
m = int(input())
a = []
for i in range(1, m + 1):
    ten = input().strip()
    ma = input().strip()
    ma_ts = 'C{0:0>3}'.format(i)
    a.append(ThiSinh(ma_ts, ten, ma))
a = sorted(a, key=lambda x: x.ten1)
print(*a, sep='\n')
