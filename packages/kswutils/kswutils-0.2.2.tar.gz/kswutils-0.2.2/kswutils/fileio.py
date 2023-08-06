import os
import pickle
import logging
from datetime import datetime

# Path vs Directory
# Path is the directory to an object (a file)
# Path: Obj
# Directory: Folder


class FileIO:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create_logger():
        dir_path = os.path.join(os.getcwd(), 'log')
        filename = "{:%Y-%m-%d_%H-%M-%S}".format(datetime.now()) + '.log'

        logging.captureWarnings(True)
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(message)s')
        logger = logging.getLogger('py.warnings')
        logger.setLevel(logging.INFO)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        fileHandler = logging.FileHandler(dir_path+'/'+filename, 'w', 'utf-8')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(formatter)
        logger.addHandler(consoleHandler)
        
        return logger        

    @staticmethod
    def get_subdirectories(baseDir):
        """ get sub-directories / sub-paths

        Args:
            baseDir (string or list): target directory(ies).

        Returns:
            list: (1d list): a *sorted* list of subdirectories / subpaths.
        """
        # Config
        skips = ['.DS_Store', '__pycache__', '.ipynb_checkpoints']

        if not isinstance(baseDir, list):
            baseDirs = [baseDir]

        dirList_all = []

        for basedir in baseDirs:
            dirList = os.listdir(basedir)

            for d in dirList:
                if os.path.basename(d) in skips:
                    continue

                dirList_all.append(os.path.join(basedir, d))

        return sorted(dirList_all)  # Capital letter --> Small letter

    @staticmethod
    def read_pickle(path):
        with open(path, 'rb') as f:
            obj = pickle.load(f)
        return obj

    @staticmethod
    def write_pickle(obj, **kwargs):
        """ write object to pickle

        Args:
            obj: object to save as pickle 
            savepath: opt. default './new.pickle'

        Returns:
            None
        """
        _savepath = kwargs.get('savepath', './new.pickle')

        with open(_savepath, 'wb') as f:
            pickle.dump(obj, f)
        # In Python 2 document, while serializing, use '.pkl'
        # In Python 3 document, while serializing, use '.pickle'
        return None

    @staticmethod
    def make_dir(dir):
        try:
            os.makedirs(dir)
        except:
            return False
        return True

    @staticmethod
    def is_exsit(dir):
        return os.path.exists(dir)

    @staticmethod
    def get_name_with_extion(dir):
        return os.path.basename(dir)

    @staticmethod
    def get_name_without_extion(dir):
        return os.path.basename(dir).split('.')[0]
    

