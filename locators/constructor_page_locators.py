from selenium.webdriver.common.by import By


class ConstructorPageLocators:

    ASSEMBLE_BURGER_TEXT = [By.XPATH, '//h1[text() = "Соберите бургер"]']
    RANDOM_INGREDIENT_ITEM = [By.XPATH, '//a[@href = "/ingredient/{ingredient_id}"]']
    INGREDIENT_COUNTER = [By.XPATH, '//a[@href = "/ingredient/{ingredient_id}"]//p']
    ORDER_PICKING_AREA = [By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_']
    ORDER_BUTTON = [By.XPATH, '//button[text() = "Оформить заказ"]']

    INGREDIENT_DETAILS_TEXT = [By.XPATH, '//h2[text() = "Детали ингредиента"]']
    INGREDIENT_DETAILS_CLOSE_BUTTON = \
        [By.XPATH, '//h2[text() = "Детали ингредиента"]/parent::div/following-sibling::button[contains(@class, "modal__close")]']

    ORDER_NUMBER_ON_SUCCESS_SCREEN = [By.XPATH, '//p[text() = "идентификатор заказа"]/preceding-sibling::h2']
    PENDING_ORDER_TEXT = [By.XPATH, '//p[text() = "Ваш заказ начали готовить"]']
    LOADING_ANIMATION = [By.XPATH, '//img[@alt = "loading animation"]']
