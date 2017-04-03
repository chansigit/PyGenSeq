import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
from statsmodels.stats.diagnostic import lillifors
from scipy.stats.mstats import normaltest

print("Asymptotic case: KDE Comparing...")
sns.set(color_codes=True)
# http://seaborn.pydata.org/generated/seaborn.set_context.html#seaborn.set_context
sns.set_context("talk", rc={"lines.linewidth": 1})

#
null_k5_set = []
null_k8_set = []
null_k11_set = []
null_k14_set = []
null_k17_set = []
null_k20_set = []
alter_k5_set = []
alter_k8_set = []
alter_k11_set = []
alter_k14_set = []
alter_k17_set = []
alter_k20_set = []

for d2 in open("null_len200_k5/null_iid.d2.txt", "r"):
    null_k5_set.append(int(d2))
for d2 in open("alter_len200_k5/alter_transition.d2.txt", "r"):
    alter_k5_set.append(int(d2))

for d2 in open("null_len200_k8/null_iid.d2.txt", "r"):
    null_k8_set.append(int(d2))
for d2 in open("alter_len200_k8/alter_transition.d2.txt", "r"):
    alter_k8_set.append(int(d2))

for d2 in open("null_len200_k11/null_iid.d2.txt", "r"):
    null_k11_set.append(int(d2))
for d2 in open("alter_len200_k11/alter_transition.d2.txt", "r"):
    alter_k11_set.append(int(d2))

for d2 in open("null_len200_k14/null_iid.d2.txt", "r"):
    null_k14_set.append(int(d2))
for d2 in open("alter_len200_k14/alter_transition.d2.txt", "r"):
    alter_k14_set.append(int(d2))

for d2 in open("null_len200_k17/null_iid.d2.txt", "r"):
    null_k17_set.append(int(d2))
for d2 in open("alter_len200_k17/alter_transition.d2.txt", "r"):
    alter_k17_set.append(int(d2))

for d2 in open("null_len200_k20/null_iid.d2.txt", "r"):
    null_k20_set.append(int(d2))
for d2 in open("alter_len200_k20/alter_transition.d2.txt", "r"):
    alter_k20_set.append(int(d2))

null_k5_set = np.array(null_k5_set)
null_k8_set = np.array(null_k8_set)
null_k11_set = np.array(null_k11_set)
null_k14_set = np.array(null_k14_set)
null_k17_set = np.array(null_k17_set)
null_k20_set = np.array(null_k20_set)

alter_k5_set = np.array(alter_k5_set)
alter_k8_set = np.array(alter_k8_set)
alter_k11_set = np.array(alter_k11_set)
alter_k14_set = np.array(alter_k14_set)
alter_k17_set = np.array(alter_k17_set)
alter_k20_set = np.array(alter_k20_set)

#fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(5,12))
plt.rcParams['figure.figsize']=(10,35)

sns.plt.subplot(811)
sns.plt.xlim(-10,1000)
sns.plt.ylim(0,0.30)
sns.distplot(null_k5_set,  kde=True, kde_kws={"label":"null k=5", "bw":2})
sns.distplot(alter_k5_set, kde=True, kde_kws={"label":"alter k=5", "bw":2})
#sns.kdeplot(null_k5_set, label="null k=5", bw=2)
#sns.kdeplot(alter_k5_set, label="alter k=5", bw=2)

sns.plt.subplot(812)
sns.plt.xlim(-10,1000)
sns.plt.ylim(0,0.30)
sns.distplot(null_k8_set,  kde=True, kde_kws={"label":"null k=8", "bw":2})
sns.distplot(alter_k8_set, kde=True, kde_kws={"label":"alter k=8", "bw":2})
#sns.kdeplot(null_k8_set, label="null k=8", bw=2)
#sns.kdeplot(alter_k8_set, label="alter k=8", bw=2)

sns.plt.subplot(813)
sns.plt.xlim(-10,1000)
sns.plt.ylim(0,0.30)
sns.distplot(null_k11_set,  kde=True, kde_kws={"label":"null k=11", "bw":2})
sns.distplot(alter_k11_set, kde=True, kde_kws={"label":"alter k=11", "bw":2})
#sns.kdeplot(null_k11_set, label="null k=11", bw=2)
#sns.kdeplot(alter_k11_set, label="alter k=11", bw=2)

sns.plt.subplot(814)
sns.plt.xlim(-10,1000)
sns.plt.ylim(0,0.30)
sns.distplot(null_k14_set,  kde=True, kde_kws={"label":"null k=14", "bw":2})
sns.distplot(alter_k14_set, kde=True, kde_kws={"label":"alter k=14", "bw":2})
#sns.kdeplot(null_k14_set, label="null k=14", bw=2)
#sns.kdeplot(alter_k14_set, label="alter k=14", bw=2)

sns.plt.subplot(815)
sns.plt.xlim(-10,300)
sns.plt.ylim(0,0.30)
sns.distplot(null_k17_set,  kde=True, kde_kws={"label":"null k=17", "bw":2})
sns.distplot(alter_k17_set, kde=True, kde_kws={"label":"alter k=17", "bw":2})
#sns.kdeplot(null_k17_set, label="null k=17", bw=2)
#sns.kdeplot(alter_k17_set, label="alter k=17", bw=2)

sns.plt.subplot(816)
sns.plt.xlim(-10,300)
sns.plt.ylim(0,0.30)
sns.distplot(null_k20_set,  kde=True, kde_kws={"label":"null k=20", "bw":2})
sns.distplot(alter_k20_set, kde=True, kde_kws={"label":"alter k=20", "bw":2})
#sns.kdeplot(null_k20_set, label="null k=20", bw=2)
#sns.kdeplot(alter_k20_set, label="alter k=20", bw=2)

plt.subplot(817)
sns.plt.xlim(-10,500)
sns.plt.ylim(0,0.20)
sns.kdeplot(null_k5_set, label="null k=5", bw=2)
sns.kdeplot(null_k8_set, label="null k=8", bw=2)
sns.kdeplot(null_k11_set, label="null k=11", bw=2)
sns.kdeplot(null_k14_set, label="null k=14", bw=2)
sns.kdeplot(null_k17_set, label="null k=17", bw=2)
sns.kdeplot(null_k20_set, label="null k=20", bw=2)

plt.subplot(818)
sns.plt.xlim(-10,500)
sns.plt.ylim(0,0.20)
sns.kdeplot(alter_k5_set, label="alter k=5", bw=2)
sns.kdeplot(alter_k11_set, label="alter k=11", bw=2)
sns.kdeplot(alter_k8_set, label="alter k=8", bw=2)
sns.kdeplot(alter_k14_set, label="alter k=14", bw=2)
sns.kdeplot(alter_k17_set, label="alter k=17", bw=2)
sns.kdeplot(alter_k20_set, label="alter k=20", bw=2)

sns.plt.savefig("exp3.kde1.pdf", dpi=1200)
sns.plt.savefig("exp3.kde1.png", dpi=1200)
print("Graph rendered! Finished!")
