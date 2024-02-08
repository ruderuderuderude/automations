%%
Obsidian Datenbank, die auf Basis von YAML bestehende Markdown Dateien mithilfe von Inline JS und Dataview kategorisiert. Mittlerweile eingestampft, da zu ressourcenintensiv. Also there's no need to reinvent Excel ¯\_(ツ)_/¯
%%
---
area: 
category: 
subcategory: 
type: 
subtype: 
supratype: 
metatype:
cssclasses:
  - max
  - cards
tags:
---
# [[Bewerbungsdatenbank]]

Gesamtanzahl an gespeicherten Ausschreibungen: $= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').length

$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "📇Terminiert" || p.Stand == "🔭In Beobachtung" || p.Stand == "🔜In Warteposition" || p.Stand == "🏃🏽Bearbeitbar" || p.Stand == "🚧In Bearbeitung").length offene Ausschreibungen
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🚧In Bearbeitung"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "📇Terminiert" && p.Relevant == "✔️"|| p.Stand == "🔭In Beobachtung" && p.Relevant == "✔️"|| p.Stand == "🔜In Warteposition" && p.Relevant == "✔️"|| p.Stand == "🚧In Bearbeitung" && p.Relevant == "✔️").length relevante, offene Ausschreibungen
Gefiltert nach Rolle.

Ungefiltert
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
UI/UX
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
WHERE
contains(Rolle, "UX")
Foto
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
WHERE
contains(Rolle, "Foto") 
OR contains(Rolle, "Photo")
Video
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
WHERE
contains(Rolle, "Video")
Bildbearbeitung
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
WHERE
contains(Rolle, "Bildbearbeit")
Motion
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
WHERE
contains(Rolle, "Motion")
Sonstige
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "✔️"
WHERE
!contains(Rolle, "Foto")
AND
!contains(Rolle,"Photo")
AND
!contains(Rolle,"Video")
AND
!contains(Rolle, "Motion")
AND
!contains(Rolle, "Bildbearbeit")
AND
!contains(Rolle, "UX")
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "📇Terminiert" && p.Relevant == "🌻"|| p.Stand == "🔭In Beobachtung" && p.Relevant == "🌻"|| p.Stand == "🔜In Warteposition" && p.Relevant == "🌻").length weniger relevante, offene Ausschreibungen
Auch hier gefiltertet nach Rolle.

Ungefiltert
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
UI/UX
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
WHERE
contains(Rolle, "UX")
Foto
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
WHERE
contains(Rolle, "Foto")
Video
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
WHERE
contains(Rolle, "Video")
Bildbearbeitung
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
WHERE
contains(Rolle, "Bildbearbeit")
Motion
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
WHERE
contains(Rolle, "Motion")
Sonstige
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Benefitexistenz: " + Benefitexistenz as Benefitexistenz,
"Benefits: " + Benefits as Benefits,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
FROM
"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
sort Abgabe desc
sort Anlauf desc
sort choice(Priorität = "⏫+", "1", choice(Priorität = "⏫", "2", choice(Priorität = "🔼", "3", choice(Priorität = "⏯", "4", choice(Priorität = "🔽", "5", choice(Priorität = "➡️", "6", "7")))))) asc
sort choice(Stand = "🚧In Bearbeitung", "1", 
choice(Stand = "⏸Pausiert", "2", 
choice(Stand = "⌛Warten", "3", 
choice(Stand = "📇Terminiert", "4", 
choice(Stand = "🔭In Beobachtung", "5", 
choice(Stand = "🔜In Warteposition", "6", 
choice(Stand = "🏃🏽Bearbeitbar", "2", 
choice(Stand = "⏩Verpasst", "8", 
choice(Stand = "⌛Auf Antwort warten", "7", 
choice(Stand = "🗑️Abgebrochen", "9", 
choice(Stand = "🗃️Archiviert", "9", 
choice(Stand = "🏅Teilgenommen", "9", 
choice(Stand = "🕊️Veröffentlicht", "9", 
choice(Stand = "💯Abgeschlossen", "9", "9"))))))))))))))
WHERE  
Stand = "📇Terminiert"  
OR  
Stand = "🔭In Beobachtung"
OR  
Stand = "🔜In Warteposition"
OR
Stand = "🏃🏽Bearbeitbar"
OR
Stand = "⏸Pausiert"
OR
Stand = "⌛Warten"
WHERE
Relevant = "🌻"
WHERE
!contains(Rolle, "Foto")
AND
!contains(Rolle,"Photo")
AND
!contains(Rolle,"Video")
AND
!contains(Rolle, "Motion")
AND
!contains(Rolle, "Bildbearbeit")
AND
!contains(Rolle, "UX")
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "⏩Verpasst").length Ausschreibungen verpasst
table Ausschreibung, Anschreiben
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Stand = "⏩Verpasst"
sort file.name asc
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "🗑️Abgebrochen").length Ausschreibungen abgebrochen
table Ausschreibung, Anschreiben
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Stand = "🗑️Abgebrochen" OR Stand = "🗑️Aufgegeben"
sort file.name desc
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "⌛Auf Antwort warten").length Ausschreibungen, bei denen ich auf Antwort warte
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Stand = "⌛Auf Antwort warten"
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Stand == "👻Ghosted").length Ausschreibungen, bei denen ich geghosted wurde
TABLE  
WITHOUT ID
file.link as "Offene Bewerbungen", 
Ausschreibung as Ausschreibung,
Anschreiben as Anschreiben,
url as URL,
AusschreibungURL as AusschreibungURL,
maps as maps,
kununu as kununu,
glassdoor as glassdoor,
indeed as indeed,
xing as xing,
linkedin as linkedin,
northdata as northdata,
"Kununurating: " + Kununurating as Kununurating,
"Glassdoorrating: " + Glassdoorrating as Glassdoorrating,
"Indeedrating: " + Indeedrating as Indeedrating,
"Xingrating: " + Xingrating as Xingrating,
"Linkedinrating: " + Linkedinrating as Linkedinrating,
"Anlauf: " + Anlauf as Anlauf,
"Abgabe: " + Abgabe as Abgabe,
"Abgegeben: " + choice(Abgegeben,"✔️","❌") as Abgegeben,
"Stand: " + Stand as Stand,
"Rolle: " + Erfahrungsgrad + " " + Rolle as Rolle,
"Arbeitszeit: " + Arbeitszeit as Arbeitszeit,
"Sprache: " + Sprache as Sprache,
"Gehaltswunsch: " + choice(Gehaltswunsch,"✔️","❌") as Gehaltswunsch,
"Gehaltshöhe: " + Gehaltshöhe as Gehaltshöhe,
"Eintrittsdatumangabe: " + choice(Eintrittsdatumangabe,"✔️","❌") as Eintrittsdatumangabe,
"Eintrittsdatum: " + Eintrittsdatum as Eintrittsdatum,
"Ergebnis: " + Ergebnis as Ergebnis,
"Relevanz: " + Relevant as Relevant,
"Notiz: " + Notiz as Notiz
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Stand = "👻Ghosted"
$=dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Ergebnis == "🌻").length Ausschreibungen bei denen ich zum Bewerbungsgespräch eingeladen wurde oder anderweitig etwas gutes passiert ist
table Ausschreibung, Anschreiben
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Ergebnis = "🌻"
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Ergebnis == "✔️" && p.Stand == "🏅Teilgenommen").length erfolgreiche Ausschreibungen
table Ausschreibung, Anschreiben
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Ergebnis = "✔️"
sort file.name desc
$= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Ergebnis == "❌" && p.Stand == "🏅Teilgenommen").length Ausschreibungen unerfolgreich
list Abgabe
from "Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"
where metatype = "🔮Bewerbung"
where Ergebnis = "❌"
sort Abgabe desc
Statistik
Verschickte Bewerbungen: $= dv.pages('"Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank"').where(p => p.Abgegeben == true).length