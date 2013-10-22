characters = 'qwertyuiopasdfghjklzxcvbnm ';
a = 263
m = 65519

def approximate_search(T, S):
  """
  Search for string S in document T. Return the position of the first match,
  or None if no match.

  Parameters
  ----------
  T : str
      Document to search.
  S : str
      String to search in document.

  Returns
  -------
  pos : int or None
      Position of first approximate match of S in T, or None if no match.
  """
  sLength = len(S)
  tLength = len(T)

  if sLength > tLength:
    return None
  sHash = rolling_hash(S)
  sHashVariants = compute_variants_and_hashes(S)
  for i in range(tLength - sLength):
    substringT = T[i: i + sLength]
    substringTHash = rolling_hash(substringT)
    if (sHash == substringTHash):
      if (S == substringT):
        return i
    for j in sHashVariants:
      if j[1] == substringTHash:
        if j[0] == list(substringT):
          return i
  return None

def rolling_hash(string):
  sum = 0
  for i in range(len(string)):
    if string[i] != " ":
      # let space be 0, a = 1, b = 2...z=26
      sum += (ord(string[i]) - 96) * (a ** (len(string) - 1 - i))
      sum %= m

  return sum

def compute_variants_and_hashes(string):

  # array of variants and their hashes as tuples (variant, hash)
  variants = [];

  # Make it into a mutable type.
  originalString = list(string)
  originalStringHash = rolling_hash(originalString)
  stringLength = len(string)
  # The string we actually mutate.
  dummyString = list(string)

  for i in range(stringLength):
    # compute the original digit value
    digitValue = compute(originalString[i], stringLength, i)
    for j in characters:
      if (j != originalString[i]):
        # replace the digit
        dummyString[i] = j
        # print dummyString
        # print originalString
        # Compute the new hash value, which can be computed by
        # getting the original hash value and subtracting the
        # value of the digit here * a ** position from right.
        dummyStringHash = (originalStringHash - digitValue + compute(dummyString[i], stringLength, i)) % m
        variants.append((dummyString, dummyStringHash))
    # set back to original
    dummyString = list(string)
  # swaps
  for i in range(stringLength - 1):
    dummyVariable = originalString[i]
    dummyString[i] = originalString[i + 1]
    dummyString[i + 1] = dummyVariable
    digitIValue = (compute(originalString[i + 1], stringLength, i) - compute(originalString[i], stringLength, i)) % m
    digitJValue = (compute(originalString[i], stringLength, i + 1) - compute(originalString[i + 1], stringLength, i + 1)) % m
    dummyStringHash = (originalStringHash + digitIValue + digitJValue) % m
    variants.append((dummyString, dummyStringHash))
    dummyString = list(string)
  return variants

def compute(character, stringLength, index):
  if character == " ":
    return 0
  return ((ord(character) - 96) * a ** (stringLength - index - 1)) % m

# print approximate_search("the quick brown fox jumps over the lazy dog", "uqick")
# print approximate_search("the quick brown fox jumps over the lazy dog", "the")
# print approximate_search("the quick brown fox jumps over the lazy dog", "thez")
# print approximate_search("the quick brown fox jumps over the lazy dog", "hello world")
