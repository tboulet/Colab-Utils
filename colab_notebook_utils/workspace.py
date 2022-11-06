import os

import requests
import urllib.parse
import google.colab
import os
from typing import List

def get_notebook_workspace(verbose = True) -> str:
    """Get the current working directory.
    
    Returns:
        str: current working directory
    """
    colab_path = os.getcwd()
    if verbose: print(
    f"The current workspace path is: {colab_path} \n\
Your files will be searched/saved here. \n\
\n\
If you want to change it, you can do so by running:\n\
os.chdir('/path/to/your/workspace') \n\
\n\
If you want to set it automatically as your notebook location, run: \n\
set_notebook_location_as_workspace()")
    return colab_path
    
    
    
def get_notebook_location(verbose = True) -> List[str]:
    """Search and return a list containing the possible locations of the notebook file (usually of lenght 1).

    Returns:
        list: list of possible locations of the notebook file
    """
    google.colab.drive.mount('/content/drive')
    found_files = []
    paths = ['/']
    nb_address = 'http://172.28.0.2:9000/api/sessions'
    response = requests.get(nb_address).json()
    name = urllib.parse.unquote(response[0]['name'])

    dir_candidates = []

    for path in paths:
        for dirpath, subdirs, files in os.walk(path):
            for file in files:
                if file == name:
                    found_files.append(os.path.join(dirpath, file))

    found_files = list(set(found_files))

    if len(found_files) == 1:
        nb_dir = os.path.dirname(found_files[0])
        dir_candidates.append(nb_dir)
    elif not found_files:
        if verbose: print('Notebook file name not found.')
    elif len(found_files) > 1:
        if verbose: print('Multiple matches found, returning list of possible locations.')
        dir_candidates = [os.path.dirname(f) for f in found_files]

    return dir_candidates



def set_notebook_location_as_workspace(verbose = True) -> List[str]:
    """Set the notebook location as the current working directory.

    Returns:
        list: list of possible locations of the notebook file Also returns the list of possible locations of the notebook file.
    """
    found_files = []
    paths = ['/']
    nb_address = 'http://172.28.0.2:9000/api/sessions'
    response = requests.get(nb_address).json()
    name = urllib.parse.unquote(response[0]['name'])

    dir_candidates = []

    for path in paths:
        for dirpath, subdirs, files in os.walk(path):
            for file in files:
                if file == name:
                    found_files.append(os.path.join(dirpath, file))

    found_files = list(set(found_files))

    if len(found_files) == 1:
        nb_dir = os.path.dirname(found_files[0])
        dir_candidates.append(nb_dir)
        print('Singular location found, setting directory:')
        os.chdir(dir_candidates[0])
    elif not found_files:
        if verbose: print('Notebook file name not found.')
    elif len(found_files) > 1:
        if verbose: print('Multiple matches found, returning list of possible locations.')
        dir_candidates = [os.path.dirname(f) for f in found_files]

    return dir_candidates