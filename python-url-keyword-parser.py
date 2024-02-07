# Parser für die Suche nach einem Stichwort auf einer Website
# -*- coding: utf-8 -*-
try:
    # Python 2
    import urllib2
except ImportError:
    # Python 3
    import urllib.request as urllib2

from bs4 import BeautifulSoup

def search_word_in_url(url, keyword):
    try:
        # HTML von der URL abrufen
        response = urllib2.urlopen(url)
        html = response.read()

        # HTML-Inhalt parsen
        soup = BeautifulSoup(html, 'html.parser')

        # Textinhalt der Webseite extrahieren
        page_text = soup.get_text()

        # Nach dem Keyword suchen (ignoriert Groß- und Kleinschreibung)
        if keyword.lower() in page_text.lower():
            print("{} gefunden auf {}".format(keyword, url))
            return True
        else:
            print("{} nicht gefunden auf {}".format(keyword, url))
            return False

    except Exception as e:
        print("Fehler beim Abrufen von {}: {}".format(url, e))
        return False

# Liste der URLs
urls = [
]

# Keyword nach dem gesucht werden soll
keyword = ""

# Ergebnisse speichern
results = []

# Durch alle URLs iterieren
for url in urls:
    result = search_word_in_url(url, keyword)
    results.append((url, result))

# Unicode-Zeichen für Häkchen und Kreuz
check_mark = '\u2714'
cross_mark = '\u2718'

# Markdown-Liste erstellen
markdown_list = "\n".join(["- {} {}".format(check_mark if result[1] else cross_mark, result[0]) for result in results])

# Ergebnisse ausgeben
print("Ergebnisse:")
print(markdown_list)