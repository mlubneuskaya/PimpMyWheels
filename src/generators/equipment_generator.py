import pandas as pd

name = [
    "Silnik V8", "Silnik R4", "Alternator", "Akumulator", "Amortyzator przedni", "Amortyzator tylny", 
    "Chłodnica", "Klimatyzacja", "Komputer diagnostyczny", "Koło zapasowe", "Klocki hamulcowe", 
    "Lampy przednie", "Lampy tylne", "Lusterko boczne", "Olej silnikowy", "Pasek rozrządu", "Pompa paliwa", 
    "Pompa wodna", "Przewody zapłonowe", "Przewody hamulcowe", "Sprzęgło", "Skrzynia biegów", "Świece zapłonowe", 
    "Turbosprężarka", "Uszczelka pod głowicą", "Wahacz", "Wycieraczki", "Zawór EGR", "Zderzak przedni", "Zderzak tylny", 
    "Czujnik ABS", "Czujnik temperatury", "Filtr powietrza", "Filtr oleju", "Filtr kabinowy", "Filtr paliwa", "Katalizator", 
    "Łożysko koła", "Nagrzewnica", "Pasek klinowy", "Przegub napędowy", "Regulator napięcia", "Rozrusznik", 
    "Silnik elektryczny", "Sprężyna zawieszenia", "Szyba czołowa", "Szyba tylna", "Szyba boczna", 
    "Tarcze hamulcowe", "Tłumik", "Układ wydechowy", "Zawieszenie pneumatyczne", "Zawór recyrkulacji spalin", 
    "Zestaw naprawczy", "Żarówka H4", "Żarówka LED", "Żarówka xenonowa", 
    "Pompa wspomagania", "Przewody klimatyzacji", "Rura wydechowa", "Osłona przeciwsłoneczna", "Pasy bezpieczeństwa",
    "Narzędzie diagnostyczne", "Podnośnik hydrauliczny", "Wkrętarka akumulatorowa", "Klucz dynamometryczny", 
    "Sprężarka powietrza", "Tester akumulatora", "Wózek narzędziowy", "Zestaw kluczy nasadowych", "Zestaw wierteł", 
    "Zestaw nasadek", "Zestaw imbusów", "Narzędzie do geometrii kół", "Ładowarka akumulatorów", "Miernik grubości lakieru", 
    "Tester diagnostyczny", "Narzędzie do ustawiania świateł", "Prasa hydrauliczna", "Stetoskop samochodowy", 
    "Tester ciśnienia", "Waga do kół", "Zestaw do odsysania oleju", "Zestaw do pomiaru ciśnienia", "Zestaw do regeneracji reflektorów"
]
type = [
    "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Narzędzie", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", 
    "Część", "Część", "Część", "Część", "Część",
    "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", 
    "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", 
    "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", 
    "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", 
    "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie", "Narzędzie"
]
prices = [
    25000, 10000, 700, 400, 500, 450, 
    600, 3500, 8000, 300, 200, 
    800, 700, 150, 150, 100, 250, 
    200, 100, 150, 600, 4000, 50, 
    3000, 100, 350, 40, 500, 800, 750, 
    250, 60, 30, 20, 25, 30, 1200, 
    100, 200, 50, 150, 80, 400, 
    3500, 250, 600, 500, 450, 
    300, 350, 800, 1500, 600, 
    200, 15, 30, 150, 
    500, 300, 150, 80, 120,
    1500, 1000, 600, 300, 
    2500, 200, 800, 300, 200, 
    300, 100, 50, 500, 250, 
    150, 800, 250, 150, 
    500, 200, 350, 100, 80
]

print(len(name), len(type), len(prices))
equipment = {
    "nazwa": name,
    "typ": type,
    "cena": prices
}
df = pd.DataFrame(equipment)
file_path = "data/equipment.csv"
df.to_csv(file_path, index=False)
