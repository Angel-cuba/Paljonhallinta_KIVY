# A module for calculation body mass index and body fat percentage 

# Funktioiden määrittelyt

# Body mass index
def bmi(weight, height):
    
    """Laskee painoindeksin kaavalla paino jaettuna pituuden sadaosan neliöllä
    Args:
        weight (float): weight (kg)
        height (float): height (cm)
    Returns:
        float: bmi
    """
    bmi = weight / (height/100) ** 2
    return bmi
    
# Fat percentage
def fat_percentage(bmi, age, sex):
    """Calculates the fat percentage
    Args:
        bmi (float): body mass index
        age (float): age in years
        sex (int): 1 - Male, 0 - Female
    Returns:
        float: kehon rasvaprosentti
    """
    # F-% for adults
    if age >= 18:
        fat_percentage = 1.2 * bmi + 0.23 * age - 10.8 * sex - 5.4
    else:
        # F-% for children
        fat_percentage = 1.51 * bmi - 0.70 * age - 3.6 * sex + 1.4
    
    return fat_percentage

# Testit
if __name__ == '__main__':
    
    # 1. testi oma painoindeksi
    my_height = 171
    my_weight = 74.9
    my_bmi = bmi(my_weight, my_height)
    print('Height:', my_height, 'Weight:', my_weight, 'Painoindeksi', my_bmi) 

    # 2. testi oma rasvaprosentti
    my_age = 59
    my_sex = 1
    print('Rasvaprosentti:', fat_percentage(my_bmi, my_age, my_sex))