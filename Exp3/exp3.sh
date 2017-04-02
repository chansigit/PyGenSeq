#!/bin/bash
python ../null.iid.py -t -n 10000 -l 100 -k 3   -o null_len100_k3;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 4   -o null_len100_k4;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 5   -o null_len100_k5;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 6   -o null_len100_k6;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 7   -o null_len100_k7;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 8   -o null_len100_k8;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 9   -o null_len100_k9;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 10 -o null_len100_k10;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 11 -o null_len100_k11;echo "generated!"
python ../null.iid.py -t -n 10000 -l 100 -k 12 -o null_len100_k12;echo "generated!"

python exp3.subroutine.kde1.py
