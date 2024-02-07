## Sortieren

``````
sort choice(Status = "Produce", "1", choice(Status = "Edit", "2", choice(Status = "Script", 3, choice(Status = "Research", 4, 5)))) asc
``````

## Dateien
### Tabelle aller nicht-erschaffenen Dateien mit Ursprung

``````
```dataview
TABLE without id;out AS "Uncreated files", file.link as "Origin"
FLATTEN file.outlinks as out;WHERE !(out.file) AND !contains(meta(out).path, "/")
SORT out ASC
limit 30
```
``````

[[Tabelle aller nicht-erschaffenen Dateien mit Ursprung|Anwendungsbeispiel]]

## Tags
### Tabelle aller Tags

``````
```dataview
TABLE WITHOUT ID (tag + "(" + length(rows.file.link) + ")")
AS Tags,link(sort(rows.file.name));AS Files
FROM ""
WHERE file.tags
FLATTEN file.tags
AS tag
GROUP BY tag
SORT file.name Asc
limit 30
```
``````

[[Tabelle aller Tags|Anwendungsbeispiel]]

### Tabelle eines Tags

``````
```dataview
TABLE WITHOUT ID Tags AS "Thema", rows.file.link AS "Files"
FROM #Themen/Selbstorganisation 
FLATTEN file.etags AS Tags
WHERE contains(Tags, "#Themen/Selbstorganisation/")
GROUP BY Tags
SORT Tags ASC
```
``````

[[Tabelle eines Tags|Anwendungsbeispiel]]

### Tabelle eines runtergebrochenen Tags

``````
```dataview
table without id
join( sort( map(file.etags, (x) => regexreplace(x,"#(\w+/){1,}","")) ), " ") AS Thema, file.link as "Datei"
from #Themen/Selbstorganisation 
sort tag asc
```
``````

[[Tabelle eines runtergebrochenen Tags|Anwendungsbeispiel]]

### Tabellenabfrage für Tag und bestimmten nicht Ordner mit Datumssortierung

```dataview
table without id file.link as "OKRs",choice((date < date(today)),"<span style='color: red;'>" + (date - date(today)) + "</span>",choice((date > date(today)), (date - date(today)),"Today")) as "Due Date"
from #todo/🎯OKRs and !"Templates"
where !done
sort date asc
limit 1
```

### Tabellenabfrage für Tag und bestimmten nicht Ordner und Datumssortierung

```dataview
table without id file.link as "Initiativen",choice((date < date(today)),"<span style='color: red;'>" + (date - date(today)) + "</span>",choice((date > date(today)), (date - date(today)),"Today")) as "Due Date"
from #todo/🏎Initiativen and !"Templates"
where !done
where !contains(file.name, "template")
sort date asc
limit 1
```

### Tabellenabfrage, um Projekte der nächsten 2 Wochen zu sehen

``````
```dataview
table without id file.link as "Next 2 Weeks",choice((date < date(today)),"<span style='color: red;'>" + (date - date(today)) + "</span>",choice((date > date(today)), (date - date(today)),"Today")) as "Due Date"
from #Project
where date > date(today)-dur(2 w) and date < date(today)+dur(2 w)
where !done
sort date asc
```
``````

### Tabellenabfrage für längere Projekte

``````
```dataview
table without id file.link as "Longer Projects",choice((date < date(today)),"<span style='color: red;'>" + (date - date(today)) + "</span>",choice((date > date(today)), (date - date(today)),"Today")) as "Due Date"
from #Project and !#Content
where !done
where date
where !contains(file.name, "template")
sort date asc
```
``````

### Tabellenabfrage für Projekte mit dem tag ''#Essay'

``````
```dataview
table
file.outlinks as "To", file.inlinks as "From"
from "" sort file.ctime desc
limit 30
```
``````

[[Tabelle aller kürzlich erschaffener Dateien mit In- und Outlink|Anwendungsbeispiel]]

### Tabellenabfrage um '#Quellen' zu sehen, die nicht in '#Research' verlinkt sind

``````
```dataview
table from ''#Quellen' where !contains(file.inlinks.file.tags,"#Research")
```
``````

### Tabellenabfrage für Seiten ohne Tag

``````
```dataview
table without id file.link as "working"
from #note/working`
```
``````

### Tabellenabfrage für alle Quellen ohne Link

``````
```dataview
table without id file.link as "Unlinked Sources"
from #note/source and !"Templates" and !#people
where !contains(file.inlinks.file.tags, "#note/working")
sort file.ctime desc
```
``````

### Tabellenabfrage für eine Projektinbox

``````
```dataview
table without id file.link as "Videos", Deadline
from #project and !"Templates" #content/video;sort deadline asc
flatten all(map(file.tasks, (x) ⇒ x.completed)) AS "allCompleted"
where !allCompleted`
```
``````

### Projektabfrage mit Fortschrittsbalken

This is the code I have for table:

``````
\```
TABLE WITHOUT ID link(file.path,string(project)) as "Project", dateformat(start, "yyyy-MM-dd") as "Start Date", dateformat(end, "yyyy-MM-dd") as "End Date", "<progress value='" + round(100*completed/completion_max) + "' max='100'></progress> " + round(100*completed/completion_max) + "%" AS Progress, start.year
WHERE type = "project"
\```

``````

– [Dataview: how do you show only files that have a certain year in the frontmatter?](https://reddit.com/r/ObsidianMD/comments/11ih2o6/dataview_how_do_you_show_only_files_that_have_a/)

## Ordner
### Tabelle aller Besprechungen von NVDH

``````
```dataview
TABLE date as "Date", summary as "Summary" from "meetings"
where contains(type,"meeting")
sort date desc
```
``````

[[Tabelle aller Besprechungen von NVDH|Anwendungsbeispiel]]

### Tabelle aller kürzlich erschaffener Dateien 

``````
```dataview
TABLE file.ctime as Created
FROM ""
WHERE date(now) - file.ctime <= dur(3 days)
SORT file.ctime desc
```
``````

[[Tabelle aller kürzlich erschaffener Dateien|Anwendungsbeispiel]]

### Tabelle aller kürzlich erschaffener Dateien mit In- & Outlink

``````
```dataview
table
file.outlinks as "To", file.inlinks as "From"
from "" sort file.ctime desc
limit 30
```
``````

[[Tabelle aller kürzlich erschaffener Dateien mit In- und Outlink|Anwendungsbeispiel]]

### Tabelle aller nicht-erschaffenen Dateien mit Ursprung

``````
```dataview
TABLE without id
out AS "Uncreated files", file.link as "Origin"
FLATTEN file.outlinks as out
WHERE !(out.file) AND !contains(meta(out).path, "/")
SORT out ASC
limit 30
```
``````

[[Tabelle aller nicht-erschaffenen Dateien mit Ursprung|Anwendungsbeispiel]]

### Tabelle eines runtergebrochenen Ordners

``````
```dataview
table without id file.folder AS "Pfad", file.link as "Datei"
where file.name != this.file.name and contains(file.path, "Templates")
sort file.folder ascending
```
``````

[[Tabelle eines runtebrochenen Ordners|Anwendungsbeispiel]]

### Tabelle aller Notizen in Templates

``````
```dataview
TABLE link(sort(rows.file.name)) AS Files 
FROM "Templates" WHERE file.folder
FLATTEN file.folder AS Folder
GROUP BY Folder
SORT Folder Asc
```
``````

[[Tabelle aller Notizen in Templates|Anwendungsbeispiel]]

## YAML
### Tabelle mit bestimmtem YAML Wert

``````
```dataview
table from ""
where metatype = "Tasks Query"`
```
``````

### Tabelle von Tag und YAML
Um nach Tag und Typ zu filtern, funktioniert folgende Abfrage: 

``````
```dataview
table from "x"
where type = "Bewerbung"
```
``````

### Tabelle von Tag und YAML mit Tabellensortierung

``````
```dataview
table
without id file.link as "Offene Bewerbungen", choice((Abgabe < date(today)),"<span style='color: red;'>" + (Abgabe - date(today)) + "</span>",choice((Abgabe > date(today)), (Abgabe - date(today)),"Today")) as "Wann fällig"
where type = "Bewerbung"
where Stand = "📇Terminiert" or Stand = "🚧In Bearbeitung"
sort Abgabe asc
```
``````

### Tabelle von Ordner mit YAML Wert aus Ordner mit Sortierung

``````
```dataview
table Joe, Mike
from "Bookworm"
sort Mike desc
```
``````

[Visualizing Metadata in Obsidian with YAML and Dataview](https://thesweetsetup.com/obsidian-metadata-with-yaml-and-dataview/)

### Liste  mit bestimmten YAML Wert oder Tag

``````
```dataview
LIST
FROM ""
WHERE type = "Bewerbung" or contains(file.tags, "#Typ/Bewerbungen/Proposal")
```
``````

### Wochentabelle mit YAML Daten als Emojis

```dataview
TABLE WITHOUT ID
  weekday AS "Day",
  Check-In AS "💊",
  thm-login AS "🔑",
  eve-login AS "🚀",
  push-ups AS "💪",
  write500words AS "🖊️",
  call-mum AS "📱",
  running AS "🏃‍♂️",
  apply-for-2-jobs AS "👨‍💼"
FROM "053 Selbstorganisation/Daily"
SORT file.ctime ASC
limit 1
````