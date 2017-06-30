# ==========================================================================
# IMPORTS

from cell import Cell
# ==========================================================================



# ==========================================================================
# SUPPORTING FUNCTIONS

def line_to_tuple (line, converter):
    if line == '':
        return None
    else:
        return tuple([converter(v) for v in line.split()])

def is_member (value, lst):
    try:
        lst.index(value)
        return True
    except ValueError:
        return False
# ==========================================================================



# ==========================================================================
class Grid (object):

    # ======================================================================
    # DATA MEMBERS

    g = None
    # ======================================================================



    # ======================================================================
    # INITIALIZER
    # Create the object from a file of dimensions and live-cell coordinates.

    def __init__ (self, filename):

        # Open the file.
        try:
            stream = open(filename, 'r')
        except:
            print('Failure opening ' + filename)
            exit()

        # Read the grid's dimensions.
        (rows, cols) = line_to_tuple(stream.readline(), int)

        # Read the coordinates of live cells, making a list of them.
        live_coordinates = []

        while (True):
            read_result = line_to_tuple(stream.readline(), int)
            if read_result == None:
                break
            live_coordinates.append(read_result)

        # Create the grid of Cell objects, initialized to the liveness given by the above list.
        self.g = [ [ Cell(row, col, self, is_member((row, col), live_coordinates)) for col in range(cols) ] for row in range(rows) ]

        # Close the file, since initialization is done.
        stream.close()
    # ======================================================================



    # ======================================================================
    # EVOLVER
    # Advance the grid of cells to the next generation.
    # Return whether any cell changes.

    def evolve (self):

        # First pass: Each cell must prepare to evolve by counting its
        # live neighbors.
        for row in self.g:
            for cell in row:
                cell.count_live_neighbors()

        # Second pass: Each cell must update its state for the next
        # generation.
        any_changed = False
        for row in self.g:
            for cell in row:
                changed = cell.evolve()
                if changed:
                    any_changed = True

        return any_changed
    # ======================================================================



    # ======================================================================
    # IS ALIVE Return whether the cell at the given coordinates is
    # alive.  If the coorindates are off of the grid, then consider
    # the "cell" at that position to be dead.

    def is_alive (self, coordinates):
        
        (row, col) = coordinates
        if (row < 0) or (row >= len(self.g)) or (col < 0) or (col >= len(self.g[row])):
            return False
        else:
            return self.g[row][col].alive
    # ======================================================================



    # ======================================================================
    # STRING
    # Generate a string that represents the entire grid of cells.

    def __str__ (self):

        s = ''
        for row in self.g:
            for cell in row:
                s = s + str(cell)
            s = s + '\n'

        return s
    # ======================================================================



# ==========================================================================
# END OF Grid CLASS
