python ../null.iid.py               -t -n 10000 -l 200                                       -k 8 -o null_len200_k5
python ../alternative.transition.py -t -n 10000 -l 200 --repLen  3 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen3
python ../alternative.transition.py -t -n 10000 -l 200 --repLen  6 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen6
python ../alternative.transition.py -t -n 10000 -l 200 --repLen  9 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen9
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 12 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen12
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 15 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen15
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 18 --repCnt 5 --spacerLen 10 -k 8 -o alter_repLen18
python exp5.subroutine.py
