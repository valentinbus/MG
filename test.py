class Maze:
    #Define file use to create lvl structure
    def __init__(self, file):
        self.file = file
        self.structure = []

    #Parse file to create structure
    def structure_construction(self):
        with open(self.file, 'r') as file:
            #Define total rows
            for row in file:
                row_structure = []
                #Append total number of case per row
                for case in row:
                    if case != '\n':
                        row_structure.append(case)
                #Create a table in two dimensions 
                self.structure.append(row_structure)

maze = Maze('./ressource/maze_structure')
maze.structure_construction()

x=0
y=0

i = [2+3, 4]
print(i)