import streamlit as st
import examples
import quiz
from utils import syntax_highlight, run_code
from streamlit_ace import st_ace

# Page configuration
st.set_page_config(
    page_title="Python Klassen Tutorial",
    page_icon="🐍",
    layout="wide"
)

# Custom CSS für Code-Blöcke und bessere Lesbarkeit
st.markdown("""
<style>
    /* Syntax-Highlighting und monospace Schriften für alle Code-Elemente */
    .stCode, pre, code, .CodeMirror, .stTextArea textarea {
        font-family: 'Courier New', monospace !important;
    }
    
    /* Zusätzlich für die editierbaren Textfelder */
    textarea, .stTextInput input, div[data-baseweb="textarea"] textarea, .stTextArea>div>div>textarea {
        font-family: 'Courier New', monospace !important;
        font-size: 1rem !important;
        line-height: 1.4 !important;
    }
    
    /* Für bessere Lesbarkeit von Code-Blöcken */
    .highlight {
        background-color: #f0f2f6;
        border-radius: 4px;
        padding: 0.2em 0.4em;
    }
    
    /* Speziell für Code-Editoren */
    .stTextArea textarea {
        border: 1px solid #ccc;
        background-color: #f9f9f9;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Anpassung für StreamlitApp */
    .streamlit-expanderContent pre {
        font-family: 'Courier New', monospace !important;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🐍 Python Klassen: Interaktives Tutorial")

# Navigation in der Sidebar
st.sidebar.markdown("## 📚 Themen")

# Definiere alle Themen
topics = [
    "Einführung: Entdecke die Magie der Klassen!",
    "Klassen erstellen und Objekte instanziieren",
    "Konstruktoren und Attribute",
    "Methoden und self",
    "Vererbung",
    "Polymorphismus",
    "Dunder-Methoden (Magic Methods)",
    "Klassenattribute vs. Instanzattribute",
    "Fortgeschrittene Konzepte",
    "Abschlussquiz"
]

# Wenn noch kein Thema ausgewählt wurde, setze das erste Thema als Standard
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = topics[0]

# Erzeuge für jedes Thema einen Button in der Sidebar
for topic in topics:
    if st.sidebar.button(topic, key=f"btn_{topic}"):
        st.session_state.selected_topic = topic

# Hole das ausgewählte Thema aus dem Sessionstate
selected_topic = st.session_state.selected_topic

# Topic content
if selected_topic == "Einführung: Entdecke die Magie der Klassen!":
    st.header("Einführung: Entdecke die Magie der Klassen!")
    
    st.markdown("""
    ## Was sind Klassen in Python?
    
    Stell dir Klassen wie **Baupläne** für Objekte vor. Sie definieren:
    - Welche **Daten** (Attribute) ein Objekt speichern kann
    - Welche **Funktionen** (Methoden) ein Objekt ausführen kann
    
    Im echten Leben könntest du dir eine Klasse wie einen Bauplan für ein Möbelstück vorstellen:
    - **Attribute** wären Material, Farbe, Größe, Gewicht
    - **Methoden** wären zusammenbauen(), verstellen(), transportieren()
    
    Jeder einzelne Schrank ist eine **Instanz** (ein Objekt) der Schrank-Klasse.
    """)
    
    # Bild von einem OOP-Diagramm 
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <img src="https://www.w3schools.com/python/img_oop_object.png" alt="OOP Konzept" width="500"/>
        <p style="font-style: italic; margin-top: 10px;">Konzept der objektorientierten Programmierung</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Warum Klassen verwenden?
    
    Klassen helfen uns, Code zu **organisieren** und **wiederzuverwenden**. Sie sind ein fundamentales Konzept der **objektorientierten Programmierung** (OOP).
    
    Vorteile von Klassen:
    - **Kapselung**: Daten und Methoden werden zusammen verpackt
    - **Wiederverwendbarkeit**: Code kann einfach wiederverwendet werden
    - **Modularität**: Komplexe Systeme können in überschaubare Teile aufgeteilt werden
    """)
    
    st.markdown("### Hier ist ein erstes, einfaches Beispiel:")
    code = examples.intro_example
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="intro_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Was ist hier passiert?
    
    1. Wir haben eine Klasse `Dog` definiert
    2. Wir haben zwei Hunde-Objekte (`rex` und `bella`) erstellt
    3. Jeder Hund hat seinen eigenen Namen und kann bellen
    
    Im nächsten Abschnitt lernen wir, wie man eigene Klassen erstellt!
    """)
    
    st.markdown("""
    ### Klassen sind wie Formen für Kekse 🍪
    
    Stelle dir vor, du backst Kekse:
    - Die **Klasse** ist deine Keksform
    - Die **Objekte** sind die einzelnen Kekse
    - Die **Attribute** sind die Zutaten und Eigenschaften (Größe, Farbe, Geschmack)
    - Die **Methoden** sind die Aktionen, die du mit den Keksen machen kannst (essen, dekorieren)
    
    Mit einer Keksform (Klasse) kannst du viele ähnliche Kekse (Objekte) herstellen, aber jeder Keks kann unterschiedlich dekoriert werden oder verschiedene Zutaten enthalten (unterschiedliche Attributwerte).
    """)
    
    # Interaktives Element
    st.markdown("### Probier es selbst aus - erstelle deinen eigenen Hund!")
    
    name = st.text_input("Gib deinem Hund einen Namen:")
    age = st.slider("Wie alt ist dein Hund?", 0, 20, 3)
    breed = st.selectbox("Wähle eine Rasse:", ["Labrador", "Dachshund", "Shepherd", "Pug", "Mixed"])
    
    # Zeige den Code an, der ausgeführt wird
    dog_code_template = f'''
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return f"{{self.name}} says: Woof Woof!"
    
    def info(self):
        return f"{{self.name}} is a {{self.age}} year old {{self.breed}}."

# Create your dog
my_dog = Dog("{name or 'Rex'}", {age}, "{breed}")

# Display information
print(my_dog.info())
print(my_dog.bark())
'''
    
    st.code(dog_code_template, language="python")
    
    if st.button("Hund erstellen", key="create_dog"):
        # Formatiere den Code mit den tatsächlichen Werten
        code_to_run = f'''
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return f"{{self.name}} says: Woof Woof!"
    
    def info(self):
        return f"{{self.name}} is a {{self.age}} year old {{self.breed}}."

# Create your dog
my_dog = Dog("{name}", {age}, "{breed}")

# Display information
print(my_dog.info())
print(my_dog.bark())
'''
        output = run_code(code_to_run)
        st.write("### Dein Hund:")
        st.code(output)

elif selected_topic == "Klassen erstellen und Objekte instanziieren":
    st.header("Klassen erstellen und Objekte instanziieren")
    
    st.markdown("""
    ## Wie erstellt man eine Klasse?
    
    In Python erstellt man eine Klasse mit dem Schlüsselwort `class`:
    """)
    
    code = examples.class_creation
    st.code(code, language="python")
    
    st.markdown("""
    ## Objekte erstellen (instanziieren)
    
    Nachdem wir eine Klasse definiert haben, können wir Objekte (Instanzen) dieser Klasse erstellen:
    """)
    
    code = examples.class_instantiation
    st.code(code, language="python")
    
    st.markdown("""
    ### Probier es selbst aus!
    
    Hier kannst du den Code bearbeiten und ausführen:
    """)
    
    default_code = examples.class_interactive
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="interactive_code_editor",
        min_lines=15,
        max_lines=25,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="class_create_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Wichtige Punkte:
    
    - Klassennamen beginnen üblicherweise mit einem Großbuchstaben
    - Instanzen werden erstellt, indem man die Klasse wie eine Funktion aufruft: `MeineKlasse()`
    - Jede Instanz ist ein eigenes Objekt mit eigenen Attributen
    """)
    
    st.markdown("""
    ### Objekte sind wie individuelle Spiel-Charaktere
    
    Stelle dir vor, du erstellst Charaktere in einem Spiel:
    
    ```python
    class GameCharacter:
        pass
        
    hero = GameCharacter()       # Erster Charakter
    hero.name = "Aragorn"
    hero.character_class = "Warrior"
    hero.strength = 95
    
    wizard = GameCharacter()     # Zweiter Charakter
    wizard.name = "Gandalf" 
    wizard.character_class = "Wizard"
    wizard.magic = 100
    ```
    
    Jeder Charakter ist ein eigenes Objekt mit individuellen Eigenschaften!
    """)

elif selected_topic == "Konstruktoren und Attribute":
    st.header("Konstruktoren und Attribute")
    
    st.markdown("""
    ## Der Konstruktor: `__init__`
    
    Der Konstruktor ist eine spezielle Methode, die automatisch aufgerufen wird, wenn ein neues Objekt erstellt wird.
    
    In Python ist der Konstruktor die `__init__`-Methode:
    """)
    
    code = examples.constructor_example
    st.code(code, language="python")
    
    st.markdown("""
    ### Attribute festlegen
    
    Im Konstruktor werden typischerweise die Attribute eines Objekts festgelegt:
    - Attribute sind Variablen, die zu einem Objekt gehören
    - Sie speichern den Zustand eines Objekts
    - Auf Attribute greift man mit dem Punktoperator zu: `objekt.attribut`
    """)
    
    code = examples.attributes_example
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="constructor_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Der Konstruktor ist wie ein Geburtshelfer
    
    Stelle dir vor, der `__init__`-Konstruktor ist wie ein Geburtshelfer für deine Objekte:
    
    - Er wird automatisch gerufen, wenn ein neues Objekt "geboren" wird
    - Er bereitet das neue Objekt auf seine Existenz vor
    - Er stattet das Objekt mit allem aus, was es für sein Leben braucht (Attribute)
    
    Ohne einen gut definierten Konstruktor wären deine Objekte wie Babys ohne Namen, Identität oder Eigenschaften!
    """)
    
    st.markdown("""
    ### Praktische Übung
    
    Erstelle eine Klasse `Student` mit Attributen für Name, Alter und Studienfach:
    """)
    
    default_code = examples.student_class
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="student_code_editor",
        min_lines=15,
        max_lines=25,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="student_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Zusammenfassung:
    
    - Der `__init__`-Konstruktor wird automatisch aufgerufen, wenn ein neues Objekt erstellt wird
    - Der erste Parameter ist immer `self` und bezieht sich auf die aktuelle Instanz
    - Attribute werden mit `self.attributname` definiert
    - Attribute können mit Werten initialisiert werden, die beim Erstellen des Objekts übergeben werden
    """)

elif selected_topic == "Methoden und self":
    st.header("Methoden und self")
    
    st.markdown("""
    ## Was sind Methoden?
    
    Methoden sind Funktionen, die zu einer Klasse gehören. Sie definieren das **Verhalten** der Objekte:
    
    - Methoden werden innerhalb der Klasse definiert
    - Der erste Parameter einer Methode ist immer `self`
    - `self` bezieht sich auf das aktuelle Objekt
    """)
    
    code = examples.methods_example
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="methods_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ## Warum `self`?
    
    `self` ist eine Referenz auf die aktuelle Instanz:
    
    - Es ermöglicht den Zugriff auf Attribute und andere Methoden innerhalb der Klasse
    - Es muss immer als erster Parameter angegeben werden
    - Beim Methodenaufruf wird `self` automatisch übergeben
    
    Ohne `self` wüsste Python nicht, auf welches spezifische Objekt sich die Methode bezieht.
    """)
    
    st.markdown("""
    ### `self` ist wie ein Namensschild
    
    Stelle dir vor, du bist auf einer Party mit vielen identisch aussehenden Zwillingen:
    
    - Jeder Zwilling trägt ein Namensschild (`self`), um seine Identität zu zeigen
    - Wenn jemand eine Aktion ausführt (eine Methode aufruft), weiß man durch das Namensschild, wer genau die Aktion ausführt
    - Ohne Namensschilder könnte niemand unterscheiden, welcher Zwilling was tut
    
    In Python erlaubt `self` den Objekten, ihre eigene Identität zu kennen und ihre eigenen Daten zu verwenden.
    """)
    
    st.markdown("""
    ### Verschiedene Arten von Methoden
    
    In Python gibt es drei Haupttypen von Methoden:
    
    1. **Instanzmethoden**: Arbeiten mit Objektattributen (verwenden `self`)
    2. **Klassenmethoden**: Arbeiten mit Klassenattributen (verwenden `@classmethod` und `cls`)
    3. **Statische Methoden**: Gehören zur Klasse, arbeiten aber nicht mit Klassen- oder Instanzdaten (`@staticmethod`)
    """)
    
    code = examples.method_types
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="method_types_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Übung: Bankkonto mit Methoden
    
    Erstelle eine Klasse `Bankkonto` mit Methoden zum Einzahlen und Abheben:
    """)
    
    default_code = examples.bank_account
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="bank_code_editor",
        min_lines=15,
        max_lines=25,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="bank_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Zusammenfassung:
    
    - Methoden definieren das Verhalten von Objekten
    - `self` bezieht sich auf die aktuelle Instanz
    - Es gibt verschiedene Arten von Methoden: Instanzmethoden, Klassenmethoden und statische Methoden
    - Methoden können mit anderen Methoden interagieren und auf Attribute zugreifen
    """)

elif selected_topic == "Vererbung":
    st.header("Vererbung")
    
    st.markdown("""
    ## Was ist Vererbung?
    
    Vererbung ist ein Konzept, bei dem eine Klasse (die Kindklasse) Eigenschaften und Methoden einer anderen Klasse (der Elternklasse) übernimmt.
    
    Vorteile der Vererbung:
    - Code-Wiederverwendung
    - Erstellung von Klassenhierarchien
    - Logische Organisation von Code
    """)
    
    st.markdown("""
    ### Vererbung ist wie ein Familienstammbaum
    
    Stelle dir vor, Vererbung funktioniert wie in einer Familie:
    
    - Die **Elternklasse** gibt ihre "Gene" (Attribute und Methoden) an ihre "Kinder" weiter
    - **Kindklassen** erben alle Eigenschaften ihrer Eltern
    - **Kindklassen** können zusätzliche Eigenschaften haben oder geerbte Eigenschaften verändern
    - Mehrere Kinder können vom selben Elternteil erben (und sich trotzdem unterscheiden)
    
    Genau wie ein Kind Augenfarbe oder Haarfarbe von seinen Eltern erben kann, erbt eine Kindklasse Attribute und Methoden von ihrer Elternklasse!
    """)
    
    st.markdown("""
    ### Wie funktioniert Vererbung in Python?
    
    In Python wird Vererbung durch Angabe der Elternklasse in Klammern nach dem Namen der Kindklasse implementiert:
    """)
    
    code = examples.inheritance_basic
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="inheritance_basic_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Die `super()`-Funktion
    
    Die `super()`-Funktion ermöglicht den Zugriff auf Methoden der Elternklasse:
    """)
    
    code = examples.super_function
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="super_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Mehrfachvererbung
    
    Python unterstützt auch Mehrfachvererbung, bei der eine Klasse von mehreren Elternklassen erben kann:
    """)
    
    code = examples.multiple_inheritance
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="multiple_inherit_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Übung: Fahrzeug-Hierarchie
    
    Erstelle eine Klassenhierarchie für verschiedene Fahrzeugtypen:
    """)
    
    default_code = examples.vehicle_hierarchy
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="vehicle_code_editor",
        min_lines=15,
        max_lines=25,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="vehicle_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Zusammenfassung:
    
    - Vererbung ermöglicht die Wiederverwendung von Code
    - Eine Kindklasse erbt alle Attribute und Methoden der Elternklasse
    - Mit `super()` kann auf die Elternklassenmethoden zugegriffen werden
    - Python unterstützt Mehrfachvererbung
    """)

elif selected_topic == "Polymorphismus":
    st.header("Polymorphismus")
    
    st.markdown("""
    ## Was ist Polymorphismus?
    
    Polymorphismus bedeutet "viele Formen" und ist ein Konzept, bei dem:
    
    - Objekte verschiedener Klassen über eine gemeinsame Schnittstelle angesprochen werden können
    - Eine Methode je nach Kontext unterschiedlich reagieren kann
    
    Polymorphismus ist eng mit Vererbung verbunden und ein Grundprinzip der objektorientierten Programmierung.
    """)
    
    st.markdown("""
    ### Polymorphismus ist wie ein Universaladapter
    
    Stelle dir Polymorphismus wie einen Universalstecker vor:
    
    - Du kannst verschiedene Geräte (Klassen) anschließen
    - Jedes Gerät reagiert anders, wenn es Strom bekommt (gleiche Methode, verschiedenes Verhalten)
    - Der Stecker kümmert sich nicht darum, was angeschlossen ist - er funktioniert mit allem
    
    In Python ermöglicht uns Polymorphismus, verschiedene Objekte mit der gleichen Schnittstelle zu behandeln, obwohl sie unterschiedlich reagieren!
    """)
    
    st.markdown("""
    ### Beispiel für Polymorphismus
    
    Hier ein Beispiel, wie verschiedene Tiere unterschiedliche Laute von sich geben:
    """)
    
    code = examples.polymorphism_basic
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="poly_basic_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Methoden-Überschreibung (Method Overriding)
    
    Bei der Methoden-Überschreibung implementiert eine Kindklasse eine Methode neu, die bereits in der Elternklasse existiert:
    """)
    
    code = examples.method_overriding
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="override_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Duck Typing
    
    Python folgt dem Prinzip "Duck Typing": "Wenn es wie eine Ente aussieht und wie eine Ente quakt, dann ist es wahrscheinlich eine Ente."
    
    Das bedeutet, dass der Typ eines Objekts weniger wichtig ist als sein Verhalten (seine Methoden und Eigenschaften):
    """)
    
    code = examples.duck_typing
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="duck_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Übung: Geometrische Formen
    
    Implementiere verschiedene geometrische Formen mit einer gemeinsamen Methode zur Flächenberechnung:
    """)
    
    default_code = """import math

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
        super().__init__(seite, seite)  # Wir nutzen den Rechteck-Konstruktor
        self.seite = seite
    
    def __str__(self):
        return f"Quadrat mit Seitenlänge {self.seite}"

# Formen erstellen
formen = [
    Kreis(5),
    Rechteck(4, 6),
    Quadrat(3)
]

# Polymorphismus in Aktion
for form in formen:
    print(f"{form}:")
    print(f"  Fläche: {form.fläche():.2f}")
    print(f"  Umfang: {form.umfang():.2f}")
"""
    st.code(default_code, language="python", line_numbers=True)
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="shapes_code_editor",
        min_lines=15,
        max_lines=30,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="shapes_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Zusammenfassung:
    
    - Polymorphismus erlaubt es, verschiedene Klassen einheitlich zu behandeln
    - Methoden-Überschreibung ermöglicht es Kindklassen, das Verhalten der Elternklasse anzupassen
    - Duck Typing in Python konzentriert sich auf das Verhalten von Objekten, nicht auf ihre Typen
    - Polymorphismus macht Code flexibler und leichter erweiterbar
    """)

elif selected_topic == "Dunder-Methoden (Magic Methods)":
    st.header("Dunder-Methoden (Magic Methods)")
    
    st.markdown("""
    ## Was sind Dunder-Methoden?
    
    "Dunder" steht für "Double Underscore" (doppelter Unterstrich). Diese speziellen Methoden werden auch als "Magic Methods" bezeichnet.
    
    Sie beeinflussen, wie Objekte mit eingebauten Python-Funktionen und Operatoren interagieren:
    
    - Beginnen und enden mit doppelten Unterstrichen: `__method__`
    - Werden automatisch aufgerufen, wenn bestimmte Aktionen ausgeführt werden
    - Erlauben die Anpassung des Standardverhaltens von Objekten
    """)
    
    st.markdown("""
    ### Dunder-Methoden sind wie Zaubersprüche
    
    Stelle dir Dunder-Methoden wie magische Zaubersprüche vor:
    
    - Sie haben eine besondere Syntax (beginnen und enden mit `__`)
    - Sie werden automatisch "ausgelöst", wenn bestimmte Aktionen passieren
    - Sie verleihen deinen Objekten "magische Fähigkeiten" (spezielle Verhaltensweisen)
    
    Mit Dunder-Methoden kannst du Objekte erstellen, die sich wie eingebaute Python-Typen verhalten - sie können addiert, verglichen, in Listen verwendet oder als Strings ausgegeben werden!
    """)
    
    st.markdown("""
    ### Häufig verwendete Dunder-Methoden
    
    Hier sind einige der wichtigsten Dunder-Methoden:
    
    - `__init__`: Konstruktor (wird beim Erstellen eines Objekts aufgerufen)
    - `__str__`: String-Darstellung (wird bei `str()` oder `print()` aufgerufen)
    - `__repr__`: "Offizielle" String-Darstellung (wird bei `repr()` aufgerufen)
    - `__len__`: Gibt die Länge zurück (wird bei `len()` aufgerufen)
    - `__add__`, `__sub__`, etc.: Arithmetische Operatoren (+, -, etc.)
    - `__eq__`, `__lt__`, etc.: Vergleichsoperatoren (==, <, etc.)
    """)
    
    st.markdown("""
    ### Beispiel: String-Darstellung und Vergleich
    """)
    
    code = """class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    # Wird bei print() oder str() aufgerufen
    def __str__(self):
        return f"{self.name}, {self.alter} Jahre"
    
    # Wird bei repr() aufgerufen (für Debugging)
    def __repr__(self):
        return f"Person('{self.name}', {self.alter})"
    
    # Vergleichsoperatoren
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.alter == other.alter
    
    def __lt__(self, other):
        if not isinstance(other, Person):
            raise TypeError("Kann Person nur mit anderer Person vergleichen")
        return self.alter < other.alter

# Personen erstellen
person1 = Person("Anna", 30)
person2 = Person("Max", 25)
person3 = Person("Anna", 30)  # Gleiche Werte wie person1

# String-Darstellung testen
print(str(person1))  # Ruft __str__ auf
print(repr(person1))  # Ruft __repr__ auf

# Vergleiche testen
print(f"person1 == person2: {person1 == person2}")  # Ruft __eq__ auf
print(f"person1 == person3: {person1 == person3}")  # Ruft __eq__ auf
print(f"person1 < person2: {person1 < person2}")    # Ruft __lt__ auf
print(f"person2 < person1: {person2 < person1}")    # Ruft __lt__ auf
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="dunder_basic_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Operatoren überladen
    
    Mit Dunder-Methoden kannst du auch festlegen, wie Objekte auf Operatoren reagieren:
    """)
    
    code = """class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Addition mit + Operator
    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)
    
    # Subtraktion mit - Operator
    def __sub__(self, other):
        return Vektor(self.x - other.x, self.y - other.y)
    
    # Multiplikation mit * Operator
    def __mul__(self, skalar):
        return Vektor(self.x * skalar, self.y * skalar)
    
    # Länge mit len() Funktion
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    # String-Darstellung
    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

# Vektoren erstellen
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

# Operationen mit Vektoren
v3 = v1 + v2  # Addition
v4 = v1 - v2  # Subtraktion
v5 = v1 * 2   # Multiplikation mit Skalar

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"v1 - v2 = {v4}")
print(f"v1 * 2 = {v5}")
print(f"Länge von v1: {len(v1)}")
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="operator_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Übung: Karte für ein Kartenspiel
    
    Erstelle eine `Karte`-Klasse mit Dunder-Methoden für Vergleich und Darstellung:
    """)
    
    default_code = """class Karte:
    WERTE = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 
             10: "10", 11: "Bube", 12: "Dame", 13: "König", 14: "Ass"}
    FARBEN = {"Herz": "♥", "Karo": "♦", "Pik": "♠", "Kreuz": "♣"}
    
    def __init__(self, wert, farbe):
        self.wert = wert
        self.farbe = farbe
    
    # String-Darstellung
    def __str__(self):
        return f"{self.WERTE[self.wert]} {self.FARBEN[self.farbe]}"
    
    # Offizielle String-Darstellung
    def __repr__(self):
        return f"Karte({self.wert}, '{self.farbe}')"
    
    # Vergleichsoperatoren für den Kartenwert
    def __eq__(self, other):
        return self.wert == other.wert
        
    def __lt__(self, other):
        return self.wert < other.wert
    
    def __gt__(self, other):
        return self.wert > other.wert

# Karten erstellen
karte1 = Karte(14, "Herz")  # Ass
karte2 = Karte(12, "Pik")   # Dame
karte3 = Karte(14, "Karo")  # Ass (anderes Ass)

# Ausgabe
print(f"Karte 1: {karte1}")
print(f"Karte 2: {karte2}")
print(f"Karte 3: {karte3}")

# Vergleiche
print(f"Ist {karte1} > {karte2}? {karte1 > karte2}")
print(f"Ist {karte1} == {karte3}? {karte1 == karte3}")
print(f"Ist {karte2} < {karte3}? {karte2 < karte3}")

# Kartenliste sortieren
karten = [karte2, karte1, karte3]
print("\nUnsortierte Karten:")
for karte in karten:
    print(f"  {karte}")

print("\nSortierte Karten:")
for karte in sorted(karten):
    print(f"  {karte}")
"""
    st.code(default_code, language="python", line_numbers=True)
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="cards_code_editor",
        min_lines=15,
        max_lines=25,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="cards_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Zusammenfassung:
    
    - Dunder-Methoden sind spezielle Methoden, die mit doppelten Unterstrichen beginnen und enden
    - Sie werden automatisch bei bestimmten Operationen aufgerufen
    - Sie ermöglichen die Anpassung des Verhaltens von Objekten
    - Mit ihnen kannst du Operatoren überladen und benutzerdefinierte Klassen wie eingebaute Typen verwenden
    """)

elif selected_topic == "Klassenattribute vs. Instanzattribute":
    st.header("Klassenattribute vs. Instanzattribute")
    
    st.markdown("""
    ## Zwei Arten von Attributen
    
    In Python gibt es zwei Haupttypen von Attributen:
    
    1. **Instanzattribute**: Gehören zu einer spezifischen Instanz (einem Objekt)
    2. **Klassenattribute**: Gehören zur Klasse selbst und werden von allen Instanzen geteilt
    """)
    
    st.markdown("""
    ### Unterschiede visualisiert
    
    Stelle dir eine Klasse als Fabrik vor:
    
    - **Klassenattribute** sind wie die Fabrikeinstellungen - gleich für alle Produkte
    - **Instanzattribute** sind wie individuelle Anpassungen an jedem Produkt
    
    Wenn du die Fabrikeinstellung änderst (Klassenattribut), betrifft das alle zukünftigen Produkte und alle existierenden Produkte, die keine individuellen Anpassungen haben.
    """)
    
    code = """class Student:
    # Klassenattribut - für alle Studenten gleich
    schule = "Python-Universität"
    anzahl_studenten = 0
    
    def __init__(self, name, studienfach):
        # Instanzattribute - für jeden Studenten individuell
        self.name = name
        self.studienfach = studienfach
        Student.anzahl_studenten += 1  # Klassenattribut erhöhen
    
    def info(self):
        return f"{self.name} studiert {self.studienfach} an der {self.schule}"
    
    # Klassenmethode - arbeitet mit Klassenattributen
    @classmethod
    def get_anzahl(cls):
        return cls.anzahl_studenten
    
    # Klassenmethode zum Ändern eines Klassenattributs
    @classmethod
    def schule_umbenennen(cls, neuer_name):
        cls.schule = neuer_name

# Studenten erstellen
student1 = Student("Anna", "Informatik")
student2 = Student("Max", "Mathematik")

# Informationen ausgeben
print(student1.info())
print(student2.info())
print(f"Anzahl Studenten: {Student.get_anzahl()}")

# Auf Klassenattribute zugreifen
print(f"Schule über Klasse: {Student.schule}")
print(f"Schule über Instanz: {student1.schule}")

# Klassenattribut ändern
Student.schule_umbenennen("Pythonic Academy")
print(f"Neuer Schulname für student1: {student1.schule}")
print(f"Neuer Schulname für student2: {student2.schule}")

# Instanzattribut überschreibt Klassenattribut
student1.schule = "Private Tutoring"
print(f"Individuelle Schule für student1: {student1.schule}")
print(f"Schule für student2 bleibt: {student2.schule}")
print(f"Klassenattribut bleibt: {Student.schule}")
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="attributes_compare_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Wann verwendet man was?
    
    - **Klassenattribute** sind nützlich für:
      - Konstanten oder Standardwerte für alle Instanzen
      - Zähler oder Statistiken über alle Instanzen
      - Gemeinsame Ressourcen
    
    - **Instanzattribute** sind besser für:
      - Einzigartige Eigenschaften jedes Objekts
      - Werte, die sich pro Instanz ändern können
    """)
    
    st.markdown("""
    ### Vorsicht bei veränderlichen Klassenattributen!
    
    Bei veränderlichen Objekten (wie Listen oder Dictionaries) als Klassenattribute sollte man vorsichtig sein:
    """)
    
    code = """class Gefährlich:
    # Eine Liste als Klassenattribut
    gemeinsame_liste = []
    
    def __init__(self, name):
        self.name = name
    
    def element_hinzufügen(self, element):
        # Fügt zur gemeinsamen Liste hinzu
        self.gemeinsame_liste.append(element)

class Sicher:
    def __init__(self, name):
        self.name = name
        # Jede Instanz bekommt ihre eigene Liste
        self.eigene_liste = []
    
    def element_hinzufügen(self, element):
        self.eigene_liste.append(element)

# Test mit der gefährlichen Klasse
obj1 = Gefährlich("Objekt 1")
obj2 = Gefährlich("Objekt 2")

obj1.element_hinzufügen("Eintrag von Objekt 1")
print(f"Obj1 Liste: {obj1.gemeinsame_liste}")
print(f"Obj2 Liste: {obj2.gemeinsame_liste}")  # Enthält denselben Eintrag!

# Test mit der sicheren Klasse
safe1 = Sicher("Safe 1")
safe2 = Sicher("Safe 2")

safe1.element_hinzufügen("Eintrag von Safe 1")
print(f"Safe1 Liste: {safe1.eigene_liste}")
print(f"Safe2 Liste: {safe2.eigene_liste}")  # Leer, wie erwartet
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="mutable_attr_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Übung: Produktkatalog
    
    Erstelle eine Klasse `Produkt` mit Klassen- und Instanzattributen:
    """)
    
    default_code = """class Produkt:
    # Klassenattribute
    währung = "€"
    rabatt_prozent = 0  # Globaler Rabatt für alle Produkte
    produkt_count = 0
    
    def __init__(self, name, preis, kategorie):
        # Instanzattribute
        self.name = name
        self.preis = preis
        self.kategorie = kategorie
        self.individueller_rabatt = 0  # Individueller Rabatt für dieses Produkt
        
        # Produktzähler erhöhen
        Produkt.produkt_count += 1
        self.produkt_id = Produkt.produkt_count
    
    def endpreis(self):
        # Berechnet den Endpreis mit Rabatten
        gesamt_rabatt = Produkt.rabatt_prozent + self.individueller_rabatt
        rabatt_faktor = 1 - (gesamt_rabatt / 100)
        return self.preis * rabatt_faktor
    
    def preis_anzeigen(self):
        return f"{self.name}: {self.endpreis():.2f} {Produkt.währung}"
    
    @classmethod
    def globalen_rabatt_setzen(cls, rabatt):
        cls.rabatt_prozent = rabatt
    
    @classmethod
    def währung_ändern(cls, neue_währung):
        cls.währung = neue_währung

# Produkte erstellen
laptop = Produkt("Laptop Pro", 1299.99, "Elektronik")
buch = Produkt("Python Mastery", 49.99, "Bücher")
smartphone = Produkt("SmartPhone X", 899.99, "Elektronik")

# Infos ohne Rabatte anzeigen
print("Originalpreise:")
print(laptop.preis_anzeigen())
print(buch.preis_anzeigen())
print(smartphone.preis_anzeigen())

# Globalen Rabatt setzen (für alle Produkte)
Produkt.globalen_rabatt_setzen(10)
print("\nMit 10% globalem Rabatt:")
print(laptop.preis_anzeigen())
print(buch.preis_anzeigen())
print(smartphone.preis_anzeigen())

# Individuellen Rabatt für ein Produkt setzen
smartphone.individueller_rabatt = 5
print("\nSmartphone mit zusätzlichem 5% Rabatt:")
print(smartphone.preis_anzeigen())

# Währung ändern
Produkt.währung_ändern("$")
print("\nPreise in Dollar:")
print(laptop.preis_anzeigen())
print(buch.preis_anzeigen())
print(smartphone.preis_anzeigen())
"""
    st.code(default_code, language="python", line_numbers=True)
    st.markdown("### Code Editor:")
    user_code = st_ace(
        value=default_code,
        language="python",
        theme="github",
        font_size=14,
        key="product_code_editor",
        min_lines=15,
        max_lines=25,
        auto_update=True
    )
    
    if st.button("Code ausführen", key="product_run"):
        output = run_code(user_code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ### Zusammenfassung:
    
    - **Klassenattribute** werden von allen Instanzen geteilt und direkt in der Klasse definiert
    - **Instanzattribute** sind für jede Instanz einzigartig und werden im `__init__` definiert
    - Vorsicht bei veränderlichen Objekten als Klassenattribute
    - Instanzen können auf Klassenattribute zugreifen, aber wenn sie ein Attribut mit dem gleichen Namen setzen, wird ein neues Instanzattribut erstellt
    """)

elif selected_topic == "Fortgeschrittene Konzepte":
    st.header("Fortgeschrittene Konzepte")
    
    st.markdown("""
    ## Eigenschaften (Properties)
    
    Properties ermöglichen kontrollierten Zugriff auf Attribute:
    - Getter und Setter-Methoden ohne die übliche Syntax
    - Zugriff wie auf normale Attribute, aber mit zusätzlicher Logik
    """)
    
    code = """class Person:
    def __init__(self, vorname, nachname, alter):
        self._vorname = vorname
        self._nachname = nachname
        self._alter = alter
    
    # Getter für voller_name
    @property
    def voller_name(self):
        return f"{self._vorname} {self._nachname}"
    
    # Getter für alter
    @property
    def alter(self):
        return self._alter
    
    # Setter für alter
    @alter.setter
    def alter(self, wert):
        if wert < 0:
            raise ValueError("Alter kann nicht negativ sein")
        self._alter = wert

# Person erstellen
person = Person("Max", "Mustermann", 30)

# Properties verwenden
print(f"Name: {person.voller_name}")
print(f"Alter: {person.alter}")

# Alter ändern
try:
    person.alter = 31
    print(f"Neues Alter: {person.alter}")
    
    person.alter = -5  # Dies wird einen Fehler auslösen
except ValueError as e:
    print(f"Fehler: {e}")

# Dies würde einen Fehler verursachen, da voller_name keinen Setter hat
# person.voller_name = "Anna Musterfrau"
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="property_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ## Abstrakte Basisklassen
    
    Abstrakte Basisklassen definieren eine Schnittstelle, die abgeleitete Klassen implementieren müssen:
    """)
    
    code = """from abc import ABC, abstractmethod

class Form(ABC):
    @abstractmethod
    def fläche(self):
        pass
    
    @abstractmethod
    def umfang(self):
        pass
    
    def info(self):
        return f"Fläche: {self.fläche()}, Umfang: {self.umfang()}"

class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius
    
    def fläche(self):
        return 3.14159 * self.radius ** 2
    
    def umfang(self):
        return 2 * 3.14159 * self.radius

class Rechteck(Form):
    def __init__(self, länge, breite):
        self.länge = länge
        self.breite = breite
    
    def fläche(self):
        return self.länge * self.breite
    
    def umfang(self):
        return 2 * (self.länge + self.breite)

# Dies würde einen Fehler verursachen, da Form abstrakt ist
# form = Form()

# Diese funktionieren, da sie alle abstrakten Methoden implementieren
kreis = Kreis(5)
rechteck = Rechteck(4, 6)

print(f"Kreis: {kreis.info()}")
print(f"Rechteck: {rechteck.info()}")
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="abc_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ## Deskriptoren und Meta-Klassen
    
    Diese fortgeschrittenen Konzepte bieten noch mehr Kontrolle über das Klassenverhalten:
    
    - **Deskriptoren** kontrollieren den Zugriff auf Attribute
    - **Meta-Klassen** sind "Klassen von Klassen" - sie kontrollieren die Klassenerstellung
    """)
    
    code = """# Beispiel für einen Deskriptor
class PositiveNumber:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} muss positiv sein")
        instance.__dict__[self.name] = value

class BankAccount:
    balance = PositiveNumber('balance')
    interest_rate = PositiveNumber('interest_rate')
    
    def __init__(self, owner, balance, interest_rate):
        self.owner = owner
        self.balance = balance  # Wird durch den Deskriptor validiert
        self.interest_rate = interest_rate  # Wird durch den Deskriptor validiert

# Konto erstellen
try:
    account = BankAccount("Max Mustermann", 1000, 0.03)
    print(f"Konto für {account.owner} erstellt mit Guthaben {account.balance}€")
    
    # Dies sollte einen Fehler auslösen
    account.balance = -500
except ValueError as e:
    print(f"Fehler: {e}")
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="descriptor_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ## Dataclasses (ab Python 3.7)
    
    Dataclasses reduzieren den Boilerplate-Code für Klassen, die hauptsächlich Daten speichern:
    """)
    
    code = """from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    alter: int
    studienfach: str
    noten: List[float] = field(default_factory=list)
    
    def notendurchschnitt(self):
        if not self.noten:
            return None
        return sum(self.noten) / len(self.noten)

# Studenten erstellen
student1 = Student("Lisa", 22, "Informatik", [1.3, 2.0, 1.7])
student2 = Student("Tom", 20, "Mathematik")
student2.noten.append(1.0)
student2.noten.append(1.3)

# Ausgabe
print(student1)
print(f"Durchschnitt von {student1.name}: {student1.notendurchschnitt()}")
print(student2)
print(f"Durchschnitt von {student2.name}: {student2.notendurchschnitt()}")

# Automatisch generierte Vergleichsmethoden
student3 = Student("Lisa", 22, "Informatik", [1.3, 2.0, 1.7])
print(f"student1 == student3: {student1 == student3}")
"""
    st.code(code, language="python")
    
    if st.button("Code ausführen", key="dataclass_run"):
        output = run_code(code)
        st.write("### Ausgabe:")
        st.code(output)
    
    st.markdown("""
    ## Zusammenfassung fortgeschrittener Konzepte
    
    Python bietet viele fortgeschrittene Konzepte für Klassen:
    
    - **Properties** (@property) für kontrollierten Zugriff auf Attribute
    - **Abstrakte Basisklassen** für die Definition von Schnittstellen
    - **Deskriptoren** für anpassbares Attributverhalten
    - **Meta-Klassen** für die Kontrolle über die Klassenerstellung
    - **Dataclasses** für datenorientierte Klassen mit weniger Boilerplate
    - **Context Manager** (`__enter__`, `__exit__`) für den with-Block
    - **Mix-ins** für die Wiederverwendung von Funktionalität ohne tiefe Vererbungshierarchien
    
    ### Nächste Schritte
    
    - Übe die Konzepte in eigenen Projekten
    - Erkunde die Python-Standardbibliothek, die viele nützliche Klassen enthält
    - Lerne über Design Patterns und fortgeschrittene OOP-Konzepte
    
    **Viel Erfolg beim Programmieren mit Python-Klassen!**
    """)

elif selected_topic == "Abschlussquiz":
    st.header("Teste dein Wissen über Python-Klassen")
    quiz.run_quiz()

# Footer
st.markdown("---")
st.markdown("🐍 **Python-Klassen Tutorial** | Erstellt mit Streamlit")