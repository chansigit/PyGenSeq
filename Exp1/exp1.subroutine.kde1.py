import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


print("KDE Comparing...")
sns.set(color_codes=True)

#http://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context
sns.set_context("talk", rc={"lines.linewidth": 0.8})

# Manually set the length #!HERE#!
for num in range(40, 201, 20):
    seqFileName = "null_len%d/null_iid.d2.txt" % num
    listName = "d2r_len%d" % num
    labelName= "seqLen=%d" % num
    globals()[listName] = []
    d2_collection = globals()[listName] 
    d2_collection = []
    for d2 in open(seqFileName, "r"):
        d2_collection.append(int(d2))
    print("%s read successfully, with %d sequences." %
          (seqFileName, len(d2_collection)))
    x=np.array(d2_collection)
    sns.kdeplot(x, bw=2 ,label=labelName)
sns.plt.savefig("exp1.kde1.pdf", dpi=1200)
sns.plt.savefig("exp1.kde1.png", dpi=1200)
print("Graph rendered! Finished!")
