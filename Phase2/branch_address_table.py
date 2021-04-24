# Branch Address Table
from collections import OrderedDict

bat = OrderedDict()

def check_in_bat(pc):
	if pc in bat.keys():
		return True
	return False

def add_to_bat(pc, dest):
	bat[pc] = dest

def get_bat(PC):
    return bat[PC]


#Static Branch Prediction (predicts 'taken' for backward branches and 'not taken' for forward branches)
def predict_taken_or_not(imm) :
	msb = format(int(imm, 16), '0>12b')[0]
	if msb == '1':
		return 'taken'
	return 'not taken'
    
























