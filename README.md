## PROJECT SCOPE
This project focuses on the general practices in England, on the practice level, chemical level and presentation level. All registered practices, including GP practices, in England are included in the data, including a number of 'dummy' practices.

The practice level shows us what is practice is called, and the addresses of the practice.

The chemical level shows us what chemicals where prescribed or dispensed which include name of chemicals.

The presentation level similar to what the practice level data, shows us what is practice is called, the address of the practice, the number of genera practicioners with each practice. We also get the number of patients registered with each practice whether they are getting a dispensing service or medical services.

This project has 4 data sources.
Namely;
* practices.csv
* bnf_codes.csv
* practice_prescribing.csv (over 1 million rows)
* practice_list_size_and_gd_count.csv
  
You can find the data dictionary [here](data_dictionary.md)

This data is a month on month dataset. I am using the December dataset by default which already has some 10 million rows.
What I hope to achieve from this dataset is to see some trends in drugs being prescribed? Can seasons be detected based on the type of drugs being described? Since these datasets have no information about the patients themselves, can it be easily determined what kind of patients are receiving certain services whether dispensing or medical services.

## DATA MODEL
A snowflake schema is used here because this contains sub-dimension tables including fact and dimension tables.
It uses normalization which splits up the data into additional tables. The splitting results in the reduction of redundancy and prevention from memory wastage.
The bnf_codes.csv is normalized 7 into dimension tables which includes;
* bnf_chapters
* bnf_sections
* bnf_paragraphs
* bnf_subparagraphs
* bnf_chemicals
* bnf_products
* bnf_presentations

The practice_list_size_and_gd_count.csv is broken into a facts and dimension tables namely;
* practices
* groups

The practice_prescribing.csv is used as the main facts table where all the tables connect to
directly or indirectly.

You can an ERD view of the snowflake schema [here](Capstone%20Udacity%20Project.png).

## ETL MODEL
On a month to month basis data from all csv files is pushed to the s3 bucket.
These files are read and wrangled using spark to normalized them into parquet files stored
on the s3 bucket.
These processed parquet files are then copied and data from them pushed to respective redshift tables.

This project is orchestrated by Airflow using two dags.

The drop_and_create_tables dag simply runs just ones and drop and creates tables ready for the main
etl process;





## DATA EXPLORATION AND ASSESSMENT