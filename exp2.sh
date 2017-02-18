#!/bin/bash
#Generating sequences
python null.iid.py -n 10000 -k 5 -l 300;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 3000;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 30000;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 300000;echo "generated!"
#Read the generated null-model sequence, compute, and plot
python exp2.subroutine.kde1.py

