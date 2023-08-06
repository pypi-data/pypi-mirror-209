import requests
import json
import logging
from urllib.parse import urljoin

class OpenAccess:
    # Constants and globals used throughout the class
    instance = None
    # Change 'localhost' to the fully qualified domain name where the OpenAccess service is hosted
    API_URL = 'https://localhost:8080' #config['API_URL']
    DEFAULT_PAGE_SIZE = '10' #config['DEFAULT_PAGE_SIZE']
    SUCCESS = 'SUCCESS'# config['SUCCESS']
    ERROR = 'ERROR' #config['ERROR']
    API_VERSION = '1.0'#config['API_VERSION']
    APPLICATION_ID = 'APP_ID'#config['APPLICATION_ID']
    api_url=None
    application_id=None

    def __init__(self, api_url=None, application_id=None, ssl_verify=False):
        '''
        Init for OpenAccess class
        Args:
            api_url [str]: 'api url where Open Access server is located.'
            application_id [str]: 'Application id needed for open access license.'
            ssl_verify [bool]: 'Parameter for ssl verify in call request.'

        Return: None
        '''
        # Set up the requests.Session to handle requests to the OpenAccess API
        self.base_url = api_url
        self.client = requests.Session()
        self.client.headers.clear()
        self.client.headers.update({
            "Application-Id": application_id,
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        self.client.verify = ssl_verify # Temporary solution for invalid security certificate causing an inability to access the api
        self.client.base_url = api_url
        self.panels = []

        # You must initialize logging, otherwise you'll not see debug output.
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    @staticmethod
    def instance():
        if not OpenAccess._instance:
            OpenAccess._instance = OpenAccess()
        return OpenAccess._instance
    

    def parse_response(self, response):
        return json.loads(response.content.decode('utf-8'))

    def build_uri_with_version(self, method_name, version):
        return "{}{}?version={}".format(self.base_url, method_name, version)

    def request_instances(self, type, page_num, panel_id=-1):
        request = self.build_uri_with_version("instances", "1.0") + f"&type_name={type}&page_number={page_num}&page_size={self.DEFAULT_PAGE_SIZE}&order_by=name"
        
        if panel_id != -1:
            request += f"&filter=panelid = {panel_id}"
    
        # OpenAccess "instances" request
        # GET /api/access/onguard/openaccess/instances
        # Retrieves instances of a particular type based on the client-supplied filter (above)
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.get(request)
        
        return self.parse_response(response)

    def get_panels_from_result(self, result):
        panels = []
        for jo in result['item_list']:
            panels.append({
                'id': jo['property_value_map']['ID'],
                'name': jo['property_value_map']['Name'],
                'status': jo['property_value_map']['IsOnline'] == True,
                'type': jo['property_value_map']['PanelType']
            })
        return panels

    def get_readers_from_result(self, result):
        readers = []
        for jo in result['item_list']:
            readers.append({
                'panelId': jo['property_value_map']['PanelID'],
                'id': jo['property_value_map']['ReaderID'],
                'name': jo['property_value_map']['Name'],
                'type': jo['property_value_map']['ControlType'],
                'hostName': jo['property_value_map']['HostName']
            })
        return readers
    
    def request_cardholder(self, autoload_badge=False, has_badges=False, cardholder_filter=None,badges_filter=None ):
        # parameter = {
        #     "auto_load_badge":True
        # }

        request = self.build_uri_with_version("cardholders", "1.2")

        if autoload_badge:
            request += f"&auto_load_badge=true"
        

        if cardholder_filter is not None:
            request += f"&cardholder_filter={cardholder_filter}"
    
        if badges_filter is not None:
            request += f"&badges_filter={badges_filter}"

        # OpenAccess "cardholders" request
        # GET /api/access/onguard/openaccess/cardholders
        # Retrieves cardholders based on the client-supplied filter (above)
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.get(request)
        
        return self.parse_response(response)
    
    def sign_in(self, username: str, password: str, directory_id: str) -> str:
        """
        OpenAccess "authentication" request

        POST /api/access/onguard/openaccess/authentication

        Logs a user into the OpenAccess service by validating their username and password, then
        returns a session token for further calls
        """

        # Create a User object to be serialized to JSON and sent as the payload in the POST request
        user = {"user_name": username, "password": password, "directory_id": directory_id}
        try:
            url = self.build_uri_with_version("authentication","1.0")
            print(url)
            response = requests.post(url, json=user, verify = False, headers = self.client.headers)
        except requests.exceptions.RequestException as e:
            return f"Connection was unexpectedly closed. Make sure you don't have anything other than OpenAccess running on port 8080. Message: {e}"

        # If a response is received, parse it into a dictionary so its properties can be retrieved easily
        if response.ok:
            result = self.parse_response(response)
            self.session_token = result["session_token"]
            self.client.headers.update({"Session-Token": self.session_token})
            return OpenAccess.SUCCESS

        # If an error occurred on the server side, return its information
        else:
            return f"A server error occurred during your request. If the status code is available, it is shown below\n{response.status_code}: {response.reason}"
        

    def get_directories(self):
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.get(self.build_uri_with_version("directories","1.0"))

        # If a response is received, parse it into a dictionary so its properties can be retrieved easily
        if response.status_code == 200:
            directories = []
            result = json.loads(response.text)

            for directory in result['item_list']:
                directories.append({
                    'Id': directory['property_value_map']['ID'],
                    'Name': directory['property_value_map']['Name']
                })
            return directories
        # If an error occurred on the server side, return None
        else:
            return None
        
    def retrieve_panels(self):
        self.panels = []  # List to hold Panel objects to be displayed

        # Request the first page of panels
        result = self.request_instances("Lnl_Panel", 1)

        pageCount = result['total_pages']  # Number of pages to iterate over.

        # Convert the response to Panel objects and add them to the list
        self.panels.extend(self.get_panels_from_result(result))

        # Make a GET request for each page of panels we need
        for i in range(2, pageCount + 1):
            # Request the appropriate page of Panels
            result = self.request_instances("Lnl_Panel", i)

            # Convert the response to Panel objects and add them to the list
            self.panels.extend(self.get_panels_from_result(result))

        return self.panels

    def get_panels(self):
        return self.panels

    def retrieve_readers(self, panelId):
        readers = [] # List to hold Reader objects to be displayed

        # Request the first page of readers for the specified panel
        result = self.request_instances("Lnl_Reader", 1, panelId)

        if result["count"] == 0:
            return readers

        pageCount = result["total_pages"] # Number of pages to iterate over.

        # Convert the response to Reader objects and add them to the list
        readers.extend(self.get_readers_from_result(result))

        # Make a GET request for each page of readers we need
        for i in range(2, pageCount + 1):
            # Request the appropriate page of readers for the specified Panel
            result = self.request_instances("Lnl_Reader", i, panelId)

            # Convert the response to Reader objects and add them to the list
            readers.extend(self.get_readers_from_result(result))

        return readers
    
    def get_panels_filtered(self, panel_filter:str):
        """
        Get panel information using a filter panel_filter(str)
        i.e. get_panel_filtered(panel_filter="ID=8")

        GET /api/access/onguard/openaccess/instances

        Get a supported data class against a specific instance of a particular type (Lnl_Panel against a panelID in this case)
        """

        # Data object to be serialized by PostAsJsonAsync
        em = {
            "type_name":"Lnl_Panel", 
            "filter":panel_filter
        }

        
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.get(self.build_uri_with_version("instances","1.0"), json=em, verify=self.client.verify)

        # If a response is recieved, parse it into a dict so its properties can be retrieved easily
        if response.status_code == 200:
            return self.parse_response(response)

        # If an error occurred on the server side, return its information
        else:
            return f"A server error occurred during your request. If the status code is available, it is shown below\n{response.status_code}: {response.text}"
    
    def get_readers_filtered(self, reader_filter:str):
        """
        Get reader information using a reader panel_filter(str)
        i.e. get_reader_filtered(reader_filter="ReaderID=8 AND PanelID=9")

        GET /api/access/onguard/openaccess/instances

        Get a supported data class against a specific instance of a particular type (Lnl_Reader against a panelID in this case)
        """

        # Data object to be serialized by PostAsJsonAsync
        em = {
            "type_name":"Lnl_Reader", 
            "filter":reader_filter
        }

        
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.get(self.build_uri_with_version("instances","1.0"), json=em, verify=self.client.verify)

        # If a response is recieved, parse it into a dict so its properties can be retrieved easily
        if response.status_code == 200:
            return self.parse_response(response)

        # If an error occurred on the server side, return its information
        else:
            return f"A server error occurred during your request. If the status code is available, it is shown below\n{response.status_code}: {response.text}"
    
    def OpenDoor(self, reader):
        """
        OpenAccess "execute_method" request

        POST /api/access/onguard/openaccess/execute_method

        Executes a supported method against a specific instance of a particular type (OpenDoor() against a reader in this case)
        """
        # Dictionary of identifying attributes
        prop_value = {
            "PanelID": str(reader.panelId), 
            "ReaderID": str(reader.id)
        }

        # Dictionary of method parameters (none)
        parameter_value = {}

        # Data object to be serialized by PostAsJsonAsync
        em = {
            "method_name":"OpenDoor", 
            "type_name":"Lnl_Reader", 
            "property_value_map":prop_value, 
            "in_parameter_value_map":parameter_value
        }

        
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.post(self.build_uri_with_version("execute_method","1.0"), json=em, verify=False)

        # If a response is recieved, parse it into a dict so its properties can be retrieved easily
        if response.status_code == 200:
            return self.SUCCESS

        # If an error occurred on the server side, return its information
        else:
            return f"A server error occurred during your request. If the status code is available, it is shown below\n{response.status_code}: {response.text}"
        

    def send_incomming_event(self, reader, incommingEvent):
        """
        Send incomming event "execute_method" request

        POST /api/access/onguard/openaccess/execute_method

        Executes a supported method against a specific instance of a particular type (SendIncommingEvente() against a reader in this case)
        """
        # Dictionary of identifying attributes
        prop_value = {
            "Category": 0,
            "Description": "Incomming Event",
            "SupportParameters" : 0,
            "TypeID": 4,
            "PanelID": str(reader.panelId), 
            "ReaderID": str(reader.id)
        }

        # Dictionary of method parameters (none)
        parameter_value = {
            "Device": incommingEvent.device,
            "SubDevice": incommingEvent.subdevice,
            "Description": incommingEvent.description,
            "Source": incommingEvent.source,
            "IsAccessGrant":incommingEvent.isAccessGrant,
            "IsAccessDeny":incommingEvent.isAccessDeny,
            "BadgeID":incommingEvent.badgeId

        }

        # Data object to be serialized by PostAsJsonAsync
        em = {
            "method_name":"SendIncomingEvent", 
            "type_name":"Lnl_IncomingEvent", 
            "property_value_map":prop_value, 
            "in_parameter_value_map":parameter_value
        }

        
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.post(self.build_uri_with_version("execute_method","1.0"), json=em, verify=self.client.verify)

        # If a response is recieved, parse it into a dict so its properties can be retrieved easily
        if response.status_code == 200:
            return self.SUCCESS

        # If an error occurred on the server side, return its information
        else:
            return f"A server error occurred during your request. If the status code is available, it is shown below\n{response.status_code}: {response.text}"
        


    def badge_last_location(self, instances_filter=''):
        """
        Get de last location using a filter instances_filter(str)
        i.e. badge_last_location(instalces_filter="BadgeID=1234 AND AccessFlag=1 AND PanelID=10 AND ReaderID=2")
        i.e. badge_last_location(instalces_filter="AccessFlag=1 AND PanelID=10 AND ReaderID=2 AND EventTime>\"2023-05-09T15:35:00\"")

        GET /api/access/onguard/openaccess/instances

        Get a supported data class against a specific instance of a particular type (Lnl_BadgeLastLocation against a reader and a badgeId in this case)
        """

        # Data object to be serialized by PostAsJsonAsync
        em = {
            "type_name":"Lnl_BadgeLastLocation", 
            "filter":instances_filter
        }

        
        self.client.headers.update({"Session-Token": self.session_token})
        response = self.client.get(self.build_uri_with_version("instances","1.0"), json=em, verify=self.client.verify)

        # If a response is recieved, parse it into a dict so its properties can be retrieved easily
        if response.status_code == 200:
            return self.parse_response(response)

        # If an error occurred on the server side, return its information
        else:
            return f"A server error occurred during your request. If the status code is available, it is shown below\n{response.status_code}: {response.text}"