from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED

        # initialise cell and 2d list which is in row x column (so 1,2 would be row 1 column 2)
        self.spreadsheet = []


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        
        
        # TO BE IMPLEMENTED
        # make 2d lists with the newlist variable being a row and teh content being a column
        #[CellA(row,col,val), CellB(row,col,val), CellC(row,col,val)]

        # initializers
        rowMax = -1
        colMax = -1

        # find dimensions for spreadsheet
        for cell in lCells:
            if (rowMax < cell.row):
                rowMax = cell.row

            if (colMax < cell.col):
                colMax = cell.col

        # build the spreadsheet size filling each column with nulls
        # make temp list
        tempColList = []
        
        # append columns to spreadsheet
        for i in range(0, rowMax + 1):

            # build col
            tempColList = []

            for i in range(0, colMax + 1):
                tempColList.append(None)

            self.spreadsheet.append(tempColList)

        # Insert Cells by spreadsheet[row][col] = val
        for cell in lCells:
            self.spreadsheet[cell.row][cell.col] = cell.val


    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        if (self.uninitialisedBoardCheck()):
            return False
        
        tempColList = []
        for i in range(0, self.colNum()): # creates a new blank row
            tempColList.append(None)
        
        self.spreadsheet.append(tempColList)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        if (self.uninitialisedBoardCheck()):
            return False
        
        rowAmount = self.rowNum()
        
        for i in range(0, rowAmount): # appends a new blank column for each row in the spreadsheet
            self.spreadsheet[i].append(None)
        
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # TO BE IMPLEMENTED
        if (self.uninitialisedBoardCheck()):
            return False
        
        # checks if input is valid
        if (rowIndex < 0 or rowIndex > self.rowNum()):
            return False
        
        # make a new empty column for the new row
        tempColList = []
        for i in range(0, self.colNum()):
            tempColList.append(None)

        # insert new row
        self.spreadsheet.insert(rowIndex, tempColList)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        # TO BE IMPLEMENTED
        if (self.uninitialisedBoardCheck()):
            return False
        
        # checks if input is valid
        if (colIndex < 0 or colIndex > self.colNum()):
            return False
        
        # go through each row, split each column for desired index and add new None value at desired index
        for row in self.spreadsheet:
            row.insert(colIndex, None)

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
        # checking if input is within spreadsheet dimension range
        if ((rowIndex < 0 or rowIndex > self.rowNum() - 1) or (colIndex < 0 or colIndex > self.colNum() - 1)):
            return False
        
        # update the inputted value
        self.spreadsheet[rowIndex][colIndex] = value

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return len(self.spreadsheet)


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        return len(self.spreadsheet[0])



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        # initializer
        returnList = []

        # check the value is with in the spreadsheet using a nested for loop
        for i in range(0, self.rowNum()):

            for j in range(0, self.colNum()):

                if (self.spreadsheet[i][j] == value):
                    currCellIndex = [i, j]
                    returnList.append(currCellIndex)

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return returnList



    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        # initializer
        returnList = []

        # check if the the values are either a int or a float for all indexes in the spreadsheet
        for i in range(0, self.rowNum()):

            for j in range(0, self.colNum()):
                
                if isinstance(self.spreadsheet[i][j], (int, float)):
                    currCell = Cell(i, j, self.spreadsheet[i][j])
                    returnList.append(currCell)

        # TO BE IMPLEMENTED
        return returnList

    def uninitialisedBoardCheck(self) -> bool:
        """
        @return Returns false if rowNum or colNum do not exist, otherwise returns true.
        """

        if (self.rowNum() < 0 or self.colNum() < 0):
            return True
        
        return False