# Resort Management Data Warehouse and BI

## Overview

This repository contains the implementation of a Data Warehouse and Business Intelligence solution developed for the **Big Data Management** course offered by the Department of Computer Science and Artificial Intelligence.

The project focuses on the design and implementation of a Data Warehouse for a Resort Management domain, including conceptual modelling, logical design, ETL development, Data Warehouse implementation, and Business Intelligence reporting using Metabase.

## Course Information

**School:** University of Palermo

**Course:** Big Data Management

**Department:** Computer Science and Artificial Intelligence

**Instructor:** Prof. Simona Ester Rombo

**Project Title:** Resort Management Data Warehouse and BI (Data Warehouse Design and Business Intelligence Implementation)

**Date:** June 2026

## Team Members

* Saloni Sharma
* Gabriele Zimmerhofer
* Francis Ofosu Aboagye
* David Tetteh Kwao

## Project Objectives

The project involved:

1. Identifying managerial decisional queries.
2. Selecting analytical facts from the provided E/R schema.
3. Refining the schema through reification.
4. Performing conceptual modelling using attribute trees, pruning and grafting.
5. Designing fact schemas and snowflake schemas.
6. Implementing and populating the Operational Database.
7. Implementing the Data Warehouse and ETL processes.
8. Developing Business Intelligence dashboards and reports using Metabase.

## Repository Structure

```text
Resort_Management_DW_BI/
│
├── Python_Data_Generation/
├── OLTP_Database/
├── Data_Warehouse/
├── Metabase_Reports/
├── Diagrams/
├── Documentation/
│   └── Team 4_Resort_Management_DW_BI_Project Report.pdf
│
└── README.md
```

## Technologies Used

* Python
* MySQL
* MySQL Workbench
* SQL
* Metabase
* Draw.io

### Python Libraries

* random
* datetime
* collections.Counter

## Data Warehouse Components

### Fact Tables

* FACT_PAYMENT
* FACT_ROOM_RENTAL

### Dimension Tables

* DIM_DATE
* DIM_CUSTOMER
* DIM_RESORT
* DIM_HOTEL
* DIM_ROOM

## Business Intelligence Features

The implemented dashboards support:

* Revenue Analysis
* Customer Geography Analysis
* Customer Demographic Analysis
* Seasonal Analysis
* Room Rental Analysis
* Accommodation Performance Analysis

## Documentation

The complete project report is available in:

```text
Documentation/
└── Resort_Management_Data_Warehouse_And_BI_Report.pdf
```

## License

This repository was developed for academic purposes as part of the Big Data Management course.
