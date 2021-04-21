# Branch Address Table
from collections import OrderedDict

bat = OrderedDict()

def check_in_bat(pc):
	if pc in bat.keys():
		return True, bat[pc]
	return False

def add_to_bat(pc, dest):
	bat[pc] = dest

def get_bat():
    return bat


#Static Branch Prediction (predicts 'taken' for backward branches and 'not taken' for forward branches)
def predict_taken_or_not(PC, dest) :

	diff = int(alu(PC, dest, 32, 32, 'subtract'),16)
	if diff > 0 :
		return 'taken'
	else :
		return 'not taken'
    
























