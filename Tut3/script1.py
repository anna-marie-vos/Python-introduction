# install pandas using pip3
# in command line use: pip3 install pandas
#  install ipython3 in terminal using: sudo apt-get install ipython3
#  in ipython3 in terminal do the following:
import pandas
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["col1","col2","col3"])
df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["col1","col2","col3"],index=["first","second"])
df2 = pandas.DataFrame([{"Name":"John", "age":5},{"Name":"Joye"}])
