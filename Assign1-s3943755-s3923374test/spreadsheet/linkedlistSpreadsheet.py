from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

class Cell:
    def __init__(self, row: int, col: int, val: float):
        # a cell object has the row, column and value
        self.row = row
        self.col = col
        self.val = val

class Node:
    def __init__(self, cell = None):
        self.cell = cell
        self.right = None
        self.down = None
        self.up = None
        self.left = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = Node()
        self.head.right = self.head
        self.head.left = self.head
        self.head.up = self.head
        self.head.down = self.head
        self.rowHeads = []
        self.colHeads = []


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED

        # initialize column headers
        for i in range(max(lCells, key = lambda c: c.col).col + 1):
            colHead = Node()
            colHead.right = colHead
            colHead.left = colHead
            colHead.up = colHead
            colHead.down = colHead
            self.colHeads.append(colHead)

        # initialize row headers
        for i in range(max(lCells, key = lambda c: c.row).row + 1):
            rowHead = Node()
            rowHead.right = rowHead
            rowHead.left = rowHead
            rowHead.up = rowHead
            rowHead.down = rowHead
            self.rowHeads.append(rowHead)

        # add cells to the data structure
        for cell in lCells:
            node = Node(cell)
            rowHead = self.rowHeads[cell.row]
            colHead = self.colHeads[cell.col]
            prevNode = colHead
            while prevNode.down != colHead and prevNode.down.cell.row < cell.row:
                prevNode = prevNode.down
            node.down = prevNode.down
            prevNode.down = node
            node.up = prevNode
            node.down.up = node

            prevNode = rowHead
            while prevNode.right != rowHead and prevNode.right.cell.col < cell.col:
                prevNode = prevNode.right
            node.right = prevNode.right
            prevNode.right = node
            node.left = prevNode
            node.right.left = node
         


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """

        # TO BE IMPLEMENTED
        rowHead = Node()
        rowHead.right = rowHead
        rowHead.left = rowHead
        rowHead.up = self.rowHeads[-1]
        rowHead.down = self.rowHeads[-1].down
        self.rowHeads[-1].down = rowHead
        rowHead.down.up = rowHead
        self.rowHeads.append(rowHead)


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        # TO BE IMPLEMENTED
        # Create a new column header node
        newColHead = Node()
        newColHead.right = newColHead
        newColHead.left = newColHead
        newColHead.up = self.head
        newColHead.down = self.head

        # Link new column header node to previous column header node
        prevColHead = self.colHeads[-1]
        prevColHead.right = newColHead
        newColHead.left = prevColHead

        # Update column header list
        self.colHeads.append(newColHead)

        # Update nodes in each row
        for rowHead in self.rowHeads:
            # Create a new node for the new column
            newNode = Node()
            newNode.right = newNode
            newNode.left = newNode
            newNode.up = rowHead
            newNode.down = rowHead.down

            # Link new node to previous node in row
            prevNode = rowHead
            while prevNode.right != rowHead and prevNode.right.cell.col < len(self.colHeads) - 1:
                prevNode = prevNode.right
            newNode.right = prevNode.right
            prevNode.right = newNode
            newNode.left = prevNode
            newNode.right.left = newNode

            # Update nodes above and below new node
            newNode.up.down = newNode
            newNode.down.up = newNode

        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # TO BE IMPLEMENTED
        if rowIndex < 0 or rowIndex >= len(self.rowHeads):
            return False

        newRowHead = Node()
        newRowHead.right = newRowHead
        newRowHead.left = newRowHead
        newRowHead.up = self.head
        newRowHead.down = self.head

        prevRowHead = self.rowHeads[rowIndex]
        nextRowHead = prevRowHead.down

        newRowHead.down = nextRowHead
        nextRowHead.up = newRowHead
        newRowHead.up = prevRowHead
        prevRowHead.down = newRowHead

        self.rowHeads.insert(rowIndex + 1, newRowHead)

        for i in range(len(self.colHeads)):
            newCell = Node(Cell(rowIndex+1, i, 0))
            prevNode = prevRowHead.right
            while prevNode != prevRowHead and prevNode.cell.col < i:
                prevNode = prevNode.right
            newCell.right = prevNode
            prevNode.left.right = newCell
            newCell.left = prevNode.left
            prevNode.left = newCell
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """

        # TO BE IMPLEMENTED
        # Check if the column index is valid
        if colIndex < -1 or colIndex >= len(self.colHeads):
            return False

        # Create a new column header node
        newColHead = Node()
        newColHead.right = newColHead
        newColHead.left = newColHead
        newColHead.up = self.colHeads[0].up
        newColHead.down = self.colHeads[0]
        newColHead.up.down = newColHead
        newColHead.down.up = newColHead

        # Insert the new column header into the column headers list
        if colIndex == -1:
            self.colHeads.insert(0, newColHead)
        else:
            self.colHeads.insert(colIndex+1, newColHead)

        # Link the new column header with the neighboring columns
        if colIndex == -1:
            prevColHead = self.colHeads[1]
        else:
            prevColHead = self.colHeads[colIndex]
        newColHead.left = prevColHead
        newColHead.right = prevColHead.right
        prevColHead.right = newColHead
        newColHead.right.left = newColHead

        # Update the nodes in the new column
        currNode = newColHead.up
        while currNode != newColHead:
            newNode = Node()
            newNode.cell = Cell(currNode.cell.row, len(self.colHeads) - 2, 0)
            newNode.up = currNode.up
            newNode.down = currNode
            currNode.up.down = newNode
            currNode.up = newNode
            prevNode = newNode
            currNode = currNode.up

            # Link the new node with the neighboring nodes
            while prevNode.right != newNode and prevNode.right.cell.col < newNode.cell.col:
                prevNode = prevNode.right
            newNode.right = prevNode.right
            prevNode.right = newNode
            newNode.left = prevNode
            newNode.right.left = newNode


        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED
        # Check if the row and column indices are within the range of the linked list
        if rowIndex >= len(self.rowHeads) or colIndex >= len(self.colHeads):
            return False

        # Find the node corresponding to the given cell and update its value
        rowHead = self.rowHeads[rowIndex]
        colHead = self.colHeads[colIndex]
        node = colHead
        while node.down != colHead and node.down.cell.row <= rowIndex:
            node = node.down
            if node.cell and node.cell.row == rowIndex and node.cell.col == colIndex:
                node.cell.val = value
                return True

        # If the node is not found, return False
        return False


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return len(self.rowHeads) - 1

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return len(self.colHeads)



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED
        result = []

        # iterate over all rows
        for rowHead in self.rowHeads:
            currentNode = rowHead.right
            while currentNode != rowHead:
                # check if the cell value matches the input value
                if currentNode.cell.val == value:
                    # add the cell's row and column to the result list
                    result.append((currentNode.cell.row, currentNode.cell.col))
                currentNode = currentNode.right
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return result



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        # TO BE IMPLEMENTED
        cells = []
        for rowHead in self.rowHeads:
            currNode = rowHead.right
            while currNode != rowHead:
                if currNode.cell is not None:
                    cells.append(currNode.cell)
                currNode = currNode.right

        # TO BE IMPLEMENTED
        return cells
