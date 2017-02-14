import numpy as np
import os
import matplotlib.pyplot as plt
import argparse
from time import clock
# ========================== Note ===================================
# This version suport nucleic acid sequence generation only.
# The protein sequence generation is unimplemented.


# =========================  parameters =============================

def check_positiveInt(value):
    ("return the value itself if it is a positive integer,"
     "otherwise triger an ArgumentTypeError.")
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % value)
    return ivalue


parser = argparse.ArgumentParser()
# Random seed
parser.add_argument("-s", "--rndSeed", type=int, default=42,
                    help="Set random seed")
# Alphabet of symbols to be generated
parser.add_argument("-a", "--alphabet", type=str, nargs='+',
                    default=['a', 'g', 'c', 't'],
                    help="""Alphabet of symbols to be generated.
                         Please pass a space-seperated string to the function.
                         e.g. 'a g c t' is a valid input.""")
# Probabilities of occurence of each symbol
parser.add_argument("-p", "--prob", type=str, nargs='+',
                    default=["0.25", "0.25", "0.25", "0.25"],
                    help="""Probabilities of occurence of each symbol.
                            Please pass a space-seperated string to the function.
                            e.g. '1.0/6 1.0/3 1.0/6 1.0/3' is a valid input.""")
# Count of total sequences generated
parser.add_argument("-n", "--seqCnt", type=check_positiveInt, default=10000,
                    help="Count of total sequences to be generated")
# Length of each sequence generated
parser.add_argument("-l", "--seqLen", type=check_positiveInt, default=120,
                    help="Length of each sequence generated")
# K-mer length
parser.add_argument("-k", "--kmerLen", type=check_positiveInt, default=5,
                    help="Length of K-mer")
# Verbosity option: pop up a new window to show hitogram if specified
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show histogram image")
# Show running time if specified
parser.add_argument("-t", "--timing", action="store_true",
                    help="Use timekeeper")

# Parse command line arguments
args = parser.parse_args()

# Assign arguments into program variables
rndSeed = args.rndSeed
symbolAlphabet = args.alphabet
symbolProb = []
if len(args.alphabet) is not len(args.prob):
    raise argparse.ArgumentTypeError("""Alphabet list and Probability list
                                        should have the same length.""")
for pr in args.prob:
    symbolProb.append(eval(pr))
if abs(sum(symbolProb) - 1) > 1e-5:
    raise argparse.ArgumentTypeError("Sum of probabilities must be one.")

seqCnt = args.seqCnt
seqLen = args.seqLen
kmerLen = args.kmerLen

# ============================= Init ================================
# Timekeeper
if args.timing:
    tick = clock()

#        [Random Initialization]
np.random.seed(rndSeed + seqLen + seqCnt)
symbols = np.array(symbolAlphabet)
prob = np.array(symbolProb)

#        [Output Directory Initialization]
# Create a folder containing the result like "len80".
# If existed, remove it and recreate one.
dirName = "len%d" % (seqLen)
if os.path.exists(dirName):
    __import__('shutil').rmtree(path=dirName)
os.makedirs(dirName)


# ======================= Generate sequences ========================
# Create a new file with name "null_iid.seq.txt" within the output directory
nullModelSeqFile = open("%s/null_iid.seq.txt" % dirName, "w")

# Initialize count of each letter's occurence over all sequences
nA = nG = nC = nT = 0

# Generate `seqCnt` sequences
seqCollection = []
for i in range(1, seqCnt + 1):
    seq = np.random.choice(symbols, seqLen, list(prob))  # one sequence
    # store generated sequence for latter use
    seqCollection.append(''.join(seq))
    # update the letter counts
    nA = nA + (seq == 'a').sum()
    nG = nG + (seq == 'g').sum()
    nC = nC + (seq == 'c').sum()
    nT = nT + (seq == 't').sum()

# Write sequences into file
for seq in seqCollection:
    strseq = seq + '\n'       # append '\n' after the sequence
    nullModelSeqFile.write(strseq)                      # write to file
nullModelSeqFile.close()

# ============================ Write Profile =========================
#           [Introduction to the Context of the Profile]
#
# 1. Symbol refers to the letter that appears in the generated strings.
#    For instance, it stands for {a, g, c, t} when generating genome
#    sequence, and stands for amino acid when generating protein sequence.
#
# 2. Probab means the probability of occurence for each letter
#
# 3. SeqLength means the sequence length and SeqCnt means the sequence count
#
# 4. Random Seed is the seed used when generating psudo-random numbers
#
# 5. `Count:` and `Freq:` reports the total count of generated letters
#    and their frequencies.
profile = open("%s/profile" % dirName, "w")
profile.write("Symbol: %s\n" % ('    '.join(map(str, symbolAlphabet))))
profile.write("Probab: %s\n" % ('    '.join(map(str, symbolProb))))
profile.write("SeqLength=%d    SeqCnt=%d\n" % (seqLen, seqCnt))
profile.write("Random Seed=%d\n" % rndSeed)
profile.write('Count: nA=%d    nG=%d    nC=%d    nT=%d\n' % (nA, nG, nC, nT))
profile.write('Freq:  nA=%f    nG=%f    nC=%f    nT=%f\n' %
              (nA / (seqCnt * seqLen), nG / (seqCnt * seqLen),
               nC / (seqCnt * seqLen), nT / (seqCnt * seqLen))
              )
profile.close()


# ======================== Calculate statistic ========================
def c_n_2(n):
    "Amplifier function to be applied on k-mer count"
    return n * (n - 1)


def D2(seq, kmerLen, amplifier):
    "return D_2^R value of `seq`"
    seqLen = len(seq)
    kmerHash = dict()
    D2result = 0
    # A sliding window moves along the string from `kmerBeginPos`
    # to `seqLen-kmerLen+1`, dividing the string into k-mers and
    # counting the occurence of each k-mer with a dict() `kmerHash`.
    for kmerBeginPos in range(0, seqLen - kmerLen + 1):
        kmer = seq[kmerBeginPos:kmerBeginPos + kmerLen]
        kmerCount = kmerHash.get(kmer, 0)
        kmerHash[kmer] = kmerCount + 1
    # Apply amplifier function to the count of k-mers, and sum them up.
    for (kmer, kmerCount) in kmerHash.items():
        D2result = D2result + amplifier(kmerCount)
    # Return D2 Value
    return D2result


# Create a new file with name "null_iid.d2_k5.txt" within the output directory.
# This file holds the calculated D_2^R values.
d2_output = open("%s/null_iid.d2_k%d.txt" % (dirName, kmerLen), "w")


# Open the generated sequence file
# and Calculate each sequence's D_2^R statistic,
# then write the statistic into the new d2_output file
d2_collection = []
for read in seqCollection:
    stat = D2(seq=read, kmerLen=kmerLen, amplifier=c_n_2)
    d2_collection.append(stat)
    d2_output.write(str(stat) + "\n")
d2_output.close()

# Draw histogram of D_2^R values
d2_collection = np.array(d2_collection)
plt.hist(d2_collection, bins=100, histtype='bar', color='green', alpha=0.5)
plt.title('$D_2^R$ distribution')
plt.savefig("%s/null_iid.d2_k%d.png" % (dirName, kmerLen))

if args.timing:
    tock = clock()
    print("Taking {} seconds".format((tock - tick)))

if args.verbose:
    plt.show()
