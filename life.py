from grid import Grid
from time import sleep

def play (grid, max_gen):
    generation = 0
    changed = True
    print('Generation = ' + str(generation))
    print(grid)
    while (generation < max_gen) and changed:
        changed = grid.evolve()
        print('Generation = ' + str(generation))
        print(grid)
        sleep(0.01)
        generation += 1
    return generation

def run_life(filename, max_gen):
    return play(Grid(filename), max_gen)

def main ():
    # filename = input('Enter the name of the initialization file: ')
    filename = "dflt_gridfile.txt"
    max_gen = int(input('Enter the maximum number of generations to compute: '))
    grid = Grid(filename)
    play(grid, max_gen)

if __name__ == '__main__':
    main()