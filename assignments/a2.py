# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType
        An initialized Rat location, with its symbol, row location, and column location.

        symbol: the 1-character symbol for the rat
        row: the row where the rat is located
        col: the column where the rat is located
        num_sprouts_eaten: the number of sprouts that this rat has eaten, which is initially 0.

        Preconditions:
        len(symbol) == 1
        row >= 0
        col >= 0
        
        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """
        assert len(symbol) == 1,\
               'symbol is not an 1-character.'
        
        self.symbol = symbol
        self.set_location(row, col)
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Set the location of the rat to a given row number and column number set.

        >>> rat = Rat('P', 1, 4)
	>>> rat.set_location(3, 5)
        >>> rat.row
        3
        >>> rat.col
        5
        """
        assert row >= 0, \
           'row cannot be negative.'

        assert col >= 0, \
           'col cannot be negative.'
        
        self.row = row
        self.col = col
        
    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add one to the rat's instance variable num_sprouts_eaten.

        >>> rat = Rat('P', 1, 4)
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        >>> rat = Rat('J', 4, 3)
        >>> rat.eat_sprout()
        >>> rat.eat_sprout()
        >>> rat1.__str__()
        'J at (4, 3) ate 2 sprouts.'
        """
        
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize this maze's four instance variables:

        maze: a maze with contents specified by the second parameter.
        rat_1: the first rat in the maze.
        rat_2: the second rat in the maze.
        num_sprouts_left: the number of uneaten sprouts in this maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  Rat('J', 1, 1), \
                  Rat('P', 1, 4))
        >>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', 'J', '.', '.', 'P', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze.num_sprouts_left
        3
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        self.maze[rat_1.row][rat_1.col] = rat_1.symbol
        self.maze[rat_2.row][rat_2.col] = rat_2.symbol

        num_sprouts_left = 0
        for row in maze:
            num_sprouts_left = num_sprouts_left + row.count(SPROUT)

        self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze.

        Preconditions:
        0 <= row < len(maze)
	0 <= col < len(maze[0])

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  Rat('J', 1, 1),\
                  Rat('P', 1, 4))
        >>> maze.is_wall(0, 0)
        True
        >>> maze.is_wall(1, 0)
        True
        >>> maze.is_wall(4, 2)
        True
        >>> maze.is_wall(4, 1)
        False
        """
        '''assert (row >= 0 and row < len(self.maze)),\
               '{} is out of range.'.format(row) 

	assert (col >= 0 and col < len(self.maze[0])),\
               '{} is out of range.'.format(col)'''
	
        return self.get_character(row, col) == WALL
    
    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column. If there is a rat at that location, then its character should be returned rather than HALL

        Preconditions:
        0 <= row < len(maze)
	0 <= col < len(maze[0])
	
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  Rat('J', 1, 1),\
                  Rat('P', 1, 4))
        >>> maze.get_charater(0, 0)
        '#'
        >>> maze.get_charater(1, 2)
        '.'
        >>> maze.get_charater(4, 1)
        '@'
        >>> maze.get_charater(1, 1)
        'J'
        >>> maze.get_charater(1, 4)
        'P'
        """

        '''assert (row >= 0 and row < len(self.maze)),\
               '{} is out of range.'.format(row) 

	assert (col >= 0 and col < len(self.maze[0])),\
               '{} is out of range.'.format(col)'''

        return self.maze[row][col]
        
    def move(self, rat, vertical, horizontal):
        """ (Maze, Rat, int, int) ->bool

        The first parameter represents a maze, the second represents a rat,
        the third represents a vertical direction change (UP, NO_CHANGE or DOWN),
        and the fourth represents a horizontal direction change (LEFT, NO_CHANGE
        or RIGHT).
        
        Return True if and only if there wasn't a wall in the way.

        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  rat_1,\
                  rat_2)
        >>> maze.move(maze, rat_1, UP, RIGHT)
        False
        >>> maze.move(maze, rat_1, NO_CHANGE, RIGHT)
        True        
        """

        assert vertical == LEFT or vertical == RIGHT, \
           'vertical direction wrong.'

        assert horizontal == UP or horizontal == DOWN, \
           'horizontal direction wrong.'

        newrow = rat.row + vertical
        newcol = rat.col + horizontal

        result = True
        if self.is_wall(newrow, newcol):
            result = False
            
        if self.get_character(newrow, newcol) == SPROUT:
            self.maze[row][col] = HALL
            rat.eat_sprout()
            num_sprouts_left -= 1

        rat.set_location(newrow, newcol)
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        return result

    def __str__(self):
        """ (Maze) -> str

        Return a string representation of the maze.

        >>> rat_1 = Rat('J', 1, 1)
        >>> rat_2 = Rat('P', 1, 4)
        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  rat_1,\
                  rat_2)
        >>> maze.__str__()
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        result = ''

        for row in self.maze:
            for char in row:
                result = result + char
            result = result + '\n'

        return result + '{0}\n{1}'.format(
            self.rat_1.__str__(), self.rat_2.__str__())


