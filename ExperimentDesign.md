# Experiment Design

##1. Null model
Parameters taken into consideration: 

* -n --seqCnt 
* -l --seqLen
* -k --kmerLen


### 1.1 Experiment 1: Sequence Length Variation
Investigate sequence length's impact on the distribution.
Controled parameters: -n 10000 -k 5 

    python null.iid.py -n 10000 -k 5 -l 40
    python null.iid.py -n 10000 -k 5 -l 60
    python null.iid.py -n 10000 -k 5 -l 80
    python null.iid.py -n 10000 -k 5 -l 100
    python null.iid.py -n 10000 -k 5 -l 120
    python null.iid.py -n 10000 -k 5 -l 140
    python null.iid.py -n 10000 -k 5 -l 160
    python null.iid.py -n 10000 -k 5 -l 180
    python null.iid.py -n 10000 -k 5 -l 200

Read the generated null-model sequence files and plot the kernel density estimation to see the tendency.

    # manually set lenth from 40 to 200 in this script
    python exp1.subroutine.kde1.py

