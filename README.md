A beadandómhoz kettő file tartozik. A programkódot tartalmazó 'weather.py' és a megjelenítésre használt 'weather.html'.

A program futtatásához kell egy Sense Hat, amennyiben nincs a Raspberry Pi-re felszerelve,
a program figyelmezteti a felhasználót, hogy nem észlelt Sense Hat-et ezért a program futtatása nem lehetséges.

A programot a Sense Hat-hez tartozó parancsokkal készítettem, 'sense.get_temperature' parancsal lekértem az érzékelt hőmérsékletet
sense.get_humidity parancsal a páratartalmat valamint sense.get_pressure parancsal a légnyomást.

Figyelembe kell venni, hogy mivel a Sense Hat az épp működő Raspberry Pi felett helyezkedik el éppen ezért a hőmérséklet melyet kiír
nem feltétlenül a szoba hőmérséklete, (25-26 fokos szobában 35-36 celsius fokot érzékelt)

A beolvasott adatokat egy teljesen alap html oldalra iratja ki.

A program futtatása a következő képpen működik.
1. Terminálban a python3 weather.py parancsal elindítható a program
2. Böngészőben a 0.0.0.0:5000 es címen megtekinthető a Pi által érzékelt paraméterek, új értékekért csak frissíteni kell a weblapot a program folyamatosan frissíti az adatokat.
