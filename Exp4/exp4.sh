python ../null.iid.py              -t -n 10000 -l 200                                       -k 5 -o null_len200_k5
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 5 -o alter_len200_k5

python ../null.iid.py              -t -n 10000 -l 200                                       -k 8 -o null_len200_k8
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 8 -o alter_len200_k8

python ../null.iid.py              -t -n 10000 -l 200                                       -k 11 -o null_len200_k11
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 11 -o alter_len200_k11

python ../null.iid.py              -t -n 10000 -l 200                                       -k 14 -o null_len200_k14
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 14 -o alter_len200_k14

python ../null.iid.py              -t -n 10000 -l 200                                       -k 17 -o null_len200_k17
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 17 -o alter_len200_k17

python ../null.iid.py              -t -n 10000 -l 200                                       -k 20 -o null_len200_k20
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 20 -o alter_len200_k20

python exp4.subroutine.py
