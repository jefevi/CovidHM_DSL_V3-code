# Building the covidhm database
This directory contains:

--> postgres folder: Scripts that can be used to create:
    -- a new instance of the covid Database
    -- a new instance of the V3 schema
    -- tables of schema
    -- load data from csv into schema tables *

--> data_wrangling folder:
    -- Scripts to adapt V2 csv format to V3 tables
    -- Scripts to adapt V3 csv format to V3 tables

*Please carefully review the warnings inside the '03_postgres_create_tables.sql' file when importing the data.*