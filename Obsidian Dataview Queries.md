## Dateien
### alle Aufgaben, die auf eine Notiz verweisen und noch nicht abgeschlossen sind

``````
```dataview
task
where contains(outlinks,[[Obsidian Dataview Aufgabenabfragen]])
where status = " "
```
``````

## Tag
### Unvollendete Aufgaben mit einem bestimmten Tag

``````
```dataview
task FROM ""
WHERE !completed
WHERE contains(tags, "#todo/Video")
FLATTEN tags
GROUP BY tags
```
``````

### Abfrage für das Tag 'Content Ideen'

``````
```dataview
task
where contains(tags, "#content/video")
where status = " "
```
``````

### Abfrage von Aufgaben, die älter als eine Woche sind

``````
```dataview
task
from !#content and !#note/working and !#dashboard
where status = " "
where created < date(today) - dur(1 weeks) and created
group by file.link
limit 30
```
``````
