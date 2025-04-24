import streamlit as st
import sys
from io import StringIO
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def syntax_highlight(code, language="python"):
    """
    Hebt Syntax in einem Code-Block hervor und gibt Code mit Syntax-Highlighting zurück.
    
    Args:
        code (str): Der zu formatierende Code.
        language (str): Die Programmiersprache, standardmäßig Python.
        
    Returns:
        Der formatierte Code mit Syntax-Highlighting.
    """
    # Syntax-Highlighting mit Zeilennummern
    return st.code(code, language=language, line_numbers=True)

def run_code(code):
    """
    Führt Python-Code aus und gibt die Ausgabe zurück.
    """
    # Umleiten von stdout
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        # Code in einem geschützten Kontext ausführen
        exec(code)
        sys.stdout = old_stdout
        return redirected_output.getvalue()
    except Exception as e:
        sys.stdout = old_stdout
        return f"Fehler: {str(e)}"
