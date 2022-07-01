

class Set_Start_Block:
    def __init__(self, num_rows):
        self.start_block = []
        self.num_rows = num_rows
    
    def get_start_block(self):
        return (len(self.start_block), self.start_block)

    def get_default_block(self):
        if len(self.start_block):
            self.num_rows = len(self.start_block)
            
