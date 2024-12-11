class Chunk:
    __closing_chars = [')', ']', '}', '>']
    __map_opening_closing_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}

    def __init__(self, char: chr = ' ', parent: 'Chunk' = None):
        self.char = char
        self.children: ['Chunk'] = []
        self.parent: 'Chunk' = parent
        self.open: bool = True
        self.is_corrupted: bool = False

    def add_child(self, char: chr) -> 'Chunk':
        child = Chunk(char, self)
        self.children.append(child)
        return child


    def add_next_char(self, char: chr) -> bool:
        if char in self.__closing_chars:
            return self.__close(char)
        else:
            return self.__open(char)

    def __open(self, char: chr) -> bool:
        # root initialisieren
        if self.char == ' ':
            self.char = char
            return not self.is_corrupted

        if not self.children or not self.children[-1].open:
            child = self.add_child(char)
            return not child.is_corrupted
        else:
            lastOpenChild = self.children[-1]
            return lastOpenChild.add_next_char(char)

    def __close(self, char: chr) -> bool:
        if not self.children or not self.children[-1].open:
            if self.__map_opening_closing_chars[self.char] == char:
                self.open = False
            else:
                self.set_is_corrupted()
            return not self.is_corrupted

        return self.children[-1].add_next_char(char)

    def set_is_corrupted(self):
        self.is_corrupted = True
        if self.parent:
            self.parent.set_is_corrupted()


    def __str__(self):
        return "'" + self.char + "', " + str(self.children)

    def __repr__(self):
        return self.__str__()

    def get_completion_sequence(self) -> str:
        sequence = ""
        for child in self.children:
            sequence += child.get_completion_sequence()
        if self.open:
            sequence += self.__map_opening_closing_chars[self.char]
        return sequence
