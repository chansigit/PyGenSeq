#!/bin/bash
python null.iid.py -t -n 10000 -l 100 -k 3;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 4;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 5;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 6;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 7;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 8;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 9;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 10;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 11;echo "generated!"
python null.iid.py -t -n 10000 -l 100 -k 12;echo "generated!"

python exp3.subroutine.kde1.py
