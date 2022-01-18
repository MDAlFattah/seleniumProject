import time
from baseSelenium import BaseSelenium


class ServicePage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.service_page = 'services'

    def select_service_page(self):
        """Selecting service page"""
        service = self.service_page
        service_sitem = BaseSelenium.locator_finder_by_id(self, service)
        service_sitem.click()
        time.sleep(2)

    def select_add_service_button(self):
        """selecting new service button"""
        add_new_service = 'addApp'
        add_new_service_stiem = BaseSelenium.locator_finder_by_id(self, add_new_service)
        add_new_service_stiem.click()
        time.sleep(2)

    def service_search_option(self, search_keyword):
        """checking service page search options"""
        search = 'foxxSearch'
        service_search_stiem = BaseSelenium.locator_finder_by_id(self, search)
        service_search_stiem.click()
        service_search_stiem.clear()
        time.sleep(2)

        print(f'Searching for {search_keyword} \n')
        service_search_stiem.send_keys(search_keyword)
        time.sleep(1)

        # checking search find the correct demo services
        if search_keyword == 'demo':
            search_item = '//*[@id="availableFoxxes"]/div[2]/div/div[1]/p[1]/span'
            expected_text = 'demo-graphql'
            demo_graphql_stiem = BaseSelenium.locator_finder_by_xpath(self, search_item)
            # print(f'{demo_graphql_stiem}')
            assert demo_graphql_stiem.text == expected_text, f"Expected text{expected_text} " \
                                                             f"but got {demo_graphql_stiem.text}"
        if search_keyword == 'tab':
            search_item = '//*[@id="availableFoxxes"]/div[7]/div/div[1]/p[1]/span'
            expected_text = 'tableau-connector'
            demo_graphql_stiem = BaseSelenium.locator_finder_by_xpath(self, search_item)
            # print(f'{demo_graphql_stiem}')
            assert demo_graphql_stiem.text == expected_text, f"Expected text{expected_text} " \
                                                             f"but got {demo_graphql_stiem.text}"
        if search_keyword == 'grafana':
            search_item = '//*[@id="availableFoxxes"]/div[3]/div/div[1]/p[1]/span'
            expected_text = 'grafana-connector'
            demo_graphql_stiem = BaseSelenium.locator_finder_by_xpath(self, search_item)
            assert demo_graphql_stiem.text == expected_text, f"Expected text{expected_text} " \
                                                             f"but got {demo_graphql_stiem.text}"

    def service_category_option(self):
        """checking service page category options"""
        category = 'categorySelection'

        print('Selecting category options \n')
        select_service_category_sitem = BaseSelenium.locator_finder_by_id(self, category)
        select_service_category_sitem.click()
        time.sleep(1)

    def service_filter_category_option(self):
        """selecting category search option"""
        filter_option = 'Category-filter'
        filter_option_stiem = BaseSelenium.locator_finder_by_xpath(self, filter_option)
        filter_option_stiem.click()
        filter_option_stiem.clear()
        time.sleep(1)

    def select_category_option_from_list(self, category):
        """checking service page category options"""
        if category == 'connector':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="connector-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'service':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="service-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'geo':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="geo-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'demo':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="demo-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'graphql':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="graphql-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'prometheus':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="prometheus-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'monitoring':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="monitoring-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

    def select_category_option_search_filter(self, keyword):
        """checking service page category option's filter option"""
        filter_placeholder = 'Category-filter'
        filter_placeholder_sitem = BaseSelenium.locator_finder_by_id(self, filter_placeholder)
        filter_placeholder_sitem.click()
        filter_placeholder_sitem.clear()
        filter_placeholder_sitem.send_keys(keyword)
        time.sleep(1)

        if keyword == 'geo':
            search_category = '//*[@id="geo-option"]/span[3]'
            search_category_sitem = BaseSelenium.locator_finder_by_xpath(self, search_category)
            expected_text = 'geo'
            assert search_category_sitem.text == expected_text, f"Expected text{expected_text} " \
                                                                f"but got {search_category_sitem.text}"

        if keyword == 'demo':
            search_category = '//*[@id="demo-option"]/span[3]'
            search_category_sitem = BaseSelenium.locator_finder_by_xpath(self, search_category)
            expected_text = 'demo'
            assert search_category_sitem.text == expected_text, f"Expected text{expected_text} " \
                                                                f"but got {search_category_sitem.text}"

        if keyword == 'connector':
            search_category = '//*[@id="connector-option"]/span[3]'
            search_category_sitem = BaseSelenium.locator_finder_by_xpath(self, search_category)
            expected_text = 'connector'
            assert search_category_sitem.text == expected_text, f"Expected text{expected_text} " \
                                                                f"but got {search_category_sitem.text}"

    def select_demo_geo_s2_service(self):
        """Selecting demo geo s2 service from the list"""
        print('Selecting demo_geo_s2 service \n')
        geo_service = '//*[@id="availableFoxxes"]/div[1]/div/div[3]'
        geo_service_sitem = BaseSelenium.locator_finder_by_xpath(self, geo_service)
        geo_service_sitem.click()
        time.sleep(2)

    def check_demo_geo_s2_service(self):
        """checking general stuff of demo_geo_s2 service"""
        self.select_demo_geo_s2_service()
        github_link = '//*[@id="information"]/div/div[2]/div[1]/p[3]/span[2]/a'
        github_link_sitem = BaseSelenium.locator_finder_by_xpath(self, github_link)
        page_title = super().switch_tab(github_link_sitem)

        expected_title = 'GitHub - arangodb-foxx/demo-geo-s2: A Foxx based geo ' \
                         'example using the new (v3.4+) s2 geospatial index'

        assert page_title == expected_title, f"Expected text{expected_title} but got {page_title}"
        self.driver.back()

    def install_demo_geo_s2_service(self, mount_path):
        """Installing demo geo s2 service from the list"""
        self.select_demo_geo_s2_service()

        print('Installing demo_geo_s2 service \n')
        service = 'installService'
        service_sitem = BaseSelenium.locator_finder_by_id(self, service)
        service_sitem.click()
        time.sleep(2)

        # select a mount point FIXME
        print(f'Selecting service mount point at {mount_path} \n')
        mount_point = 'new-app-mount'
        mount_point_sitem = BaseSelenium.locator_finder_by_id(self, mount_point)
        mount_point_sitem.click()
        mount_point_sitem.clear()
        mount_point_sitem.send_keys(mount_path)

        # selecting install button
        print('Selecting install button \n')
        install_btn = 'modalButton1'
        install_btn_sitem = BaseSelenium.locator_finder_by_id(self, install_btn)
        install_btn_sitem.click()
        time.sleep(5)

        # checking service has been created successfully
        success = '//*[@id="installedList"]/div[2]/div/div[1]/p[2]/span'

        try:
            success_sitem = BaseSelenium.locator_finder_by_xpath(self, success).text
            if success_sitem == 'demo-geo-s2':
                print(f"{success_sitem} has been successfully created \n")
            else:
                print('Could not locate the desired service! refreshing the UI \n')
                self.driver.refresh()
                time.sleep(1)
                success_sitem = BaseSelenium.locator_finder_by_xpath(self, success).text
                if success_sitem == 'demo-geo-s2':
                    print(f"{success_sitem} has been successfully created \n")
        except Exception:
            raise Exception('Failed to create the service!!')
