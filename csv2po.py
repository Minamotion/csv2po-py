import csv, sys, os

#region [Make sure output exists]
if not os.path.exists("./output/"):
	os.mkdir("./output/")
#endregion
#region [Get requested]
files: list[str]= []
can_append_files_now = False

for i in range(len(sys.argv)):
	arg = sys.argv[i]
	if arg == "-i": # Python would also pass this script as a param
		can_append_files_now = True
		continue
	if can_append_files_now:
		files.append(arg)
#endregion
#region [Scan CSV files]
tr: dict[str, dict[str, str]]= {}
for file in files:
	langs = []
	with open(file, "r") as f:
		table = csv.reader(f)
		row_i = 0
		for row in table:
			if row_i > 0:
				key = row.pop(0)
				column_i = 0
				tr[key] = {}
				while len(row) > 0:
					tr[key][langs[column_i]] = row.pop(0)
					column_i += 1
			else:
				row.pop(0)
				while len(row) > 0:
					found = False
					lang = row.pop(0)
					for lang_i in range(len(langs)):
						if langs[lang_i] == lang:
							found = True
							break
					if not found:
						langs.append(lang)
			row_i += 1
#endregion
#region [Set result]
result: dict[str, str] = {}
for k in tr.keys():
	v = tr.get(k)
	for kk in v.keys():
		vv = v.get(kk)
		if result.get(kk) == None:
			result[kk] = f'# Generated using csv2po.py\n# which was made by Minamotion :)\n# https://github.com/Minamotion/csv2po-py\n\nmsgid ""\nmsgstr ""\n"Language: {kk}\\n"\n\n'
		result[kk] += f'msgid "{k}"\nmsgstr "{vv.replace('"', '\\"')}"\n\n'
#endregion
#region [Write PO files]
for key, value in result.items():
	with open(f"output/{key}.po", "w") as f:
		f.write(value)
		f.close()
#endregion

print("Nothing went wrong! Probably! Go check!")
