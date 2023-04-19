from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

class Cell:
    def __init__(self, row: int, col: int, val: float):
        # a cell object has the row, column and value
        self.row = row
        self.col = col
        self.val = val

class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None
# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.row_head = Node()
        self.row_tail = Node()
        self.row_head.next = self.row_tail
        self.row_tail.prev = self.row_head
        self.col_head = Node()
        self.col_tail = Node()
        self.col_head.next = self.col_tail
        self.col_tail.prev = self.col_head
        self.num_rows = 0
        self.num_cols = 0

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # sets the num_rows and num_cols variables to the maximum dimensions possible from the sample data
        self.num_rows = max(lCells, key = lambda c: c.row).row + 1
        self.num_cols = max(lCells, key = lambda c: c.col).col + 1

        # builds an empty spreadsheet along with the pointers for the nodes
        for j in range(self.num_rows):
            row_node = Node()
            row_node.prev = self.row_tail.prev
            self.row_tail.prev.next = row_node
            row_node.next = self.row_tail
            self.row_tail.prev = row_node
            for i in range(self.num_cols):
                new_node = Node()
                new_node.data = Cell(i, j, 0)
                new_node.prev = row_node
                row_node.next = new_node
                row_node = new_node
                prev_col_node = self.col_head
                for k in range(j):
                    prev_col_node = prev_col_node.next
                prev_col_node.next.prev = new_node
                new_node.next = prev_col_node.next
                prev_col_node.next = new_node
                new_node.prev_col = prev_col_node
                row_node.next_row = self.col_head.next
                self.col_head.next.prev_col = row_node
        row_node.next_row = self.col_head.next
        self.col_head.next.prev_col = row_node

        # updates the empty spreadsheet to include the sample data
        for i in range(len(lCells)):
            self.update(lCells[i].row, lCells[i].col, lCells[i].val)  


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        new_row_node = Node()
        new_row_node.prev = self.row_tail.prev
        self.row_tail.prev.next = self.row_tail
        self.row_tail.prev = new_row_node


        for i in range(self.num_cols):
            new_node = Node()
            new_node.data = Cell(i, self.num_rows, 0)
            new_node.prev = new_row_node
            new_row_node.next = new_node
            prev_col_node = self.col_head
            for k in range(self.num_rows):
                prev_col_node = prev_col_node.next
            prev_col_node.next.prev = new_node
            new_node.next = prev_col_node.next
            prev_col_node.next = new_node
            new_node.prev_col = prev_col_node
            new_row_node.next_row = self.col_head.next
            self.col_head.next.prev_col = new_row_node

        self.num_rows += 1


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        new_col_tail = Node()
        new_col_tail.prev = self.col_tail.prev
        self.col_tail.prev.next = self.col_tail
        self.col_tail.prev = new_col_tail

        curr_row_node = self.row_head.next
        for i in range(self.num_rows):
            new_node = Node()
            new_node.data = Cell(i, self.num_cols, 0)
            new_node.prev = curr_row_node.prev
            curr_row_node.prev.next = new_node
            new_node.next = curr_row_node
            curr_row_node.prev = new_node
            curr_row_node = curr_row_node.next
        
        self.num_cols += 1
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # input validation
        if rowIndex < 0 or rowIndex >= self.num_rows:
            return False
        else:
            # find the node corresponding to the row after the new row
            after_row_node = self.row_head.next
            for i in range(rowIndex):
                after_row_node = after_row_node.next

            # create new row node and link it into the row list
            new_row_node = Node()
            new_row_node.prev = after_row_node.prev
            after_row_node.prev.next = new_row_node
            new_row_node.next = after_row_node
            after_row_node.prev = new_row_node

            # create col list and pointers, and link the head back to the row list
            current_col_node = self.col_head.next
            for j in range(self.num_cols):
                new_node = Node()
                new_node.data = Cell(j, rowIndex, 0)
                new_node.prev_col = current_col_node
                new_node.next_col = current_col_node.next_col
                current_col_node.next_col.prev_col = new_node
                current_col_node.next_col = new_node
                current_col_node = current_col_node.next_col

            self.num_rows += 1
            return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        # input validation
        if colIndex < -1 or colIndex >= self.num_cols:
            return False
        if colIndex == -1:
            colIndex = 0
        current_row_node = self.row_head.next
        while current_row_node != self.row_tail:
            # create new col nodes in specified position
            new_node = Node()
            new_node.data = Cell(current_row_node.next.data.row, colIndex, 0)
            new_node.prev = current_row_node
            new_node.next = current_row_node.next
            current_row_node.next.prev = new_node
            current_row_node.next = new_node
            current_row_node = current_row_node.next
        new_col_node = Node()
        new_col_node.prev = self.col_tail.prev
        self.col_tail.prev.next = new_col_node
        new_col_node.next = self.col_tail
        self.col_tail.prev = new_col_node
        self.num_cols += 1
        current_row_node = self.row_head.next
        while current_row_node != self.row_tail:
            current_node = current_row_node.next
            for i in range(colIndex, self.num_cols):
                current_node.data.col = i
                current_node = current_node.next

        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # input validation
        if rowIndex < 0 or rowIndex >= self.num_rows or colIndex < 0 or colIndex >= self.num_cols:
            return False
        else:
            # navigate to the specified node and change the value
            current_row_node = self.row_head.next
            for j in range(rowIndex):
                current_row_node = current_row_node.next

            current_node = current_row_node.next
            for i in range(colIndex):
                current_node = current_node.next
            
            current_node.data.val = value
            return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.num_rows

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        return self.num_cols



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # iterates through row and col nodes, searching for cells have the value that match the parameter
        result = []
        curr_node = self.row_head.next
        while curr_node != self.row_tail:
            row_node = curr_node
            col_node = row_node.next
            while col_node != None:
                if col_node.data.val == value:
                    result.append((col_node.data.row, col_node.data.col))
                col_node = col_node.next
            curr_node = curr_node.next
        return result



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # iterates through row and col nodes, searching for cells have values
        cells = []
        curr_row_node = self.row_head.next
        while curr_row_node != self.row_tail:
            curr_col_node = curr_row_node.next
            while curr_col_node != None:
                if curr_col_node.data.val != None:
                    cells.append(curr_col_node.data)
                curr_col_node = curr_col_node.next
            curr_row_node = curr_row_node.next
        
        return cells
