%%
Alte Fassung einer Einzelbewerbung, zur Sammlung aller bewerbungsspezifischer Details. 
%%

---
<%* await tp.file.move("Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.01 Bewerbungsdatenbank/" + tp.file.title);
const Monat = moment().locale('de').format("YYYY-MM");
const Firmenname = await tp.system.prompt("Wie heißt die Firma?")
const Rolle = await tp.system.prompt("Wie wird die Rolle bezeichnet?");
const FileName = Monat + " " + Firmenname + " " + Rolle;
const Linkname = moment().locale('de').format("YYYY-MM-DD") + " " + Firmenname + " " + Rolle
await tp.file.rename(FileName);

// Benennung von deinen YAMLs
let folders = tp.file.folder(true).split('/')

// Extract the relevant folder names
let area = folders[1] ? folders[1].slice(4) : '-';
let category = folders [2] ? folders[2].slice(4) : '-';
let subcategory = folders[3] ? folders[3].slice(4) : '-';
let type = folders[4] ? folders[4].slice(7) : '-';
let subtype = folders[5] ? folders[5].slice(0) : '-';
let supratype = folders[6] ? folders[6] : '-';-%>area: <% area %>
category: <% category %>
subcategory: <% subcategory %>
type: <% type %>
subtype: <% subtype %>
supratype: <% supratype %>
metatype: 🔮Bewerbung
Firma: <%Firmenname%>
Anlauf: <%await tp.system.prompt("Online seit? Anlauf?")%>
Abgabe: <%await tp.system.prompt("Abgabetermin?")%> <%await tp.file.include("[[TMP YAML Standvorschläge]]") %>
Abgegeben: false
Arbeitszeit: <%await tp.system.suggester([
"Vollzeit",
"Teilzeit"
], [
"Vollzeit",
"Teilzeit"
]) %>
Rolle: <%Rolle%>
Sprache: <%await tp.system.suggester([
"Auf Deutsch",
"Auf Englisch",
"Auf Französisch"
], [
"🇩🇪",
"🇬🇧",
"🇫🇷"
]) %>
Gehaltswunsch: <%await tp.system.suggester([
"Keine Gehaltswunschangabe",
"Mit Gehaltswunschangabe"
], [
"false",
"true"
]) %>
Gehaltshöhe: <%await tp.system.prompt("Angegebene Gehaltshöhe?")%>
Eintrittsdatumangabe: <%await tp.system.suggester([
"Ohne Eintrittsdatumangabe",
"Mit Eintrittsdatumangabe"
], [
"false",
"true"
]) %>
Eintrittsdatum:
Ergebnis: <%await tp.system.suggester([
"Aktuell In Bearbeitung",
"Aktuell Auf Antwort warten",
"In den Papierkorb",
"Negative Antwort",
"Positive Antwort",
"50-50 Antwort"
], [
"✏️",
"🤷‍♂️",
"🗑️",
"❌",
"✔️",
"🌻"
]) %>
Relevant: <%await tp.system.suggester([
"Vollkommen relevant",
"Teils Teils relevant",
"Nicht relevant"
], [
"✔️",
"🌻",
"❌"
], "Test:") %>
Notiz:
url: "[URL](<%await tp.system.prompt("Website URL?")%>)"
maps: "[Google Maps](https://www.google.com/maps?q=<%Firmenname.replace(/ /g, '%20')%>%20Hamburg)"
kununu: "[Kununu](https://www.kununu.com/de/search?q=<%Firmenname.replace(/ /g, '%20')%>%20Hamburg)"
glassdoor: "[Glassdoor](https://www.glassdoor.com/Search/results.htm?keyword=<%Firmenname.replace(/ /g, '%20')%>%20Hamburg)"
indeed: "[Indeed](https://www.google.com/search?q=<%Firmenname.replace(/ /g, '+')%>+Hamburg+site%3A+www.indeed.de&safe=active&ssui=on)"
xing: "[Xing](https://www.google.com/search?q=<%Firmenname.replace(/ /g, '+')%>+Hamburg+site%3A+www.xing.de&safe=active&ssui=on)"
linkedin: "[LinkedIn](https://www.google.com/search?q=<%Firmenname.replace(/ /g, '+')%>+Hamburg+site%3A+www.linkedin.de&safe=active&ssui=on)"
northdata: "[NorthData](https://www.northdata.de/<%Firmenname.replace(/ /g, '+')%>+Hamburg)"
Ausschreibung: "[[<%FileName%> Ausschreibung|Ausschreibung]]"
AusschreibungURL: "[URL Ausschreibung](<%await tp.system.prompt("Ausschreibung URL?")%>)"
Anschreiben: "[[<%FileName%> Anschreiben|Anschreiben]]"
Benefitexistenz: <%await tp.system.suggester([
"Keine Benefits",
"Tatsächlich relevante Benefits",
"50-50"
], [
"❌",
"✔️",
"🌻"
]) %>
Benefits: <%await tp.system.prompt("Welche Benefits?")%>
cssclass: wide
---
%%
[Lokaler Ordner](es:<% FileName.replace(/ /g, '%20')%>)
backlinks:: [[224.01 Bewerbungsdatenbank]]
<% tp.file.folder(true) %>
Fortschritt:: `= "<progress value='" + (length(filter(this.file.tasks.completed, (t) => t = true)) / length(this.file.tasks.text)) * 100 + "' max='100'></progress>" + " " + (length(filter(this.file.tasks.completed, (t) => t = true)) / length(this.file.tasks.text)) * 100 + "%"`
%%
## <p align="right">[[<% folders[folders.length-2] %>|⬆]] [📁](es:<% FileName.replace(/ /g, '%20')%>)</p> 
# [[<%FileName%>]]
[Website](<%await tp.system.prompt("Website URL?")%>)

- [[Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.02 Bewerbungsdokumente/224.02.06 Ausschreibungen/<%Linkname%> Ausschreibung|<%Linkname%> Ausschreibung]]
- [[Ablage/200 ⚡ Selbststaendigkeit & Job/220 Öffentlichkeit/224 Bewerbungen/224.02 Bewerbungsdokumente/224.02.01 Anschreiben/<%Linkname%> Anschreiben|<%Linkname%> Anschreiben]]

%%
creation:: <% tp.file.creation_date("YYYY-MM-DD") %>
template date:: <% tp.date.now("YYYY-MM-DD") %>
author::
about::
links::
tag::
%%