from itertools import combinations

def calc_team_score(team, matrix):
    team_score = 0
    pairs = list(combinations(team, 2))

    for pair in pairs:
        x, y = pair
        team_score += matrix[x][y] + matrix[y][x]

    return team_score

def main():
    n = int(input())
    start = []
    for _ in range(n):
        start.append(list(map(int, input().split())))

    # start 매트릭스를 전치시켜 link 매트릭스를 계산한다.
    link = list(map(list, zip(*start)))

    # 전체 인원을 2팀으로 분할한다.
    people = [i for i in range(n)]
    start_teams = list(combinations(people, n//2))

    diff = 1e9
    for start_team in start_teams:
        # start 팀의 인원들을 제외한 팀들로 구성된 link 팀을 계산한다.
        link_team = tuple([i for i in people if i not in start_team])
        
        start_team_score = calc_team_score(start_team, start)
        link_team_score = calc_team_score(link_team, link)

        diff = min(diff, abs(start_team_score - link_team_score))

    print(diff)

if __name__ == "__main__":
    main()
