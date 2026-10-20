import sqlite3
import pandas as pd

# =====================================================================
# PART 1: CONNECTING TO THE DATA
# =====================================================================

# STEP 1A & 1B
# Connect to the SQLite database
conn = sqlite3.connect("data.sqlite")

# Reference view: employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# =====================================================================
# PART 2: BASIC SELECT FILTERING
# =====================================================================

# STEP 2
# Retrieve employeeNumber and lastName
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# STEP 3
# Retrieve lastName first, then employeeNumber
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)


# =====================================================================
# PART 3: ALIASING IN SELECT
# =====================================================================

# STEP 4
# Retrieve lastName, and alias employeeNumber as 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)


# =====================================================================
# PART 4: CASE FUNCTION
# =====================================================================

# STEP 5
# Bin job titles into 'Executive' or 'Not Executive' under column 'role'
df_executive = pd.read_sql("""
    SELECT 
        CASE 
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)


# =====================================================================
# PART 5: BUILT-IN FUNCTIONS - STRINGS
# =====================================================================

# STEP 6
# Get length of lastName as 'name_length'
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""", conn)

# STEP 7
# Extract first two characters of jobTitle as 'short_title'
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)


# =====================================================================
# PART 6: BUILT-IN FUNCTIONS - NUMERICS & DATES
# =====================================================================

# Reference view: orderDetails table
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Find total amount for all orders as sum of rounded total prices
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""", conn)["total_price"].sum()

# STEP 9
# Query orderDate from the 'orders' table (not orderDetails)
df_day_month_year = pd.read_sql("""
    SELECT 
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)