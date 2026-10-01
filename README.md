# csv2po-py
Converts One or Multiple CSV Files to PO Translation Files.

This thing was made in a night.

## Syntax

`python csv2po.py -i file1.csv file2.csv ... fileN.csv`

Like that

## Requirements

If converting mutliple CSV Files, CSV Files must all be like this:

- fileA.csv
	```csv
	key,en,es
	greet,Hello!,Hola!
	```
- fileB.csv
	```csv
	key,en,es
	farewell,Bye!,Adios!
	```
with the 1st row unchanging

So, not like this:
- fileA.csv
	```csv
	key,en,es
	greet,Hello!,Hola!
	```
- fileB.csv
	```csv
	key,es,en
	farewell,Adios!,Bye!
	```
because merging these thingies depends on the 1st row being unchanged because of course it does.

## Why no .gitignore?
As far as I'm aware, this script doesn't need it.