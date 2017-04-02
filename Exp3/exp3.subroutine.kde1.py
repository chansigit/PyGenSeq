import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
from statsmodels.stats.diagnostic import lillifors
from scipy.stats.mstats import normaltest

print("Asymptotic case: KDE Comparing...")
sns.set(color_codes=True)
# http://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context
sns.set_context("talk", rc={"lines.linewidth": 0.2})

# k=3,4,5, ..., 12
d2_collection_k3 = []
d2_collection_k4 = []
d2_collection_k5 = []
d2_collection_k6 = []
d2_collection_k7 = []
d2_collection_k8 = []
d2_collection_k9 = []
d2_collection_k10 = []
d2_collection_k11 = []
d2_collection_k12 = []

for d2 in open("null_len100_k3/null_iid.d2.txt", "r"):
    d2_collection_k3.append(int(d2))
d2_collection_k3 = np.array(d2_collection_k3)

for d2 in open("null_len100_k4/null_iid.d2.txt", "r"):
    d2_collection_k4.append(int(d2))
d2_collection_k4 = np.array(d2_collection_k4)

for d2 in open("null_len100_k5/null_iid.d2.txt", "r"):
    d2_collection_k5.append(int(d2))
d2_collection_k5 = np.array(d2_collection_k5)

for d2 in open("null_len100_k6/null_iid.d2.txt", "r"):
    d2_collection_k6.append(int(d2))
d2_collection_k6 = np.array(d2_collection_k6)

for d2 in open("null_len100_k7/null_iid.d2.txt", "r"):
    d2_collection_k7.append(int(d2))
d2_collection_k7 = np.array(d2_collection_k7)

for d2 in open("null_len100_k8/null_iid.d2.txt", "r"):
    d2_collection_k8.append(int(d2))
d2_collection_k8 = np.array(d2_collection_k8)

for d2 in open("null_len100_k9/null_iid.d2.txt", "r"):
    d2_collection_k9.append(int(d2))
d2_collection_k9 = np.array(d2_collection_k9)

for d2 in open("null_len100_k10/null_iid.d2.txt", "r"):
    d2_collection_k10.append(int(d2))
d2_collection_k10 = np.array(d2_collection_k10)

for d2 in open("null_len100_k11/null_iid.d2.txt", "r"):
    d2_collection_k11.append(int(d2))
d2_collection_k11 = np.array(d2_collection_k11)

for d2 in open("null_len100_k12/null_iid.d2.txt", "r"):
    d2_collection_k12.append(int(d2))
d2_collection_k12 = np.array(d2_collection_k12)


plt.subplot(221)
sns.kdeplot(d2_collection_k3, label="k=3" ,bw=3 )
sns.kdeplot(d2_collection_k4, label="k=4",bw=3)
sns.kdeplot(d2_collection_k5, label="k=5",bw=3)
sns.kdeplot(d2_collection_k6, label="k=6",bw=3)

plt.subplot(222)
sns.kdeplot(d2_collection_k7, label="k=7",bw=3)
sns.kdeplot(d2_collection_k8, label="k=8",bw=3)

plt.subplot(212)
sns.kdeplot(d2_collection_k9, label="k=9",bw=3)
sns.kdeplot(d2_collection_k10, label="k=10",bw=3)
sns.kdeplot(d2_collection_k11, label="k=11",bw=3)
sns.kdeplot(d2_collection_k12, label="k=12",bw=3)

sns.plt.savefig("exp3.kde1.pdf", dpi=1200)
sns.plt.savefig("exp3.kde1.png", dpi=1200)
print("Graph rendered! Finished!")
