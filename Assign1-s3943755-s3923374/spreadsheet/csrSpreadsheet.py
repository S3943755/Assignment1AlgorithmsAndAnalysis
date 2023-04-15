from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------




class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.colA = []
        self.valA = []
        self.sumA = [0]
        self.colLength = -1


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        # TO BE IMPLEMENTED
        # Quick sort all the cells based on row then append the sorted array cell value's into valA and column index into colA
        lCells = self.quickSortCol(lCells)

        sum = 0
        row = 0

        # append all cells into self variables and calculate sum
        for cell in lCells:
            self.colA.append(cell.col)
            self.valA.append(cell.val)
            self.colLength =  cell.col

            # checks if the row for the cell is the same as the row focused on for sumA index
            while (row != cell.row):
                self.sumA.append(sum)

                row += 1
            
            sum += cell.val

        # add self again for final cell
        self.sumA.append(sum)
        
        print("colA:", self.colA)
        print("valA:", self.valA)
        print("sumA:", self.sumA)


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        

        # TO BE IMPLEMENTED
        self.sumA.append(self.sumA[self.rowNum - 1])


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        self.colLength += 1


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        # TO BE IMPLEMENTED
        # check if input is within range of the spreadsheet
        if (rowIndex < 0 or rowIndex > self.rowNum()):
            return False
        
        # move sumA values to add new row
        self.sumA.insert(rowIndex, self.sumA[rowIndex - 1])

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        # TO BE IMPLEMENTED
        if (colIndex < 0 or colIndex > self.colLength):
            return False

        for col in self.colA:
            if col >= colIndex:
                col += 1

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

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED

        return len(self.sumA) - 1


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return self.colLength




    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []




    def entries(self) -> [Cell]:
        """
        @return a list of cells that have values (i.e., all non None cells).
        """

        return []

    def quickSortCol(self, lCells: [Cell]) -> [Cell]:
        """
        @return a sorted list of the inputted cells.
        """
        
        if len(lCells) <= 1:
            return lCells
        
        else:
            pivot = lCells[0]
            leftVals = []
            rightVals = []

            for i in range(1, len(lCells)):
                
                if (lCells[i].row < pivot.row):
                    leftVals.append(lCells[i])

                else:
                    rightVals.append(lCells[i])
        
        return self.quickSortCol(leftVals) + [pivot] + self.quickSortCol(rightVals)