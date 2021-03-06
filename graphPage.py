import time
from selenium.webdriver.common.keys import Keys
from baseSelenium import BaseSelenium


class GraphPage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.select_graph_page_id = "graphs"
        self.select_create_graph_id = "createGraph"
        self.select_example_graph_btn_id = "tab-exampleGraphs"
        self.select_knows_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[1]/td[2]/button"
        self.select_traversal_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[2]/td[2]/button"
        self.select_k_shortest_path_id = "//*[@id='exampleGraphs']/table/tbody/tr[3]/td[2]/button"
        self.select_maps_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[4]/td[2]/button"
        self.select_world_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[5]/td[2]/button"
        self.select_social_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[6]/td[2]/button"
        self.select_city_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[7]/td[2]/button"
        self.select_connected_component_graph_id = "//*[@id='exampleGraphs']/table/tbody/tr[8]/td[2]/button"

        self.select_knows_graphs_setting_btn_id = "knows_graph_settings"
        self.select_knows_graphs_setting_btn_id_check = "knows_graph_settings"

        self.select_traversal_graphs_setting_btn_id = "traversalGraph_settings"
        self.select_traversal_graphs_setting_btn_id_check = "traversalGraph_settings"

        self.select_k_shortest_path_graphs_setting_btn_id = "kShortestPathsGraph_settings"
        self.select_k_shortest_path_graphs_setting_btn_id_check = "kShortestPathsGraph_settings"

        self.select_maps_graphs_setting_btn_id = "mps_graph_settings"
        self.select_maps_graphs_setting_btn_id_check = "mps_graph_settings"

        self.select_world_graphs_setting_btn_id = "worldCountry_settings"
        self.select_world_graphs_setting_btn_id_check = "worldCountry_settings"

        self.select_social_graphs_setting_btn_id = "social_settings"
        self.select_social_graphs_setting_btn_id_check = "social_settings"

        self.select_route_planner_graphs_setting_btn_id = "routeplanner_settings"
        self.select_route_planner_graphs_setting_btn_id_check = "routeplanner_settings"

        self.select_connected_graphs_setting_btn_id = "connectedComponentsGraph_settings"

        self.select_knows_graph_manual_id = "knows_graph_manual_settings"

        self.confirm_delete_graph_id = "modalButton0"
        self.delete_with_collection_id = "dropGraphCollections"
        self.select_really_delete_btn_id = "modal-confirm-delete"

        self.select_collection_page_id = "collections"
        self.select_graph_cancel_btn_id = "modalButton3"

        self.select_search_id = "searchInput"

        self.knows_graph_id = "knows_graph_tile"
        self.select_share_id = "//*[@id='loadFullGraph']/span/i"
        self.select_load_full_graph_id = "modalButton1"
        self.select_camera_download_icon = "//*[@id='downloadPNG']/span/i"
        self.select_full_screen_btn_id = "//*[@id='graph-fullscreen-btn']/span/i"

        self.configure_graph_settings_id = "settingsMenu"
        self.select_graph_layout_option_id = "g_layout"
        self.select_renderer_id = "g_renderer"
        self.select_depth_id = "//*[@id='g_depth']"
        self.select_limit_id = "//*[@id='g_limit']"
        self.add_collection_name_id = "g_nodeLabelByCollection"
        self.select_color_collection_id = "g_nodeColorByCollection"
        self.select_size_by_edges_id = "g_nodeSizeByEdges"
        self.select_add_edge_col_name_id = "g_edgeLabelByCollection"
        self.select_color_node_by_edge_id = "g_edgeColorByCollection"
        self.select_edge_type_id = "g_edgeType"
        self.select_restore_settings_id = "/html//button[@id='restoreGraphSettings']"
        self.select_tooltips_id = "//*[@id='graphSettingsView']/div/div[2]/div[1]/div[5]/i"

        self.select_sort_settings_id = "graphManagementToggle"
        self.select_sort_descend_id = "//*[@id='graphManagementDropdown']/ul/li[2]/a/label/i"
        self.select_resume_layout_btn_id = "//*[@id='toggleForce']/i"

        self.create_new_collection_id = "createCollection"
        self.new_collection_name_id = "new-collection-name"
        self.save_collection_btn_id = "//*[@id='modalButton1']"
        self.select_upload_btn_id = "/html//a[@id='importCollection']"
        self.select_choose_file_btn_id = "/html//input[@id='importDocuments']"
        self.select_confirm_upload_btn_id = "confirmDocImport"

        self.select_new_graph_name_id = "createNewGraphName"

    # creating graph manually
    def create_manual_graph(self):
        collectionPage = self.select_collection_page_id
        collectionPage = \
            BaseSelenium.locator_finder_by_id(self, collectionPage)
        collectionPage.click()

        # first collection for the knows_graph_manual begins
        col1 = self.create_new_collection_id
        col1_name = self.new_collection_name_id
        col1_save = self.save_collection_btn_id
        col1_select = "//*[@id='collection_knows_edge']/div/h5"
        col1_edge_id = "new-collection-type"
        col1_upload = self.select_upload_btn_id
        col1_file = self.select_choose_file_btn_id
        col1_import = self.select_confirm_upload_btn_id
        path1 = 'C:\\Users\\rearf\\Desktop\\collections\\knows_edge.json'

        print("Creating knows_edge collections for knows_graph_manual Graph\n")
        col1 = \
            BaseSelenium.locator_finder_by_id(self, col1)
        col1.click()

        col1_name = \
            BaseSelenium.locator_finder_by_id(self, col1_name)
        col1_name.click()
        super().send_key_action("knows_edge")

        BaseSelenium.locator_finder_by_select(self, col1_edge_id, 1)

        col1_save = \
            BaseSelenium.locator_finder_by_xpath(self, col1_save)
        col1_save.click()

        col1_select = \
            BaseSelenium.locator_finder_by_xpath(self, col1_select)
        col1_select.click()

        # selecting collection upload btn
        col1_upload = \
            BaseSelenium.locator_finder_by_xpath(self, col1_upload)
        col1_upload.click()
        time.sleep(3)

        # This method will upload the file with the file path given
        col1_file = \
            BaseSelenium.locator_finder_by_xpath(self, col1_file)
        time.sleep(2)
        col1_file.send_keys(path1)

        print("Importing knows_edge.json to the collection\n")
        col1_import = \
            BaseSelenium.locator_finder_by_id(self, col1_import)
        col1_import.click()
        time.sleep(2)
        print("Importing knows_edge.json to the collection completed\n")

        self.driver.back()

        # second collection for the knows_graph_manual begins
        col2 = self.create_new_collection_id
        col2_name = self.new_collection_name_id
        col2_save = self.save_collection_btn_id
        col2_select = "//*[@id='collection_persons']/div/h5"
        col2_upload = self.select_upload_btn_id
        col2_file = self.select_choose_file_btn_id
        col2_import = self.select_confirm_upload_btn_id
        path2 = 'C:\\Users\\rearf\\Desktop\\collections\\persons.json'

        print("Creating person_vertices collections for knows_graph_manual Graph\n")
        col2 = \
            BaseSelenium.locator_finder_by_id(self, col2)
        col2.click()

        col2_name = \
            BaseSelenium.locator_finder_by_id(self, col2_name)
        col2_name.click()
        col2_name.send_keys("persons")

        col2_save = \
            BaseSelenium.locator_finder_by_xpath(self, col2_save)
        col2_save.click()

        col2_select = \
            BaseSelenium.locator_finder_by_xpath(self, col2_select)
        col2_select.click()

        # selecting collection upload btn
        col2_upload = \
            BaseSelenium.locator_finder_by_xpath(self, col2_upload)
        col2_upload.click()
        time.sleep(3)

        # This method will upload the file with the file path given
        col2_file = \
            BaseSelenium.locator_finder_by_xpath(self, col2_file)
        time.sleep(2)
        col2_file.send_keys(path2)

        print("Importing person_vertices.json to the collection\n")
        col2_import = \
            BaseSelenium.locator_finder_by_id(self, col2_import)
        col2_import.click()
        time.sleep(3)
        print("Importing person_vertices.json to the collection completed\n")

    # selecting Graph tab
    def select_graph_page(self):
        self.select_graph_page_id = \
            BaseSelenium.locator_finder_by_id(self, self.select_graph_page_id)
        self.select_graph_page_id.click()

    # adding knows_graph_manual graph
    def adding_knows_manual_graph(self):
        select_graph_id = self.select_create_graph_id
        select_graph_id = \
            BaseSelenium.locator_finder_by_id(self, select_graph_id)
        select_graph_id.click()

        # list of id's for manual graph
        new_graph = self.select_new_graph_name_id
        # edge_definition = "row_newEdgeDefinitions0"
        # from_collection = "s2id_fromCollections0"
        # to_collection = "s2id_toCollections0"
        # create_btn_id = "modalButton1"
        # knows_graph_id = '//*[@id="knows_graph_manual_tile"]/div/h5'

        new_graph = BaseSelenium.locator_finder_by_id(self, new_graph)
        new_graph.click()
        new_graph.clear()
        new_graph.send_keys("knows_graph_manual")

        if self.deployment == 3:
            shard = 'general-numberOfShards'  # define number of shards for the graph
            replication_factor = 'general-replicationFactor'
            write_concern = 'general-writeConcern'
            # defining number of shard, replication and write concern
            shard = BaseSelenium.locator_finder_by_id(self, shard)
            shard.click()
            shard.send_keys('9')

            replication_factor = BaseSelenium.locator_finder_by_id(self, replication_factor)
            replication_factor.click()
            replication_factor.send_keys('3')

            write_concern = BaseSelenium.locator_finder_by_id(self, write_concern)
            write_concern.click()
            write_concern.send_keys('3')
        else:
            print("Manual graph creation is not in Cluster mode. \n")

        edge_definition = 'row_newEdgeDefinitions0'
        edge_text = '//*[@id="s2id_autogen21"]'

        # selecting edge definition from auto suggestion
        edge_definition = \
            BaseSelenium.locator_finder_by_id(self, edge_definition)
        edge_definition.click()
        print('displayed: ', edge_definition.is_displayed())

        time.sleep(2)

        edge_text = BaseSelenium.locator_finder_by_xpath(self, edge_text)
        # print('displayed: ', edge_definition.is_displayed())
        edge_text.click()
        edge_text.send_keys('1')

        # self.driver.execute_script("arguments[0].click();", username)
        # edge_definition.send_keys('aa')
        # super().send_key_action(Keys.ENTER)

        time.sleep(2)
        # edge_text = BaseSelenium.locator_finder_by_id(self, edge_text)
        # print('displayed: ', edge_text.is_displayed())
        #
        # self.driver.execute("document.getElementById('s2id_newEdgeDefinitions0').value='testuser'")

        # edge_text.click()
        # edge_text.send_keys('fattah')
        # super().send_key_action(Keys.ENTER)

        # # selecting from collection from auto suggestion
        # from_collection = \
        #     BaseSelenium.locator_finder_by_id(self, from_collection)
        # from_collection.click()
        # super().send_key_action(Keys.ENTER)
        #
        # time.sleep(1)
        #
        # # selecting to collection from auto suggestion
        # to_collection = \
        #     BaseSelenium.locator_finder_by_id(self, to_collection)
        # to_collection.click()
        # super().send_key_action(Keys.ENTER)
        #
        # time.sleep(1)
        #
        # # selecting create graph btn
        # create_btn_id = \
        #     BaseSelenium.locator_finder_by_id(self, create_btn_id)
        # create_btn_id.click()
        #
        # time.sleep(2)
        #
        # # selecting newly created graph btn
        # knows_graph_id = \
        #     BaseSelenium.locator_finder_by_xpath(self, knows_graph_id)
        # knows_graph_id.click()
        #
        # time.sleep(3)
        # self.driver.back()

    # creating satellite graph
    def adding_satellite_graph(self):
        if super().current_package_version() >= 3.8:
            self.select_graph_page()
            select_graph_id = self.select_create_graph_id
            select_graph_id = \
                BaseSelenium.locator_finder_by_id(self, select_graph_id)
            select_graph_id.click()

            # list of id's for satellite graph
            select_satellite = 'tab-satelliteGraph'
            new_graph = self.select_new_graph_name_id
            edge_definition = "s2id_newEdgeDefinitions0"
            from_collection = "s2id_fromCollections0"
            to_collection = "s2id_toCollections0"
            create_btn_id = "modalButton1"

            # selecting satellite graph tab
            select_satellite = \
                BaseSelenium.locator_finder_by_id(self, select_satellite)
            select_satellite.click()

            new_graph = \
                BaseSelenium.locator_finder_by_id(self, new_graph)
            new_graph.click()
            new_graph.clear()
            super().send_key_action("satellite_graph")

            # selecting edge definition from auto suggestion
            edge_definition = \
                BaseSelenium.locator_finder_by_id(self, edge_definition)
            edge_definition.click()

            super().send_key_action('knows_edge')
            super().send_key_action(Keys.ENTER)
            # selecting from collection from auto suggestion
            from_collection = \
                BaseSelenium.locator_finder_by_id(self, from_collection)
            from_collection.click()

            super().send_key_action('persons')
            super().send_key_action(Keys.ENTER)

            time.sleep(1)

            # selecting to collection from auto suggestion
            to_collection = \
                BaseSelenium.locator_finder_by_id(self, to_collection)
            to_collection.click()

            super().send_key_action('persons')
            super().send_key_action(Keys.ENTER)

            time.sleep(1)

            # selecting create graph btn
            create_btn_id = \
                BaseSelenium.locator_finder_by_id(self, create_btn_id)
            create_btn_id.click()

            time.sleep(2)

            # importing collections using arangoimport
            print("Importing knows_edge collections \n")
            cmd_for_knows_edge = 'cmd /c "arangoimp --file C:\\Users\\rearf\Desktop\\collections\\knows_edge.json ' \
                                 '--collection "knows_edge" --type=json --server.username root --server.password "" ' \
                                 '--server.endpoint tcp://127.0.0.1:8529 --to-collection-prefix profiles_smart' \
                                 ' --from-collection-prefix profiles_smart"'
            super().command(cmd_for_knows_edge)

            time.sleep(1)

            print("Importing persons collections \n")
            cmd_for_persons = 'cmd /c "arangoimp --file C:\\Users\\rearf\\Desktop\\collections\\persons.json ' \
                              '--collection "persons" --type=json --server.username root --server.password ""' \
                              ' --server.endpoint tcp://127.0.0.1:8529"'
            super().command(cmd_for_persons)

            time.sleep(1)

            # Selecting satellite graph settings to view and delete
            satellite_settings_id = '//*[@id="satellite_graph_tile"]/div/h5'
            satellite_settings_id = \
                BaseSelenium.locator_finder_by_xpath(self, satellite_settings_id)
            satellite_settings_id.click()

            time.sleep(5)
            self.driver.back()
            time.sleep(1)

            print("\n")
            print("Smart Graph deleting started \n")
            satellite_settings_id = 'satellite_graph_settings'
            satellite_settings_id = BaseSelenium.locator_finder_by_id(self, satellite_settings_id)
            satellite_settings_id.click()

            delete_btn = 'modalButton0'
            delete_btn = BaseSelenium.locator_finder_by_id(self, delete_btn)
            delete_btn.click()

            delete_check_id = 'dropGraphCollections'
            delete_check_id = BaseSelenium.locator_finder_by_id(self, delete_check_id)
            delete_check_id.click()

            delete_confirm_btn = 'modal-confirm-delete'
            delete_confirm_btn = BaseSelenium.locator_finder_by_id(self, delete_confirm_btn)
            delete_confirm_btn.click()

            time.sleep(2)
            print("Satellite Graph deleted successfully \n")
            self.driver.refresh()

        else:
            print('Satellite Graph is not supported for the current package \n')

    def adding_smart_graph(self, disjointgraph=False):

        if super().current_package_version() >= 3.6 and disjointgraph is False:
            select_graph_id = self.select_create_graph_id
            select_graph_id = \
                BaseSelenium.locator_finder_by_id(self, select_graph_id)
            select_graph_id.click()

            # list of id's for smart graph
            select_smart = 'tab-smartGraph'
            new_graph = self.select_new_graph_name_id
            shard = 'new-numberOfShards'
            replication = 'new-replicationFactor'
            write_concern = 'new-writeConcern'
            disjoint = 'new-isDisjoint'
            smart_attribute = "new-smartGraphAttribute"

            edge_definition = "s2id_newEdgeDefinitions0"
            from_collection = "s2id_fromCollections0"
            to_collection = "s2id_toCollections0"
            create_btn_id = "modalButton1"

            # selecting smart graph tab
            select_smart = \
                BaseSelenium.locator_finder_by_id(self, select_smart)
            select_smart.click()

            new_graph = \
                BaseSelenium.locator_finder_by_id(self, new_graph)
            new_graph.click()
            new_graph.clear()
            new_graph.send_keys("smart_graph")

            # specifying number of shards
            shard = \
                BaseSelenium.locator_finder_by_id(self, shard)
            shard.click()
            shard.send_keys('3')
            time.sleep(1)

            # specifying replication of shards
            replication = \
                BaseSelenium.locator_finder_by_id(self, replication)
            replication.click()
            replication.send_keys('3')
            time.sleep(1)

            # specifying write concern of shards
            write_concern = \
                BaseSelenium.locator_finder_by_id(self, write_concern)
            write_concern.click()
            write_concern.send_keys('1')
            time.sleep(1)

            # specifying write disjoint graphs
            if disjointgraph:
                disjoint = \
                    BaseSelenium.locator_finder_by_id(self, disjoint)
                disjoint.click()
            else:
                print('Disjoint Graph not selected. \n')
            time.sleep(1)

            # specifying write concern of shards
            smart_attribute = \
                BaseSelenium.locator_finder_by_id(self, smart_attribute)
            smart_attribute.click()
            smart_attribute.send_keys('community')
            time.sleep(1)

            # scrolling down
            super().scroll(1)
            time.sleep(2)

            # selecting edge definition from auto suggestion
            edge_definition = \
                BaseSelenium.locator_finder_by_id(self, edge_definition)
            edge_definition.click()
            time.sleep(1)

            super().send_key_action('relations')
            super().send_key_action(Keys.ENTER)

            # selecting from collection from auto suggestion
            from_collection = \
                BaseSelenium.locator_finder_by_id(self, from_collection)
            from_collection.click()

            super().send_key_action('profiles')
            super().send_key_action(Keys.ENTER)

            time.sleep(1)

            # selecting to collection from auto suggestion
            to_collection = \
                BaseSelenium.locator_finder_by_id(self, to_collection)
            to_collection.click()
            super().send_key_action('profiles')
            super().send_key_action(Keys.ENTER)

            time.sleep(1)

            # selecting create graph btn
            create_btn_id = \
                BaseSelenium.locator_finder_by_id(self, create_btn_id)
            create_btn_id.click()
            time.sleep(2)

            print("Importing profile collections \n")
            cmd_for_profile = 'cmd /c "arangoimp --file C:\\Users\\rearf\\Desktop\\collections\\profiles.jsonl ' \
                              '--collection "profiles" --type=jsonl --server.username root --server.password ""' \
                              ' --server.endpoint tcp://127.0.0.1:8529"'
            super().command(cmd_for_profile)

            time.sleep(1)

            print("Importing relations collections \n")
            cmd_for_relation = 'cmd /c "arangoimp --file C:\\Users\\rearf\Desktop\\collections\\relations.jsonl ' \
                               '--collection "relations" --type=json --server.username root --server.password "" ' \
                               '--server.endpoint tcp://127.0.0.1:8529 --to-collection-prefix profiles_smart' \
                               ' --from-collection-prefix profiles_smart"'
            super().command(cmd_for_relation)

            time.sleep(1)

            # opening smart graph
            smart_graph = 'smart_graph_tile'
            smart_graph = BaseSelenium.locator_finder_by_id(self, smart_graph)
            smart_graph.click()
            time.sleep(2)

            # loading full graph
            load_graph = 'loadFullGraph'
            load_graph = BaseSelenium.locator_finder_by_id(self, load_graph)
            load_graph.click()
            time.sleep(1)

            load_full_graph = 'modalButton1'
            load_full_graph = BaseSelenium.locator_finder_by_id(self, load_full_graph)
            load_full_graph.click()
            time.sleep(5)

            self.driver.back()

            time.sleep(2)

            print("\n")
            print("Smart Graph deleting started \n")
            smart_settings = 'smart_graph_settings'
            smart_settings = BaseSelenium.locator_finder_by_id(self, smart_settings)
            smart_settings.click()

            delete_btn = 'modalButton0'
            delete_btn = BaseSelenium.locator_finder_by_id(self, delete_btn)
            delete_btn.click()

            delete_check_id = 'dropGraphCollections'
            delete_check_id = BaseSelenium.locator_finder_by_id(self, delete_check_id)
            delete_check_id.click()

            delete_confirm_btn = 'modal-confirm-delete'
            delete_confirm_btn = BaseSelenium.locator_finder_by_id(self, delete_confirm_btn)
            delete_confirm_btn.click()

            time.sleep(2)
            print("Smart Graph deleted successfully \n")

            self.driver.refresh()

        else:
            print('Disjoint Graph is not supported for the current package \n')

    # Creating new example graphs
    def select_create_graph(self, graph):
        select_graph = self.select_create_graph_id
        select_graph = \
            BaseSelenium.locator_finder_by_id(self, select_graph)
        select_graph.click()
        time.sleep(1)
        # Selecting example graph button
        self.select_example_graph_btn_id = \
            BaseSelenium.locator_finder_by_id(self, self.select_example_graph_btn_id)
        self.select_example_graph_btn_id.click()
        time.sleep(1)

        if graph == 1:
            self.select_knows_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_knows_graph_id)
            self.select_knows_graph_id.click()
        elif graph == 2:
            self.select_traversal_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_traversal_graph_id)
            self.select_traversal_graph_id.click()
        elif graph == 3:
            self.select_k_shortest_path_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_k_shortest_path_id)
            self.select_k_shortest_path_id.click()
        elif graph == 4:
            self.select_maps_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_maps_graph_id)
            self.select_maps_graph_id.click()
        elif graph == 5:
            self.select_world_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_world_graph_id)
            self.select_world_graph_id.click()
        elif graph == 6:
            self.select_social_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_social_graph_id)
            self.select_social_graph_id.click()
        elif graph == 7:
            self.select_city_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_city_graph_id)
            self.select_city_graph_id.click()
        elif graph == 8:
            self.select_connected_component_graph_id = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_connected_component_graph_id)
            self.select_connected_component_graph_id.click()
        else:
            print("Invalid Graph\n")
        time.sleep(2)

    # selecting collection tab and search for required collections
    def check_required_collection(self, graph):
        collectionPage = self.select_collection_page_id
        collectionPage = \
            BaseSelenium.locator_finder_by_id(self, collectionPage)
        collectionPage.click()

        if graph == 1:
            s1 = self.select_search_id
            s2 = self.select_search_id
            person = "//*[@id='collection_persons']/div/h5"
            knows = "//*[@id='collection_knows']/div/h5"

            knows = BaseSelenium.locator_finder_by_xpath(self, knows)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("knows")
            if knows.text == 'knows':
                print("knows collection creation has been validated.\n")
            else:
                print("knows collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            person = BaseSelenium.locator_finder_by_xpath(self, person)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("persons")
            if person.text == 'persons':
                print("persons collection creation has been validated.\n")
            else:
                print("person collection not found\n")
            time.sleep(3)

        elif graph == 2:
            s1 = self.select_search_id
            s2 = self.select_search_id
            circle = "//*[@id='collection_circles']/div/h5"
            edges = "//*[@id='collection_edges']/div/h5"

            circle = BaseSelenium.locator_finder_by_xpath(self, circle)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("circles")
            if circle.text == 'circles':
                print("circle collection creation has been validated.\n")
            else:
                print("circle collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            edges = BaseSelenium.locator_finder_by_xpath(self, edges)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("edges")
            if edges.text == 'edges':
                print("edges collection creation has been validated.\n")
            else:
                print("edges collection not found\n")
            time.sleep(3)

        elif graph == 3:
            s1 = self.select_search_id
            s2 = self.select_search_id
            connections = "//*[@id='collection_connections']/div/h5"
            places = "//*[@id='collection_places']/div/h5"

            connections = BaseSelenium.locator_finder_by_xpath(self, connections)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("connections")
            if connections.text == 'connections':
                print("connections collection creation has been validated.\n")
            else:
                print("connections collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            places = BaseSelenium.locator_finder_by_xpath(self, places)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("places")
            if places.text == 'places':
                print("places collection creation has been validated.\n")
            else:
                print("places collection not found\n")
            time.sleep(3)

        elif graph == 4:
            s1 = self.select_search_id
            s2 = self.select_search_id
            mps_edges = "//*[@id='collection_mps_edges']/div/h5"
            mps_verts = "//*[@id='collection_mps_verts']/div/h5"

            mps_edges = BaseSelenium.locator_finder_by_xpath(self, mps_edges)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("mps_edges")
            if mps_edges.text == 'mps_edges':
                print("mps_edges collection creation has been validated.\n")
            else:
                print("mps_edges collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            mps_verts = BaseSelenium.locator_finder_by_xpath(self, mps_verts)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("mps_verts")
            if mps_verts.text == 'mps_verts':
                print("mps_verts collection creation has been validated.\n")
            else:
                print("mps_verts collection not found\n")
            time.sleep(3)

        elif graph == 5:
            s1 = self.select_search_id
            s2 = self.select_search_id
            worldEdges = "//*[@id='collection_worldEdges']/div/h5"
            worldVertices = "//*[@id='collection_worldVertices']/div/h5"

            worldEdges = BaseSelenium.locator_finder_by_xpath(self, worldEdges)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("worldEdges")
            if worldEdges.text == 'worldEdges':
                print("worldEdges collection creation has been validated.\n")
            else:
                print("worldEdges collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            worldVertices = BaseSelenium.locator_finder_by_xpath(self, worldVertices)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("worldVertices")
            if worldVertices.text == 'worldVertices':
                print("worldVertices collection creation has been validated.\n")
            else:
                print("worldVertices collection not found\n")
            time.sleep(3)

        elif graph == 6:
            s1 = self.select_search_id
            s2 = self.select_search_id
            s3 = self.select_search_id
            female = "//*[@id='collection_female']/div/h5"
            male = "//*[@id='collection_male']/div/h5"
            relation = "//*[@id='collection_relation']/div/h5"

            female = BaseSelenium.locator_finder_by_xpath(self, female)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("female")
            if female.text == 'female':
                print("female collection creation has been validated.\n")
            else:
                print("female collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            male = BaseSelenium.locator_finder_by_xpath(self, male)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("male")
            if male.text == 'male':
                print("male collection creation has been validated.\n")
            else:
                print("male collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            relation = BaseSelenium.locator_finder_by_xpath(self, relation)
            s3 = BaseSelenium.locator_finder_by_id(self, s3)
            s3.click()
            s3.clear()
            s3.send_keys("relation")
            if relation.text == 'relation':
                print("relation collection creation has been validated.\n")
            else:
                print("relation collection not found\n")
            time.sleep(3)

        elif graph == 7:
            s1 = self.select_search_id
            s2 = self.select_search_id
            s3 = self.select_search_id
            s4 = self.select_search_id
            s5 = self.select_search_id
            frenchCity = "//*[@id='collection_frenchCity']/div/h5"
            frenchHighway = '//*[@id="collection_frenchHighway"]/div/h5'
            germanCity = '//*[@id="collection_germanCity"]/div/h5'
            germanHighway = '//*[@id="collection_germanHighway"]/div/h5'
            internationalHighway = '//*[@id="collection_internationalHighway"]/div/h5'

            frenchCity = BaseSelenium.locator_finder_by_xpath(self, frenchCity)
            s1 = BaseSelenium.locator_finder_by_id(self, s1)
            s1.click()
            s1.clear()
            s1.send_keys("frenchCity")
            if frenchCity.text == 'frenchCity':
                print("frenchCity collection creation has been validated.\n")
            else:
                print("frenchCity collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            frenchHighway = BaseSelenium.locator_finder_by_xpath(self, frenchHighway)
            s2 = BaseSelenium.locator_finder_by_id(self, s2)
            s2.click()
            s2.clear()
            s2.send_keys("frenchHighway")
            if frenchHighway.text == 'frenchHighway':
                print("frenchHighway collection creation has been validated.\n")
            else:
                print("frenchHighway collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            germanCity = BaseSelenium.locator_finder_by_xpath(self, germanCity)
            s3 = BaseSelenium.locator_finder_by_id(self, s3)
            s3.click()
            s3.clear()
            s3.send_keys("germanCity")
            if germanCity.text == 'germanCity':
                print("germanCity collection creation has been validated.\n")
            else:
                print("germanCity collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            germanHighway = BaseSelenium.locator_finder_by_xpath(self, germanHighway)
            s4 = BaseSelenium.locator_finder_by_id(self, s4)
            s4.click()
            s4.clear()
            s4.send_keys("germanHighway")
            if germanHighway.text == 'germanHighway':
                print("germanHighway collection creation has been validated.\n")
            else:
                print("germanHighway collection not found\n")
            time.sleep(3)
            self.driver.refresh()

            internationalHighway = BaseSelenium.locator_finder_by_xpath(self, internationalHighway)
            s5 = BaseSelenium.locator_finder_by_id(self, s5)
            s5.click()
            s5.clear()
            s5.send_keys("internationalHighway")
            if internationalHighway.text == 'internationalHighway':
                print("internationalHighway collection creation has been validated.\n")
            else:
                print("internationalHighway collection not found\n")
            time.sleep(3)

        self.driver.back()
        self.driver.refresh()

    # Checking required collections creation for the particular example graph.
    def checking_collection_creation(self, graph):
        if graph == 1:
            self.select_knows_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_knows_graphs_setting_btn_id_check)
            self.select_knows_graphs_setting_btn_id_check.click()
        elif graph == 2:
            self.select_traversal_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_traversal_graphs_setting_btn_id_check)
            self.select_traversal_graphs_setting_btn_id_check.click()
        elif graph == 3:
            self.select_k_shortest_path_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_k_shortest_path_graphs_setting_btn_id_check)
            self.select_k_shortest_path_graphs_setting_btn_id_check.click()
        elif graph == 4:
            self.select_maps_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_maps_graphs_setting_btn_id_check)
            self.select_maps_graphs_setting_btn_id_check.click()
        elif graph == 5:
            self.select_world_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_world_graphs_setting_btn_id_check)
            self.select_world_graphs_setting_btn_id_check.click()
        elif graph == 6:
            self.select_social_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_social_graphs_setting_btn_id_check)
            self.select_social_graphs_setting_btn_id_check.click()
        elif graph == 7:
            self.select_route_planner_graphs_setting_btn_id_check = \
                BaseSelenium.locator_finder_by_id(self, self.select_route_planner_graphs_setting_btn_id_check)
            self.select_route_planner_graphs_setting_btn_id_check.click()
        else:
            print("Invalid Graph choice\n")

        time.sleep(3)
        self.select_graph_cancel_btn_id = \
            BaseSelenium.locator_finder_by_id(self, self.select_graph_cancel_btn_id)
        self.select_graph_cancel_btn_id.click()
        time.sleep(3)

    # Sorting all graphs to descending and then ascending again
    def select_sort_descend(self):
        self.select_sort_settings_id = \
            BaseSelenium.locator_finder_by_id(self, self.select_sort_settings_id)
        self.select_sort_settings_id.click()
        time.sleep(2)

        descend = self.select_sort_descend_id
        ascend = self.select_sort_descend_id

        print("Sorting Graphs to Descending\n")
        descend = \
            BaseSelenium.locator_finder_by_xpath(self, descend)
        descend.click()
        time.sleep(2)

        print("Sorting Graphs to Ascending\n")
        ascend = \
            BaseSelenium.locator_finder_by_xpath(self, ascend)
        ascend.click()
        time.sleep(2)

    # Selecting Knows Graph for checking graph functionality
    def inspect_knows_graph(self):
        print("Selecting Knows Graph\n")
        graph = self.knows_graph_id
        graph = BaseSelenium.locator_finder_by_id(self, graph)
        graph.click()
        time.sleep(4)

        print("Selecting Knows Graph share option\n")
        share = self.select_share_id
        share = BaseSelenium.locator_finder_by_xpath(self, share)
        share.click()
        time.sleep(2)

        print("Selecting load full graph button\n")
        full_graph = self.select_load_full_graph_id
        full_graph = BaseSelenium.locator_finder_by_id(self, full_graph)
        full_graph.click()
        time.sleep(4)

        if self.driver.name == "chrome":  # this will check browser name
            print("Download has been disabled for the Chrome browser \n")
        else:
            print("Selecting Graph download button\n")
            camera = self.select_camera_download_icon
            camera = BaseSelenium.locator_finder_by_xpath(self, camera)
            camera.click()
            time.sleep(3)
            # super().clear_download_bar()

        # print("Selecting full screen mode\n")
        # full_screen = self.select_full_screen_btn_id
        # full_screen = BaseSelenium.locator_finder_by_xpath(self, full_screen)
        # full_screen.click()
        # time.sleep(3)
        # print("Return to normal mode\n")
        # super().escape()
        # time.sleep(3)

        print("Selecting Resume layout button \n")
        resume = self.select_resume_layout_btn_id
        pause = self.select_resume_layout_btn_id

        self.driver.refresh()

        resume = BaseSelenium.locator_finder_by_xpath(self, resume)
        resume.click()
        time.sleep(3)
        pause = BaseSelenium.locator_finder_by_xpath(self, pause)
        pause.click()
        time.sleep(3)

    # Checking all the options inside graph settings
    def graph_setting(self):
        configure_graph_settings_id = BaseSelenium.locator_finder_by_id(self, self.configure_graph_settings_id)
        configure_graph_settings_id.click()
        time.sleep(2)
        print("Selecting different layouts for the graph\n")
        print("Selecting Fruchtermann layout\n")
        layout2 = self.select_graph_layout_option_id
        BaseSelenium.locator_finder_by_select(self, layout2, 2)
        time.sleep(3)

        print("Selecting Force layout\n")
        layout1 = self.select_graph_layout_option_id
        BaseSelenium.locator_finder_by_select(self, layout1, 1)
        time.sleep(3)

        print("Selecting WebGL experimental renderer\n")
        renderer = self.select_renderer_id
        BaseSelenium.locator_finder_by_select(self, renderer, 1)
        time.sleep(3)

        print("Changing Search Depth\n")
        depth1 = self.select_depth_id
        depth2 = self.select_depth_id
        depth1 = BaseSelenium.locator_finder_by_xpath(self, depth1)
        depth1.clear()
        time.sleep(3)
        depth2 = BaseSelenium.locator_finder_by_xpath(self, depth2)
        depth2.send_keys("4")

        print("Changing Search Limit\n")
        limit = self.select_limit_id
        limit1 = self.select_limit_id
        limit2 = self.select_limit_id

        BaseSelenium.locator_finder_by_xpath(self, limit).click()
        time.sleep(2)
        limit1 = BaseSelenium.locator_finder_by_xpath(self, limit1)
        limit1.clear()
        limit2 = BaseSelenium.locator_finder_by_xpath(self, limit2)
        limit2.send_keys("300")
        time.sleep(3)

        print("Adding collection name with nodes to YES\n")
        BaseSelenium.locator_finder_by_select(self, self.add_collection_name_id, 0)
        time.sleep(3)

        print("Selecting color by collection to NO\n")
        BaseSelenium.locator_finder_by_select(self, self.select_color_collection_id, 0)
        time.sleep(3)

        print("Selecting size by edges to NO\n")
        BaseSelenium.locator_finder_by_select(self, self.select_size_by_edges_id, 1)
        time.sleep(3)

        print("Adding edge name to the node to YES\n")
        BaseSelenium.locator_finder_by_select(self, self.select_add_edge_col_name_id, 0)
        time.sleep(3)

        print("Adding Color by edge collection ot YES\n")
        BaseSelenium.locator_finder_by_select(self, self.select_color_node_by_edge_id, 1)
        time.sleep(3)

        print("Selecting different representation of relation between nodes\n")
        print("Maximizing the window")
        self.driver.maximize_window()
        time.sleep(2)

        tip1 = self.select_depth_id
        tip2 = self.select_depth_id
        tip4 = self.select_depth_id
        tip5 = self.select_depth_id
        tip6 = self.select_depth_id

        restore1 = self.select_restore_settings_id
        restore2 = self.select_restore_settings_id
        restore4 = self.select_restore_settings_id
        restore5 = self.select_restore_settings_id
        restore6 = self.select_restore_settings_id

        type1 = self.select_edge_type_id
        type3 = self.select_edge_type_id
        type4 = self.select_edge_type_id
        type5 = self.select_edge_type_id
        type6 = self.select_edge_type_id

        self.driver.find_element_by_xpath(tip1).click()
        super().scroll(1)
        time.sleep(2)
        restore1 = BaseSelenium.locator_finder_by_xpath(self, restore1)
        restore1.click()
        time.sleep(1)

        print("Changing relation representation type to Line")
        BaseSelenium.locator_finder_by_select(self, type1, 0)
        time.sleep(5)

        self.driver.find_element_by_xpath(tip2).click()
        super().scroll(1)
        time.sleep(2)
        restore2 = BaseSelenium.locator_finder_by_xpath(self, restore2)
        restore2.click()
        time.sleep(1)

        print("Changing relation representation type to Curve")
        BaseSelenium.locator_finder_by_select(self, type3, 2)
        time.sleep(5)

        self.driver.find_element_by_xpath(tip4).click()
        super().scroll(1)
        time.sleep(2)
        restore4 = BaseSelenium.locator_finder_by_xpath(self, restore4)
        restore4.click()
        time.sleep(1)

        print("Changing relation representation type to Dotted")
        BaseSelenium.locator_finder_by_select(self, type4, 3)
        time.sleep(5)

        self.driver.find_element_by_xpath(tip5).click()
        super().scroll(1)
        time.sleep(2)
        restore5 = BaseSelenium.locator_finder_by_xpath(self, restore5)
        restore5.click()
        time.sleep(1)

        print("Changing relation representation type to Dashed")
        BaseSelenium.locator_finder_by_select(self, type5, 4)
        time.sleep(5)

        self.driver.find_element_by_xpath(tip6).click()
        super().scroll(1)
        time.sleep(2)
        restore6 = BaseSelenium.locator_finder_by_xpath(self, restore6)
        restore6.click()
        time.sleep(1)

        print("Changing relation representation type to Tapered\n")
        BaseSelenium.locator_finder_by_select(self, type6, 5)
        time.sleep(5)

        print("Going Back to original window size \n")
        self.driver.set_window_size(1250, 1000)  # custom window size
        self.driver.back()
        time.sleep(3)

    # Deleting created graphs
    def delete_graph(self, graph):

        if graph == 1:
            self.select_knows_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_knows_graphs_setting_btn_id)
            self.select_knows_graphs_setting_btn_id.click()
            print("Deleting knows Graph\n")
            time.sleep(1)
        elif graph == 2:
            self.select_traversal_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_traversal_graphs_setting_btn_id)
            self.select_traversal_graphs_setting_btn_id.click()
            print("Deleting Traversal Graph\n")
            time.sleep(2)
        elif graph == 3:
            self.select_k_shortest_path_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_k_shortest_path_graphs_setting_btn_id)
            self.select_k_shortest_path_graphs_setting_btn_id.click()
            print("Deleting K Shortest Path Graph\n")
            time.sleep(1)
        elif graph == 4:
            self.select_maps_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_maps_graphs_setting_btn_id)
            self.select_maps_graphs_setting_btn_id.click()
            print("Deleting Mps Graph\n")
            time.sleep(1)
        elif graph == 5:
            self.select_world_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_world_graphs_setting_btn_id)
            self.select_world_graphs_setting_btn_id.click()
            print("Deleting World Graph\n")
            time.sleep(1)
        elif graph == 6:
            self.select_social_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_social_graphs_setting_btn_id)
            self.select_social_graphs_setting_btn_id.click()
            print("Deleting Social Graph\n")
            time.sleep(1)
        elif graph == 7:
            self.select_route_planner_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_route_planner_graphs_setting_btn_id)
            self.select_route_planner_graphs_setting_btn_id.click()
            print("Deleting City Graph\n")
            time.sleep(1)
        elif graph == 8:
            self.select_connected_graphs_setting_btn_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_connected_graphs_setting_btn_id)
            self.select_connected_graphs_setting_btn_id.click()
            print("Deleting Connected Component Graph\n")
            time.sleep(1)
        # for manual graph
        elif graph == 9:
            self.select_knows_graph_manual_id = \
                BaseSelenium.locator_finder_by_id(self, self.select_knows_graph_manual_id)
            self.select_knows_graph_manual_id.click()
            print("Deleting knows_graph_manual Graph\n")
            time.sleep(1)
        else:
            print("Invalid Graph")

        confirm_delete_graph_sitem = BaseSelenium.locator_finder_by_id(self, self.confirm_delete_graph_id)
        confirm_delete_graph_sitem.click()
        time.sleep(1)

        delete_with_collection_sitem = \
            BaseSelenium.locator_finder_by_id(self, self.delete_with_collection_id)
        delete_with_collection_sitem.click()
        time.sleep(1)

        select_really_delete_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.select_really_delete_btn_id)
        select_really_delete_btn_sitem.click()
        time.sleep(3)
