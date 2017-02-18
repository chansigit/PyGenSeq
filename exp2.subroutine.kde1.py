import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

print("Asymptotic case: KDE Comparing...")
sns.set(color_codes=True)
# http://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context
sns.set_context("talk", rc={"lines.linewidth": 0.2})

# lengths: 300   3000   30000  300000
d2_collection_l300 = []
d2_collection_l3000 = []
d2_collection_l30000 = []
d2_collection_l300000 = []

for d2 in open("null_len300/null_iid.d2.txt", "r"):
    d2_collection_l300.append(int(d2))
d2_collection_l300 = np.array(d2_collection_l300)

for d2 in open("null_len3000/null_iid.d2.txt", "r"):
    d2_collection_l3000.append(int(d2))
d2_collection_l3000 = np.array(d2_collection_l3000)

for d2 in open("null_len30000/null_iid.d2.txt", "r"):
    d2_collection_l30000.append(int(d2))
d2_collection_l30000 = np.array(d2_collection_l30000)

for d2 in open("null_len300000/null_iid.d2.txt", "r"):
    d2_collection_l300000.append(int(d2))
d2_collection_l300000 = np.array(d2_collection_l300000)


sns.kdeplot(d2_collection_l300, label="seqLen=300")
sns.kdeplot(d2_collection_l3000, label="seqLen=3000")
sns.kdeplot(d2_collection_l30000, label="seqLen=30000")
sns.kdeplot(d2_collection_l300000, label="seqLen=300000")
sns.plt.savefig("exp2.kde1.pdf", dpi=1200)
sns.plt.savefig("exp2.kde1.png", dpi=1200)
print("Graph rendered! Finished!")
