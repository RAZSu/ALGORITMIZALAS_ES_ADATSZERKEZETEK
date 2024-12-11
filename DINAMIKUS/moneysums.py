deflehetséges_összegek ( n , érmék ):
    # Halmaz az összes lehetséges összeg követésére
    összegeket= {0}​​ 
    
    érmékben lévő érmék esetében :
        új_összegek= beállítva ()
        s - re összegben :
            új_összegek. add ( s + érme )
        összegeket. frissítés ( new_sums )
    
    # Távolítsuk el a 0-t és rendezzük
    összegeket. eldobni ( 0 )
    rendezett_összegek= rendezve ( összegek )
    
    return len ( sorted_sums ), rendezett_sums
 
# Bemenet olvasása
importsys
bemenet= sys . stdin . olvas
adat= bemenet (). osztott vonalak ()
 
n= int ( adat [ 0 ])
érméket= lista ( térkép ( int , adat [ 1 ]. felosztás ()))
 
# Eredmény kiszámítása
k, összegek = lehetséges_összegek ( n , érmék )
 
# Kimenet kiírása
nyomtatás( k )
nyomtatás( " " . join ( map ( str , summas )