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
            self.colLength =  cell.col + 1 # + 1 due to index 0

            # checks if the row for the cell is the same as the row focused on for sumA index
            while (row != cell.row):
                self.sumA.append(sum)

                row += 1
            
            sum += cell.val

        # add self again for final cell
        self.sumA.append(sum)

        #print("colA:", self.colA)
        #print("valA:", self.valA)
        #print("sumA:", self.sumA)
        
        ##print("colA:", self.colA)
        ##print("valA:", self.valA)
        ##print("sumA:", self.sumA)
        ##print("colLength:", self.colLength)


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        if (self.uninitialisedBoardCheck()):
            return False

        self.sumA.append(self.sumA[self.rowNum()])
        return True


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """

        # TO BE IMPLEMENTED
        if (self.uninitialisedBoardCheck()):
            return False

        self.colLength += 1
        return True


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
        # check for valid initialisation met
        if (self.uninitialisedBoardCheck()):
            return False
        
        if (colIndex < 0 or colIndex > self.colNum() - 1): # where colLength is -1 due to index
            return False

        for i in range(0, len(self.colA)):
            if self.colA[i] >= colIndex:
                self.colA[i] += 1
        
        self.colLength += 1

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
        # check for valid initialisation met

        #print()
        #print("UPDATE CALLED")
        #print("Input Row:", rowIndex, "Input Col:", colIndex, "Input Val:", value)
        #print()
        if (self.uninitialisedBoardCheck()):
            return False
        
        if ((rowIndex < 0 or rowIndex > self.rowNum()) or (colIndex < 0 or colIndex > self.colNum() - 1)):
            return False
        
        #print("before")
        #print("colA:", self.colA)
        #print("valA:", self.valA)
        #print("sumA:", self.sumA)

        focusRowCheck = False
        indexSumA = 1 # the index that corresponds to teh current focusRowIndex (which is + 1 of it)
        colAIndex = 0 # uses the same index for colA and valA
        
        focusRowIndex = 0 # focusRowIndex is the current row in terms of a spreadsheet dimension 
        rowFound = False
        prevValue = 0

        while rowFound != True:
            if focusRowIndex == rowIndex: # find desired row, if so update all future values to fix the new / changed value
                rowFound = True
                #print("Row found")
                #print("Row:", focusRowIndex)
                #print("colAIndex:",colAIndex)
                #print("sum val", self.sumA[indexSumA], "prev sum val", self.sumA[indexSumA - 1])

                if (self.sumA[indexSumA] != self.sumA[indexSumA - 1]): # checks if the current row has an existing value stored
                    difference = self.sumA[indexSumA] - self.sumA[indexSumA - 1] # check logic for what happens if there is existing but more than 1 value as current only checks if theres only 1 value in the row
                    #print("difference")

                    # think this is about only difference - valA at index = 0

                    # if input col value is before what is currently stored
                    if (colIndex < self.colA[colAIndex]):
                        #print("Row stored before")
                        self.colA.insert(colAIndex, colIndex)
                        self.valA.insert(colAIndex, value)
                        self.sumA[indexSumA] = self.sumA[indexSumA] + value

                        for i in range(indexSumA + 1, self.rowNum() + 1):
                            self.sumA[i] = self.sumA[i] + value

                    # if input col is teh same as the currently stored one (meaning replace)
                    elif (colIndex == self.colA[colAIndex]):
                        #print("Row replaced")
                        prevVal = self.valA[colAIndex]

                        self.colA[colAIndex] = colIndex
                        self.valA[colAIndex] = value
                        self.sumA[indexSumA] = self.sumA[indexSumA] + value - prevVal

                        for i in range(indexSumA + 1, self.rowNum() + 1):
                            self.sumA[i] = self.sumA[i] + value - prevVal

                    # if input col value is after what is currently stored
                    elif (colIndex > self.colA[colAIndex]):
                        #print("Row stored after")
                        colAIndex + 1
                        self.colA.insert(colAIndex, colIndex)
                        self.valA.insert(colAIndex, value)
                        self.sumA[indexSumA] = self.sumA[indexSumA] + value

                        for i in range(indexSumA + 1, self.rowNum() + 1):
                            self.sumA[i] = self.sumA[i] + value
                else:
                    #print("Row stored before due to only val in row")
                    #print(self.sumA[indexSumA] != self.sumA[indexSumA - 1])
                    #print(self.sumA[indexSumA])
                    #print(value)

                    #FIX ME, CURRENTLY ONLY PREPENDS IT
                    
                    self.colA.insert(colAIndex, colIndex)
                    self.valA.insert(colAIndex, value)
                    self.sumA[indexSumA] = self.sumA[indexSumA] + value

                    for i in range(indexSumA + 1, self.rowNum() + 1):
                        self.sumA[i] = self.sumA[i] + value

                self.sumA = [round(x,1) for x in self.sumA]

                

            else: # if desired row is not found, check if the current row has a new value by looking a tthe sumA[currIndex] compared to previous
                #print("Row NOT found")
                if (self.sumA[indexSumA] != self.sumA[indexSumA - 1]):
                    colAIndex += 1

            indexSumA += 1
            focusRowIndex += 1
        #print()

        #print("colA:", self.colA)
        #print("valA:", self.valA)
        #print("sumA:", self.sumA)
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
        if (self.uninitialisedBoardCheck()):
            return False

        # see if value is not in valA, and if so return empty array to reduce runtime
        if value not in self.valA:
            return []
        
        count = self.valA.count(value)
        
        returnCells = []
        currRowIndex = 0
        colAIndex = 0
        i = 1 # index position for sumA to determine row

        # if so see which row by checking when sum vals is >= input (this accounts for multiple numbers in a row)
        while (count != len(returnCells)):
            if (self.sumA[i - 1] != self.sumA[i]): # finding when a row has value by seeing if prev row is the same as teh current row we're focusing on
                difference = self.sumA[i] - self.sumA[i - 1]

                if (difference == self.valA[colAIndex]): # only 1 value in the row
                    if (self.valA[colAIndex] == value):
                        returnCells.append([currRowIndex, self.colA[colAIndex]])
                    else:
                        colAIndex += 1 # look at next column as current is incorrect
                else: # for multiple values
                    j = i
                    sumOfCurrentRow = 0
                    while(sumOfCurrentRow != difference):
                        sumOfCurrentRow = self.sumA[j]
                        sumOfCurrentRow = round(sumOfCurrentRow, 1)
                        if (self.valA[j] == value):
                            returnCells.append([currRowIndex, self.colA[colAIndex]])

                        j += 1
                    i = j

            currRowIndex += 1
            i += 1




        # REPLACE WITH APPROPRIATE RETURN VALUE
        return returnCells




    def entries(self) -> [Cell]:
        """ 
        @return a list of cells that have values (i.e., all non None cells).
        """

        # basically how we construct :sip: but for sumA to find row
        entriesList = []
        row = 0
        colAIndex = 0

        for i in range(1,len(self.sumA)):
            if (self.sumA[i - 1] != self.sumA[i]): # finding when a row has value by seeing if prev row is the same as teh current row we're focusing on
                difference = self.sumA[i] - self.sumA[i - 1]
                difference = round(difference, 1)

                if (difference == self.valA[colAIndex]): # meaning only 1 number
                    currCell = Cell(row, self.colA[colAIndex], self.valA[colAIndex])
                    entriesList.append(currCell)

                    colAIndex += 1
                else: # for multiple values
                    sumAppended = self.valA[colAIndex]
                    #print("!! Multiple values detected !!")
                    #print(self.valA[colAIndex])
                    currCell = Cell(row, self.colA[colAIndex], self.valA[colAIndex])
                    entriesList.append(currCell)
                    while (sumAppended != difference):
                        
                        colAIndex += 1
                        sumAppended += self.valA[colAIndex]
                        sumAppended = round(sumAppended, 1)
                        #print(self.valA[colAIndex])
                        currCell = Cell(row, self.colA[colAIndex], self.valA[colAIndex])
                        entriesList.append(currCell)
                    colAIndex += 1
                        
            row += 1
        return entriesList

    def quickSortCol(self, lCells: [Cell]) -> [Cell]: # FIX ME sort for numbers in the same row w/diff columns
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

                # FIX ME sort by row as well *should work but test me with #prints*
                elif lCells[i].row == pivot.row:
                    if (lCells[i].col < pivot.col):
                        leftVals.append(lCells[i])

                    else:
                        rightVals.append(lCells[i])

                else:
                    rightVals.append(lCells[i])
        
        return self.quickSortCol(leftVals) + [pivot] + self.quickSortCol(rightVals)
    
    
    def uninitialisedBoardCheck(self) -> bool:
        """
        @return Returns false if rowNum or colNum do not exist, otherwise returns true.
        """

        if (self.rowNum() < 0 or self.colNum() < 0):
            return True
        
        return False