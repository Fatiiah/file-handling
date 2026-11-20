import numpy as np

with open('loan_data.csv', 'r') as file:

    
    data = np.genfromtxt(
        file,
        delimiter=',',
        skip_header=1,
        usecols=8,
        dtype=float
    )




# Step 4: Remove missing loan amounts
loan_amounts = data[~np.isnan(data)]


mean_loan = np.mean(loan_amounts)
median_loan = np.median(loan_amounts)
std_loan = np.std(loan_amounts)

 
print("Number of valid loan amounts:", len(loan_amounts))
print("Mean Loan Amount:", mean_loan)
print("Median Loan Amount:", median_loan)
print("Standard Deviation:", std_loan)
