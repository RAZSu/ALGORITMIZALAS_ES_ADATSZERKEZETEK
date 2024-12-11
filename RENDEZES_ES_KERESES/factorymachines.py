def minimális_idő(n, t, gépek):
    # Bináris keresés határai
    bal = 1
    jobb = t * min(gépek)
    válasz = jobb
    
    while bal <= jobb:
        közép = (bal + jobb) // 2
        
        # Számoljuk meg, hány termék készül el adott idő alatt
        összes_termék = sum(közép // k for k in gépek)
        
        if összes_termék >= t:
            # Ha elég termék készül, csökkentjük az időtartamot
            válasz = közép
            jobb = közép - 1
        else:
            # Ha nem elég, növeljük az időtartamot
            bal = közép + 1
    
    return válasz

# Bemenet olvasása
import sys
bemenet = sys.stdin.read
adatok = bemenet().splitlines()

n, t = map(int, adatok[0].split())
gépek = list(map(int, adatok[1].split()))

# Minimális idő kiszámítása
eredmény = minimális_idő(n, t, gépek)

# Kimenet
print(eredmény)
