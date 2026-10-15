-- View: public.view_cleaned_loan_risk
-- Description: Filters raw consumer loan data down to mature cycles, 
-- cleans employment tenure to numeric format, and engineers the binary default indicator.

DROP VIEW IF EXISTS public.view_cleaned_loan_risk;

CREATE OR REPLACE VIEW public.view_cleaned_loan_risk AS
SELECT 
    id,
    loan_amnt AS loan_amount,
    funded_amnt,
    term,
    int_rate,
    installment,
    grade,
    sub_grade,
    emp_title,
    
    -- Normalize employment string tenure ('10+ years', '< 1 year') into clean integers
    CASE 
        WHEN emp_length = '< 1 year' THEN 0
        WHEN emp_length = '10+ years' THEN 10
        ELSE CAST(REGEXP_REPLACE(emp_length, '[^0-9]', '', 'g') AS INTEGER)
    END AS emp_years,
    
    home_ownership,
    annual_inc,
    verification_status,
    issue_d AS issue_date,
    loan_status,
    
    -- Binary outcome label: 1 = Default / Loss, 0 = Fully Paid
    CASE 
        WHEN loan_status IN ('Charged Off', 'Default') THEN 1 
        ELSE 0 
    END AS is_default,
    
    purpose,
    addr_state,
    dti,
    delinq_2yrs,
    fico_range_low,
    fico_range_high,
    open_acc,
    pub_rec,
    revol_bal,
    total_acc

FROM public.raw_loans
-- Focus strictly on completed loan outcomes; exclude currently active loans
WHERE loan_status IN ('Fully Paid', 'Charged Off', 'Default');
