# python_best_practices
this series will cover best practices of python while you work or build projects of your own. it is eveident that programming is something that definitely needs to solve a task at scale without memory and execution overheads. in order to arrive at that label of expertise we would need to program in passion and dedication, and mimic something that looks promising from the word go. So let us learn and evolve through this proceedings. we use many approaches while solving task or problem starting with iterative way and then use some of the builtin methods that python offers off the shell. often times there exists a lot of operational and execution overheads pertaining to a problem while we use these two approaches. 


      1- say for instance if you are reading a csv file using pandas (python dataframe operation library) the default way is pd.read_csv(file).
      2- other way is to read simultaneously by skipping some indexes just to fit in memory
      3- another way is to use in line parser engine to speed up the excution process. like "c", "pyarrow"
      4- or we can thik of no csv option like storing it a parquet file and use "fastparquet" in line engine.
      5- another way to look at it is that we can create a rows of dataframe as and when it is needed using yield.
      6- using yield we are not stroing anything back on memory as it is not getting initialized unlike df = pd.read_csv(df)
      
We will add many more of these industry standard best practices that are available with us from python side itself. But we tend to ignore these simple hacks to get a lot of purchase. Programming should be fun, should not be like last rescue where we need to any of the approaches and get the work done. happy learning. 
