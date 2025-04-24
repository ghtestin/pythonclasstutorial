import streamlit as st
import random

def run_quiz():
    # Fragen und Antworten für das Quiz
    all_questions = [
        {
            "frage": "Was ist eine Klasse in Python?",
            "optionen": [
                "Eine Sammlung von Funktionen",
                "Ein Bauplan für Objekte, der Attribute und Methoden definiert",
                "Eine spezielle Variable mit mehreren Werten",
                "Ein anderer Name für eine Python-Datei"
            ],
            "antwort": 1,
            "erklärung": "Eine Klasse ist ein Bauplan für Objekte, der festlegt, welche Attribute (Daten) und Methoden (Funktionen) die Objekte haben."
        },
        {
            "frage": "Was bedeutet das Schlüsselwort 'self' in Klassenmethoden?",
            "optionen": [
                "Es bezieht sich auf die Klasse selbst",
                "Es ist ein optionaler Parameter, der weggelassen werden kann",
                "Es bezieht sich auf die aktuelle Instanz des Objekts",
                "Es ist nur eine Python-Konvention ohne besondere Bedeutung"
            ],
            "antwort": 2,
            "erklärung": "'self' ist eine Referenz auf die aktuelle Instanz und ermöglicht den Zugriff auf Attribute und Methoden des Objekts."
        },
        {
            "frage": "Was macht der '__init__'-Konstruktor?",
            "optionen": [
                "Er initialisiert eine neue Klasse",
                "Er wird aufgerufen, wenn ein Objekt zerstört wird",
                "Er initialisiert die Attribute eines neu erstellten Objekts",
                "Er importiert benötigte Module automatisch"
            ],
            "antwort": 2,
            "erklärung": "Der '__init__'-Konstruktor wird automatisch aufgerufen, wenn ein neues Objekt erstellt wird, und dient zur Initialisierung der Objektattribute."
        },
        {
            "frage": "Was ist Vererbung?",
            "optionen": [
                "Ein Prozess, bei dem eine Klasse Attribute und Methoden einer anderen Klasse übernimmt",
                "Eine Methode, um Variablen zu initialisieren",
                "Ein Sicherheitsmechanismus in Python",
                "Eine Art, wie Python-Module organisiert werden"
            ],
            "antwort": 0,
            "erklärung": "Vererbung ist ein Konzept, bei dem eine Klasse (die Kindklasse) Eigenschaften und Methoden einer anderen Klasse (der Elternklasse) übernimmt."
        },
        {
            "frage": "Wie ruft man in einer Kindklasse eine Methode der Elternklasse auf?",
            "optionen": [
                "parent.method()",
                "self.parent.method()",
                "super().method()",
                "ElternKlasse.method(self)"
            ],
            "antwort": 2,
            "erklärung": "Mit 'super().method()' kann man auf Methoden der Elternklasse zugreifen, auch wenn sie in der Kindklasse überschrieben wurden."
        },
        {
            "frage": "Was ist der Unterschied zwischen Klassenattributen und Instanzattributen?",
            "optionen": [
                "Klassenattribute gehören zur Klasse und werden von allen Instanzen geteilt; Instanzattribute gehören zu einer bestimmten Instanz",
                "Klassenattribute werden in der '__init__'-Methode definiert; Instanzattribute außerhalb",
                "Es gibt keinen Unterschied, beide Begriffe bezeichnen dasselbe",
                "Klassenattribute können nur in Klassenmethoden verwendet werden; Instanzattribute nur in Instanzmethoden"
            ],
            "antwort": 0,
            "erklärung": "Klassenattribute werden von allen Instanzen geteilt, während jedes Objekt seine eigenen Instanzattribute hat."
        },
        {
            "frage": "Was sind 'Magic Methods' oder 'Dunder-Methoden' in Python?",
            "optionen": [
                "Methoden, die mit '__' beginnen und enden, wie '__init__' oder '__str__'",
                "Geheime Methoden, die nicht dokumentiert sind",
                "Methoden, die automatisch optimiert werden",
                "Methoden, die nur in der Python-Shell funktionieren"
            ],
            "antwort": 0,
            "erklärung": "Dunder-Methoden (von 'double underscore') sind spezielle Methoden, die mit doppelten Unterstrichen beginnen und enden. Sie kontrollieren, wie Objekte mit Python-Operatoren und Funktionen interagieren."
        },
        {
            "frage": "Was macht die Methode '__str__'?",
            "optionen": [
                "Sie konvertiert ein Objekt in eine Zeichenkette für die menschliche Lesbarkeit",
                "Sie speichert ein Objekt in einer Datei",
                "Sie vergleicht zwei Objekte auf Gleichheit",
                "Sie zählt die Anzahl der Attribute in einem Objekt"
            ],
            "antwort": 0,
            "erklärung": "Die '__str__'-Methode wird aufgerufen, wenn ein Objekt mit 'str()' oder 'print()' ausgegeben wird, und sollte eine für Menschen lesbare Darstellung zurückgeben."
        },
        {
            "frage": "Was ist Polymorphismus in Python?",
            "optionen": [
                "Die Fähigkeit, eine Methode mit verschiedenen Parametern zu definieren",
                "Die Fähigkeit, Objekte verschiedener Klassen in einheitlicher Weise zu behandeln",
                "Die Möglichkeit, mehrere Klassen zu einer zu kombinieren",
                "Ein Sicherheitsfeature zur Kapselung von Daten"
            ],
            "antwort": 1,
            "erklärung": "Polymorphismus ermöglicht es, Objekte verschiedener Klassen über eine gemeinsame Schnittstelle zu behandeln. In Python wird dies oft durch 'Duck Typing' erreicht."
        },
        {
            "frage": "Was bewirkt der Decorator @property in Python?",
            "optionen": [
                "Er macht ein Attribut unveränderlich (konstant)",
                "Er erlaubt den Zugriff auf private Attribute durch Getter- und Setter-Methoden",
                "Er verhindert, dass eine Methode überschrieben werden kann",
                "Er macht eine Methode zu einer Klassenmethode statt einer Instanzmethode"
            ],
            "antwort": 1,
            "erklärung": "@property ermöglicht es, Methoden wie Attribute zu behandeln und Getter/Setter zu definieren, um kontrollierten Zugriff auf Attribute zu ermöglichen."
        }
    ]
    
    # Initialisierung der Session-State-Variablen
    if 'quiz_initialized' not in st.session_state:
        st.session_state.quiz_initialized = True
        st.session_state.quiz_score = 0
        st.session_state.current_question = 0
        st.session_state.answered = False
        st.session_state.selected_option = None
        st.session_state.quiz_finished = False
        
        # Mische die Fragen und wähle 5 aus
        random.shuffle(all_questions)
        st.session_state.quiz_questions = all_questions[:5]
    
    # Quiz-Header
    st.subheader("Teste dein Wissen über Python-Klassen!")
    
    # Nur wenn das Quiz noch nicht abgeschlossen ist
    if not st.session_state.quiz_finished:
        # Aktuelle Frage aus dem gemischten Satz holen
        current_q = st.session_state.quiz_questions[st.session_state.current_question]
        
        # Fortschrittsanzeige - basierend auf der aktuellen Frage
        if st.session_state.answered:
            # Wenn geantwortet wurde, zeige die aktuelle Frage als erledigt an
            progress_value = (st.session_state.current_question + 1) / len(st.session_state.quiz_questions)
        else:
            # Wenn noch nicht geantwortet wurde, zeige die aktuelle Frage als in Bearbeitung an
            progress_value = st.session_state.current_question / len(st.session_state.quiz_questions)
        
        st.progress(progress_value)
        st.write(f"Frage {st.session_state.current_question + 1} von {len(st.session_state.quiz_questions)}")
        
        # Frage anzeigen
        st.markdown(f"### {current_q['frage']}")
        
        # Unterschiedliche Ansicht je nachdem, ob die Frage beantwortet wurde oder nicht
        if not st.session_state.answered:
            # Antwortoptionen als Radio-Buttons
            option_index = st.radio(
                "Wähle die richtige Antwort:",
                options=range(len(current_q['optionen'])),
                format_func=lambda i: current_q['optionen'][i],
                key=f"radio_{st.session_state.current_question}"
            )
            
            # Button zur Antwortprüfung
            if st.button("Antwort prüfen", key=f"check_answer_{st.session_state.current_question}"):
                # Speichere die gewählte Option
                st.session_state.selected_option = option_index
                st.session_state.answered = True
                
                # Punktezählung
                if option_index == current_q['antwort']:
                    st.session_state.quiz_score += 1
                
                st.rerun()
        else:
            # Anzeige der Ergebnisse nach der Antwort
            result_container = st.container()
            with result_container:
                st.subheader("Auswertung:")
                
                # Zeige alle Optionen mit Markierungen für richtig/falsch
                for i, option in enumerate(current_q['optionen']):
                    # Markiere die ausgewählte Antwort
                    if i == st.session_state.selected_option:
                        if i == current_q['antwort']:
                            # Richtige Antwort wurde ausgewählt
                            st.success(f"✓ {option}")
                        else:
                            # Falsche Antwort wurde ausgewählt
                            st.error(f"✗ {option}")
                    # Markiere die richtige Antwort, falls sie nicht ausgewählt wurde
                    elif i == current_q['antwort']:
                        st.success(f"✓ {option}")
                    else:
                        # Normale nicht-ausgewählte Optionen
                        st.write(f"  {option}")
                
                # Erklärung zur Antwort
                st.info(f"**Erklärung:** {current_q['erklärung']}")
            
            # Button-Container für "Nächste Frage" oder "Quiz beenden"
            button_container = st.container()
            with button_container:
                # Wenn noch Fragen übrig sind, zeige "Nächste Frage"-Button
                if st.session_state.current_question < len(st.session_state.quiz_questions) - 1:
                    if st.button("Nächste Frage", key=f"next_question_{st.session_state.current_question}"):
                        # Zur nächsten Frage wechseln
                        st.session_state.current_question += 1
                        st.session_state.answered = False
                        st.session_state.selected_option = None
                        st.rerun()
                else:
                    # Bei der letzten Frage "Quiz beenden"-Button anzeigen
                    if st.button("Quiz beenden", key="end_quiz"):
                        st.session_state.quiz_finished = True
                        st.rerun()
    else:
        # Anzeige der Endergebnisse
        percent = (st.session_state.quiz_score / len(st.session_state.quiz_questions)) * 100
        
        st.write(f"## Quiz abgeschlossen!")
        st.write(f"Du hast **{st.session_state.quiz_score}** von **{len(st.session_state.quiz_questions)}** Fragen richtig beantwortet ({percent:.1f}%).")
        
        # Bewertung basierend auf dem Prozentsatz
        if percent >= 80:
            st.success("🎉 Herzlichen Glückwunsch! Du beherrschst die Grundlagen der Python-Klassen!")
        elif percent >= 60:
            st.info("👍 Gute Arbeit! Du hast ein solides Verständnis, aber es gibt noch Raum für Verbesserung.")
        else:
            st.warning("🤔 Du solltest die Konzepte noch einmal wiederholen, um dein Verständnis zu verbessern.")
        
        # Button zum Neustart des Quiz
        if st.button("Quiz neu starten", key="restart_quiz"):
            # Alle Session-Variablen zurücksetzen
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.session_state.quiz_finished = False
            
            # Neue Fragen mischen und auswählen
            random.shuffle(all_questions)
            st.session_state.quiz_questions = all_questions[:5]
            st.rerun()
