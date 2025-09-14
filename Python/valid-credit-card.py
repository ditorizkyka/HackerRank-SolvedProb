import re

if __name__ == '__main__':
    n = int(input())
    
    for _ in range(n):
        card = input().strip()

        # Pola valid: 16 digit tanpa pemisah ATAU xxxx-xxxx-xxxx-xxxx
        pattern = r'^[4-6]\d{15}$|^[4-6]\d{3}(-\d{4}){3}$'

        if not re.match(pattern, card):
            print("Invalid")
            continue

        # Hapus semua '-'
        clean_card = card.replace("-", "")

        # Cek apakah ada 4 digit berturut-turut sama
        if re.search(r'(\d)\1{3,}', clean_card):
            print("Invalid")
        else:
            print("Valid")
