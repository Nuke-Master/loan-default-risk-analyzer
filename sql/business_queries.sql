-- 1. Total loans

SELECT COUNT(*) AS total_loans
FROM loans;


-- 2. Loans by purpose

SELECT
    purpose,
    COUNT(*) AS total_loans
FROM loans
GROUP BY purpose
ORDER BY total_loans DESC;


-- 3. Non-repayment rate by purpose

SELECT
    purpose,
    COUNT(*) AS total_loans,
    SUM("not.fully.paid") AS unpaid_loans,
    ROUND(AVG("not.fully.paid") * 100, 2) AS non_repayment_rate
FROM loans
GROUP BY purpose
ORDER BY non_repayment_rate DESC;