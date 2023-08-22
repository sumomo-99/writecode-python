import sys

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """シーザー暗号を復号化する
    Args:
        ciphertext: 暗号文
        shift: シフト数
    Returns:
        str: 復号文
    """
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

if __name__ == '__main__':
    args = sys.argv
    ciphertext = args[1]
    shift = int(args[2])

    decrypted_text = caesar_decrypt(ciphertext, shift)
    print("Decrypted text:", decrypted_text)
