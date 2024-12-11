def calculate_cost(p, target):
    """Kiszámítja az összköltséget egy adott célhosszhoz."""
    return sum(abs(x - target) for x in p)

def minimal_cost_recursive(p):
    # Alapeset: Ha csak egy bot van, nincs költség
    if len(p) == 1:
        return 0

    # Rendezzük a botok hosszát
    p.sort()

    # Medián meghatározása
    median = p[len(p) // 2]

    # Költség kiszámítása a mediánnal
    total_cost = calculate_cost(p, median)

    return total_cost

# Bemenet olvasása
n = int(input())
p = list(map(int, input().split()))

# Minimális összköltség kiszámítása
result = minimal_cost_recursive(p)

# Eredmény kiírása
print(result)
