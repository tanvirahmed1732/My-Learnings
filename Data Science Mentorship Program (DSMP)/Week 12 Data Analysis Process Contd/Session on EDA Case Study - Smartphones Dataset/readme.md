# Smartphone Data Cleaning and EDA — DSMP Learning Project

This repository contains my learning work for the Data Science Mentorship Program (DSMP). It documents the full process of cleaning a smartphone dataset and exploring it through EDA.

## Course Context

This work is part of the DSMP Week 12 Data Analysis Process course. The goal is to practice real-world data cleaning and exploratory analysis using a dataset collected by web scraping.

## Content Overview
- `SmartPhone Data Cleaning.ipynb` — notebook with data assessment and cleaning steps
- `Exploratory Data Analysis on Smartphone Dataset.ipynb` — notebook with EDA, visualizations, and findings

## Data Description

### Raw dataset
- File: /smartphones.csv`
- Contains raw smartphone specs gathered by web scraping
- Includes inconsistencies, missing values, and non-smartphone entries

### Cleaned dataset
- File: /smartphone_cleaned.csv`
- Contains cleaned smartphone data ready for analysis
- Includes extracted and normalized fields for easier analysis

## Learning Objectives

### Data Cleaning
- Assess data quality and identify issues
- Fix formatting problems in `price`, `processor`, `battery`, `camera`, and other columns
- Remove non-smartphone records and invalid rows
- Extract structured features from mixed columns
- Convert values to appropriate data types

### Exploratory Data Analysis
- Review distributions of price, ratings, battery capacity, and screen size
- Examine categorical trends for brands, 5G, NFC, processor types, RAM, and storage
- Analyze relationships between features and price
- Learn how data cleaning affects analysis quality

## Key Takeaways

- Clean data makes analysis much more reliable
- Higher RAM and storage are clear price drivers
- Phones with 5G and NFC generally cost more
- Battery capacity does not always map directly to higher price
- Common brands in this dataset include Xiaomi, Samsung, Vivo, Realme, and Oppo

## Notes

- This repository is intended as a learning record of DSMP coursework.
- The raw dataset and cleaned dataset are provided for reference.
- The notebooks show step-by-step progress and conclusions.

## Optional Links 
- Medium article: `https://medium.com/@tanvirahmed17341/unveiling-the-smartphone-market-a-data-driven-journey-from-scraping-to-insights-0a62acb801be`
