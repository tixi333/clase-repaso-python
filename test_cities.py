from city_functions import get_city_country

def test_city_country():
    resultado = get_city_country('santiago', 'chile')
    assert resultado == 'Santiago, Chile'