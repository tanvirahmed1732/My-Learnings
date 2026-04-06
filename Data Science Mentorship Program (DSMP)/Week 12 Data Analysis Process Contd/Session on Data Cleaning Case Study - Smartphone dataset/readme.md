# Session on Data Cleaning Case Study - Smartphone Dataset

This folder contains a comprehensive case study on data cleaning using a real-world smartphone dataset. The session demonstrates practical data cleaning techniques through hands-on examples and systematic problem identification.

## Overview

This case study focuses on cleaning a dataset containing smartphone specifications and pricing information. The dataset includes various data quality and structural issues that need to be addressed to prepare the data for analysis.

## Files

- **smartphones.csv**: The raw dataset containing smartphone data with columns including model, price, rating, sim, processor, ram, battery, display, camera, card, and os.

- **data_cleaning_smartphone_data.ipynb**: Main Jupyter notebook demonstrating the complete data cleaning process. Includes:
  - Initial data exploration (head, info, describe)
  - Duplicate detection
  - Price column cleaning (removing currency symbols and commas)
  - Identification of problematic rows across multiple columns
  - Filtering out inaccurate data (e.g., unreasonably low prices)

- **SmartPhone Data Cleaning.ipynb**: Additional notebook with complementary data cleaning exercises and examples.

## Data Quality Issues Covered

### Quality Issues (Validity, Accuracy, Completeness, Consistency)
1. **Model**: Inconsistent brand naming (e.g., OPPO variations)
2. **Price**: Contains currency symbols (₹) and commas; includes inaccurate values (e.g., price of 99)
3. **Ratings**: Missing values
4. **Processor**: Incorrect values for certain Samsung phones
5. **Memory/RAM**: Incorrect values in specific rows
6. **Battery**: Incorrect values in multiple rows
7. **Display**: Missing frequency information and incorrect values
8. **Camera**: Complex formatting issues with Dual/Triple/Quad representations
9. **Card**: Contains mixed information about OS and camera
10. **OS**: Contains information about Bluetooth and FM radio; inconsistent version naming
11. **Data Types**: Price and rating have incorrect data types

### Tidiness Issues (Structural Problems)
1. **SIM**: Can be split into separate columns (has_5g, has_NFC, has_IR_Blaster)
2. **RAM**: Should be split into RAM and ROM columns
3. **Processor**: Can be divided into processor name, cores, and CPU speed
4. **Battery**: Should include battery capacity and fast charging availability
5. **Display**: Can be split into size, resolution width/height, and frequency
6. **Camera**: Should separate front and rear camera information
7. **Card**: Can be split into supported status and extended capacity

## Learning Objectives

- Identify and categorize data quality issues using systematic assessment
- Apply appropriate cleaning techniques for different types of data problems
- Handle complex string parsing and data transformation
- Understand the importance of data validation and accuracy checks
- Practice structural data cleaning to improve dataset usability

## Usage

1. Start with `smartphones.csv` to examine the raw data
2. Follow `data_cleaning_smartphone_data.ipynb` for step-by-step cleaning process
3. Use `SmartPhone Data Cleaning.ipynb` for additional practice exercises
4. Apply the learned techniques to other datasets with similar issues