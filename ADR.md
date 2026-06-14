# ADR Document

## Architecture Overview

This project built to 2 main actions for enrollment , the first is to handle huge # of enrollment & save them , the second is to retrieve students # grouped by *region* or *grade*

### Handling Enrollment 

Handle enrollment done via adding 2 tables : 
1. Process table : this will contains raw data & status - all rows should been added 
2. Enrollment table : this will contains the succeed proceed rows only 

Enrollment process : 

1. Parse JSON file into lines 
2. Send chunks of data to proceed - chunks here will handle # of celery tasks generated + # of connection to db 
3. For each chunk celery task will be fired async in background 
4. Using atomic transactions also will handle the failure case & rollback


### Retrieving Enrollment 

API created here to have *query* param to determine which group by will be used , using annotate count with exist indexes will make this query faster 


### Handling 100M records 

Suggestion to use partitioning on db level to make setting/getting easier 
1. Partitioning can be *List Partitioning* type for specific region , partition for each region
2. In case of having huge # of records for each region , it might have *Range Partitioning* on date ranges 


