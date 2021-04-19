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
    
























