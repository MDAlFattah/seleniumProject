import time

from selenium.webdriver.common.keys import Keys

from baseSelenium import BaseSelenium


class QueryPage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.selecting_query_page_id = "queries"
        self.query_execution_area = '//*[@id="aqlEditor"]'
        self.profile_query_id = 'profileQuery'
        self.explain_query_id = 'explainQuery'
        self.create_debug_package_id = 'debugQuery'
        self.remove_all_results_id = 'removeResults'
        self.query_spot_light_id = 'querySpotlight'
        self.save_current_query_id = 'saveCurrentQuery'
        self.new_query_name_id = 'new-query-name'
        self.select_query_size_id = 'querySize'
        self.json_to_table_span_it = 'switchTypes'
        self.collection_settings_id = "//*[@id='subNavigationBar']/ul[2]/li[4]/a"
        self.graph_page = 'graphs'
        self.select_create_graph_id = "createGraph"
        self.select_world_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[5]/td[2]/button"
        self.select_example_graph_btn_id = "tab-exampleGraphs"

        self.confirm_delete_graph_id = "modalButton0"
        self.drop_graph_collection = "dropGraphCollections"
        self.select_really_delete_btn_id = "modal-confirm-delete"

        self.select_k_shortest_path_id = "//*[@id='exampleGraphs']/table/tbody/tr[3]/td[2]/button"
        self.select_k_shortest_path_graphs_setting_btn_id = "kShortestPathsGraph_settings"
        self.select_k_shortest_path_graphs_setting_btn_id_check = "kShortestPathsGraph_settings"

    # importing collections for query
    def import_collections(self):
        print("Navigating to Collection page \n")
        # Selecting collections page
        collections = "collections"
        collections = \
            BaseSelenium.locator_finder_by_id(self, collections)
        collections.click()
        time.sleep(1)

        cmd1 = 'cmd /c "arangorestore --server.endpoint tcp://127.0.0.1:8529 --input-directory ' \
               'C:\\Users\\rearf\\Desktop\\collections\\IMDB_DUMP --server.username root --server.password "" ' \
               '--number-of-shards 9 --replication-factor 2"'
        super().command(cmd1)
        time.sleep(1)

        print('Creating a blank collection\n')
        create_collection = "createCollection"
        create_collection = \
            BaseSelenium.locator_finder_by_id(self, create_collection)
        create_collection.click()

        new_collection_name = 'new-collection-name'
        new_collection_name = \
            BaseSelenium.locator_finder_by_id(self, new_collection_name)
        new_collection_name.click()
        super().send_key_action('Characters')

        new_collections_shards = 'new-collection-shards'
        new_collections_shards = \
            BaseSelenium.locator_finder_by_id(self, new_collections_shards)
        new_collections_shards.click()
        super().send_key_action('9')

        new_replication_factor = 'new-replication-factor'
        new_replication_factor = \
            BaseSelenium.locator_finder_by_id(self, new_replication_factor)
        new_replication_factor.click()
        new_replication_factor.clear()
        new_replication_factor.click()
        super().send_key_action('2')

        modalButton1 = 'modalButton1'
        modalButton1 = \
            BaseSelenium.locator_finder_by_id(self, modalButton1)
        modalButton1.click()

        self.driver.refresh()
        time.sleep(5)
        self.driver.back()
        time.sleep(1)

    # Selecting query page
    def selecting_query_page(self):
        query_page = self.selecting_query_page_id
        query_page = \
            BaseSelenium.locator_finder_by_id(self, query_page)
        query_page.click()
        time.sleep(1)

    # Clearing current query area
    def clear_query_area(self):
        super().clear_all_text('//*[@id="aqlEditor"]')
        time.sleep(2)

    def execute_insert_query(self):
        """This method will run an insert query"""

        super().select_query_execution_area()

        super().send_key_action('for i IN 1..10000')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('INSERT {')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('"name": "Ned",')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('"surname": "Stark",')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('"alive": true,')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('"age": 41,')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('"traits": ["A","H","C","N","P"]')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('} INTO Characters')

        super().query_execution_btn()
        super().scroll(1)

        # super().assert_no_error()
        # super().assert_ui_error()
        super().handle_red_bar()

    def execute_read_query(self):
        """This method will run a read query"""
        super().select_query_execution_area()
        self.clear_query_area()

        super().send_key_action('FOR c IN imdb_vertices')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('LIMIT 500')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('RETURN c')

        super().query_execution_btn()
        super().scroll(1)

    # profiling query
    def profile_query(self):
        profile = self.profile_query_id
        profile = \
            BaseSelenium.locator_finder_by_id(self, profile)
        profile.click()
        time.sleep(2)

        super().scroll()

    # explaining a query
    def explain_query(self):
        explainQuery = self.explain_query_id
        explainQuery = \
            BaseSelenium.locator_finder_by_id(self, explainQuery)
        explainQuery.click()
        time.sleep(2)

    # Downloading debug package
    def debug_package_download(self):
        if self.driver.name == "chrome":  # this will check browser name
            print("Download has been disabled for the Chrome browser \n")
        else:
            debug = self.create_debug_package_id
            debug = \
                BaseSelenium.locator_finder_by_id(self, debug)
            debug.click()
            time.sleep(2)
            debug_btn = 'modalButton1'
            debug_btn = \
                BaseSelenium.locator_finder_by_id(self, debug_btn)
            debug_btn.click()
            time.sleep(2)
            # super().clear_download_bar()

    # Removing all query results
    def remove_query_result(self):
        remove_results = self.remove_all_results_id
        remove_results = \
            BaseSelenium.locator_finder_by_id(self, remove_results)
        remove_results.click()
        time.sleep(2)

    # Selecting spot light function helper
    def spot_light_function(self, search):
        spot_light = self.query_spot_light_id
        spot_light = \
            BaseSelenium.locator_finder_by_id(self, spot_light)
        spot_light.click()
        time.sleep(2)

        # searching for COUNT attribute
        super().send_key_action(search)
        super().send_key_action(Keys.DOWN * 5)
        time.sleep(1)

        super().send_key_action(Keys.UP * 3)
        super().send_key_action(Keys.ENTER)
        time.sleep(2)

    # Updating documents
    def update_documents(self):
        print("Navigating to Collection page \n")
        # Selecting collections page
        collections = "collections"
        collections = \
            BaseSelenium.locator_finder_by_id(self, collections)
        collections.click()
        time.sleep(1)

        col_name = '//*[@id="collection_Characters"]/div/h5'
        col_name = \
            BaseSelenium.locator_finder_by_xpath(self, col_name)
        col_name.click()
        time.sleep(1)

        # get key text from the first row
        row_id = "//div[@id='docPureTable']/div[2]/div[1]"
        row_id = \
            BaseSelenium.locator_finder_by_xpath(self, row_id)
        row_id.click()
        time.sleep(1)

        doc_key = 'document-key'
        doc_key = \
            BaseSelenium.locator_finder_by_id(self, doc_key)
        key = doc_key.text
        time.sleep(2)

        # selecting query page
        query_page = self.selecting_query_page_id
        query_page = \
            BaseSelenium.locator_finder_by_id(self, query_page)
        query_page.click()

        time.sleep(1)

        super().select_query_execution_area()

        key_updated = f"UPDATE \"{key}\""

        self.clear_query_area()
        time.sleep(1)

        super().send_key_action(key_updated)
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('WITH {alive: false}')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('IN Characters')

        print("Executing Update query \n")
        super().query_execution_btn()

        super().scroll()

        self.clear_query_area()

        print("Checking update query execution ")
        super().send_key_action('for doc in Characters')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('FILTER doc.alive == false')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('RETURN doc')
        time.sleep(2)

        # selecting execute query button
        super().query_execution_btn()

        time.sleep(3)

        super().scroll()

        if self.driver.name == "chrome":  # this will check browser name
            print("Download has been disabled for the Chrome browser \n")
        else:
            print('Downloading query results \n')
            # downloading query results
            download_query_results = 'downloadQueryResult'
            download_query_results = \
                BaseSelenium.locator_finder_by_id(self, download_query_results)
            download_query_results.click()
            time.sleep(3)

            # super().clear_download_bar()

            print('Downloading query results as CSV format \n')
            # downloading CSV query results
            csv = 'downloadCsvResult'
            csv = \
                BaseSelenium.locator_finder_by_id(self, csv)
            csv.click()
            time.sleep(3)
            # super().clear_download_bar()

    # executing query with bind parameters
    def bind_parameters_query(self):
        # selecting query execution area
        super().select_query_execution_area()

        # clear the execution area
        self.clear_query_area()

        bind_alive = '//*[@id="arangoBindParamTable"]/tbody/tr[1]/td[2]/input'
        bind_name = '//*[@id="arangoBindParamTable"]/tbody/tr[2]/td[2]/input'

        super().send_key_action('FOR doc IN Characters')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('FILTER doc.alive == @alive && doc.name == @name')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('RETURN doc')
        time.sleep(2)

        bind_query = \
            BaseSelenium.locator_finder_by_xpath(self, bind_alive)
        bind_query.click()
        super().send_key_action('false')

        bind_alive = \
            BaseSelenium.locator_finder_by_xpath(self, bind_name)
        bind_alive.click()
        super().send_key_action('Ned')

        # execute query with bind parameters
        super().query_execution_btn()

        super().scroll()

        json = self.json_to_table_span_it
        table = self.json_to_table_span_it

        print('Changing execution format JSON format to Table format\n')
        json = \
            BaseSelenium.locator_finder_by_id(self, json)
        json.click()
        time.sleep(3)

        print('Changing execution format Table format to JSON format\n')
        table = \
            BaseSelenium.locator_finder_by_id(self, table)
        table.click()
        time.sleep(3)

        # fixme bug found https://arangodb.atlassian.net/browse/BTS-559
        # print('Switch output to JSON format \n')
        # output_switch_json = 'json-switch'
        # output_switch_json = \
        #     BaseSelenium.locator_finder_by_id(self, output_switch_json)
        # output_switch_json.click()
        # time.sleep(3)

        # print('Switch output to Table format \n')
        # output_switch_table = 'table-switch'
        # output_switch_table = \
        #     BaseSelenium.locator_finder_by_id(self, output_switch_table)
        # output_switch_table.click()
        # time.sleep(3)

        # clear the execution area
        self.clear_query_area()

    # importing new queries
    def import_queries(self, path):
        toggle_query = 'toggleQueries1'
        toggle_query = \
            BaseSelenium.locator_finder_by_id(self, toggle_query)
        toggle_query.click()
        time.sleep(1)

        print('Importing query started \n')
        # import query
        imp_query = 'importQuery'
        imp_query = \
            BaseSelenium.locator_finder_by_id(self, imp_query)
        imp_query.click()
        time.sleep(1)

        imp_queries = 'importQueries'
        imp_queries = \
            BaseSelenium.locator_finder_by_id(self, imp_queries)
        time.sleep(2)
        imp_queries.send_keys(path)
        time.sleep(2)

        # confirm importing queries
        confirm_query = 'confirmQueryImport'
        confirm_query = \
            BaseSelenium.locator_finder_by_id(self, confirm_query)
        confirm_query.click()
        time.sleep(1)
        print('Importing query completed \n')

        print("Checking imported query \n")
        run_query = 'runQuery'
        run_query = \
            BaseSelenium.locator_finder_by_id(self, run_query)
        run_query.click()
        time.sleep(3)

        if self.driver.name == "chrome":  # this will check browser name
            print("Download has been disabled for the Chrome browser \n")
        else:
            print('Exporting newly imported query\n')
            select_imp_query = '//*[@id="arangoMyQueriesTable"]/tbody/tr[1]/td[1]'
            select_imp_query = \
                BaseSelenium.locator_finder_by_xpath(self, select_imp_query)
            select_imp_query.click()
            time.sleep(1)

            export_query = 'exportQuery'
            export_query = \
                BaseSelenium.locator_finder_by_id(self, export_query)
            export_query.click()
            time.sleep(3)

            # super().clear_download_bar()
        time.sleep(5)

        print('Deleting imported query \n')
        query = '//*[@id="arangoMyQueriesTable"]/tbody/tr[1]/td[1]'
        query = \
            BaseSelenium.locator_finder_by_xpath(self, query)
        query.click()
        time.sleep(1)

        delete_query = 'deleteQuery'
        delete_query = \
            BaseSelenium.locator_finder_by_id(self, delete_query)
        delete_query.click()
        time.sleep(1)

        Del_btn = 'modalButton1'
        Del_btn = \
            BaseSelenium.locator_finder_by_id(self, Del_btn)
        Del_btn.click()
        time.sleep(1)

        del_confirm_btn = 'modal-confirm-delete'
        del_confirm_btn = \
            BaseSelenium.locator_finder_by_id(self, del_confirm_btn)
        del_confirm_btn.click()
        time.sleep(1)

        print('Return back to query execution area \n')
        editor_btn = '//*[@id="subNavigationBar"]/ul[2]/li[1]'
        editor_btn = \
            BaseSelenium.locator_finder_by_xpath(self, editor_btn)
        editor_btn.click()
        time.sleep(1)

    # saving custom query and check slow query
    def custom_query(self):
        self.clear_query_area()

        print("Executing Custom query\n")
        super().send_key_action('return sleep(10)')

        save_query = self.save_current_query_id
        save_query = \
            BaseSelenium.locator_finder_by_id(self, save_query)
        save_query.click()

        query_name = self.new_query_name_id
        query_name = \
            BaseSelenium.locator_finder_by_id(self, query_name)
        query_name.click()
        super().send_key_action('Custom query')

        btn = 'modalButton1'
        btn = \
            BaseSelenium.locator_finder_by_id(self, btn)
        btn.click()

        # cleaning current query area
        self.clear_query_area()

        # checking saved query
        saved_query = 'toggleQueries1'
        saved_query = \
            BaseSelenium.locator_finder_by_id(self, saved_query)
        saved_query.click()

        print('Checking custom query in action \n')
        explain_query = "explQuery"
        explain_query = \
            BaseSelenium.locator_finder_by_id(self, explain_query)
        explain_query.click()
        time.sleep(2)

        print('Clearing query results\n')
        remove = self.remove_all_results_id
        remove = \
            BaseSelenium.locator_finder_by_id(self, remove)
        remove.click()
        time.sleep(2)

        print("Running query from saved query\n")
        run_query = 'runQuery'
        run_query = \
            BaseSelenium.locator_finder_by_id(self, run_query)
        run_query.click()
        time.sleep(2)

        print('Copying query from saved query\n')
        copy_query = 'copyQuery'
        copy_query = \
            BaseSelenium.locator_finder_by_id(self, copy_query)
        copy_query.click()
        time.sleep(2)

        self.clear_query_area()

        print('Checking running query tab\n')
        slow_query = '//*[@id="subNavigationBar"]/ul[2]/li[2]/a'
        slow_query = \
            BaseSelenium.locator_finder_by_xpath(self, slow_query)
        slow_query.click()
        time.sleep(2)

        print('Checking slow query history \n')
        slow_query_history = '//*[@id="subNavigationBar"]/ul[2]/li[3]/a'
        slow_query_history = \
            BaseSelenium.locator_finder_by_xpath(self, slow_query_history)
        slow_query_history.click()
        time.sleep(5)

        print('Deleting slow query history \n')
        del_slow_query_history = 'deleteSlowQueryHistory'
        del_slow_query_history = \
            BaseSelenium.locator_finder_by_id(self, del_slow_query_history)
        del_slow_query_history.click()
        time.sleep(1)

        del_btn = 'modalButton1'
        del_btn = \
            BaseSelenium.locator_finder_by_id(self, del_btn)
        del_btn.click()
        time.sleep(2)

        confirm_del_btn = 'modal-confirm-delete'
        confirm_del_btn = \
            BaseSelenium.locator_finder_by_id(self, confirm_del_btn)
        confirm_del_btn.click()
        time.sleep(2)

        self.driver.refresh()

        # return back to saved query
        saved_query_01 = 'toggleQueries1'
        saved_query_01 = \
            BaseSelenium.locator_finder_by_id(self, saved_query_01)
        saved_query_01.click()
        time.sleep(2)

        print('Deleting Saved query\n')
        delete_query = 'deleteQuery'
        delete_query = \
            BaseSelenium.locator_finder_by_id(self, delete_query)
        delete_query.click()
        time.sleep(1)
        Del_btn = 'modalButton1'
        Del_btn = \
            BaseSelenium.locator_finder_by_id(self, Del_btn)
        Del_btn.click()
        time.sleep(1)

        del_confirm_btn = 'modal-confirm-delete'
        del_confirm_btn = \
            BaseSelenium.locator_finder_by_id(self, del_confirm_btn)
        del_confirm_btn.click()
        time.sleep(1)

        toggle_queries = 'toggleQueries2'
        toggle_queries = \
            BaseSelenium.locator_finder_by_id(self, toggle_queries)
        toggle_queries.click()
        time.sleep(1)
        print('Deleting Saved query completed\n')
        self.clear_query_area()

    # Graph query
    def world_country_graph_query(self):
        print('Creating worldCountry example graph \n')
        graph = self.graph_page
        graph = \
            BaseSelenium.locator_finder_by_id(self, graph)
        graph.click()
        time.sleep(2)

        select_graph = self.select_create_graph_id
        select_graph = \
            BaseSelenium.locator_finder_by_id(self, select_graph)
        select_graph.click()
        time.sleep(1)

        # Selecting example graph button
        example = self.select_example_graph_btn_id
        example = \
            BaseSelenium.locator_finder_by_id(self, example)
        example.click()
        time.sleep(1)

        # select worldCountry graph
        self.select_world_graph_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_world_graph_id)
        self.select_world_graph_id.click()
        time.sleep(4)

        # navigating back to query tab
        query = self.selecting_query_page_id
        query = \
            BaseSelenium.locator_finder_by_id(self, query)
        query.click()
        time.sleep(1)

        super().clear_all_text(self.query_execution_area)

        print('Executing sample graph query for worldCountry Graph \n')
        super().send_key_action('FOR v, e, p IN 1..1')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('ANY "worldVertices/continent-south-america"')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('GRAPH "worldCountry"')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('RETURN {v, e, p}')

        time.sleep(2)

        super().query_execution_btn()

        super().scroll()

        print('Deleting worldCountry graph \n')
        graph_id = "worldCountry_settings"
        self.delete_all_graph(graph_id)
        self.driver.refresh()

    # K Shortest Paths Graph Query
    def k_shortest_paths_graph_query(self):
        print('Creating KShortestPaths example graph \n')
        graph = self.graph_page
        graph = \
            BaseSelenium.locator_finder_by_id(self, graph)
        graph.click()
        time.sleep(2)

        select_graph = self.select_create_graph_id
        select_graph = \
            BaseSelenium.locator_finder_by_id(self, select_graph)
        select_graph.click()
        time.sleep(1)

        # Selecting example graph button
        graph_example_id = self.select_example_graph_btn_id
        graph_example_id = \
            BaseSelenium.locator_finder_by_id(self, graph_example_id)
        graph_example_id.click()
        time.sleep(1)

        # selecting kshortestpaths graph from example graph
        self.select_k_shortest_path_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_k_shortest_path_id)
        self.select_k_shortest_path_id.click()
        time.sleep(1)

        # navigating back to query tab
        query = self.selecting_query_page_id
        query = \
            BaseSelenium.locator_finder_by_id(self, query)
        query.click()
        time.sleep(1)

        super().clear_all_text(self.query_execution_area)

        print('Executing sample graph query for KShortestPaths Graph')
        super().send_key_action('FOR path IN OUTBOUND K_SHORTEST_PATHS')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('"places/Birmingham" TO "places/StAndrews"')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('GRAPH "kShortestPathsGraph"')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('LIMIT 4')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('RETURN path')
        time.sleep(2)

        super().query_execution_btn()
        time.sleep(3)

        super().scroll(1)
        time.sleep(8)

        # print('Switch output to JSON format')
        # output_switch_json = 'json-switch'
        # output_switch_json = \
        #     BaseSelenium.locator_finder_by_id(self, output_switch_json)
        # output_switch_json.click()

        # super().select_query_execution_area()
        #
        # super().scroll(1)
        # time.sleep(3)

        # print('Switch output to Graph')
        # output_switch_graph = 'graph-switch'
        # output_switch_graph = \
        #     BaseSelenium.locator_finder_by_id(self, output_switch_graph)
        # output_switch_graph.click()

        # super().query_execution_btn()
        #
        # super().scroll(1)
        # time.sleep(3)

        # print('Observe current query on Graph viewer \n')
        # graph_page_btn = 'copy2gV'
        # graph_page_btn = \
        #     BaseSelenium.locator_finder_by_id(self, graph_page_btn)
        # graph_page_btn.click()
        # time.sleep(5)
        #
        # print('Navigate back to query page\n')
        # query_page = self.selecting_query_page_id
        # query_page = \
        #     BaseSelenium.locator_finder_by_id(self, query_page)
        # query_page.click()
        # time.sleep(2)

        print('Clear query execution area \n')
        super().clear_all_text(self.query_execution_area)

        print('Executing one more KShortestPaths graph query \n')
        super().send_key_action('FOR v, e IN OUTBOUND SHORTEST_PATH "places/Aberdeen" TO "places/London"')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('GRAPH "kShortestPathsGraph"')
        super().send_key_action(Keys.ENTER)
        super().send_key_action('RETURN { place: v.label, travelTime: e.travelTime }')
        time.sleep(2)

        super().query_execution_btn()

        super().scroll()

        print('Deleting KShortestPath graph \n')
        graph_id = "kShortestPathsGraph_settings"
        self.delete_all_graph(graph_id)
        self.driver.refresh()

    # Example City Graph
    def city_graph(self):
        print('Creating example City Graph \n')
        graph = self.graph_page
        graph = \
            BaseSelenium.locator_finder_by_id(self, graph)
        graph.click()
        time.sleep(2)

        select_graph = self.select_create_graph_id
        select_graph = \
            BaseSelenium.locator_finder_by_id(self, select_graph)
        select_graph.click()
        time.sleep(1)

        # Selecting example graph button
        graph_example_id = self.select_example_graph_btn_id
        graph_example_id = \
            BaseSelenium.locator_finder_by_id(self, graph_example_id)
        graph_example_id.click()
        time.sleep(1)

        # selecting City Graph from example
        route_planner = '//*[@id="exampleGraphs"]/table/tbody/tr[7]/td[2]/button'
        route_planner = \
            BaseSelenium.locator_finder_by_xpath(self, route_planner)
        route_planner.click()
        time.sleep(4)

        # navigating back to query tab
        query = self.selecting_query_page_id
        query = \
            BaseSelenium.locator_finder_by_id(self, query)
        query.click()
        time.sleep(1)

        super().clear_all_text(self.query_execution_area)

        super().send_key_action('for u in germanCity return u')
        time.sleep(1)

        # execute query
        super().query_execution_btn()

        super().scroll()

        time.sleep(1)

        # print('Switch output to JSON format')
        # output_switch_json = 'json-switch'
        # output_switch_json = \
        #     BaseSelenium.locator_finder_by_id(self, output_switch_json)
        # output_switch_json.click()
        #
        # super().select_query_execution_area()
        # super().scroll(1)
        #
        # print('Switch output to Table format')
        # output_switch_table = 'table-switch'
        # output_switch_table = \
        #     BaseSelenium.locator_finder_by_id(self, output_switch_table)
        # output_switch_table.click()
        #
        # super().select_query_execution_area()
        # super().scroll(1)

        print('Deleting City graph \n')
        graph_id = "routeplanner_settings"
        self.delete_all_graph(graph_id)
        self.driver.refresh()

    # changing the number of output
    def number_of_results(self):
        super().select_query_execution_area()
        time.sleep(1)

        print('Changing query results size 1000 to 100 \n')
        query_size = self.select_query_size_id
        BaseSelenium.locator_finder_by_select(self, query_size, 0)
        time.sleep(1)

        super().select_query_execution_area()
        time.sleep(1)

        print('Execute sample query\n')
        # self.query('FOR c IN imdb_vertices\n\tLIMIT 500\nRETURN c')
        super().send_key_action('FOR c IN imdb_vertices')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('LIMIT 500')
        super().send_key_action(Keys.ENTER)
        super().send_key_action(Keys.TAB)
        super().send_key_action('RETURN c')
        time.sleep(2)

        super().query_execution_btn()

        super().scroll()

        self.driver.refresh()

    # Deleting Collection using any collections locator id
    def delete_collection(self, collection):
        collection = \
            BaseSelenium.locator_finder_by_xpath(self, collection)
        collection.click()
        settings = self.collection_settings_id
        settings = \
            BaseSelenium.locator_finder_by_xpath(self, settings)
        settings.click()

        delete_collection_id = "//*[@id='modalButton0']"
        delete_collection_id = \
            BaseSelenium.locator_finder_by_xpath(self, delete_collection_id)
        delete_collection_id.click()
        time.sleep(2)

        delete_collection_confirm_id = "//*[@id='modal-confirm-delete']"
        delete_collection_confirm_id = \
            BaseSelenium.locator_finder_by_xpath(self, delete_collection_confirm_id)
        delete_collection_confirm_id.click()

    # deleting all the collections
    def delete_all_collections(self):
        collection_page = 'collections'
        collection_page = \
            BaseSelenium.locator_finder_by_id(self, collection_page)
        collection_page.click()
        time.sleep(2)

        print('deleting Characters collections \n')
        characters = '//*[@id="collection_Characters"]/div/h5'
        self.delete_collection(characters)

        print('deleting imdb_edges collections \n')
        imdb_edges = '//*[@id="collection_imdb_edges"]/div/h5'
        self.delete_collection(imdb_edges)

        print('deleting imdb_vertices collections \n')
        imdb_edges = '//*[@id="collection_imdb_vertices"]/div/h5'
        self.delete_collection(imdb_edges)

    # deleting any graphs with given graph id
    def delete_all_graph(self, graph_id):
        print('Navigating back to graph page \n')
        graph = self.graph_page
        graph = \
            BaseSelenium.locator_finder_by_id(self, graph)
        graph.click()
        time.sleep(2)

        graphs_setting_btn_id = \
            BaseSelenium.locator_finder_by_id(self, graph_id)
        graphs_setting_btn_id.click()
        time.sleep(1)

        confirm = self.confirm_delete_graph_id
        confirm = \
            BaseSelenium.locator_finder_by_id(self, confirm)
        confirm.click()
        time.sleep(1)

        drop = self.drop_graph_collection
        drop = \
            BaseSelenium.locator_finder_by_id(self, drop)
        drop.click()
        time.sleep(1)

        really = self.select_really_delete_btn_id
        really = \
            BaseSelenium.locator_finder_by_id(self, really)
        really.click()
        time.sleep(3)

        # navigate back to query page
        query_page = self.selecting_query_page_id
        query_page = \
            BaseSelenium.locator_finder_by_id(self, query_page)
        query_page.click()
        time.sleep(3)

        # selecting query execution area
        super().select_query_execution_area()

        # clearing all text from the execution area
        super().clear_all_text(self.query_execution_area)
