class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(Locators.SEARCH_RESULT_LINK)


