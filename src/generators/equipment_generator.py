import os 

import pandas as pd
# Poprawione listy nazw i typów, upewniając się, że obie mają po 100 elementów.

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
print(len(name), len(type))
equipment_data_corrected = {
    "nazwa": name,
    "typ": type
}
df_corrected = pd.DataFrame(equipment_data_corrected)
csv_file_path_corrected = "data/equipment.csv"
df_corrected.to_csv(csv_file_path_corrected, index=False)
