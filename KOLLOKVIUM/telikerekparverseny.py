def max_teli_kerekparverseny(N, M, K, magassagok):
    iranyok = [(0, 1, 'J'), (1, 0, 'L')]  # Jobbra és lefelé mozgás
    dp = [[0] * M for _ in range(N)]  # Maximális hossz tárolása
    szulo = [[None] * M for _ in range(N)]  # Útvonal visszakövetése

    # Dinamikus programozás a táblázat feltöltéséhez
    for i in range(N):
        for j in range(M):
            for di, dj, lep in iranyok:
                ni, nj = i - di, j - dj
                if 0 <= ni < N and 0 <= nj < M and abs(magassagok[i][j] - magassagok[ni][nj]) <= K:
                    if dp[ni][nj] + 1 > dp[i][j]:
                        dp[i][j] = dp[ni][nj] + 1
                        szulo[i][j] = (ni, nj, lep)

    # Maximum hossz keresése
    max_hossz = 0
    vegpont = None
    for i in range(N):
        for j in range(M):
            if dp[i][j] > max_hossz:
                max_hossz = dp[i][j]
                vegpont = (i, j)

    # Útvonal visszakövetése
    utvonal = []
    jelenlegi = vegpont
    while jelenlegi:
        ni, nj, lep = szulo[jelenlegi[0]][jelenlegi[1]] if szulo[jelenlegi[0]][jelenlegi[1]] else (None, None, None)
        if lep:
            utvonal.append(lep)
        jelenlegi = (ni, nj) if ni is not None and nj is not None else None

    # Kiírás
    kezdo_pont = vegpont
    for lep in utvonal[::-1]:
        if lep == 'L':
            kezdo_pont = (kezdo_pont[0] - 1, kezdo_pont[1])
        elif lep == 'J':
            kezdo_pont = (kezdo_pont[0], kezdo_pont[1] - 1)

    return max_hossz, (kezdo_pont[0] + 1, kezdo_pont[1] + 1), ''.join(utvonal[::-1])


# Bemenet beolvasása
N, M, K = map(int, input().split())
magassagok = [list(map(int, input().split())) for _ in range(N)]

# Megoldás meghívása
max_hossz, kezdo_pont, utvonal = max_teli_kerekparverseny(N, M, K, magassagok)

# Kimenet
print(max_hossz)
print(kezdo_pont[0], kezdo_pont[1])
print(utvonal)
