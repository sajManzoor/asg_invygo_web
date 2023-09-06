class PageObjectManager:
    _instance = None

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super(PageObjectManager, cls).__new__(cls)
            cls._instance.driver = driver
            cls._instance.initialize_pages()
        return cls._instance

    def initialize_pages(self):
        self._home_page = None
        self._cars_page = None
        self._car_list_section = None
        # Add other page properties here


    @property
    def home_page(self):
        if self._home_page is None:
            from pages.homepage.home_page import HomePage
            self._home_page = HomePage(self.driver)
        return self._home_page

    @property
    def cars_page(self):
        if self._cars_page is None:
            from pages.cars_page.cars_page import MonthlySubscriptionPage
            self._cars_page = MonthlySubscriptionPage(self.driver)
        return self._cars_page


    @property
    def car_list_section(self):
        if self._car_list_section is None:
            from pages.cars_page.cars_page import CarListSection
            self._car_list_section = CarListSection(self.driver)
        return self._car_list_section
