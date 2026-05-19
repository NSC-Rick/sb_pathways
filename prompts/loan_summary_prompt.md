# Loan Readiness Summary Prompt

## Purpose
This prompt will be used to generate AI-powered summaries of completed Loan Readiness workbooks for advisors.

## Context
When a client completes the Loan Readiness pathway, their workbook responses will be processed to create a concise snapshot that highlights:
- Loan request details
- Financial readiness assessment
- Documentation completeness
- Risk factors and gaps

## Prompt Template (Future Implementation)

```
You are reviewing a loan readiness workbook. Create a concise summary for a business advisor that includes:

1. **Loan Request** (2-3 sentences)
   - Amount requested and purpose
   - Timeline and urgency

2. **Financial Position** (2-3 sentences)
   - Current financial health
   - Collateral and guarantees available

3. **Readiness Assessment** (bullet list)
   - Documentation completeness
   - Strengths of the application
   - Gaps or weaknesses

4. **Advisor Focus Areas** (bullet list)
   - What should the advisor help with?
   - What questions need addressing?

Keep the summary under 300 words. Flag any red flags or missing critical documents.
```

## Notes
- This will integrate with workbook submission system
- Summary should assess application strength objectively
- Should highlight missing documentation early
