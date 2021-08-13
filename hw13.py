# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.

def transfer_temperature(temperature, mode=0):
    # mode=0 Цельсия в Фаренгейт
    # mode=1 Фаренгейт в Цельсия
    return 5 / 9 * (temperature - 32) if mode else 9 / 5 * temperature + 32


print(f"40 Цельсия = {transfer_temperature(40)} Фаренгейта")
print(f"104 Фаренгейта = {transfer_temperature(104, 1)} Цельсия")
