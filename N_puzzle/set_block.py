

class Set_Start_Block:
    def __init__(self):
        self.suffle = 200
        self.num_rows = 4        
        self.start_block = []
        self.get_block()
    
    def get_start_block(self):
        return (self.num_rows, self.start_block)

    def get_block(self):
        if len(self.start_block):
            self.num_rows = len(self.start_block)
        else:
            self.onInit()

    def onInit(self):
        # Create sequential array.
        self.numbers = list(range(1, self.num_row * self.num_row))
        self.numbers.append(0)
        # Add number to the two-dimensional array.
        self.blocks = []
        for row in range(self.num_row):
            self.blocks.append([])
            for column in range(self.num_row):
                temp = self.numbers[row * self.num_row + column]
                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)
            
