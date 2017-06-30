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

def main ():
    filename = input('Enter the name of the initialization file: ')
    max_gen = int(input('Enter the maximum number of generations to compute: '))
    grid = Grid(filename)
    play(grid, max_gen)

if __name__ == '__main__':
    main()
