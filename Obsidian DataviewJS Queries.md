## An diesem Tag

````
```dataviewjs
// set your own minimum year and the path to your journals (if applicable)
const minYear = 2012;
const journalPath = '';
// const journalPath = 'Areas/Journals';

const rangeOfYears = (start, end) => Array(end - start + 1)
  .fill(start)
  .map((year, index) => year + index)
const d = moment();
const currentYear = d.year();
const availableYears = rangeOfYears(minYear, currentYear);
const month = ("0" + (d.month() + 1)).slice(-2);
const day = ("0" + (d.date())).slice(-2);
const dateString = month + '-' + day;

availableYears.forEach((y) => {
	var note = dv.page(${journalPath}/${y}-${dateString});
	if (note) {
		dv.el('span', [[${note.file.path}|${y}]] );
	}
});
```
````

## Dateiinhalt des Vaults

``````
```dataviewjs
let pages = dv.pages('"Ablage"');

// Create a new array to store the sorted groups
let sortedGroups = [];

// Set the initial header level to 1
let headerLevel = 1;

// Iterate through the groups, and push the "Ablage" group first
for (let group of pages.groupBy(b => b.file.folder.replace(/^Ablage\//, ""))) {
    if (group.key === 'Ablage') {
        sortedGroups.unshift(group);
    } else {
        sortedGroups.push(group);
    }
}

for (let group of sortedGroups) {
    // Split the group key by '/' to check the number of subfolders
    let subfolders = group.key.split('/');
    // Increase the header level for each subfolder, but limit it to 6
    headerLevel += subfolders.length - 1;
    if (headerLevel > 6) {
        headerLevel = 6;
    }
    dv.header(headerLevel, group.key);
    dv.list(group.rows.file.link); 
    // Reset the header level for the next group
    headerLevel = 1;
}
```
``````

## Dateiinhalt des Vaults - verbessert

``````
```
dataviewjs
let pages = dv.pages();

// Get the current folder name
let currentFolder = pages[0].file.folder;

// Create a new array to store the filtered pages
let filteredPages = pages.filter(page => page.file.folder.startsWith(currentFolder))

// Create a new array to store the sorted groups
let sortedGroups = [];

// Set the initial header level to 1
let headerLevel = 3;

// Iterate through the groups, and push the current folder's group first
for (let group of filteredPages.groupBy(b => b.file.folder.replace(new RegExp(`^${currentFolder}/`, ""), ""))) {
	if (group.key === currentFolder) {
		sortedGroups.unshift(group);
	} else {
		sortedGroups.push(group);
	}
}

for (let group of sortedGroups) {
	// Split the group key by '/' to check the number of subfolders
	let subfolders = group.key.split('/');
	// Increase the header level for each subfolder
	headerLevel += subfolders.length - 1;
	    if (headerLevel > 6) {
        headerLevel = 6;
    }
	dv.header(headerLevel, group.key);
	dv.list(group.rows.file.link);
	// Reset the header level for the next group
headerLevel = 1;
}
```
``````

## Dateiinhalt von Templates nach Subfolder Headertiefe

``````
```dataviewjs
let pages = dv.pages('"Templates"');

// Create a new array to store the sorted groups
let sortedGroups = [];

// Set the initial header level to 3
let headerLevel = 3;

// Iterate through the groups, and push the "Templates" group first
for (let group of pages.groupBy(b => b.file.folder.replace(/^Templates\//, ""))) {
    if (group.key === 'Templates') {
        sortedGroups.unshift(group);
    } else {
        sortedGroups.push(group);
    }
}

for (let group of sortedGroups) {
    // Split the group key by '/' to check the number of subfolders
    let subfolders = group.key.split('/');
    // Increase the header level for each subfolder
    headerLevel += subfolders.length - 1;
    dv.header(headerLevel, group.key);
    dv.list(group.rows.file.link); 
    // Reset the header level for the next group
    headerLevel = 3;
}
```
``````

[[030 🟣 Obsidian#Ordnerinhalt von Templates|Anwendungsbeispiel]]

## Einfache Liste von tags/Ordnern etc.

``````
```dataviewjs
dv.header(2, "Wikipedia")
dv.list(dv.pages("#Quellen/Wikipedia").file.link)
```
``````

## Liste mit eigenem Header

``````
```dataviewjs
dv.header(4, "Wikipedia");
dv.list(dv.pages("#Quellen/Wikipedia").file.link);
```
``````

## Liste mit Tags (Ausgang für alle ChatGPT Geschichten)

``````
```dataviewjs
let pages = dv.pages("#Themen/Selbstorganisation");
for (let group of pages.groupBy(b => b.tag)) {
   dv.header(3,group.key.replace(/^.*?\//, ""));
   dv.list(group.rows.file.link); 
}
```
``````

## Liste von Subtags abgezogen

``````
```dataviewjs
let pages = dv.pages("#Themen/Selbstorganisation");
for (let group of pages.groupBy(b => b.tag.replace(/^Themen\/Selbstorganisation\//, ""))) {
   dv.header(3,group.key);
   dv.list(group.rows.file.link); 
}
```
``````

[[030 🟣 Obsidian#Recherche|Anwendungsbeispiel]]