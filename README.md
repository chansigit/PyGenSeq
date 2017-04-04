# *** PyGenSeq ***
## Experiment Design

### 1. Null model
Parameters taken into consideration:

* -n --seqCnt
* -l --seqLen
* -k --kmerLen

##### 1.1 Experiment 1 - Null Model: Sequence Length Variation
Investigate sequence length's impact on the distribution.
Controled parameters: -n 10000 -k 5

To start the experiment, run:

    bash exp1.sh

`exp1.sh` contains the following contents:

    # Generating sequences and compute D_2^R values
    python null.iid.py -n 10000 -k 5 -l 40
    python null.iid.py -n 10000 -k 5 -l 60
    python null.iid.py -n 10000 -k 5 -l 80
    python null.iid.py -n 10000 -k 5 -l 100
    python null.iid.py -n 10000 -k 5 -l 120
    python null.iid.py -n 10000 -k 5 -l 140
    python null.iid.py -n 10000 -k 5 -l 160
    python null.iid.py -n 10000 -k 5 -l 180
    python null.iid.py -n 10000 -k 5 -l 200

    # Read the D_2^R of generated null-model sequence files and plot
    # the kernel density estimation to see the tendency.
    # manually set lenth from 40 to 200 in this script
    python exp1.subroutine.kde1.py

The result is shown in the figure:
![image](Exp1/exp1.kde1.png)

##### 1.2 Experiment 2 - Null Asymptotic: Sequence Length Tends to Infinity
Investigate how the distribution varies as the sequence length tends to infinity
Controled parameters: -n 10000 -k 5

To start the experiment, run:

    bash exp2.sh

`exp2.sh` contains the following contents:

    # Generating sequences and compute D_2^R values
    python null.iid.py -n 10000 -k 5 -l 300
    python null.iid.py -n 10000 -k 5 -l 3000
    python null.iid.py -n 10000 -k 5 -l 30000
    python null.iid.py -n 10000 -k 5 -l 300000

    #Read the D_2^R of generated null-model sequences, compute, and plot
    python exp2.subroutine.kde1.py

The result is shown in the figure:
![image](Exp2/exp2.kde1.png)

If we scale up the figure, we can see four seperated peaks:
the blue one and the green one are on the left,
the read and short one besides the above two,
and the tiny purple one on the right.

Unfortunately, both lillifors test and normality test in `exp2.subroutine.kde1.py`
indicate the asymptotic distribution is not a normal distribution.


##### 1.3 Experiment 3 - Null Model: K-mer Length Variation
Investigate K-mer length's impact on the distribution.
Controled parameters: -n 10000 -l 200

To start the experiment, run:

    bash exp3.sh


`exp3.sh` contains the following contents:

    # Calculate D2 with different k
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

    # Read the D_2^R of generated sequences in the two group, compute and plot
    python exp3.subroutine.kde1.py

The result is shown in the figure:
![image](Exp3/exp3.kde1.png)
We can see that higher k-values will push the distribution curve to the
left side and make it thinner and higher.

### 2. Alternative model
In alternative model, repeats are inserted into sequences generated with i.i.d method.
In addition to parameters mentioned above in the null model:
* -n --seqCnt
* -l --seqLen
* -k --kmerLen

,we have to further consider parameters that are used to generate repeats:
* --repLen
* --repCnt
* --spacerLen

Our alternative model inserts one repetitive section that has a structure looks like:

`" Repeat--Spacer--Repeat--Spacer-- ... -- Spacer--Repeat "`

All "Repeat"s are identical and have the same length,
while all "Spacer"s are different from each other but share the same length.

Note that the "Spacer" part is a null string for tandem repeats.
The parameter `repLen` adjusts the length of "Repeat",
the parameter `repCnt` adjusts the number of "Repeat" in the repetitive section,
and the parameter "spacerLen" adjusts the length of non-repetitive interspaced strings.

##### 2.1 Experiment 4 - Alternative model: K-mer length's impact on D_2^R
In this experiment, we generated sequences under the null model and the alternative model,
compute the $D_2^R$ values and plot their histograms and kernel density estimations.

    python ../null.iid.py               -t -n 10000 -l 200                                       -k 5 -o null_len200_k5
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 5 -o alter_len200_k5

    python ../null.iid.py               -t -n 10000 -l 200                                       -k 8 -o null_len200_k8
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 8 -o alter_len200_k8

    python ../null.iid.py               -t -n 10000 -l 200                                       -k 11 -o null_len200_k11
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 11 -o alter_len200_k11

    python ../null.iid.py               -t -n 10000 -l 200                                       -k 14 -o null_len200_k14
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 14 -o alter_len200_k14

    python ../null.iid.py               -t -n 10000 -l 200                                       -k 17 -o null_len200_k17
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 17 -o alter_len200_k17

    python ../null.iid.py               -t -n 10000 -l 200                                       -k 20 -o null_len200_k20
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 20 -o alter_len200_k20

    python exp4.subroutine.py

The result is shown in the following figure.

From the figure we can observe that:
- Under null model, the spikes stay at the zero point when k>=8
- Smaller k values will lead to more duplicated identical k-mers, pushing the peaks to the right side.
- k=8 is a good choice for repeats detecting because the distance between the null model's peak and the alternative model's peak
  is the farthest under this condition.

![image](Exp4/exp4.kde1.ps.png)

##### 2.2 Experiment 5 - Alternative model: repLen's impact on D_2^R (Unimplemented)
    python ../null.iid.py               -t -n 10000 -l 200                                       -k 8 -o null_len200_k8
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen  3 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen3
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen  6 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen6
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen  9 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen9
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 12 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen12
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 15 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen15
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen18
    python exp5.subroutine.py

##### 2.3 Experiment 6 - Alternative model: repCnt's impact on D_2^R (Unimplemented)
    python ../null.iid.py               -t -n 10000 -l 200                                        -k 8 -o null_len200_k8
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen 10 -k 8 -o alter_repCnt5
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  6 --spacerLen 10 -k 8 -o alter_repCnt6
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  7 --spacerLen 10 -k 8 -o alter_repCnt7
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  8 --spacerLen 10 -k 8 -o alter_repCnt8
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  9 --spacerLen 10 -k 8 -o alter_repCnt9
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt 10 --spacerLen 10 -k 8 -o alter_repCnt10
    python exp6.subroutine.py

##### 2.4 Experiment 7 - Alternative model: spacerLen's impact on D_2^R (Unimplemented)
    python ../null.iid.py               -t -n 10000 -l 200                                        -k 8 -o null_len200_k8
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen  0 -k 8 -o alter_repCnt5
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen  3 -k 8 -o alter_repCnt6
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen  6 -k 8 -o alter_repCnt7
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen  9 -k 8 -o alter_repCnt8
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen 12 -k 8 -o alter_repCnt9
    python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen 15 -k 8 -o alter_repCnt10
    python exp7.subroutine.py
