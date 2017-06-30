from life import run_life
from math import sqrt
from random import gauss

DFLT_FILENAME = 'dflt_gridfile.txt'

DATASET_SIZE = 1
GRID_SIZE = 50

CLUSTER_EDGE_SIZE = 10
NUM_ACTIVE_CELLS = 10

MU = GRID_SIZE / 2
SIGMA = sqrt(CLUSTER_EDGE_SIZE*3/4)

def gauss_limited(mu, sigma, low, high):
	a = gauss(mu,sigma)
	while (low <= a <= high) == False:
		a = gauss(mu,sigma)
	return a

def main ():
	for x in range(DATASET_SIZE):
		F = open(DFLT_FILENAME, 'w')
		F.write(str(GRID_SIZE) + " " + str(GRID_SIZE) + "\n")
		active_cells = []
		all_cells = [0]* (GRID_SIZE * GRID_SIZE)

		while len(active_cells) < NUM_ACTIVE_CELLS:
			cell = (int(gauss_limited(MU, SIGMA, MU-CLUSTER_EDGE_SIZE, MU+CLUSTER_EDGE_SIZE)), int(gauss_limited(MU, SIGMA, MU-CLUSTER_EDGE_SIZE, MU+CLUSTER_EDGE_SIZE)))
			if cell not in active_cells:
				active_cells.append(cell)
				all_cells[sum(cell)] = 1
				F.write(str(cell[0]) + " " + str(cell[1]) +"\n")

		F.close()






if __name__ == '__main__':
	main()