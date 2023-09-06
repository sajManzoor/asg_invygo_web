from utils.constants import Constants
from tests.base_case import TestBaseCase
from utils.services import get_all_filters, get_all_car_cards
from data.models import BrandName


class TestBrandFilter(TestBaseCase):

    def setup_method(self, method):
        super().setup_method(method)
        self.navigate_to_cars_page()


    def test_brand_filter_location(self):
        filter_list = self.page_manager.cars_page.filter_list
        # brand filter should be at the second position
        brand_filter = filter_list[1]
        brand_filter_text = brand_filter.text
        assert brand_filter_text == Constants.BRANDS_FILTER_LABEL, \
            f"{brand_filter_text} displayed - Expected is {Constants.BRANDS_FILTER_LABEL}"

    def test_brand_filter_select_filter(self):
        brand_filter_element = self.page_manager.cars_page.filter_list[1]
        brand_filter_element.click()
        filter_option_list = self.page_manager.cars_page.\
            get_selected_filter_options(brand_filter_element)

        # choose the first filter option
        filter_option_list[0].click()
        self.page_manager.cars_page.press_filter_done_button(brand_filter_element)

        observed_selected_filter = self.page_manager.cars_page.get_selected_filter_option_label(brand_filter_element)
        assert observed_selected_filter.text in brand_filter_element.text, f"Exp - {observed_selected_filter} " \
                                                                           f"Obs - {brand_filter_element.text}"

    def test_brand_filter_options(self):
        data = get_all_filters()
        brand_name_objects = [BrandName(brand['key'], brand['label'], brand['count']) for brand in data['brandNames']]

        brand_filter_element = self.page_manager.cars_page.filter_list[1]
        brand_filter_element.click()
        filter_option_list = self.page_manager.cars_page.\
            get_selected_filter_options(brand_filter_element)

        assert len(filter_option_list)
        for option, brand in zip(filter_option_list, brand_name_objects):
            assert option.text == brand.key

    def test_validate_brand_filter_results(self):

        data = get_all_filters()
        brand_name_objects = [BrandName(brand['key'], brand['label'], brand['count']) for brand in data['brandNames']]

        brand_filter_element = self.page_manager.cars_page.filter_list[1]
        brand_filter_element.click()
        filter_option_list = self.page_manager.cars_page.\
            get_selected_filter_options(brand_filter_element)

        # choose the first filter option
        filter_option_list[0].click()
        self.page_manager.cars_page.press_filter_done_button(brand_filter_element)
        assert len(self.page_manager.car_list_section.car_cards)
        for element in self.page_manager.car_list_section.car_cards:
            car_data = get_all_car_cards(brand_name_objects[0].key)
            car_name = self.page_manager.car_list_section.get_car_card_details(element)
            assert car_name == f"{car_data['brandName']} {car_data['carName']}"

    def teardown_method(self, method):
        super().teardown_method(method)







