# Customer churn prediction project

# Exploring data

## Observations:
1. Both genders have the same churning rate
2. Not senior citizens tend to keep their 
3. People who have dependents (for example, children, a spouse, elderly parents, or others who rely on the customer for financial support) churn less that the ones who don't.
4. People who have phone services churn way more
5. Month-to-month contracts have a dramatically higher churn rate than other contract types
6. Customers with Fiber optic service show a significantly higher churn rate compared to those with DSL
7. Customers paying by Electronic check are more sustainable
8. The higher the monthly charges the higher the churn rate
9. it is observed that Customers who came with partners are very less likely to churn

## Conclusion 1:
The most related features with a high churn rate are:<br>
* Contract
* Tenure
* Internet
* Payment methodes
* Demographics
* Add-ons<br>
We are going to explore them more...

### Tenure behavior:
$\rightarrow$ The higher the months the customer has stayed with the company, the smaller the churn rate is.<br>
only fair ig<br>
$\rightarrow$ Inversed relationship between churning and tenure, but very important

### Payment methodes and churn
- Major customers who **churn** were having *Electronic Check *as Payment Method. Customers who opted for *Credit-Card automatic transfer* or *Bank Automatic Transfer* and *Mailed Check* as Payment Method were less likely to **move out**.


# Conclusions 2:
1. the minimum monthly charge is 20$, the maximum is approximately 120$
2. 75% of the clients pay less than 90$ (pricey? yes i guess)
3. 50% of the clients payment amount is between 35 and 90 dollars<br>
...

# Conclusion 3:

*   **Internet Service is the #1 Price Driver:**
    *   Fiber Optic = Highest Bills
    *   DSL = Medium Bills
    *   No Internet = Lowest Bills

*   **Contract Length Signals Customer Type:**
    *   Month-to-Month = Higher paying, but high-risk (likely to leave).
    *   Two-Year Contracts = Lower paying, but most loyal and stable.

*   **Dependents Have a Minor Impact:**
    *   Customers with no dependents tend to spend slightly more.

# Key Customer Profiles:

*   Clients with Month-to-month contacts who are also more likely paying for premium services like Fibre Optic with Electronic Checks
* Loyal Customers are the ones using long term contracts, automatic payment methodes(Bank or credit card Automatic Transfer and Mailed Check)
$\rightarrow$ It seems like we have to migrate hight-risk (short term and highly paying contracts) to low-risk loyal customers activities.