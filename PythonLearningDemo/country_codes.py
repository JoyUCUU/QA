from  pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal 使用两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return  code
    return  None
print(get_country_code('Andorra'))
print(get_country_code('United Arb Emirates'))
print(get_country_code('Afghanistan'))