from pathlib import Path

path = Path('m_pi_digits.txt')
contents = path.read_text()

fecha = (input("Ingrese una fecha en formato ddmmaa: "))

if fecha in contents:
    print("¡Felicidades! Tu fecha aparece en los dígitos de pi.")
else:
    print("Lo siento, tu fecha no aparece en los dígitos de pi.")