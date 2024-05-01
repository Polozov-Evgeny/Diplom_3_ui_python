class Urls:

    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CONSTRUCTOR_URL = f'{MAIN_URL}/'
    INGREDIENT_CARD_URL = MAIN_URL + '/ingredient/{id}'
    ORDER_FEED_URL = f'{MAIN_URL}/feed'
    ORDER_FEED_CARD_URL = MAIN_URL + '/feed/{id}'

    REGISTRATION_URL = f'{MAIN_URL}/register'
    LOGIN_URL = f'{MAIN_URL}/login'
    FORGOT_PASSWORD_URL = f'{MAIN_URL}/forgot-password'
    RESET_PASSWORD_URL = f'{MAIN_URL}/reset-password'

    ACCOUNT_URL = f'{MAIN_URL}/account'
    PROFILE_URL = f'{ACCOUNT_URL}/profile'
    ORDER_HISTORY_URL = f'{ACCOUNT_URL}/order-history'
    ORDER_HISTORY_CARD_URL = ACCOUNT_URL + '/order-history/{id}'
