import time
import semver
from baseSelenium import BaseSelenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


# from selenium.webdriver.common.keys import Keys


class ViewsPage(BaseSelenium):
    # views id after creation
    select_improved_arangosearch_view_01 = "//h5[contains(text(),'improved_arangosearch_view_01')]"
    select_improved_arangosearch_view_02 = "//h5[contains(text(),'improved_arangosearch_view_02')]"
    select_modified_views_name = "//h5[contains(text(),'modified_views_name')]"

    search_first_view = '//*[@id="firstView"]/div/h5'
    search_second_view = '//*[@id="secondView"]/div/h5'

    select_renamed_view_id = "/html//div[@id='thirdView']"
    select_second_view_id = "//div[@id='secondView']//h5[@class='collectionName']"

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.select_views_tab_id = "/html//a[@id='views']"
        self.create_new_views_id = "/html//a[@id='createView']"
        self.naming_new_view_id = "/html//input[@id='newName']"
        self.select_create_btn_id = "//div[@id='modal-dialog']//button[@class='button-success']"
        self.select_views_settings_id = "//a[@id='viewsToggle']/span[@title='Settings']"

        # self.select_sorting_views_id = "//div[@id='viewsDropdown']/ul//label[@class='checkbox checkboxLabel']"
        self.select_sorting_views_id = '//*[@id="viewsDropdown"]/ul/li[2]/a/label/i'

        self.search_views_id = "/html//input[@id='viewsSearchInput']"
        self.select_first_view_id = "//*[@id='firstView']/div/h5"
        self.select_collapse_btn_id = "//*[@id='propertiesEditor']/div/div[1]/button[2]"
        self.select_expand_btn_id = "//*[@id='propertiesEditor']/div/div[1]/button[1]"
        self.select_editor_mode_btn_id = "//div[@id='propertiesEditor']//div[@class='jsoneditor-modes']" \
                                         "/button[@title='Switch editor mode']"
        self.switch_to_code_editor_mode_id = "//div[@id='propertiesEditor']//div[@class='jsoneditor-anchor']" \
                                             "//div[@class='jsoneditor-contextmenu']/ul[@class='jsoneditor-menu']" \
                                             "//button[@title='Switch to code highlighter']"
        self.compact_json_data_id = "/html//div[@id='propertiesEditor']//button[@title='Compact JSON data, remove all whitespaces (Ctrl+Shift+\)']"
        self.switch_to_tree_editor_mode_id = "//div[@id='propertiesEditor']/div[@class='jsoneditor " \
                                             "jsoneditor-mode-code']//div[@class='jsoneditor-anchor']//" \
                                             "ul[@class='jsoneditor-menu']//button[@title='Switch to tree editor']"
        self.click_arangosearch_documentation_link_id = "//div[@id='viewDocumentation']//a[@href=" \
                                                        "'https://www.arangodb.com/docs/stable" \
                                                        "/arangosearch-views.html']"
        self.select_inside_search_id = "//*[@id='propertiesEditor']/div/div[1]/table" \
                                       "/tbody/tr/td[2]/div/table/tbody/tr/td[2]/input"
        self.search_result_traverse_up_id = "/html//div[@id='propertiesEditor']/div[@class='jsoneditor " \
                                            "jsoneditor-mode-tree']//table[@class='jsoneditor-search']" \
                                            "//div[@title='Search fields and values']/table//button[@title=" \
                                            "'Previous result (Shift+Enter)']"
        self.search_result_traverse_down_id = "/html//div[@id='propertiesEditor']/div[@class=" \
                                              "'jsoneditor jsoneditor-mode-tree']//table[@class=" \
                                              "'jsoneditor-search']//div[@title=" \
                                              "'Search fields and values']/table//button[@title='Next result (Enter)']"
        self.change_consolidation_policy_id = "/html//div[@id='propertiesEditor']/div[@class=" \
                                              "'jsoneditor jsoneditor-mode-tree']/div[3]/div[@class=" \
                                              "'jsoneditor-tree']//table[@class='jsoneditor-tree']" \
                                              "/tbody/tr[16]/td[3]/table[@class='jsoneditor-values']//tr/td[4]/div"
        self.clicking_rename_views_btn_id = "renameViewButton"

        self.rename_views_name_id = "/html//input[@id='editCurrentName']"
        self.rename_views_name_confirm_id = "//div[@id='modal-dialog']//button[@class='button-success']"

        self.delete_views_btn_id = "deleteViewButton"
        self.delete_views_confirm_btn_id = "//div[@id='modal-dialog']//button[@class='button-danger']"
        self.final_delete_confirmation_id = "modal-confirm-delete"

    # selecting views tab
    def select_views_tab(self):
        select_views_tab_sitem = self.locator_finder_by_xpath(self.select_views_tab_id)
        select_views_tab_sitem.click()

    # creating new views tab
    def create_new_views(self, name):
        print(f'Creating {name} started \n')
        create_new_views_sitem = self.locator_finder_by_xpath(self.create_new_views_id)
        create_new_views_sitem.click()

        print('Naming new views \n')
        naming_new_view_sitem = self.locator_finder_by_xpath(self.naming_new_view_id)
        naming_new_view_sitem.click()
        naming_new_view_sitem.send_keys(name)

        print('Creating new views tab \n')
        select_create_btn_sitem = self.locator_finder_by_xpath(self.select_create_btn_id)
        select_create_btn_sitem.click()
        time.sleep(2)
        print(f'Creating {name} completed \n')

    # selecting view setting
    def select_views_settings(self):
        select_views_settings_sitem = self.locator_finder_by_xpath(self.select_views_settings_id)
        select_views_settings_sitem.click()
        time.sleep(3)

    # sorting multiple views into descending
    def select_sorting_views(self):
        select_sorting_views_sitem = self.locator_finder_by_xpath(self.select_sorting_views_id)
        select_sorting_views_sitem.click()
        time.sleep(3)

    # searching views
    def search_views(self, expected_text, search_locator):
        search_views_sitem = self.locator_finder_by_xpath(self.search_views_id)
        search_views_sitem.click()
        search_views_sitem.clear()
        search_views_sitem.send_keys(expected_text)
        time.sleep(2)

        print(f'Checking that we get the right results for {expected_text}\n')
        # version = self.get_current_package_version()
        # if semver.VersionInfo.parse(version) <= "3.8.0":
        if self.current_package_version() <= semver.VersionInfo.parse("3.8.0"):
            if expected_text == 'firstView':
                found = self.locator_finder_by_xpath(search_locator).text
                assert found == expected_text, f"Expected views title {expected_text} but got {found}"
            elif expected_text == 'secondView':
                found = self.locator_finder_by_xpath(search_locator).text
                assert found == expected_text, f"Expected views title {expected_text} but got {found}"
        else:
            if expected_text == 'improved_arangosearch_view_01':
                found = self.locator_finder_by_xpath(search_locator).text
                assert found == expected_text, f"Expected views title {expected_text} but got {found}"
            elif expected_text == 'improved_arangosearch_view_02':
                found = self.locator_finder_by_xpath(search_locator).text
                assert found == expected_text, f"Expected views title {expected_text} but got {found}"
        self.driver.refresh()

    # selecting first view
    def select_first_view(self):
        select_first_view_sitem = self.locator_finder_by_xpath(self.select_first_view_id)
        select_first_view_sitem.click()

    # selecting collapse all btn
    def select_collapse_btn(self):
        select_collapse_btn_sitem = self.locator_finder_by_xpath(self.select_collapse_btn_id)
        select_collapse_btn_sitem.click()
        time.sleep(3)

    # selecting expand all btn
    def select_expand_btn(self):
        select_expand_btn_sitem = self.locator_finder_by_xpath(self.select_expand_btn_id)
        select_expand_btn_sitem.click()
        time.sleep(3)

    # selecting object tabs
    def select_editor_mode_btn(self):
        select_editor_btn_sitem = self.locator_finder_by_xpath(self.select_editor_mode_btn_id)
        select_editor_btn_sitem.click()
        time.sleep(3)

    # switching editor mode to Code
    def switch_to_code_editor_mode(self):
        switch_to_code_editor_mode_sitem = \
            self.locator_finder_by_xpath(self.switch_to_code_editor_mode_id)
        switch_to_code_editor_mode_sitem.click()
        time.sleep(3)

    # switching editor mode to Code compact view
    def compact_json_data(self):
        compact_json_data_sitem = self.locator_finder_by_xpath(self.compact_json_data_id)
        compact_json_data_sitem.click()
        time.sleep(3)

    # switching editor mode to Tree
    def switch_to_tree_editor_mode(self):
        switch_to_tree_editor_mode_sitem = \
            self.locator_finder_by_xpath(self.switch_to_tree_editor_mode_id)
        switch_to_tree_editor_mode_sitem.click()
        time.sleep(3)

    # Clicking on arangosearch documentation link
    def click_arangosearch_documentation_link(self):
        self.click_arangosearch_documentation_link_id = \
            self.locator_finder_by_xpath(self.click_arangosearch_documentation_link_id)
        title = self.switch_tab(self.click_arangosearch_documentation_link_id)
        expected_title = 'Views Reference | ArangoSearch | Indexing | Manual | ArangoDB Documentation'
        assert title in expected_title, f"Expected page title {expected_title} but got {title}"

    # Selecting search option inside views
    def select_inside_search(self, keyword):
        select_inside_search_sitem = self.locator_finder_by_xpath(self.select_inside_search_id)
        select_inside_search_sitem.click()
        select_inside_search_sitem.clear()
        select_inside_search_sitem.send_keys(keyword)

    # traverse search results down
    def search_result_traverse_down(self):
        search_result_traverse_down_sitem = \
            self.locator_finder_by_xpath(self.search_result_traverse_down_id)
        for x in range(8):
            search_result_traverse_down_sitem.click()
            time.sleep(1)

    # traverse search results up
    def search_result_traverse_up(self):
        search_result_traverse_up_sitem = self.locator_finder_by_xpath(self.search_result_traverse_up_id)
        for x in range(8):
            search_result_traverse_up_sitem.click()
            time.sleep(1)

    # Select Views rename btn
    def clicking_rename_views_btn(self):
        clicking_rename_btn_sitem = self.locator_finder_by_id(self.clicking_rename_views_btn_id)
        clicking_rename_btn_sitem.click()
        time.sleep(1)

    # changing view name
    def rename_views_name(self, name):
        rename_views_name_sitem = self.locator_finder_by_xpath(self.rename_views_name_id)
        rename_views_name_sitem.click()
        rename_views_name_sitem.clear()
        rename_views_name_sitem.send_keys(name)

    # Confirm rename views
    def rename_views_name_confirm(self):
        rename_views_name_confirm_sitem = self.locator_finder_by_xpath(self.rename_views_name_confirm_id)
        rename_views_name_confirm_sitem.click()
        time.sleep(2)

    # creating improved views tab
    def create_improved_views(self, view_name, types):
        """This method will create the improved views for v3.9+"""
        print('Selecting views create button \n')
        create_new_views_id = self.locator_finder_by_xpath(self.create_new_views_id)
        create_new_views_id.click()
        time.sleep(2)

        print(f'Select name for the {view_name} \n')
        name_id = 'newName'
        name_id_sitem = self.locator_finder_by_id(name_id)
        name_id_sitem.click()
        name_id_sitem.clear()
        name_id_sitem.send_keys(view_name)
        time.sleep(2)

        print(f'Selecting primary compression for {view_name} \n')
        primary_compression = 'newPrimarySortCompression'
        self.locator_finder_by_select(primary_compression, types)  # keep it default choice
        time.sleep(2)

        print(f'Select primary sort for {view_name} \n')
        primary_sort = '//*[@id="accordion2"]/div/div[1]/a/span[2]/b'
        primary_sort_sitem = self.locator_finder_by_xpath(primary_sort)
        primary_sort_sitem.click()
        time.sleep(2)

        print(f'Select primary field for {view_name} \n')
        primary_field = '//*[@id="newPrimarySort-row-0"]/td[1]/input'
        primary_field_sitem = self.locator_finder_by_xpath(primary_field)
        primary_field_sitem.click()
        primary_field_sitem.clear()
        primary_field_sitem.send_keys('attr')
        time.sleep(2)

        print(f'Selecting direction for {view_name} \n')
        direction = '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/table/tbody/tr/th/table/tbody/tr/td[2]/select'
        self.locator_finder_by_select_using_xpath(direction, types)  # keep it default choice

        print(f'Select stored value for {view_name} \n')
        sorted_value = '//*[@id="accordion3"]/div/div[1]/a/span[2]/b'
        sorted_value_sitem = self.locator_finder_by_xpath(sorted_value)
        sorted_value_sitem.click()
        time.sleep(2)

        # version = self.current_package_version()

        # if version >= 3.9:
        if self.current_package_version() >= semver.VersionInfo.parse("3.9.0"):
            print('stored value has been skipped.\n')
        else:
            print(f'Select stored field for {view_name} \n')
            # stored_field = "//div[contains(@id,'s2id_field')]"
            stored_field = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/th/table/tbody/tr/td[1]/div"

            stored_field_sitem = self.locator_finder_by_xpath(stored_field)
            stored_field_sitem.click()
            stored_field_sitem.clear()
            stored_field_sitem.send_keys('attr')
            stored_field_sitem.send_keys(Keys.ENTER)
            time.sleep(2)

        print(f'Selecting stored direction for {view_name} \n')
        stored_direction = '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/table/tbody' \
                           '/tr/th/table/tbody/tr/td[2]/select'
        self.locator_finder_by_select_using_xpath(stored_direction, types)  # keep it default choice
        time.sleep(2)

        print(f'Select advance options for {view_name} \n')
        advance_option = '//*[@id="accordion4"]/div/div[1]/a/span[2]/b'
        advance_option_sitem = self.locator_finder_by_xpath(advance_option)
        advance_option_sitem.click()
        time.sleep(2)

        print(f'Select write buffer value for {view_name} \n')
        write_buffer = 'newWriteBufferIdle'
        write_buffer_sitem = self.locator_finder_by_id(write_buffer)
        write_buffer_sitem.click()
        write_buffer_sitem.clear()
        write_buffer_sitem.send_keys('50')
        time.sleep(2)

        print(f'Select write buffer value for {view_name} \n')
        write_buffer_active = 'newWriteBufferActive'
        write_buffer_active_sitem = self.locator_finder_by_id(write_buffer_active)
        write_buffer_active_sitem.click()
        write_buffer_active_sitem.clear()
        write_buffer_active_sitem.send_keys('8')
        time.sleep(2)

        print(f'Select max write buffer value for {view_name} \n')
        max_buffer_size = 'newWriteBufferSizeMax'
        max_buffer_size_sitem = self.locator_finder_by_id(max_buffer_size)
        max_buffer_size_sitem.click()
        max_buffer_size_sitem.send_keys('33554434')
        time.sleep(2)

        print(f'Selecting creation button for {view_name} \n')
        max_buffer_size = 'modalButton1'
        max_buffer_size_sitem = self.locator_finder_by_id(max_buffer_size)
        max_buffer_size_sitem.click()
        max_buffer_size_sitem.send_keys('33554434')
        time.sleep(2)
        self.driver.refresh()

    def checking_modified_views(self, current_deployment):
        """This method will check views for 3.10.x package version"""
        print('Selecting improved views \n')
        views = "//*[text()='improved_arangosearch_view_01']"
        views_sitem = self.locator_finder_by_xpath(views)
        views_sitem.click()
        time.sleep(2)

        print('Selecting Consolidation Policy \n')
        policy = "//*[text()='Consolidation Policy']"
        policy_sitem = self.locator_finder_by_xpath(policy)
        policy_sitem.click()
        time.sleep(2)

        print('Selecting segments min value \n')
        segment_min = "/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/table/tbody/tr[2]/th[2]/input"
        segment_min_sitem = self.locator_finder_by_xpath(segment_min)
        segment_min_sitem.click()
        segment_min_sitem.clear()
        segment_min_sitem.send_keys('4')
        time.sleep(2)

        print('Selecting segments max value \n')
        segment_max = "/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/table/tbody/tr[3]/th[2]/input"
        segment_max_sitem = self.locator_finder_by_xpath(segment_max)
        segment_max_sitem.click()
        segment_max_sitem.clear()
        segment_max_sitem.send_keys('14')
        time.sleep(2)

        print('Selecting bytes value \n')
        segment_bytes = "/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/table/tbody/tr[4]/th[2]/input"
        segment_bytes_sitem = self.locator_finder_by_xpath(segment_bytes)
        segment_bytes_sitem.click()
        segment_bytes_sitem.clear()
        segment_bytes_sitem.send_keys('5368709128')
        time.sleep(2)

        print('Selecting bytes floor value \n')
        segment_floor = "/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/table/tbody/tr[5]/th[2]/input"
        segment_floor_sitem = self.locator_finder_by_xpath(segment_floor)
        segment_floor_sitem.click()
        segment_floor_sitem.clear()
        segment_floor_sitem.send_keys('2097158')
        time.sleep(2)

        print('Saving the consolidation policy with new value \n')
        save = '//*[@id="modal-dialog"]/div[2]/button/i'
        save_sitem = self.locator_finder_by_xpath(save)
        save_sitem.click()
        time.sleep(3)

        print('Select JSON tab \n')
        json = '//*[@id="subNavigationBar"]/ul[2]/li[5]/a'
        json_sitem = self.locator_finder_by_xpath(json)
        json_sitem.click()
        time.sleep(1)

        print("Switch editor mode to Compact mode Code \n")
        compact = '//*[@id="JSON"]/div/div[2]/div/div/div/div/div[1]/button[2]'
        compact_sitem = self.locator_finder_by_xpath(compact)
        compact_sitem.click()
        time.sleep(1)

        print("Switch editor mode to normal mode Code \n")
        normal = '//*[@id="JSON"]/div/div[2]/div/div/div/div/div[1]/button[1]'
        normal_sitem = self.locator_finder_by_xpath(normal)
        normal_sitem.click()

        if current_deployment == 3:
            print('Changing name of the view is disabled for cluster deployment \n')
        else:
            print('Select Settings tab \n')
            settings = "//*[text()='Settings']"
            settings_sitem = self.locator_finder_by_xpath(settings)
            settings_sitem.click()

            print('Change view name \n')
            name = '/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/table/tbody/tr[1]/th[2]/input'
            name_stiem = self.locator_finder_by_xpath(name)
            name_stiem.click()
            name_stiem.clear()
            name_stiem.send_keys('modified_views_name')
            time.sleep(2)

            save_btn = '//*[@id="modal-dialog"]/div[2]/button[2]'
            save_btn_sitem = self.locator_finder_by_xpath(save_btn)
            save_btn_sitem.click()
            time.sleep(2)

    def delete_new_views(self, name):
        """this method will delete all the newer version views"""
        self.select_views_tab()
        try:
            views = ''
            if name == 'modified_views_name':
                views = "//*[text()='modified_views_name']"
            elif name == 'improved_arangosearch_view_01':
                views = "//*[text()='improved_arangosearch_view_01']"
            elif name == 'improved_arangosearch_view_02':
                views = "//*[text()='improved_arangosearch_view_02']"

            views_sitem = self.locator_finder_by_xpath(views)
            views_sitem.click()
            time.sleep(2)

            settings_tab = "//*[text()='Settings']"
            settings_tab_sitem = self.locator_finder_by_xpath(settings_tab)
            settings_tab_sitem.click()
            time.sleep(2)

            delete_btn = '//*[@id="modal-dialog"]/div[2]/button[1]'
            delete_btn_sitem = self.locator_finder_by_xpath(delete_btn)
            delete_btn_sitem.click()
            time.sleep(2)

            confirm_delete_btn = ''
            if name == 'modified_views_name':
                confirm_delete_btn = '//*[@id="modal-content-delete-modified_views_name"]/div[3]/button[2]'
            elif name == 'improved_arangosearch_view_01':
                confirm_delete_btn = '//*[@id="modal-content-delete-improved_arangosearch_view_01"]/div[3]/button[2]'
            elif name == 'improved_arangosearch_view_02':
                confirm_delete_btn = '//*[@id="modal-content-delete-improved_arangosearch_view_02"]/div[3]/button[2]'

            confirm_delete_btn_sitem = self.locator_finder_by_xpath(confirm_delete_btn)
            confirm_delete_btn_sitem.click()
            time.sleep(2)

            self.driver.refresh()
            time.sleep(2)

        except TimeoutException as ex:
            print(f'Error found, Can not delete views {ex} \n')

    def checking_improved_views(self, name, locator, current_deployment):
        """This method will check improved views"""
        print(f'Checking {name} started \n')
        print(f"Selecting {name}'s settings button\n")
        self.select_views_settings()

        print("Sorting views to descending\n")
        self.select_sorting_views()
        print("Sorting views to ascending\n")
        self.select_sorting_views()

        print("Views search option testing\n")
        self.search_views("improved_arangosearch_view_01", self.select_improved_arangosearch_view_01)
        self.search_views("improved_arangosearch_view_02", self.select_improved_arangosearch_view_02)

        print(f'Selecting {name} for checking \n')
        select_view_sitem = self.locator_finder_by_xpath(locator)
        select_view_sitem.click()

        self.select_collapse_btn()
        print("Selecting expand button \n")
        self.select_expand_btn()
        print("Selecting editor mode \n")
        self.select_editor_mode_btn()
        print("Switch editor mode to Code \n")
        self.switch_to_code_editor_mode()
        print("Switch editor mode to Compact mode Code \n")
        self.compact_json_data()

        print("Selecting editor mode \n")
        self.select_editor_mode_btn()
        print("Switch editor mode to Tree \n")
        self.switch_to_tree_editor_mode()

        print("Clicking on ArangoSearch documentation link \n")
        self.click_arangosearch_documentation_link()
        print("Selecting search option\n")
        self.select_inside_search("i")
        print("Traversing all results up and down \n")
        self.search_result_traverse_down()
        self.search_result_traverse_up()

        if current_deployment == 3:
            print('Renaming views are disabled for the Cluster deployment')
        else:
            print(f"Rename {name} to modified_name started \n")
            self.clicking_rename_views_btn()
            self.rename_views_name("modified_views_name")
            self.rename_views_name_confirm()
            print("Rename the current Views completed \n")
        print(f'Checking {name} Completed \n')

    def delete_views(self, name, locator):
        """This method will delete views"""
        self.select_views_tab()
        try:
            print(f'Selecting {name} for deleting \n')
            select_view_sitem = self.locator_finder_by_xpath(locator)
            select_view_sitem.click()
            time.sleep(1)

            delete_views_btn_sitem = self.locator_finder_by_id(self.delete_views_btn_id)
            delete_views_btn_sitem.click()
            time.sleep(1)

            delete_views_confirm_btn_sitem = self.locator_finder_by_xpath(self.delete_views_confirm_btn_id)
            delete_views_confirm_btn_sitem.click()
            time.sleep(1)

            final_delete_confirmation_sitem = self.locator_finder_by_id(self.final_delete_confirmation_id)
            final_delete_confirmation_sitem.click()
            print(f'Selecting {name} for deleting completed \n')
            time.sleep(1)
        except TimeoutException as e:
            print('FAIL: could not delete views properly', e, '\n')
