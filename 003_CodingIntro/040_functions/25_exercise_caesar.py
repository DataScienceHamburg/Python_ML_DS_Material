#%% 
# wikipedia: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence

def caesar(text, offset = 3, mode='encrypt'):
    """Encrypt or Decrypt Caesar Chiffre

    Args:
        text (str): The text to en/decrypt
        offset (int, optional): The offset in the alphabet. Defaults to 3.
        mode (str, optional): can be either 'encrypt' or 'decrypt'. Defaults to 'encrypt'.

    Returns:
        str: encrypted/decrypted text
    """
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    text = text.upper()
    
    for i in range(len(text)):
        letter_pos_in_alphabet = ALPHABET.index(text[i])
        
        letter_pos_with_offset = (letter_pos_in_alphabet + offset) % 26 if mode=='encrypt' else (letter_pos_in_alphabet - offset) % 26
        result = f"{result}{ALPHABET[letter_pos_with_offset]}"
    return result
#%% test encrypt
caesar(text='hello', offset=3, mode='encrypt')
# %%
caesar(text='KHOOR', offset = 3, mode='decrypt')
# %%
