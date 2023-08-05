Trabalhe com formatação de números de uma maneira rápido e fácil.

```python
from lealNumeros import LealNumerosAPI

# Put punctuation in numbers
print(LealNumerosAPI.numerosPontuados(10000))
# Output: 10.000

# Put symbols
        # Available formats: (8)    (pt-Br: mil | en: Thousand (Multiple languages))
        #                           M (Million)
        #                           B (Billion)
        #                           T (Trillion)
        #                           Q (Quadrillion)
        #                           Qi (Quintillion)
        #                           Sx (Sextillion)
        #                           Sp (Septillion)
print(LealNumerosAPI.numerosSimbolos(10000))
# Output: 10Mil

# Write the name of the number
print(LealNumerosAPI.numerosNome(100, lang='pt-br')) # Multiple language (Exemplo: en (ENGLISH))
# Output: Cem (pt-br)

# Write differences between numbers
print(LealNumerosAPI.numerosDiferenca(5, 10))
# Output: 5

# Write differences between days
print(f'{LealNumerosAPI.dataDiferenca(1, 2, 2023)} Days')

# Calculator
account = input('What is the mathematical account? (ex .: 10 + 5)')
result = LealNumerosAPI.numerosCalculadora(account)
print(result)

# CHANGELOGS -> https://discord.com/invite/394ChkbKrt
# 0.0.6 - Added multiple languages
# 0.0.5 - Added function to calculate (add, subtract, multiply and divide)
# 0.0.5 - Added function to compare days (by date: day/month/year)
# 0.0.4 - Added function to compare difference between numbers.
```

---

Discord: silvaleal#7458
Suporte: [https://discord.gg/394ChkbKrt](https://discord.gg/394ChkbKrt)
