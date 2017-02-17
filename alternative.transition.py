import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from time import clock
# ========================== Note ===================================
# This version suport nucleic acid sequence generation only.
# The protein sequence generation is unimplemented.
#
# In this program, a transition-model repeats rendering methods is
# implemented:
# 1. Randomly choose a fragment in the sequence and replace the
#    succeeding letters with repeat element.
# 2. The repeat rendering method accepts three parameters:
#    repLen(repetend length), spacerLen(spacer length),
#    and repCnt(repetend count). A complete repeat region is
#    composed of alternate repetends and spacers.
# 3. More specifically, a head point is randomly selected
#    in each sequence. Then a subsequence starts from the head point
#    with length of `repLen` is recognized as repetend. After the
#    repetend, a subsequence with length of `spacerLen` is then
#    recognized as a spacer. Then another repetend comes afterwards, etc.
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
#                      [Program Basic Options]
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

#                    [Null Model Background Sequence Generation]
# Count of total sequences generated
parser.add_argument("-n", "--seqCnt", type=check_positiveInt, default=10000,
                    help="Count of total sequences to be generated")
# Length of each sequence generated
parser.add_argument("-l", "--seqLen", type=check_positiveInt, default=120,
                    help="Length of each sequence generated")

#                  [Alternative Model Sequence Generation]
# Repetend length
parser.add_argument("--repLen", type=check_positiveInt, default=8,
                    help="Length of repetends")
# Repetend Count
parser.add_argument("--repCnt", type=check_positiveInt, default=3,
                    help="Count of repetends")
# Spacer length
parser.add_argument("--spacerLen", type=int, default=0,
                    help="Length of spacers")


#                     [D_2^R Statistic Computation]
# K-mer length
parser.add_argument("-k", "--kmerLen", type=check_positiveInt, default=5,
                    help="Length of K-mer")


#                  [Program Running Settings]
# Verbosity option: pop up a new window to show hitogram if specified
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Show histogram image")
# Histogram display option: number of histogram bins
parser.add_argument("-b", "--binNum", type=check_positiveInt, default=100,
                    help="Number of histogram bins")
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
repLen = args.repLen
repCnt = args.repCnt
spacerLen = args.spacerLen
binNum = args.binNum

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
dirName = "alter_len%d" % (seqLen)
if os.path.exists(dirName):
    __import__('shutil').rmtree(path=dirName)
os.makedirs(dirName)


# ======================= Generate sequences ========================
# Create a new file with name "alternative.seq.txt" within the output directory
alterModelSeqFile = open("%s/alter.seq.txt" % dirName, "w")

# Initialize count of each letter's occurence over all sequences
nA = nG = nC = nT = 0


def addRepeat(seq, seqLen, repLen, spacerLen, repCnt):
    "Add repeats to`seq`"
    # total length of repetitive region
    totRepLen = repCnt * repLen + (repCnt - 1) * spacerLen
    # 1. Choose a repeat-starting position between [0, seqLen-totRepLen]
    #    randomly
    repStartPos = np.random.randint(seqLen - totRepLen)
    # 2. Extract repetend
    repetend = seq[repStartPos:repStartPos + repLen]
    # 3. Extract (repCnt-1) spacers and concatenate them with repetends,
    #    thus constructing a whole repetitive region in a sequence
    wholeRepeat = repetend
    spacerCnt = repCnt - 1
    for spacerNum in range(1, spacerCnt + 1):
        spacerStartPos = repStartPos + repLen * spacerNum\
            + spacerLen * (spacerNum - 1)
        wholeRepeat = wholeRepeat + \
            seq[spacerStartPos:spacerStartPos + spacerLen] + repetend
    # 4. Integrate the repetitive region into the raw sequence
    addedSeq = seq[0:repStartPos] + wholeRepeat + seq[repStartPos + totRepLen:]
    return (addedSeq, repStartPos)

# Generate `seqCnt` sequences
seqCollection = []
repBeginPosCollection = []
for i in range(1, seqCnt + 1):
    seq = ''.join(np.random.choice(
        symbols, seqLen, list(prob)))  # one sequence
    ret = addRepeat(seq=seq, seqLen=seqLen, repLen=repLen,
                    spacerLen=spacerLen, repCnt=repCnt)
    seq = ret[0]
    repBegin = ret[1]
    # store generated sequence for latter use
    seqCollection.append(seq)

    repBeginPosCollection.append(repBegin)
    # update the letter counts
    seq = np.array(seq)
    nA = nA + (seq == 'a').sum()
    nG = nG + (seq == 'g').sum()
    nC = nC + (seq == 'c').sum()
    nT = nT + (seq == 't').sum()

# Write sequences into file
for seq in seqCollection:
    strseq = seq + '\n'       # append '\n' after the sequence
    alterModelSeqFile.write(strseq)                      # write to file
alterModelSeqFile.close()

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


# Create a new file with name "alter_transition.d2_k5.txt" within the output directory.
# This file holds the calculated D_2^R values.
d2_output = open("%s/alter_transition.d2.txt" % (dirName), "w")


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
sns.set(color_codes=True)
hist = sns.distplot(d2_collection, kde=False, bins=binNum,
                    hist_kws={"histtype": "bar", "alpha": 0.5, "color": "g"},
                    axlabel="$D_2^R$ Values", )
plot = hist.get_figure()
plot.savefig("%s/alter_transition.d2.hist.pdf" % (dirName), dpi=1200)
plot.savefig("%s/alter_transition.d2.hist.png" % (dirName), dpi=1200)

if args.timing:
    tock = clock()
    print("Taking {} seconds".format((tock - tick)))

if args.verbose:
    plt.show()
