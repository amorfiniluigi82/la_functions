class Files:

    def __init__(self, name):
        self.name = name

    def get_content(self):
        """
        getContent = Lettura file
        """
        with open(self.name, "r") as f:
            r = f.read()
            return r

    def set_content(self, content):
        """
        setContent = Scrittura file singola riga
        """
        with open(self.name, "w") as f:
            w = f.write(content)
            return w

    def add_content(self, content):
        """
        addContent = Scrittura file in appeso
        """
        with open(self.name, "a") as f:
            w = f.write(content)
            return w
