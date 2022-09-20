# Where to Start

start by studting the type of data collected by Splunk looking for the more valuable data for hunting, some enterprise collect logs not useful for hunting malicious activities (such as system health, troubleshooting).

Look for the list of indices `index` stord on the system
```
| eventcount summarize=false index=* | dedup index | fields index
```
then log for logs `source`
```
index=* | stats count by source
```
and then look for the `sourcetype`
```
index=* | stats count by sourcetype
```
then collect what are the most interesting search queries to start your hunt from
for example:
```
index=edr source=processes
index=ndr source=http_traffic
index=access_logs source=iis
```
these logs depends on the collected logs on your Splunk

Note: in `source` you will find some logs has the log path, just ignore them and look for their `sourcetype`
```
index=* NOT source="/*" NOT source="C:\\*" | stats count by source
```




# Splunk Search Queries

## list all avaliable indices
```
| eventcount summarize=false index=* | dedup index | fields index
```

## Get the stats counts
```
| stats count by <field>
```

## Split field to get the root folders from path
```
| eval p=split(Path , "\\") | eval s_path=mvjoin(mvindex(p , 0 , 1) , "\\") | stats count by s_path
```
the field `s_path` contains the root folder, increase the number `1` to get the subfolders


## Get number of hosts with specific value
To get how many time a process executed and the number of hosts executed on.

```
| stats count distinct_count(host) as num_hosts by Process
```

## parse logs field
if you have a message or field that is not parsed, use `rex` command
example
```
| rex field=Message "<Command>(?<cmd>.*)<\/Command>" | rex field=Message "<Arguments>(?<args>.*)<\/Arguments>"
```
this search command will extract the `cmd` and `args` from field `Message` 
Note: Case sensitive 


## Parse Datetime field
if you want to have a `date` field, use the following
```
| convert timeformat="%Y-%m-%d" ctime(_time) AS date 
```
this way you can count by date like
```
| convert timeformat="%Y-%m-%d" ctime(_time) AS date | stats count by user,date
```
