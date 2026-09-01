def crypt(word: str):
  cryptword = ""
  for l in word:
    cryptword += "_"
  return cryptword

def replace_letter(word: str, hidden_word: str, letter: str) -> str:
  new_word = ""
  for i, l in enumerate(word.replace(" ", "")):
    new_word += letter if letter == hidden_word[i] else l
  return new_word

def spacing(word: str) -> str:
  new_word = ""
  for l in word:
    new_word += l + " "
  return new_word.strip()