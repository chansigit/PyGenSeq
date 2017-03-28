# Experiment Design

##1. Null model
Parameters taken into consideration: 

* -n --seqCnt 
* -l --seqLen
* -k --kmerLen


### 1.1 Experiment 1 - Null Model: Sequence Length Variation
Investigate sequence length's impact on the distribution.
Controled parameters: -n 10000 -k 5 

To start the experiment, run:

    bash exp1.sh

`exp1.sh` contains the following contents:

    # Generating sequences
    python null.iid.py -n 10000 -k 5 -l 40
    python null.iid.py -n 10000 -k 5 -l 60
    python null.iid.py -n 10000 -k 5 -l 80
    python null.iid.py -n 10000 -k 5 -l 100
    python null.iid.py -n 10000 -k 5 -l 120
    python null.iid.py -n 10000 -k 5 -l 140
    python null.iid.py -n 10000 -k 5 -l 160
    python null.iid.py -n 10000 -k 5 -l 180
    python null.iid.py -n 10000 -k 5 -l 200

    # Read the generated null-model sequence files and plot 
    # the kernel density estimation to see the tendency.
    # manually set lenth from 40 to 200 in this script
    python exp1.subroutine.kde1.py

### 1.2 Experiment 2 - Null Asymptotic: Sequence Length Tends to Infinity
Investigate how the distribution varies as the sequence length tends to infinity
Controled parameters: -n 10000 -k 5 

To start the experiment, run:

    bash exp2.sh

`exp2.sh` contains the following contents:

    # Generating sequences
    python null.iid.py -n 10000 -k 5 -l 300
    python null.iid.py -n 10000 -k 5 -l 3000
    python null.iid.py -n 10000 -k 5 -l 30000
    python null.iid.py -n 10000 -k 5 -l 300000

    #Read the generated null-model sequences, compute, and plot
    python exp2.subroutine.kde1.py

### 1.3 Experiment 3 - Null Model: K-mer Length Variation (Unimplemented)
Investigate K-mer length's impact on the distribution.
Controled parameters: -n 10000 -l 200

To start the experiment, run:

    bash exp3.sh

`exp3.sh` contains the following contents:

    # Generating Group1 sequences 
    python null.iid.py -t -n 10000 -l 100 -k 3
    python null.iid.py -t -n 10000 -l 100 -k 4
    python null.iid.py -t -n 10000 -l 100 -k 5
    python null.iid.py -t -n 10000 -l 100 -k 6
    python null.iid.py -t -n 10000 -l 100 -k 7
    python null.iid.py -t -n 10000 -l 100 -k 8
    python null.iid.py -t -n 10000 -l 100 -k 9
    python null.iid.py -t -n 10000 -l 100 -k 10 
    python null.iid.py -t -n 10000 -l 100 -k 11
    python null.iid.py -t -n 10000 -l 100 -k 12

    # Generating Group2 sequences
    python null.iid.py -t -n 10000 -l 30000 -k 3
    python null.iid.py -t -n 10000 -l 30000 -k 4
    python null.iid.py -t -n 10000 -l 30000 -k 5
    python null.iid.py -t -n 10000 -l 30000 -k 6
    python null.iid.py -t -n 10000 -l 30000 -k 7
    python null.iid.py -t -n 10000 -l 30000 -k 8
    python null.iid.py -t -n 10000 -l 30000 -k 9
    python null.iid.py -t -n 10000 -l 30000 -k 10
    python null.iid.py -t -n 10000 -l 30000 -k 11
    python null.iid.py -t -n 10000 -l 30000 -k 12

    # Read the generated sequences in the two group, compute and plot
    python exp3.subroutine.kde1.py

### 1.4 Experiment 4 - Alternative model: (Unimplemented)
Generated various kinds of sequences with different parameters under 
alternative model.

