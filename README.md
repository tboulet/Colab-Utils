# Colab-Utils
Usefull tools for dealing with colab notebooks


## Installation

Go in a colab notebook and run the following cell:

```python
!pip install colab_notebook_utils
```


You will need to mount your drive in the first place.

```python
from google.colab import drive
drive.mount('/content/drive')
```

## Set workspace

You can get the workspace path that Colab use (which is different that the location of your notebook, it should be /content/)
    
```python   
from colab_notebook_utils.workspace import get_workspace_path
get_workspace_path()
```

You can automatically set this workspace as the location of your notebook, which is useful when you want to save files in the workspace, or when you want to use a relative path to a file in the workspace.
    
```python
from colab_notebook_utils.workspace import set_notebook_location_as_workspace
set_notebook_location_as_workspace()
```