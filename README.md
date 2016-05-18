# Assignment1
This assignment deals with reading an input file named purchases.txt. This file is of the below format, but is seperated by tabs.

| DATE       | TIME  | STORE-LOCATION | ITEM             | COST   | PAYMENT-METHOD |
|------------|-------|----------------|------------------|--------|---------------:|
| 2012-01-01 | 09:00 | Lincoln        | Garden           | 136.9  | Visa           |
| 2012-01-01 | 09:00 | Buffalo        | Women's Clothing | 483.82 | Visa           |
| 2012-01-01 | 09:00 | San Jose       | Women's Clothing | 215.82 | Cash           |

The mapper.py and reducer.py are the hadoop mapper and reducer code to parse the above data and determine the following information from the raw data:

1. Sales breakdown by product category across all of the stores.
2. The monetary value for the highest individual sale for each separate store.
3. The total sales value across all the stores, and the total number of sales. Assuming there is only one reducer.

The output.txt contains the result of the map-reduce job, which calculates the above three information from the purchases.txt input file.

Due to the size of the purchases.txt file, it could not be commited to the branch. The complete file can be downloaded from the below link:
https://dl.dropboxusercontent.com/u/25077628/purchases.txt

