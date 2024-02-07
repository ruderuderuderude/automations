## Dateien
### Alle Dateien mit Datum im Titel

Listet alle Dateien auf, die ein Datum im Titel haben(in der Form `yyyy-mm-dd`), und listet sie in der Reihenfolge des Datums auf: 

``````
```dataview
LIST file.day WHERE file.day
SORT file.day DESC
```
``````

### Alle kürzlich bearbeiteten Dateien

``````
```dataview
LIST 
" | <small>*Modified: "+file.mtime+"*</small> 
| <small>Created: "+file.ctime+"</small>"  
FROM ""
WHERE file.name != this.file.name
SORT file.mtime DESC
LIMIT 15
```
``````

### Alle Waisen

``````
```dataview
list
from ""
where length(file.inlinks) =0 and length(file.outlinks) = 0
```
``````

[[Liste aller Waisen|Anwendungsbeispiel]]

## Links
### Alle Inlinks

``````
```dataview
list where
contains(file.outlinks, this.file.link)
sort file.name asc
```
``````

### Alle  Links mit bestimmten Backlink YAML

``````
```dataview
list 
where backlinks = this.file.link
sort file.name asc
```
``````

## Tags
### Liste von Tag
Beispiele um Tags abzufragen

``````
```dataview
list FROM #
```
``````

``````
```dataview
list from #todo/🏎Initiativen
```
``````

[[Liste von Tag|Anwendungsbeispiel]]

### Liste eines Tags als Überschrift

``````
```dataview
LIST without ID
"## " + tag + "</h2> <br>" + join(rows.file.link, "<br>")
FROM #Themen/Selbstorganisation;where contains(file.etags, "#Themen/Selbstorganisation/");FLATTEN file.etags as TAG
WHERE tag
GROUP BY tag
```
``````

## Ordner
### Gruppen- und Sortieransichten

*Unsortierte Variante*
``````
```dataview
LIST rows.file.link
FROM "Templates"
WHERE !contains(file.folder, "_Archive") AND !contains(file.name, "_Working on")
GROUP BY file.folder AS Example
SORT Example DESC
```
``````

[[Unsortierte Variante|Anwendungsbeispiel]]

*Sortierte Variante*
``````
```dataview
LIST
sort(rows.file.link)
FROM "Templates"
WHERE !contains(file.folder, "_Archive") AND !contains(file.name, "_Working on")
GROUP BY file.folder
```
``````
[[Sortierte Variante|Anwendungsbeispiel]]

 https://forum.obsidian.md/t/help-with-group-and-sort-with-dataview-plugin/28649

### Liste mit Link zur Erstellung eines MOC

``````
```dataview
LIST rows.file.link
FROM "Templates"
FLATTEN regexreplace(file.folder, "^(.*/)(.+)$", "$2/$2.md") AS parent_foldernote
FLATTEN regexreplace(file.folder, "^(.*/)(.+)$", "$2") AS parent_name
WHERE file.name != parent_name
GROUP BY link(parent_foldernote)
```
``````

[[Liste mit Link zur Erstellung eines MOC|Anwendungsbeispiel]]

### Liste aller Ordner und Ordner vom Aktuellen Ordner

``````
 ```dataview
LIST rows.file.link
where contains(file.folder,this.file.folder)
sort file.name asc
GROUP BY file.folder
```
``````

### File.folder bold

``````
```dataview
LIST sort(rows.file.link)
FROM "Ablage/000 🌿 Meta & PKM/030 🟣 Obsidian/037 Obsidian Periodic Notes"
GROUP BY "**" + file.folder + "**"
```
``````

## YAML
### Liste von einem YAML

``````
```dataview
list from ""
where metatype = "🕵🏻‍♂️Dataview Abfrage"
```
``````

[[Liste von einem YAML|Anwendungsbeispiel]]

### Liste  mit bestimmten YAML Wert oder Tag

``````
```dataview
LIST
FROM ""
WHERE type = "Bewerbung" or contains(file.tags, "#Typ/Bewerbungen/Proposal")
```
``````

### Liste nach YAML Wert und danach gruppiert

``````
```dataview
list without ID
"<br> " + "** " + tag + "** <br><br>" + join(rows.file.link, "<br>")
from #Themen/<%typesliced%><%subtypesliced%><%supratypesliced%><%folders7sliced%><%folders8sliced%><% title.replace(/ /g, '').replace(/&/g, '').replace(/,/g, '').replace(/'/g, '')%>
where !contains(metatype, "🌌Glossar")
sort file.name desc
sort metatype asc
group by tag
> ```
``````

### Liste nach Metatype gruppiert und eigener Sortierung

``````
```dataview
list without ID
"<br> " + "** " + metatype + "** <br><br>" + join(rows.file.link, "<br>") 
from "" where metatype = "✉️Brief" OR metatype = "🗯️Chat" OR metatype = "📔Journal" or metatype = "👇Kommentar" or metatype = "📝Notiz" or contains(file.folder, "Ablage/800 💎 Privates/801 Aulë/804 Privater Briefverkehr & Journal") AND category = "Aulë" AND contains(subcategory, "Privater Briefverkehr") 
sort file.name desc
sort metatype asc
group by metatype
sort choice(metatype = "✉️Brief", "1", choice(metatype = "🗯️Chat", "2", choice(metatype = "📔Journal", "3", choice(metatype = "👇Kommentar", "4", "5")))) asc
```
``````

### Liste mit Inline YAML, wo es auftaucht

``````
```dataview
LIST choice(length((log)[0]) = 1, list(log), log)
WHERE log
limit 1
```
``````

[Can we make a cleaner Dataview list? - Resolved help - Obsidian Forum](https://forum.obsidian.md/t/can-we-make-a-cleaner-dataview-list/32843/19)