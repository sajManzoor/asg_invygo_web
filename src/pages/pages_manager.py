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
        self._monthly_subs_page = None
        # Add other page properties here


    @property
    def home_page(self):
        if self._home_page is None:
            from pages.homepage.home_page import HomePage
            self._home_page = HomePage(self.driver)
        return self._home_page

    @property
    def monthly_subs_page(self):
        if self._monthly_subs_page is None:
            from pages.monthly_subscription.monthly_subscription_page import MonthlySubscriptionPage
            self._monthly_subs_page = MonthlySubscriptionPage(self.driver)
        return self._monthly_subs_page
