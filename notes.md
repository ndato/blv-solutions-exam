# Notes on the Challenges
## Challenge # 1
- Input for N should be Integer **AND** Dictionary or Integer **AND** String, in the case of having the input as a string to be converted into a Dictionary. For the latter case, we can use `ast.literal_eval()` to convert String into a Dictionary. But for simplicity, let's assume that the Input is Dictionary.
- `shift_char` and `replace_char` are assumed to be not used, meaning no need to check if input `m` is a single character. 
## Challenge # 2
- Assumption is the three lists (L1, L2, L3) all match with each other. Meaning L1[0], L2[0], and L3[0] corresponds to Employee[0], L1[N], L2[N], and L3[N] to Employee[N], etc.
- We cannot assume that 4 weeks == 1 month because there are only 52 weeks. So had to compute first the Annual Employee Cost, then divide by 12 to get the Monthly Employee Cost.
- Double checked on the rounding of Significant Figures on the money. Will be using the IFRS Accounting Standard, only round the significant figures when displaying.
- Had to change the input naming (L1, L2, L3) to something that makes more business sense.
- Assumption is Hourly Rate is always positive and that you can't earn money from hiring an Employee per hour. If ever, that should be on the Income Generated computation.
- Assume currency is in $.