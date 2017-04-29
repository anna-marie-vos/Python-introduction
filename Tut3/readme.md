## Jupyter.
* go to the website: http://jupyter.org/ and download it and install it.
* then in the terminal type: jupyter notebook
* To start jupyter notebook type in command line: jupyter notebook
* in jupyter, start a new python three session,
* to delete a line in jupyter hold escape and press D+D
and type:
* `import os`
 * `os.listdir()`
 * press alt+enter to execute the code in jupyter notebook
 * `import pandas`
 * `df1 = pandas.read_csv("TestValues1.csv")`
 * df1 and then press alt+enter
 * here are some the pandas commands: http://pandas.pydata.org/pandas-docs/stable/10min.html
 * `pandas.read_json("somefile.json")`
* to read xlsx files you need to install the following: sudo pip3 install xlrd
* to find help about pandas, type in jupyter, the method and a ? example: pandas.read_csv?
* when referencing dropping columns you need to reference 1 and for rows reference 0 it needs to look like:
* `df7.drop("332 Hill St",0)` this is a row
* `df7.drop('City',1)` this is a columns
* drop multiple columns: `df7.drop(df7.columns[0:3],1)`
* `df7.index` gives you a list of the index row names
* `df7.columns` gives you a list of the index column names
* to add a column and fill it with data: `df7["continent"] = df7.shape[0]*["North America"]`
* To see the shape of your dataframe: `df7.shape` this will output the (5,7) <<this is a tuple, which means 5 rows and 7 columns
* There is no easy way to add a row, so transpose your table and then add a columns and transpose again: df7.T
