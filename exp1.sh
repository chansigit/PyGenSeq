#!/bin/bash
python null.iid.py -n 10000 -k 5 -l 40;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 60;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 80;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 100;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 120;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 140;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 160;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 180;echo "generated!"
python null.iid.py -n 10000 -k 5 -l 200;echo "generated!"
python exp1.subroutine.kde1.py

