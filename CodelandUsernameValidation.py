# CodelandUsernameValidation.py(Python 3    Coderbyte Challenge)
# This function validates a username based on specific criteria:
# 1. Length must be between 4 and 25 characters.
# 2. Must start with a letter.
# 3. Can only contain letters, digits, and underscores.
# 4. Cannot end with an underscore.
# 5. Cannot contain special characters other than underscores.
# The function returns "true" if the username is valid, otherwise "false".


def CodelandUsernameValidation(strParam):
    # Validate the username based on the specified criteria
  varName = strParam
  varFiltersName = True

  if len(varName) < 4 or len(varName) > 25:
    return "false"

  if not varName[0].isalpha():
    return "false"

  for char in varName:
    if not (char.isalpha() or char.isdigit() or char == '_'):
      varFiltersName = False
      break

  if not varFiltersName:
    return "false"

  if varName[-1] == '_':
    return "false"

  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))