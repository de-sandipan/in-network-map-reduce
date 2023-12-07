### In-network MapReduce

## Code:
  - codes/01_cluster_setup.ipynb - (input parameter) cluster_size
    - Creates a cluster and setup applicable network to deploy hadoop-3.3.6
      
  - codes/02_hadoop_installation.ipynb - (input parameter) slice_name
    - Deploy Hadoop
    - NameNode: 1
    - DataNode: cluster_size-1
      
  - codes/03_hadoop_ui.ipynb - 
    - Create the tunnelling for HDFS and MapReduce WebUI
  
  - codes/04_hadoop_start_stop.ipynb - 
    - Starts/Stops daemons for MapReduce
      
  - codes/05_hadoop_job_execution.ipynb -
    - Sets up local files for MapReduce job Execution
  
  - codes/06_cleanup.ipynb - 
    - Cleanup cluster as needed
  
  - codes/src_codes/mapper.py - 
    - Mapper job for word count
  
  - codes/src_codes/reducer.py
    - Reducer job for word count
  
    
  
