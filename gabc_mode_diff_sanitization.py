import os

ll = os.listdir(".")
nomodes = []
for f in ll:
  gabc=open(f, encoding="utf-8").read()
  if not "mode:" in gabc:
    nomodes.append(f)
# here, manually check nomodes and remove them from ll if they indeed should not have modes (OR* and R/Br)
noeus = []
for f in ll:
  gabc=open(f, encoding="utf-8").read()
  if not "<eu>" in gabc:
    noeus.append(f)
# here, manually check noeus and remove them from ll if they indeed should not have eus (antiphons without psalms, hymns)

# this prints a list of all euouaes used in a list of gabc files
# all files must have eus and modes
results = defaultdict(set)
for f in ll:
  gabc=open(f, encoding="utf-8").read()
  mode = gabc.split("mode:")[1].split('\n')[0]
  eu = "<eu>" + gabc.split("<eu>")[1].split("(::)")[0]+"(::)"
  results[mode].add(eu)
for x in sorted(list(results.keys())): print(x, results[x])

###############################

# this ensures that all antiphons that have an euouae also have a french mode indication
ll = os.listdir(".")
raw_euouaes = open("../standard_euouaes.txt", encoding="utf-8").read().split("\n\n")
euouaes = {}
for triplet in raw_euouaes:
  [mode, eu, freu] = triplet.split("\n")
  euouaes[eu]=freu
for f in ll:
  gabc=open(f, encoding="utf-8").read()
  if "<eu>" in gabc:
    eu = "<eu>" + gabc.split("<eu>")[1].split("(::)")[0]+"(::)"
    gabc = gabc.split("<eu>")[0] + "\n" + eu + "\n" + euouaes[eu]
    fw = open(f, "w", encoding="utf-8")
    fw.write(gabc)
    fw.close()