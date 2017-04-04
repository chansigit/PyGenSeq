python ../null.iid.py               -t -n 10000 -l 200                                        -k 8 -o null_len200_k5
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  5 --spacerLen 10 -k 8 -o alter_repCnt5
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  6 --spacerLen 10 -k 8 -o alter_repCnt6
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  7 --spacerLen 10 -k 8 -o alter_repCnt7
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  8 --spacerLen 10 -k 8 -o alter_repCnt8
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt  9 --spacerLen 10 -k 8 -o alter_repCnt9
python ../alternative.transition.py -t -n 10000 -l 200 --repLen 10 --repCnt 10 --spacerLen 10 -k 8 -o alter_repCnt10
python exp6.subroutine.py