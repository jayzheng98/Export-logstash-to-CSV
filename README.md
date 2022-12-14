# Prerequisite
 [ELK](https://www.elastic.co/what-is/elk-stack) 
 
 [Python3](https://www.python.org/downloads/)
<br>

# Notice
**1.** The format of ELK index name must be like `test-%{yyyy.MM.dd}`. Sure you can customize it in the config file of "logstash", but please ensure the uniformity
<br>

# Usage
**1.** Change the `output->csv->fields`&`input->elasticsearch->query` in the `convert_csv.conf` file according to your own needs
 - *You can customize the `output->csv->path` for the output file*
 - *Don't need to care about the value of `input->elasticsearch->index` as it will be changed automatically once you run the `.py` file*

**2.** Put the `convert_csv.conf` into the `bin` directory of logstash. In my case, it is `D:\ELK\logstash-7.8.0\bin\convert_csv.conf`*

**3.** Execute the `logstash2csv.py` and start exporting!
