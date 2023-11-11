freq = {}
for item in db.Manufacturer:
  if (item in freq):
    freq[item] += 1
  else:
    freq[item] = 1
models=list(freq.values())
manu=list(freq.keys())

plt.figure(figsize=(28,13))
plt.grid(zorder=0)
plt.bar(freq.keys(),freq.values(),color="brown",zorder=3)
plt.title("Number of models per Manufacturer",fontsize=25)
plt.xlabel("Manufacturers",fontsize=20)
plt.ylabel("No. of models",fontsize=20)