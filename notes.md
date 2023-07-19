# Notes on the Challenges
## Challenge # 1
- Input for N should be Integer **AND** Dictionary or Integer **AND** String, in the case of having the input as a string to be converted into a Dictionary. For the latter case, we can use `ast.literal_eval()` to convert String into a Dictionary. But for simplicity, let's assume that the Input is Dictionary.
- `shift_char` and `replace_char` are assumed to be not used, meaning no need to check if input `m` is a single character. 