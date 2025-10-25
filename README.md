----------------------------------
BA Orbit Rings Mini app
----------------------------------


---------------------------------------
Biró András — monogram: BA 
---------------------------------------


Indítás: (PyCharm 2025.2): main.py
----------------------------------------------

Feladat leírása
Mini „naprendszer” szimuláció turtle grafikával,ahol több bolygó körpályán kering egy középpont körül. 
Van benne: animáció (ontimer), eseménykezelés (onkey, onscreenclick), új bolygó felvétele, törlés, sebességszabályzás és a középpont áthelyezése.
----------------------------------------------------------------

Vezérlés 
Egérkattintás: - középpont áthelyezése.
Billentyűk:
   N - új bolygó. 
   Delete - utolsó bolygó törlése. 
   Z - sebesség csökkentése. 
   X - sebesség növelése.
   Space - animáció megállítása; Space újra - animáció folytatása.  
   Esc - kilépés.
-------------------------------------------------------------------------------------

Modulok és a modulokban használt függvények

math
A bolygók helyzetének kiszámításához és a szögértékek kezeléséhez:
   sin(θ) – y-koordináta meghatározása
   cos(θ) – x-koordináta meghatározása
   radians(x) – fok → radián átváltás
   pi – teljes kör (2π) kiszámításához használt konstans

random
Új bolygók véletlen paramétereinek előállításához:
   randrange(a, b) – véletlen egész érték (pl. bolygó sugara, színkomponens)
   uniform(a, b) – véletlen valós szám (pl. kezdő szög, szögsebesség)
   choice(lista) – előjel véletlen kiválasztása (óramutató járása szerinti vagy ellentétes irány)

turtle
Grafikus megjelenítéshez és eseménykezeléshez:
   Screen() – ablak létrehozása
   circle(r) – körpálya kirajzolása
   update() – képernyő frissítése
   onkey(f, key) – billentyűesemény kezelése
   onscreenclick(f) – egérkattintás kezelése
   ontimer(f, ms) – ismétlődő animációs hívás
   listen(), mainloop() – eseményfigyelés és futtatás

ba_orbits (saját modul)
A bolygók szögének normalizálása, frissítése:
   BA_wrap_angle(theta) – szög normalizálása [0, 2π) tartományra
   BA_polar_to_cart(cx, cy, R, theta) – polár → derékszögű átszámítás
   BA_step(planets, speed_scale, dt) – minden bolygó szögének frissítése
----------------------------------------------------------------------------------------------

Osztályok
class BAPlanet 
    R: pályasugár (px)  
    theta: aktuális szög (rad)  
    omega: szögsebesség (rad/s), előjele az irány  
    size: bolygó sugara (px)  
    color: RGB szín  
class BAAppState
    planets: `BAPlanet` objektumok listája  
    center: (x, y) középpont  
    speed: animáció sebesség  
    running: animáció fut-e  
    info_turtle: státuszkiíró teknős
--------------------------------------------------------------------