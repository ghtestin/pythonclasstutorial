# Beispiel: Einführung
intro_example = """
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says: Woof!"

# Create objects
rex = Dog("Rex")
bella = Dog("Bella")

# Call methods
print(rex.bark())
print(bella.bark())
"""

# Beispiel: Klassen erstellen
class_creation = """
class Person:
    # Die Klasse Person repräsentiert eine Person mit Namen und Alter
    pass  # 'pass' bedeutet, dass die Klasse zunächst leer ist
"""

# Beispiel: Objekte instanziieren
class_instantiation = """
class Person:
    pass

# Objekte erstellen
person1 = Person()  # Erste Instanz der Klasse Person
person2 = Person()  # Zweite Instanz der Klasse Person

# Attribute dynamisch hinzufügen
person1.name = "Anna"
person1.alter = 30

person2.name = "Max"
person2.alter = 25

print(f"{person1.name} ist {person1.alter} Jahre alt")
print(f"{person2.name} ist {person2.alter} Jahre alt")
"""

# Interaktives Beispiel: Klassen erstellen
class_interactive = """
class Person:
    pass

# Objekte erstellen und Attribute zuweisen
person1 = Person()
person1.name = "Anna"
person1.alter = 30
person1.beruf = "Programmiererin"

# Noch ein Objekt erstellen
person2 = Person()
person2.name = "Max"
person2.alter = 25
person2.beruf = "Designer"

# Ausgabe der Attribute
print(f"{person1.name} ist {person1.alter} Jahre alt und arbeitet als {person1.beruf}")
print(f"{person2.name} ist {person2.alter} Jahre alt und arbeitet als {person2.beruf}")

# Ändere ein Attribut
person1.alter = 31
print(f"{person1.name} hatte Geburtstag und ist jetzt {person1.alter} Jahre alt")
"""

# Beispiel: Konstruktor
constructor_example = """
class Person:
    def __init__(self, name, alter):
        # Dies ist der Konstruktor
        self.name = name
        self.alter = alter
        print(f"Eine neue Person namens {name} wurde erstellt!")

# Objekte mit Konstruktor erstellen
person1 = Person("Anna", 30)
person2 = Person("Max", 25)
"""

# Beispiel: Attribute
attributes_example = """
class Person:
    def __init__(self, name, alter):
        self.name = name  # Instanzattribut
        self.alter = alter  # Instanzattribut
    
    def geburtstag_feiern(self):
        self.alter += 1
        return f"{self.name} ist jetzt {self.alter} Jahre alt!"

# Objekte erstellen
person1 = Person("Anna", 30)
person2 = Person("Max", 25)

# Auf Attribute zugreifen
print(f"{person1.name} ist {person1.alter} Jahre alt")
print(f"{person2.name} ist {person2.alter} Jahre alt")

# Methode aufrufen, die ein Attribut ändert
print(person1.geburtstag_feiern())
"""

# Beispiel: Student-Klasse
student_class = """
class Student:
    def __init__(self, name, alter, studienfach):
        self.name = name
        self.alter = alter
        self.studienfach = studienfach
        self.noten = []
    
    def note_hinzufuegen(self, note):
        self.noten.append(note)
    
    def durchschnitt_berechnen(self):
        if not self.noten:
            return "Keine Noten vorhanden"
        return sum(self.noten) / len(self.noten)
    
    def info(self):
        return f"{self.name}, {self.alter} Jahre, studiert {self.studienfach}"

# Studenten erstellen
student1 = Student("Lisa", 22, "Informatik")
student2 = Student("Tom", 20, "Mathematik")

# Noten hinzufügen
student1.note_hinzufuegen(1.3)
student1.note_hinzufuegen(2.0)
student1.note_hinzufuegen(1.7)

# Informationen ausgeben
print(student1.info())
print(f"Notendurchschnitt: {student1.durchschnitt_berechnen()}")

print(student2.info())
print(f"Notendurchschnitt: {student2.durchschnitt_berechnen()}")
"""

# Beispiel: Methoden
methods_example = """
class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite
    
    def flaeche_berechnen(self):
        return self.laenge * self.breite
    
    def umfang_berechnen(self):
        return 2 * (self.laenge + self.breite)
    
    def beschreiben(self):
        return f"Rechteck mit Länge {self.laenge} und Breite {self.breite}"

# Rechteck erstellen
mein_rechteck = Rechteck(5, 3)

# Methoden aufrufen
print(mein_rechteck.beschreiben())
print(f"Fläche: {mein_rechteck.flaeche_berechnen()} Quadrateinheiten")
print(f"Umfang: {mein_rechteck.umfang_berechnen()} Einheiten")
"""

# Beispiel: Methoden-Typen
method_types = """
class MathematischeOperationen:
    pi = 3.14159  # Klassenattribut
    
    def __init__(self, wert):
        self.wert = wert  # Instanzattribut
    
    # Instanzmethode - verwendet self
    def verdoppeln(self):
        return self.wert * 2
    
    # Klassenmethode - verwendet cls
    @classmethod
    def kreis_umfang(cls, radius):
        return 2 * cls.pi * radius
    
    # Statische Methode - verwendet weder self noch cls
    @staticmethod
    def addieren(a, b):
        return a + b

# Instanz erstellen
math_ops = MathematischeOperationen(5)

# Instanzmethode aufrufen
print(f"Verdoppelt: {math_ops.verdoppeln()}")

# Klassenmethode aufrufen
print(f"Umfang eines Kreises mit Radius 7: {MathematischeOperationen.kreis_umfang(7)}")

# Statische Methode aufrufen
print(f"10 + 20 = {MathematischeOperationen.addieren(10, 20)}")
"""

# Beispiel: Bankkonto
bank_account = """
class Bankkonto:
    def __init__(self, kontonummer, kontoinhaber, kontostand=0):
        self.kontonummer = kontonummer
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand
        self.transaktionen = []
    
    def einzahlen(self, betrag):
        if betrag <= 0:
            return "Betrag muss größer als 0 sein"
        
        self.kontostand += betrag
        self.transaktionen.append(f"Einzahlung: +{betrag} €")
        return f"{betrag} € eingezahlt. Neuer Kontostand: {self.kontostand} €"
    
    def abheben(self, betrag):
        if betrag <= 0:
            return "Betrag muss größer als 0 sein"
        
        if betrag > self.kontostand:
            return "Nicht genügend Guthaben"
        
        self.kontostand -= betrag
        self.transaktionen.append(f"Abhebung: -{betrag} €")
        return f"{betrag} € abgehoben. Neuer Kontostand: {self.kontostand} €"
    
    def kontoauszug(self):
        print(f"Kontoauszug für {self.kontoinhaber} (Konto: {self.kontonummer})")
        print(f"Aktueller Kontostand: {self.kontostand} €")
        print("Transaktionen:")
        for transaktion in self.transaktionen:
            print(f"- {transaktion}")

# Konto erstellen und testen
mein_konto = Bankkonto("DE123456789", "Max Mustermann", 1000)
print(mein_konto.einzahlen(500))
print(mein_konto.abheben(200))
print(mein_konto.abheben(2000))  # Sollte fehlschlagen
mein_konto.kontoauszug()
"""

# Beispiel: Vererbung (grundlegend)
inheritance_basic = """
class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def laut_machen(self):
        return "Ein unbestimmter Tierlaut"
    
    def info(self):
        return f"{self.name} ist {self.alter} Jahre alt"

# Kindklasse, die von Tier erbt
class Hund(Tier):
    def laut_machen(self):
        return "Wuff!"
    
    def schwanz_wedeln(self):
        return f"{self.name} wedelt mit dem Schwanz"

# Kindklasse, die von Tier erbt
class Katze(Tier):
    def laut_machen(self):
        return "Miau!"
    
    def schnurren(self):
        return f"{self.name} schnurrt"

# Objekte erstellen
bello = Hund("Bello", 5)
mieze = Katze("Mieze", 3)

# Methoden der Elternklasse
print(bello.info())
print(mieze.info())

# Überschriebene Methoden
print(f"{bello.name} macht: {bello.laut_machen()}")
print(f"{mieze.name} macht: {mieze.laut_machen()}")

# Spezifische Methoden der Kindklassen
print(bello.schwanz_wedeln())
print(mieze.schnurren())
"""

# Beispiel: super() Funktion
super_function = """
class Fahrzeug:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0
    
    def fahren(self, strecke):
        self.kilometerstand += strecke
        return f"{self.marke} {self.modell} ist {strecke} km gefahren"
    
    def info(self):
        return f"{self.marke} {self.modell} ({self.baujahr}), {self.kilometerstand} km"

class Auto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_tueren):
        # Aufruf des Konstruktors der Elternklasse
        super().__init__(marke, modell, baujahr)
        self.anzahl_tueren = anzahl_tueren
    
    def info(self):
        # Aufruf der info-Methode der Elternklasse
        basis_info = super().info()
        return f"{basis_info}, {self.anzahl_tueren} Türen"

# Auto erstellen
mein_auto = Auto("VW", "Golf", 2020, 5)

# Auto fahren lassen
print(mein_auto.fahren(150))

# Informationen anzeigen (überschriebene Methode)
print(mein_auto.info())
"""

# Beispiel: Mehrfachvererbung
multiple_inheritance = """
class Fahrrad:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
    
    def fahren(self):
        return f"{self.marke} {self.modell} wird getreten"
    
    def bremsen(self):
        return f"{self.marke} {self.modell} bremst"

class Elektrogerät:
    def __init__(self, leistung):
        self.leistung = leistung
    
    def einschalten(self):
        return "Gerät eingeschaltet"
    
    def ausschalten(self):
        return "Gerät ausgeschaltet"

# Mehrfachvererbung
class Elektrofahrrad(Fahrrad, Elektrogerät):
    def __init__(self, marke, modell, leistung, batteriekapazität):
        Fahrrad.__init__(self, marke, modell)
        Elektrogerät.__init__(self, leistung)
        self.batteriekapazität = batteriekapazität
        self.unterstützung_aktiv = False
    
    def motor_aktivieren(self):
        self.unterstützung_aktiv = True
        return f"E-Bike Unterstützung von {self.marke} {self.modell} aktiviert"
    
    def laden(self):
        return f"{self.marke} {self.modell} wird mit {self.leistung} Watt geladen"
    
    def fahren(self):
        if self.unterstützung_aktiv:
            return f"{self.marke} {self.modell} fährt mit elektrischer Unterstützung"
        else:
            return super().fahren()  # Ruft die Methode der Elternklasse Fahrrad auf

# E-Bike erstellen
e_bike = Elektrofahrrad("Cube", "Reaction Hybrid", 250, 625)

# Methoden beider Elternklassen nutzen
print(e_bike.fahren())  # Ohne Motorunterstützung
print(e_bike.einschalten())
print(e_bike.motor_aktivieren())
print(e_bike.fahren())  # Mit Motorunterstützung
print(e_bike.bremsen())
print(e_bike.laden())
print(f"Batteriekapazität: {e_bike.batteriekapazität} Wh")
"""

# Beispiel: Fahrzeug-Hierarchie
vehicle_hierarchy = """
class Fahrzeug:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0
    
    def fahren(self, strecke):
        self.kilometerstand += strecke
        return f"{self.marke} {self.modell} ist {strecke} km gefahren"
    
    def info(self):
        return f"{self.marke} {self.modell} ({self.baujahr}), {self.kilometerstand} km"

class Auto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_tueren):
        super().__init__(marke, modell, baujahr)
        self.anzahl_tueren = anzahl_tueren
    
    def hupen(self):
        return "Huuuup!"

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, hubraum):
        super().__init__(marke, modell, baujahr)
        self.hubraum = hubraum
    
    def wheelie(self):
        return "Macht einen Wheelie!"

class Elektroauto(Auto):
    def __init__(self, marke, modell, baujahr, anzahl_tueren, batteriekapazität):
        super().__init__(marke, modell, baujahr, anzahl_tueren)
        self.batteriekapazität = batteriekapazität
        self.ladestand = 100  # Prozent
    
    def laden(self):
        self.ladestand = 100
        return f"{self.marke} {self.modell} ist vollständig geladen"
    
    def fahren(self, strecke):
        verbrauch = strecke * 0.2  # 20% Verbrauch pro 100 km (vereinfacht)
        if self.ladestand < verbrauch:
            return f"Nicht genug Batterieladung für {strecke} km"
        
        self.ladestand -= verbrauch
        return super().fahren(strecke) + f" (Ladestand: {self.ladestand:.1f}%)"

# Fahrzeuge erstellen und testen
auto = Auto("VW", "Golf", 2020, 5)
motorrad = Motorrad("Honda", "CBR", 2021, 600)
elektroauto = Elektroauto("Tesla", "Model 3", 2022, 4, 75)

# Tests
print(auto.info())
print(auto.fahren(100))
print(auto.hupen())

print("\n" + motorrad.info())
print(motorrad.fahren(50))
print(motorrad.wheelie())

print("\n" + elektroauto.info())
print(elektroauto.fahren(200))
print(elektroauto.laden())
print(elektroauto.fahren(300))
"""

# Beispiel: Polymorphismus (grundlegend)
polymorphism_basic = """
class Tier:
    def __init__(self, name):
        self.name = name
    
    def laut_machen(self):
        pass  # Dies ist eine abstrakte Methode, die überschrieben werden sollte

class Hund(Tier):
    def laut_machen(self):
        return "Wuff!"

class Katze(Tier):
    def laut_machen(self):
        return "Miau!"

class Kuh(Tier):
    def laut_machen(self):
        return "Muuuh!"

# Polymorphismus in Aktion: Die gleiche Methode wird mit verschiedenen Objekten aufgerufen
def tier_laut_ausgeben(tier):
    print(f"{tier.name} macht: {tier.laut_machen()}")

# Verschiedene Tiere erstellen
tiere = [
    Hund("Bello"),
    Katze("Mieze"),
    Kuh("Elsa")
]

# Die gleiche Funktion mit verschiedenen Objekten aufrufen
for tier in tiere:
    tier_laut_ausgeben(tier)
"""

# Beispiel: Methoden-Überschreibung
method_overriding = """
class Fahrzeug:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
    
    def beschreibung(self):
        return f"{self.marke} {self.modell}"
    
    def fahren(self):
        return f"{self.beschreibung()} fährt"

class Auto(Fahrzeug):
    def __init__(self, marke, modell, anzahl_tueren):
        super().__init__(marke, modell)
        self.anzahl_tueren = anzahl_tueren
    
    # Überschreibung der Methode beschreibung
    def beschreibung(self):
        return f"{self.marke} {self.modell} mit {self.anzahl_tueren} Türen"
    
    def hupen(self):
        return f"{self.beschreibung()} hupt"

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, hubraum):
        super().__init__(marke, modell)
        self.hubraum = hubraum
    
    # Überschreibung der Methode beschreibung
    def beschreibung(self):
        return f"{self.marke} {self.modell} mit {self.hubraum} ccm"
    
    # Überschreibung der Methode fahren
    def fahren(self):
        return f"{self.beschreibung()} braust davon"

# Fahrzeuge erstellen
auto = Auto("VW", "Golf", 5)
motorrad = Motorrad("Honda", "CBR", 600)

# Methoden testen
print(auto.beschreibung())
print(auto.fahren())
print(auto.hupen())

print("\n" + motorrad.beschreibung())
print(motorrad.fahren())
"""

# Beispiel: Duck Typing
duck_typing = """
class Ente:
    def schwimmen(self):
        return "Die Ente schwimmt"
    
    def quaken(self):
        return "Quak!"

class Mensch:
    def schwimmen(self):
        return "Der Mensch schwimmt"
    
    def sprechen(self):
        return "Hallo!"
    
    # Eine Methode, die wie die quaken-Methode aussieht
    def quaken(self):
        return "Der Mensch imitiert: Quak!"

# Duck Typing in Aktion
def lass_quaken(objekt):
    # Wir prüfen nicht den Typ, sondern nur, ob die Methode existiert
    # "Wenn es wie eine Ente quakt..."
    return objekt.quaken()

# Objekte erstellen
ente = Ente()
mensch = Mensch()

# Die gleiche Funktion mit verschiedenen Objekten aufrufen
print(lass_quaken(ente))
print(lass_quaken(mensch))

# Beide können auch schwimmen
print(ente.schwimmen())
print(mensch.schwimmen())
"""

# Beispiel: Geometrische Formen
geometric_shapes = """
import math

class Form:
    def fläche(self):
        pass  # Abstrakte Methode, die überschrieben werden sollte
    
    def umfang(self):
        pass  # Abstrakte Methode, die überschrieben werden sollte

class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius
    
    def fläche(self):
        return math.pi * self.radius ** 2
    
    def umfang(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Kreis mit Radius {self.radius}"

class Rechteck(Form):
    def __init__(self, länge, breite):
        self.länge = länge
        self.breite = breite
    
    def fläche(self):
        return self.länge * self.breite
    
    def umfang(self):
        return 2 * (self.länge + self.breite)
    
    def __str__(self):
        return f"Rechteck mit Länge {self.länge} und Breite {self.breite}"

class Quadrat(Rechteck):
    def __init__(self, seite):
        super().__init__(seite, seite)
        self.seite = seite
    
    def __str__(self):
        return f"Quadrat mit Seitenlänge {self.seite}"

# Funktion, die mit jeder Form arbeiten kann
def form_info(form):
    print(f"Form: {form}")
    print(f"Fläche: {form.fläche():.2f}")
    print(f"Umfang: {form.umfang():.2f}")
    print()

# Formen erstellen
kreis = Kreis(5)
rechteck = Rechteck(4, 6)
quadrat = Quadrat(3)

# Informationen über alle Formen ausgeben
form_info(kreis)
form_info(rechteck)
form_info(quadrat)
"""

# Beispiel: Dunder-Methoden (grundlegend)
dunder_methods_basic = """
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    # String-Darstellung für print() und str()
    def __str__(self):
        return f"{self.name} ({self.alter} Jahre)"
    
    # "Offizielle" String-Darstellung für repr()
    def __repr__(self):
        return f"Person('{self.name}', {self.alter})"
    
    # Vergleichsoperator ==
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.alter == other.alter
    
    # Vergleichsoperator <
    def __lt__(self, other):
        if not isinstance(other, Person):
            raise TypeError("Vergleich nicht möglich")
        return self.alter < other.alter

# Personen erstellen
person1 = Person("Anna", 30)
person2 = Person("Max", 25)
person3 = Person("Anna", 30)

# __str__ testen
print(person1)  # Ruft __str__ auf

# __repr__ testen
print(repr(person2))  # Ruft __repr__ auf

# __eq__ testen (Gleichheit)
print(f"person1 == person2: {person1 == person2}")
print(f"person1 == person3: {person1 == person3}")

# __lt__ testen (kleiner als)
print(f"person1 < person2: {person1 < person2}")
print(f"person2 < person1: {person2 < person1}")
"""

# Beispiel: Operatoren überladen
operator_overloading = """
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String-Darstellung
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    # Addition: v1 + v2
    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)
    
    # Subtraktion: v1 - v2
    def __sub__(self, other):
        return Vektor(self.x - other.x, self.y - other.y)
    
    # Multiplikation mit Skalar: v * n
    def __mul__(self, skalar):
        return Vektor(self.x * skalar, self.y * skalar)
    
    # Länge des Vektors: len(v)
    def __len__(self):
        import math
        return math.floor(math.sqrt(self.x**2 + self.y**2))
    
    # Negation: -v
    def __neg__(self):
        return Vektor(-self.x, -self.y)
    
    # Vergleich: v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Vektoren erstellen
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

# Operationen testen
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"Länge von v1: {len(v1)}")
print(f"-v1 = {-v1}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == v1: {v1 == v1}")
"""

# Beispiel: Karte für ein Kartenspiel
card_class = """
class Karte:
    FARBEN = ["Herz", "Karo", "Pik", "Kreuz"]
    WERTE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
    
    def __init__(self, farbe, wert):
        if farbe not in self.FARBEN:
            raise ValueError(f"Ungültige Farbe: {farbe}")
        if wert not in self.WERTE:
            raise ValueError(f"Ungültiger Wert: {wert}")
        
        self.farbe = farbe
        self.wert = wert
    
    # String-Darstellung
    def __str__(self):
        return f"{self.wert} von {self.farbe}"
    
    # Repräsentation
    def __repr__(self):
        return f"Karte('{self.farbe}', '{self.wert}')"
    
    # Gleichheit
    def __eq__(self, other):
        if not isinstance(other, Karte):
            return False
        return self.farbe == other.farbe and self.wert == other.wert
    
    # Größenvergleich (nach Wert)
    def __lt__(self, other):
        if not isinstance(other, Karte):
            raise TypeError("Vergleich nur mit anderen Karten möglich")
        
        return self.WERTE.index(self.wert) < self.WERTE.index(other.wert)
    
    # Hash-Wert (für Sets und Dictionary-Keys)
    def __hash__(self):
        return hash((self.farbe, self.wert))

# Karten erstellen
karte1 = Karte("Herz", "Ass")
karte2 = Karte("Pik", "7")
karte3 = Karte("Herz", "Ass")  # Gleich wie karte1

# Dunder-Methoden testen
print(karte1)  # __str__
print(repr(karte2))  # __repr__

print(f"karte1 == karte2: {karte1 == karte2}")  # __eq__
print(f"karte1 == karte3: {karte1 == karte3}")  # __eq__

print(f"karte1 < karte2: {karte1 < karte2}")  # __lt__
print(f"karte2 < karte1: {karte2 < karte1}")  # __lt__

# Verwendung in Set (benötigt __hash__)
kartendeck = {karte1, karte2, karte3}
print(f"Anzahl einzigartiger Karten im Set: {len(kartendeck)}")
"""

# Beispiel: Klassenattribute vs. Instanzattribute
class_vs_instance_attributes = """
class Auto:
    # Klassenattribute - von allen Instanzen geteilt
    hersteller = "VW"  # Standardwert
    anzahl_räder = 4
    hergestellte_autos = 0
    
    def __init__(self, modell, farbe):
        # Instanzattribute - für jede Instanz individuell
        self.modell = modell
        self.farbe = farbe
        self.kilometerstand = 0
        
        # Zugriff auf Klassenattribut über den Klassennamen
        Auto.hergestellte_autos += 1
    
    def fahren(self, strecke):
        # Zugriff auf Instanzattribut
        self.kilometerstand += strecke
        return f"{self.farbe}er {self.modell} ist {strecke} km gefahren"
    
    # Eine Klassenmethode kann Klassenattribute ändern
    @classmethod
    def ändere_hersteller(cls, neuer_hersteller):
        cls.hersteller = neuer_hersteller

# Autos erstellen
auto1 = Auto("Golf", "Rot")
auto2 = Auto("Passat", "Blau")

# Auf Klassenattribute zugreifen
print(f"Hersteller: {Auto.hersteller}")
print(f"Anzahl Räder: {auto1.anzahl_räder}")  # Zugriff über Instanz
print(f"Hergestellte Autos: {Auto.hergestellte_autos}")

# Auf Instanzattribute zugreifen
print(f"Auto 1: {auto1.modell}, {auto1.farbe}")
print(f"Auto 2: {auto2.modell}, {auto2.farbe}")

# Klassenattribut über Klassenmethode ändern
Auto.ändere_hersteller("Audi")
print(f"Neuer Hersteller: {Auto.hersteller}")

# Instanzattribut eines spezifischen Autos ändern
auto1.farbe = "Grün"
print(f"Neue Farbe von Auto 1: {auto1.farbe}")
print(f"Farbe von Auto 2 (unverändert): {auto2.farbe}")

# Ein neues Auto erstellen
auto3 = Auto("A4", "Silber")
print(f"Hergestellte Autos: {Auto.hergestellte_autos}")
"""

# Beispiel: Zählen von Instanzen
counting_instances = """
class Person:
    # Klassenattribut zum Zählen der Instanzen
    anzahl_personen = 0
    
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
        # Erhöhe den Zähler bei jeder Instanziierung
        Person.anzahl_personen += 1
    
    def __del__(self):
        # Verringere den Zähler, wenn ein Objekt gelöscht wird
        Person.anzahl_personen -= 1
        print(f"{self.name} wurde gelöscht")
    
    @classmethod
    def zeige_anzahl(cls):
        return f"Es gibt aktuell {cls.anzahl_personen} Personen"

# Personen erstellen
person1 = Person("Anna", 30)
print(Person.zeige_anzahl())

person2 = Person("Max", 25)
person3 = Person("Lisa", 28)
print(Person.zeige_anzahl())

# Eine Person löschen (durch Referenz entfernen)
print("Lösche person2...")
del person2
print(Person.zeige_anzahl())
"""

# Beispiel: Veränderliche Klassenattribute
mutable_class_attributes = """
class SchulKlasse:
    # Vorsicht: Eine Liste als Klassenattribut wird von allen Instanzen geteilt!
    schüler_liste = []
    
    def __init__(self, klassen_name):
        self.klassen_name = klassen_name
    
    def füge_schüler_hinzu(self, schüler_name):
        # Ändert das gemeinsame Klassenattribut!
        self.schüler_liste.append(schüler_name)
    
    def zeige_schüler(self):
        return f"Klasse {self.klassen_name}: {', '.join(self.schüler_liste)}"

class BessereSchulKlasse:
    def __init__(self, klassen_name):
        self.klassen_name = klassen_name
        # Hier wird die Liste als Instanzattribut erstellt - jeder hat seine eigene
        self.schüler_liste = []
    
    def füge_schüler_hinzu(self, schüler_name):
        self.schüler_liste.append(schüler_name)
    
    def zeige_schüler(self):
        return f"Klasse {self.klassen_name}: {', '.join(self.schüler_liste)}"

# Problem mit veränderlichem Klassenattribut
klasse10a = SchulKlasse("10a")
klasse10b = SchulKlasse("10b")

klasse10a.füge_schüler_hinzu("Anna")
klasse10b.füge_schüler_hinzu("Max")

print(klasse10a.zeige_schüler())  # Beide Liste enthalten Anna und Max!
print(klasse10b.zeige_schüler())  # Beide Liste enthalten Anna und Max!

# Richtige Implementierung mit Instanzattributen
bessereKlasse10a = BessereSchulKlasse("10a")
bessereKlasse10b = BessereSchulKlasse("10b")

bessereKlasse10a.füge_schüler_hinzu("Anna")
bessereKlasse10b.füge_schüler_hinzu("Max")

print(bessereKlasse10a.zeige_schüler())  # Enthält nur Anna
print(bessereKlasse10b.zeige_schüler())  # Enthält nur Max
"""

# Beispiel: Produktkatalog
product_catalog = """
class Produkt:
    # Klassenattribute
    anzahl_produkte = 0
    mwst_satz = 0.19  # 19% Mehrwertsteuer
    
    def __init__(self, name, netto_preis, kategorie):
        # Instanzattribute
        self.name = name
        self.netto_preis = netto_preis
        self.kategorie = kategorie
        self.produkt_id = Produkt.anzahl_produkte + 1
        
        # Erhöhe den Produkt-Zähler
        Produkt.anzahl_produkte += 1
    
    def brutto_preis(self):
        return round(self.netto_preis * (1 + self.mwst_satz), 2)
    
    def rabatt_anwenden(self, prozent):
        self.netto_preis = round(self.netto_preis * (1 - prozent/100), 2)
    
    def info(self):
        return f"Produkt #{self.produkt_id}: {self.name} ({self.kategorie}) - {self.netto_preis}€ netto, {self.brutto_preis()}€ brutto"
    
    @classmethod
    def ändere_mwst(cls, neuer_satz):
        cls.mwst_satz = neuer_satz
    
    @classmethod
    def zeige_produktanzahl(cls):
        return f"Anzahl Produkte im Katalog: {cls.anzahl_produkte}"

# Produkte erstellen
laptop = Produkt("Gaming Laptop", 1200.0, "Elektronik")
tisch = Produkt("Schreibtisch", 299.99, "Möbel")
buch = Produkt("Python Programmierung", 49.95, "Bücher")

# Produktinformationen anzeigen
print(laptop.info())
print(tisch.info())
print(buch.info())

# Klassenattribut abfragen
print(Produkt.zeige_produktanzahl())

# Rabatt anwenden (Instanzattribut ändern)
laptop.rabatt_anwenden(10)
print(f"Laptop nach 10% Rabatt: {laptop.info()}")

# MwSt-Satz ändern (Klassenattribut ändern)
print(f"Aktueller MwSt-Satz: {Produkt.mwst_satz*100}%")
Produkt.ändere_mwst(0.16)  # 16% MwSt
print(f"Neuer MwSt-Satz: {Produkt.mwst_satz*100}%")

# Neue Bruttopreise (betrifft alle Produkte)
print(laptop.info())
print(tisch.info())
print(buch.info())
"""

# Beispiel: Properties
property_example = """
class Temperatur:
    def __init__(self, celsius=0):
        self._celsius = celsius  # Unterstrich zeigt "privates" Attribut an
    
    # Getter-Methode für Celsius
    @property
    def celsius(self):
        return self._celsius
    
    # Setter-Methode für Celsius
    @celsius.setter
    def celsius(self, wert):
        if wert < -273.15:
            raise ValueError("Temperatur unter dem absoluten Nullpunkt!")
        self._celsius = wert
    
    # Property für Fahrenheit (berechnet aus Celsius)
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    # Setter für Fahrenheit (konvertiert zu Celsius)
    @fahrenheit.setter
    def fahrenheit(self, wert):
        self.celsius = (wert - 32) * 5/9
    
    # Property für Kelvin (berechnet aus Celsius)
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    # Setter für Kelvin (konvertiert zu Celsius)
    @kelvin.setter
    def kelvin(self, wert):
        self.celsius = wert - 273.15

# Temperatur-Objekt erstellen
temp = Temperatur(25)  # 25°C

# Getter-Properties verwenden
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

# Setter-Properties verwenden
print("\nÄndere auf 30°C:")
temp.celsius = 30
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

print("\nÄndere auf 86°F:")
temp.fahrenheit = 86
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

print("\nÄndere auf 300K:")
temp.kelvin = 300
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

# Versuch, eine ungültige Temperatur zu setzen
try:
    temp.celsius = -300  # Unter dem absoluten Nullpunkt
except ValueError as e:
    print(f"\nFehler: {e}")
"""

# Beispiel: Abstrakte Klassen
abstract_classes = """
from abc import ABC, abstractmethod

class Tier(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def laut_machen(self):
        # Diese Methode muss von allen Kindklassen implementiert werden
        pass
    
    @abstractmethod
    def bewegen(self):
        # Diese Methode muss von allen Kindklassen implementiert werden
        pass
    
    def essen(self):
        # Nicht-abstrakte Methode, kann aber überschrieben werden
        return f"{self.name} isst."

class Hund(Tier):
    def laut_machen(self):
        return f"{self.name} sagt: Wuff!"
    
    def bewegen(self):
        return f"{self.name} läuft."

class Vogel(Tier):
    def laut_machen(self):
        return f"{self.name} sagt: Piep!"
    
    def bewegen(self):
        return f"{self.name} fliegt."
    
    # Überschreibt die nicht-abstrakte Methode
    def essen(self):
        return f"{self.name} pickt Körner."

# Versuche eine abstrakte Klasse zu instanziieren
try:
    tier = Tier("Generisches Tier")  # Dies sollte fehlschlagen
except TypeError as e:
    print(f"Fehler beim Erstellen einer abstrakten Klasse: {e}")

# Konkrete Klassen instanziieren
hund = Hund("Bello")
vogel = Vogel("Tweety")

# Methoden aufrufen
print(hund.laut_machen())
print(hund.bewegen())
print(hund.essen())

print("\n" + vogel.laut_machen())
print(vogel.bewegen())
print(vogel.essen())
"""

# Beispiel: Slots
slots_example = """
import sys

# Klasse ohne __slots__
class PersonOhneSlots:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# Klasse mit __slots__ (begrenzt mögliche Attribute)
class PersonMitSlots:
    __slots__ = ['name', 'alter']  # Nur diese Attribute sind erlaubt
    
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# Objekte erstellen
person1 = PersonOhneSlots("Anna", 30)
person2 = PersonMitSlots("Max", 25)

# Speicherverbrauch vergleichen
print(f"Größe ohne Slots: {sys.getsizeof(person1)} Bytes")
print(f"Größe mit Slots: {sys.getsizeof(person2)} Bytes")

# Dynamische Attributhinzufügung testen
person1.beruf = "Entwickler"  # Funktioniert
print(f"Beruf von person1: {person1.beruf}")

try:
    person2.beruf = "Designer"  # Dies sollte einen Fehler auslösen
except AttributeError as e:
    print(f"Fehler bei person2: {e}")

# __dict__ testen
print(f"person1.__dict__: {person1.__dict__}")
try:
    print(person2.__dict__)  # Objekte mit __slots__ haben kein __dict__
except AttributeError as e:
    print(f"Fehler beim Zugriff auf __dict__: {e}")
"""

# Beispiel: Metaklassen
metaclass_example = """
# Eine einfache Metaklasse
class MeineMetaklasse(type):
    def __new__(mcs, name, bases, attrs):
        # Alle Methodennamen in Großbuchstaben umwandeln
        uppercase_attrs = {
            key.upper() if not key.startswith('__') else key: value
            for key, value in attrs.items()
        }
        
        # Debug-Ausgabe
        print(f"Erstelle Klasse {name} mit überarbeiteten Attributen")
        
        # Klasse erstellen
        return super().__new__(mcs, name, bases, uppercase_attrs)

# Eine Klasse, die unsere Metaklasse verwendet
class MeineKlasse(metaclass=MeineMetaklasse):
    def methode_eins(self):
        return "Dies ist Methode eins"
    
    def methode_zwei(self):
        return "Dies ist Methode zwei"

# Objekt erstellen und testen
obj = MeineKlasse()

# Die Methodennamen wurden in Großbuchstaben umgewandelt
try:
    print(obj.methode_eins())  # Sollte nicht funktionieren
except AttributeError as e:
    print(f"Fehler: {e}")

print(obj.METHODE_EINS())  # Jetzt mit Großbuchstaben
print(obj.METHODE_ZWEI())  # Jetzt mit Großbuchstaben

# Weitere Metaklassen-Anwendung: Singleton-Muster
class SingletonMetaklasse(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMetaklasse):
    def __init__(self, wert=None):
        self.wert = wert

# Testen des Singleton-Verhaltens
singleton1 = Singleton(1)
singleton2 = Singleton(2)  # Sollte dieselbe Instanz zurückgeben

print(f"singleton1.wert: {singleton1.wert}")
print(f"singleton2.wert: {singleton2.wert}")  # Sollte immer noch 1 sein
print(f"Sind die Objekte identisch? {singleton1 is singleton2}")
"""

# Beispiel: Dataclasses
dataclass_example = """
from dataclasses import dataclass, field

# Basis-Dataclass
@dataclass
class Person:
    name: str
    alter: int
    email: str = field(default="", repr=False)  # Default-Wert und nicht in repr zeigen
    freunde: list = field(default_factory=list)  # Default ist eine leere Liste
    
    def geburtstag_feiern(self):
        self.alter += 1
        return f"{self.name} ist jetzt {self.alter} Jahre alt!"

# Vererbung mit Dataclasses
@dataclass
class Student(Person):
    uni: str
    studiengang: str
    semester: int = 1
    
    def semester_abschließen(self):
        self.semester += 1
        return f"{self.name} ist jetzt im {self.semester}. Semester"

# Objekte erstellen und testen
person = Person("Anna", 30, "anna@example.com")
student = Student("Max", 22, "max@uni.edu", [], "TU Berlin", "Informatik")

print(person)  # __repr__ wird automatisch generiert
print(student)  # Enthält auch die Attribute der Elternklasse

# Methoden aufrufen
print(person.geburtstag_feiern())
print(student.semester_abschließen())

# Demonstration der generierten Methoden
person2 = Person("Anna", 30, "anna@example.com")
print(f"person == person2: {person == person2}")  # __eq__ automatisch generiert

# Änderungen vornehmen
person.freunde.append("Max")
print(f"Freunde von {person.name}: {person.freunde}")
"""

# Beispiel: Bankkonto mit Properties
# Beispiel für Bankkonto mit Properties - als Code-Beispiel für das Tutorial
bank_account_properties = '''
# Definition der Bankkonto-Klasse
class Bankkonto:
    def __init__(self, kontonummer, inhaber, anfangsguthaben=0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self._guthaben = anfangsguthaben  # _guthaben ist "privat"
        self._gesperrt = False
        self._transaktionen = []
    
    @property
    def guthaben(self):
        # Getter für Guthaben
        if self._gesperrt:
            return "Konto gesperrt"
        return self._guthaben
    
    @property
    def ist_gesperrt(self):
        # Getter für gesperrt-Status
        return self._gesperrt
    
    @property
    def transaktionen(self):
        # Getter für Transaktionsliste
        return self._transaktionen.copy()  # Kopie zurückgeben, um direkte Änderungen zu verhindern
    
    def einzahlen(self, betrag):
        # Geld einzahlen
        if self._gesperrt:
            return "Konto gesperrt. Einzahlung nicht möglich."
        
        if betrag <= 0:
            return "Betrag muss größer als 0 sein."
        
        self._guthaben += betrag
        self._transaktionen.append(f"Einzahlung: +{betrag}€")
        return f"{betrag}€ eingezahlt. Neues Guthaben: {self._guthaben}€"
    
    def abheben(self, betrag):
        # Geld abheben
        if self._gesperrt:
            return "Konto gesperrt. Abhebung nicht möglich."
        
        if betrag <= 0:
            return "Betrag muss größer als 0 sein."
        
        if betrag > self._guthaben:
            return "Nicht genügend Guthaben."
        
        self._guthaben -= betrag
        self._transaktionen.append(f"Abhebung: -{betrag}€")
        return f"{betrag}€ abgehoben. Neues Guthaben: {self._guthaben}€"
    
    def sperren(self):
        # Konto sperren
        self._gesperrt = True
        self._transaktionen.append("Konto gesperrt")
        return "Konto wurde gesperrt."
    
    def entsperren(self):
        # Konto entsperren
        self._gesperrt = False
        self._transaktionen.append("Konto entsperrt")
        return "Konto wurde entsperrt."
    
    def kontoauszug(self):
        # Kontoauszug erstellen
        status = "gesperrt" if self._gesperrt else "aktiv"
        auszug = f"Kontoauszug für {self.inhaber} (Konto: {self.kontonummer})\\n"
        auszug += f"Status: {status}\\n"
        auszug += f"Aktuelles Guthaben: {self._guthaben}€\\n"
        auszug += "Transaktionen:\\n"
        for transaktion in self._transaktionen:
            auszug += f"- {transaktion}\\n"
        return auszug

# Beispiel-Code zur Verwendung des Bankkontos
konto = Bankkonto("DE123456789", "Max Mustermann", 1000)
konto.einzahlen(500)
konto.abheben(200)
print(f"Aktuelles Guthaben: {konto.guthaben}€")
konto.sperren()
konto.abheben(100)
konto.entsperren()
konto.abheben(100)
print(konto.kontoauszug())
'''

# Echte Implementierung der Bankkonto-Klasse für interaktive Beispiele im Tutorial
class Bankkonto:
    def __init__(self, kontonummer, inhaber, anfangsguthaben=0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self._guthaben = anfangsguthaben
        self._gesperrt = False
        self._transaktionen = []
    
    @property
    def guthaben(self):
        # Getter für Guthaben
        if self._gesperrt:
            return "Konto gesperrt"
        return self._guthaben
    
    @property
    def ist_gesperrt(self):
        # Getter für gesperrt-Status
        return self._gesperrt
    
    @property
    def transaktionen(self):
        # Getter für Transaktionsliste
        return self._transaktionen.copy()
    
    def einzahlen(self, betrag):
        # Geld einzahlen
        if self._gesperrt:
            return "Konto gesperrt. Einzahlung nicht möglich."
        
        if betrag <= 0:
            return "Betrag muss größer als 0 sein."
        
        self._guthaben += betrag
        self._transaktionen.append(f"Einzahlung: +{betrag}€")
        return f"{betrag}€ eingezahlt. Neues Guthaben: {self._guthaben}€"
    
    def abheben(self, betrag):
        # Geld abheben
        if self._gesperrt:
            return "Konto gesperrt. Abhebung nicht möglich."
        
        if betrag <= 0:
            return "Betrag muss größer als 0 sein."
        
        if betrag > self._guthaben:
            return "Nicht genügend Guthaben."
        
        self._guthaben -= betrag
        self._transaktionen.append(f"Abhebung: -{betrag}€")
        return f"{betrag}€ abgehoben. Neues Guthaben: {self._guthaben}€"
    
    def sperren(self):
        # Konto sperren
        self._gesperrt = True
        self._transaktionen.append("Konto gesperrt")
        return "Konto wurde gesperrt."
    
    def entsperren(self):
        # Konto entsperren
        self._gesperrt = False
        self._transaktionen.append("Konto entsperrt")
        return "Konto wurde entsperrt."
    
    def kontoauszug(self):
        # Kontoauszug erstellen
        status = "gesperrt" if self._gesperrt else "aktiv"
        auszug = f"Kontoauszug für {self.inhaber} (Konto: {self.kontonummer})\n"
        auszug += f"Status: {status}\n"
        auszug += f"Aktuelles Guthaben: {self._guthaben}€\n"
        auszug += "Transaktionen:\n"
        for transaktion in self._transaktionen:
            auszug += f"- {transaktion}\n"
        return auszug
