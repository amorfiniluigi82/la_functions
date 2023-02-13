import os
import sys


class System:
    
    def add_folder(self, directory):
        """
        createFolder = Crea una cartella
        https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
        import system
        system.createFolder('./data/')
        """
        try:
            if not os.path.exists(directory):
                return os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. {} '.format(directory))

    
    def getscript_path(self):
        """
        Recupera percorso file dalla cartella del file python.
        es:
        self.immagine1 = tk.PhotoImage(file="" + getScriptPath() + "/img/bissio.gif")
        """
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    
    def clear(self):
        """
            Clear Console

            cls = Windows
            clear = Linux

            clear()
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    
    def check_files(self, filepathandname):
        """
        https://gist.github.com/keithweaver/b113801cd38a354b06a4ad59e3c14a7f
        
        # Example
        if CheckFiles('./test.json'):
          print ('Yaa it exists!')
        else:
            print ('Nope! Not around')
        """
        return os.path.exists(filepathandname)

    
    def remove_folder(self, path):
        """
        delete folder
        """
        try:
            os.rmdir(path)
        except OSError:
            print("Deletion of the directory {} failed ".format(path))
        else:
            print("Successfully deleted the directory {}".format(path))
