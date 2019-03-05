# qssimport

qssimport allows you to use multiple qt stylesheet files for a single project by merging those stylesheets into a main qss file. Simply create a base .qss file that defines 1 or more @import statements that point to other stylesheets.
    

### Installation
    sudo pip install qssimport

### Usage

- The `base_dir` is the path to the stylesheets
- The `import_def` file is assumed to be stored in the stylesheets directory
   - `import_def` is file where all of the @imports need to be defined   
- The `main_stylesheet` is an optional argument that defines the name of the compiled stylesheet.
if a name is not provided, the program defaults to mainStyle.qss
  
```
 from qssimport import stylesheet
 ...
 b = stylesheet.Stylesheet(base_dir='/path/to/stylesheets/',
                            import_def_file='imports.qss',
                            main_stylesheet='myStyle.qss')
 b.create_stylesheet()

 style_sheet = "path/to/myStyle.qss"
 with open(style_sheet, 'r') as style:
     self.setStyleSheet(style.read())
 ...	   
```

### Example 
Given the following:
 ###### `import.qss` 
  ```
  @import "lineEdit.qss";
  @import "widget.qss";
  ```
  
  ###### `lineEdit.qss`
  ```
  QLineEdit{color:#FFF;}
  QLineEdit{background:#A06;}
  ```
  ###### `widget.qss`
  ```
  QWidget{background:#434343;}
  QWidget#MyWidget{background:#909090;}
  ```
##### The file you specified as `main_stylesheet` will contain all of the lines from `lineEdit.qss` and `widget.qss`  
 ###### `myStyle.qss`
  ```
  QLineEdit{color:#FFF;}
  QLineEdit{background:#A06;}
  QWidget{background:#434343;}
  QWidget#MyWidget{background:#909090;}
  ```