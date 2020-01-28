from output import Output

class Board:
    def __init__(self, letters):
        self._size = len(letters)
        self.num_rows = self._size
        self.num_cols = self._size
        self._neighbours = {}

        for row in letters:
            if len(row) != self._size:
                raise ValueError("Bad list _size %s, expected %s" % (len(row), self._size))

        for x in range(self._size):
            self._neighbours[x] = []
            for y in range (self._size):
                self._neighbours[x].append(self._calc_neighbours(x, y))

        self._letters = letters

    def get_letter(self, col, row):
        if col >= self._size or row >= self._size:
            raise ValueError("Bad coordinates")

        return self._letters[row][col]

    def _calc_neighbours(self, col, row):
        neighbours = []
        for c in range(col-1, col+2):
            for r in range(row-1, row+2):
                neighbours.append((c, r))
        neighbours.remove((col,row))
        return filter(lambda t: t[0] in range(0, self._size) and t[1] in range(0, self._size), neighbours)

    def get_neighbours(self, col, row):
        return self._neighbours[col][row]

    def __str__(self):
        output = Output()

        output.thick_bar(13)
        output.add('|           |')

        for row in self._letters:
            output.add('|  ' + ' '.join(row) + '  |')

        output.add('|           |')
        output.thick_bar(13)

        return str(output)


FILLER_LETTER = 'Z'


class HexBoard:
    """Representation of hexagonal board.

    Indexing like so:
     2 4 6
    1 3 5 7
     2 4 6
    1 3 5 7
    """
    def __init__(self, row_letters, row_starts):
        # Each row will have letters at odd or even indices
        self.num_rows = len(row_letters)
        assert len(row_letters) == len(row_starts)
        self.num_cols = max([
            row_starts[i] + 2 * (len(row_letters[i]) - 1)
            for i in range(row_starts)
        ])
        self._letters = []
        for _ in self.num_rows:
            self._letters.append(FILLER_LETTER * self.num_cols)

        for i, letters in enumerate(row_letters):
            col = row_starts[i]
            for j, c in enumerate(letters):
                self._letters[i][col] = c
                col += 2

        self.num_cols = max([len(s) for s in self._letters])

    def _calc_neighbors(self):
        pass

    def get_neighbours(self, col, row):
        return self._neighbours[col][row]

    def get_neighbors(self, col, row):
        pass

    def get_letter(self, col, row):
        return self._letters[row][col]
