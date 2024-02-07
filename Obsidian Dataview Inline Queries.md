## Automatischer Link in die Daily Note

``````
`="[[" + dateformat(date(today), "yyyy-MM-dd") + "#Erfolgstagebuch]]"`
``````

``````
`$= dv.fileLink("Ablage/000 🌿 Meta & PKM/030 🟣 Obsidian/037 Periodic Notes/Daily/" + luxon.DateTime.now().toISODate(), false, "Today")`
``````

## Fortschrittsbalken
### Aus dem Demo Vault von Bagerbach.com

``````
```dataview
TABLE WITHOUT ID
	(link(file.path, alias)) as title,
	Bar
FROM #goal
WHERE Progress != Target
SORT Type DESC
```
``````

### Aus dem Obsidian Forum
#### Inline

``````
`= "<progress value='" + (length(filter(this.file.tasks.completed, (t) => t = true)) / length(this.file.tasks.text)) * 100 + "' max='100'></progress>" + " " + (length(filter(this.file.tasks.completed, (t) => t = true)) / length(this.file.tasks.text)) * 100 + "%"`
``````

#### Aus allen Dateien From ""

``````
```dataview
TABLE file.tasks.text, length(file.tasks.text) as Total, file.tasks.completed, filter(file.tasks.completed, (t) => t = true) as C, length(filter(file.tasks.completed, (t) => t = true)) AS Completed, (length(filter(file.tasks.completed, (t) => t = true)) / length(file.tasks.text)) * 100 AS BB, "<progress value='" + (length(filter(file.tasks.completed, (t) => t = true)) / length(file.tasks.text)) * 100 + "' max='100'></progress>" AS Progress
FROM "your folder"
WHERE file.tasks
```
``````

- [Progress bar for incomplete/total tasks? - Resolved help - Obsidian Forum](https://forum.obsidian.md/t/progress-bar-for-incomplete-total-tasks/30744)

## Letzte Updates im Vault

``````
Vault Info

    🗄️ Recent file updates $=dv.list(dv.pages('').sort(f=>f.file.mtime.ts,"desc").limit(4).file.link)
    🔖 Tagged: favorite $=dv.list(dv.pages('#favorite').sort(f=>f.file.name,"desc").limit(4).file.link)
    〽️ Stats
        File Count: $=dv.pages().length
        Personal recipes: $=dv.pages('"Family/Recipes"').length

``````

## Modifikationsdatum

```
Last Modified: `=dateformat(this.file.mtime, "DDDD, HH:mm")`
```