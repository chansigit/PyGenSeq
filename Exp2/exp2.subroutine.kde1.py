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

# lengths: 300   3000   30000  300000
d2_collection_l300 = []
d2_collection_l3000 = []
d2_collection_l30000 = []
d2_collection_l300000 = []

# The following codes adopts two means of normality test:
#     statsmodels.stats.diagnostic.lillifors
# AND scipy.stats.mstats.normaltest.
# Both tests have the normal null hypothesis.
# The smaller the p-value is the more likely that null hypo
# is rejected. On the contrary, the larger the p-value is
# the more likely that the null hypo get accepted.
print("\n=============== seqLen=300 ===============")
for d2 in open("null_len300/null_iid.d2.txt", "r"):
    d2_collection_l300.append(int(d2))
d2_collection_l300 = np.array(d2_collection_l300)
print("Lilliefors test:")
print(lillifors(d2_collection_l300))
print("D’Agostino and Pearson’s test:")
print(normaltest(d2_collection_l300))

print("\n=============== seqLen=3000 ===============")
for d2 in open("null_len3000/null_iid.d2.txt", "r"):
    d2_collection_l3000.append(int(d2))
d2_collection_l3000 = np.array(d2_collection_l3000)
print("Lilliefors test:")
print(lillifors(d2_collection_l3000))
print("D’Agostino and Pearson’s test:")
print(normaltest(d2_collection_l3000))

print("\n=============== seqLen=30000 ===============")
for d2 in open("null_len30000/null_iid.d2.txt", "r"):
    d2_collection_l30000.append(int(d2))
d2_collection_l30000 = np.array(d2_collection_l30000)
print("Lilliefors test:")
print(lillifors(d2_collection_l30000))
print("D’Agostino and Pearson’s test:")
print(normaltest(d2_collection_l30000))

print("\n=============== seqLen=300000 ===============")
for d2 in open("null_len300000/null_iid.d2.txt", "r"):
    d2_collection_l300000.append(int(d2))
d2_collection_l300000 = np.array(d2_collection_l300000)
print("Lilliefors test:")
print(lillifors(d2_collection_l300000))
print("D’Agostino and Pearson’s test:")
print(normaltest(d2_collection_l300000))

sns.kdeplot(d2_collection_l300, label="seqLen=300")
sns.kdeplot(d2_collection_l3000, label="seqLen=3000")
sns.kdeplot(d2_collection_l30000, label="seqLen=30000")
sns.kdeplot(d2_collection_l300000, label="seqLen=300000")
sns.plt.savefig("exp2.kde1.pdf", dpi=1200)
sns.plt.savefig("exp2.kde1.png", dpi=1200)
print("Graph rendered! Finished!")