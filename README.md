# DCC Tool Window

##  Houdini Setup

1. Create 456.py file in 
    ```
    C:\Users\<userdir>\Documents\houdini19.0\scripts
    ```
2. Copy the following code into that file
    ```python
    import sys
    import importlib

    packages = 'path to python virtual enviroment/site-packages'
    sys.path.append(packages)

    project = 'path to project root folder'
    sys.path.append(project)
    ```
3. Open Houdini. Create a new shelf and a new shelf tool. Use the following python code in the tool.
    ```python
    from tool.ui import tool_window as tw
    from engine import engine_maya as em

    import clear
    clear.do('tool')
    clear.do('engine')
    clear.do('lib')


    t = tw.ToolWindow()
    t.show()
    ```

## Maya Setup
1. Open Maya. Open Maya script editor.
2. Run the following code:
    ```python
    import sys
    import importlib

    packages = 'path to python virtual enviroment/site-packages'
    sys.path.append(packages)

    project = 'path to project root folder'
    sys.path.append(project)

    from tool.ui import tool_window as tw
    from engine import engine_maya as em

    import clear
    clear.do('tool')
    clear.do('engine')
    clear.do('lib')


    t = tw.ToolWindow()
    t.show()
    ```