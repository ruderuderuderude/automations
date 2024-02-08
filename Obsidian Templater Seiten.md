Beispiele für Templater Seiten, die ich verwende

## Index

Ehemaliges File Creation Skript, welches direkt eine Datei verschieben möchte:

``````
<%*
const folders = this.app.vault.getAllLoadedFiles().filter(i => i.children).map(folder => folder.path);
const folderPath = await tp.system.suggester(folders, folders);
let title = tp.file.title
  if (title.startsWith("Untitled")) {
	  title = await tp.system.prompt("Title");
    await tp.file.rename(`${title}`);
  } 
await tp.file.rename(`${title}`)
await tp.file.move(`/${folderPath}/${title}`)
%><% tp.file.include("[[TMP Seitenwahl]]") %>
``````

## Archiv
### Daily Note

Archivierung von Abfragen, die zu ressourcenintensiv sind.

#### Heute erschaffen

``````
> [!success]- Heute erschaffen
> ```dataview
> table " | <small>*Modified: "+file.mtime+"*</small> 
> | <small>Created: "+file.ctime+"</small>"
> where file.ctime > this.file.day and file.ctime < (this.file.day + dur(1 day))
> sort file.ctime desc
> sort file.name asc
> sort metatype asc
> ```
``````

#### Heute modifiziert

``````
> [!success]- Heute modifiziert
> ```dataview
> table " | <small>*Modified: "+file.mtime+"*</small> 
> | <small>Created: "+file.ctime+"</small>"
> where file.mtime > this.file.day and file.mtime < (this.file.day + dur(1 day))
> sort file.mtime desc
> sort file.name asc
> sort metatype asc
> ```
``````

### Dateikreation
### Bestehende Seite mit einer Kopie der bestehenden Frontmatter erstellen

``````
---
<%*
let folders = tp.file.folder(true).split('/')
let area = folders.slice(1, 2)
let category = folders.slice(2, 3)
let subcategory = folders.slice (3, 4)
let type = folders.slice (4, 5)
-%>area: <% area.slice(4) %>
category: <% category.slice(4) %>
subcategory: <% subcategory.slice(4) %>
type: <% type %>
metatype: <% tp.file.include("[[TMP YAML Metatypevorschläge]]") %>
Datum: <% tp.frontmatter.Datum %>
Stand: <% tp.frontmatter.Stand %>
tag: <% tp.frontmatter.tag %>
Bearbeitung: <% tp.frontmatter.Bearbeitung %>
Verwendet: <% tp.frontmatter.Verwendet %>
Relevanz: <% tp.frontmatter.Relevanz %>
Priority: <% tp.frontmatter.Priority %>
Notiz: <% tp.frontmatter.Notiz %>
---
[Lokaler Ordner](es:<% tp.file.title.replace(/ /g, '%20')%>)
`=this.file.folder`
# [[<% tp.file.title %>]]
<% tp.system.clipboard()%>
%%
template date::  <% tp.date.now("YYYY-MM-DD") %>
backlinks:: [[<% type %>]]
links::
%%
``````