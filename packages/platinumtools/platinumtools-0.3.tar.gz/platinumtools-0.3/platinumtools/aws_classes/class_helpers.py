from abc import ABC, abstractmethod
from typing import List
from platinumtools.dda_constants import *
import json

class DatabaseProvider(ABC):
    def __init__(self, credentials, settings):
        self.credentials = credentials
        self.settings = settings
        

    @abstractmethod
    def publish(self, events: List[dict]):
        print("publishing to database:", events)

    @abstractmethod
    def getOne(self, key_value, key_column: str = "guid"):
        print("Getting source with: ", key_value, "in", key_column, "column")

class MockDatabaseProvider(DatabaseProvider):
    """Prints publishing and getters, using for debugging, also returns static examples
    Records the json for quicke edition and visualization in a local file.
    """
    def __init__(self, credentials, settings):
        super().__init__(credentials, settings)
        self.db = []

    def publish(self, events: List[dict]):
        self.db.extend(events)

        # Save as .. code-block:: json
        
        with open("mock_db.json", "w") as f:
            f.write(json.dumps(self.db, indent=4))

        return super().publish(events=events)

    def getOne(self, key_value, key_column: str = "guid"):
        super().getOne(key_column)
        try:
            for(i, row) in enumerate(self.db):
                if row[key_column] == key_value:
                    return row
            return []
        except Exception as e:
            print("key column", key_column, " : ", key_value, "not found")
            print("Exception:", e)
            print("self.db", len(self.db))
            for(i, row) in enumerate(self.db):
                print(i, row['guid'])
            return []


class MockStagingDatabaseProviderPrePopulated(MockDatabaseProvider):
    def __init__(self, credentials, settings):
        super().__init__(credentials, settings)
        self.db = STAGING_EVENTS_SAMPLE



class MockStagingDatabaseProviderWithChrome(MockDatabaseProvider):
    """Extension Mock Staging Database of rthe Config mapper to work better with Chrome
    """
    def __init__(self, credentials, settings):
        super().__init__(credentials, settings)
        self.db = STAGING_EVENTS_SAMPLE_WITH_CHROME


import psycopg2
    
class PostgreSQLProvider(DatabaseProvider):
    """Publishes into PostgreSQL as key and expects a body column to be published as  
    """

    def __init__(self, credentials, settings):
        """Initiates with the database credentials, and settings as the specfici tables it is looking for
        Requires:
            pandas
            psycopg2

        Args:
            credentials (dict): Credentails for database {USERNAME, PASSWORD, HOST, DB}
            settings (dict): {TABLE}
        """
        super().__init__(credentials, settings)
        # Initiate SQl connection
        self.connection = psycopg2.connect(user=credentials['USERNAME'], password=credentials['PASSWORD'], host=credentials['HOST'], database=credentials['DB'])
        self.cursor = self.connection.cursor()

    def fetchFromElse(self, fetchFrom: dict, key, elseGets):
        """Fetches value from dictionary otherwise it gets:

        Args:
            fetchFrom (dict): _description_
            key (_type_): _description_
            elseGets (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key in fetchFrom:
            return fetchFrom[key]
        return elseGets
    
    def publish(self, events: List[dict]):
        """Publishes
        Expected parameters to have unders settings:
        - TABLENAME
        - COLUMN_NAMES
    
        Args:
            events (List[dict]): List of events to publish.
        """

        # Fetches the proper credentials based on the environemnt


        # Update Settings"
        column_names = self.settings.get("COLUMN_NAMES", ["employee_guid", "timestamp_utc", "application", "operation"])
        tablename= self.settings.get("TABLENAME", "events")

        # Pushes the changes into SQL
        insert_sql = f"INSERT INTO {tablename} ({', '.join(column_names)}) VALUES ({', '.join(['%s'] * len(column_names))})"
        # print("Created insert_SQL:", insert_sql)
        # Execute the INSERT statement for each dictionary in the list
        print("attepting to get rows from events:", events)

        import json
        from typing import List

        def cleanQueryArgument(queryArgument):
            # If the queryArg is a list or dict, format it into a way that is query insertable
            if isinstance(queryArgument, (dict)):
                # If the is List and the first element is a dict, then it is a list of objects
                return json.dumps(queryArgument)
            if isinstance(queryArgument, List) and len(queryArgument) >0 and isinstance(queryArgument[0], dict):
                # return an array of strings of the json
                for(i, item) in enumerate(queryArgument):
                    queryArgument[i] = cleanQueryArgument(item)
            
            return queryArgument

        for row in events:
            values = []
            for col in column_names:
                value = row.get(col, None)
                values.append(cleanQueryArgument(value))
            try:
                self.cursor.execute(insert_sql, values)
            except Exception as e:
                print("Exception at publish:", e, "values:", values)
        self.connection.commit()

    
    def getOne(self, key_value, key_column: str = "guid"):
        """Gets one
        Expected parameters to have under settings:
        - TABLENAME

        Args:
            source_id (str): _description_
        """
        # Get table name and other settings properties
        
        tablename= self.fetchFromElse(self.settings, "GET_TABLENAME", "event")
        row_dict = {}
        # Gets one of the sources
        self.cursor.execute(f"SELECT * FROM {tablename} WHERE {key_column} = '{key_value}'")

        row = self.cursor.fetchone()
        if row:
            row_dict = dict(zip([desc[0] for desc in self.cursor.description], row))
            print(row_dict)
        else:
            print("No rows found")
        return row_dict


    
import json, random, string
class Utils:
    """Some random utitlities
    Requirements:
    - json
    """

    def createRandomStr(length:int  = 10):
        """Generates random string with the length indicated

        Args:
            length (int, optional): length of the random string. Defaults to 10.
        """
        # Generate a random string
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return random_string

    def escapedStrToListOfObjects(escapedStr: str):
        """Escapes String that might appear on the database or queries into a list of objects or dict

        Args:
            escapedStr (str): escaped String

        Returns:
            List: List of objects/or dict

..code-block
        '[         {\"name\": \"Alice\", \"age\": 25, \"gender\": \"F\"},         {\"name\": \"Bob\", \"age\": 30, \"gender\": \"M\"},         {\"name\": \"Charlie\", \"age\": 35, \"gender\": \"M\"}     ]'
        ->
        [{'name': 'Alice', 'age': 25, 'gender': 'F'}, {'name': 'Bob', 'age': 30, 'gender':
 'M'}, {'name': 'Charlie', 'age': 35, 'gender': 'M'}]
        """
        try:
            escapedStr = escapedStr.strip()
            return json.loads(escapedStr)
        except Exception as e:
            return []


        
class OrganizationalQuerier(ABC):
    def __init__(self, organization_id):
        self.organization_id = organization_id
        
    def getCredential(organization_id: str, service: str):
        """Gets organization identification. 

        Args:
            organization_id (str): 
            service (str): gets ervices
        """
        pass

    def getEmployeesDenormalized(organization_id: str):
        """Gets all of the employees data in the organization

        Args:
            organization_id (str): organization string
        """
        

        pass
    def getEmployeeDenormalized(employee_id: str):
        """Gets the data of the employee based on th

        Args:
            employee_id (str): id of th employee which data we want to denormalize
        """
        pass

    def getEmployeeDataWhere(key: str, value: str):
        """Gets the employee data where the key is equal to the value

        Args:
            key (str): key to be searched
            value (str): value to be searched

        Returns:
            dict: employee data
        """
        return {}
    
    def isRootOrUpdateRoot(span_guid: str, event_endtime: str, event_duration: int) -> dict:
        """If the event is root returns {is_root: true, total_duration = current_duration, root_reference: span_guid}
        Otherwise: {is_root: false, total_duration = current_duration + root_duration, root_reference: root_guid}

        Args:
            span_guid (str): guid of the group span
            event_endtime (datetime): endtime of the event request
            event_duration (number): duration in seconds 

        Returns:
            dict: {is_root: bool, total_duration: number, root_reference: str}
        """
        return {}

# Sample profile of an employee, that is just used by default.

sample_profile_employee_1 = {
            "organization_id": 123456,
            "employee_guid": "ab3c-asd1-100G",
            "employee_id": 789012,
            "employee_team_id": [1, 2, 3],
            "profile_id": [4, 5, 6],
            "employee_timezone": "US/Eastern",
            "employee_time_slot_split": 6,
            "employee_work_hours_start": [9, 10, 11, 9, 9, 0, 0],
            "employee_work_days": [0, 1, 2, 3, 4],
            "employee_work_hours_end": [17, 18, 19, 17, 17, 0, 0],
            "employee_escape_dates": ["2022-04-15", "2022-06-10"],
            "profile_mapping_instruction": {"instruction1": "value1", "instruction2": "value2"}
    }

class MockOrganizationQuerier(OrganizationalQuerier):
    
    

    def __init__(self, organization_id):
        """
        Doesn't intiialize the database because that has been provided will be there for all.
        """

        super().__init__(organization_id)

    def getCredential(organization_id: str, service: str):
        return super().getCredential(service)
        
    def getEmployeesDenormalized(self, organization_id: str):
        return super().getEmployeesDenormalized(organization_id)

    # Here is where  it actually gets the hours and so forth of the empoyee
    def getOrganizationParameters(employee_guid: str) -> List[dict]:
        sample_organization_parameters = [
        {
            "organization_id": 123456,
            "employee_guid": employee_guid,
            "employee_id": 789012,
            "employee_team_id": [1],
            "profile_id": [4, 5, 6],
            "employee_timezone": "US/Eastern",
            "employee_time_slot_split": 6,
            "employee_work_hours_start": [9, 10, 11, 9, 10, 0, 0],
            "employee_work_days": [0, 1, 2, 3, 4],
            "employee_work_hours_end": [17, 18, 19, 17, 24, 0, 0],
            "employee_escape_dates": ["2022-04-15", "2022-06-10"],
            "profile_mapping_instruction": {"instruction1": "value1", "instruction2": "value2"}
        },
        {
            "organization_id": 123456,
            "employee_id": 321098,
            "employee_team_id": [7, 8],
            "employee_guid": "ab3c-asd1-561a",
            "profile_id": [1, 2, 3],
            "employee_timezone": "Asia/Tokyo",
            "employee_time_slot_split": 6,
            "employee_work_hours_start": [9, 10, 11, 9, 9, 0, 0],
            "employee_work_days": [0, 1, 2, 3, 4],
            "employee_work_hours_end": [17, 18, 19, 17, 17, 0, 0],
            "employee_escape_dates": ["2022-03-01", "2022-09-01"],
            "profile_mapping_instruction": {"instruction5": "value5", "instruction6": "value6"}
        }
        ] 
        return sample_organization_parameters

    def getOrganizationParameters_365(orgnaization_guid_365: str) -> List[dict]:
        # Here it returns as the O365 id first as the main key.

        sample_organization_parameters_365_formatted = {
        "organization_id": "8de4e5d3-49de-4b57-a209-organization",
            "nelson@o365.devcooks.com": sample_profile_employee_1,
            "apolo@o365.devcooks.com": sample_profile_employee_1
        }
        return sample_organization_parameters_365_formatted

    def getOrganizationParameters_salesforce(orgnaization_guid_salesforce: str) -> List[dict]:

        """Salesforce frmatted means, that it would return you with the salesforce actor id as the key.

        Returns:
            dict: It should return you the organization parameters for salesforce example.
        """

        sample_organization_parameters_salesforce_formatted = {
        "organization_id": "123e4567-e89b-12d3-a456-client",
         "nwang@platinumfilings.com": sample_profile_employee_1
        }
        return sample_organization_parameters_salesforce_formatted

    def getOrganizationParameters_connectorguid(organization_guid_chrome: str) -> List[dict]:
        # Shows the connector guid first, such as chrome-extension-ddap-1 used for chome
        sample_organization_parameters_365_formatted = {
        
        "organization_id": organization_guid_chrome,
        "chrome-extension-ddap-2": sample_profile_employee_1,
        "chrome-extension-ddap-1":sample_profile_employee_1,
        "another-connector-guid-2": sample_profile_employee_1,

        }
        return sample_organization_parameters_365_formatted

    def getEmployeeDataWhere(key: str, value: str):
        """Gets the employee data where the key is equal to the value

        Args:
            key (str): key to be searched
            value (str): value to be searched

        Returns:
            dict: employee data
        """
        result_employee = sample_profile_employee_1.copy()
        result_employee.key = value
        return result_employee

    def isRootOrUpdateRoot(span_guid: str, event_endtime: str, event_duration: int) -> dict:
        """If the event is root returns {is_root: false, total_duration = current_duration, root_reference: span_guid}
        Otherwise: {is_root: true, total_duration = current_duration + root_duration, root_reference: root_guid}

        Args:
            span_guid (str): guid of the group span
            event_endtime (datetime): endtime of the event request
            event_duration (number): duration in seconds 

        Returns:
            dict: {is_root: bool, total_duration: number, root_reference: str}
        """
        root_guid = {
            "ab3c-asd1-100G":
            {
                "span_guid": "ab3c-asd1-100G",
                "root_guid": "ab3c-asd1-100G",
                "root_duration": 25,
                "root_endtime": "2021-08-01T00:00:00Z"
            },
            "ab3c-asd1-123g":            
            {
                "span_guid": "ab3c-asd1-123g",
                "root_guid": "ab3c-asd1-123g",
                "root_duration": 11,
                "root_endtime": "2021-08-01T00:00:00Z"
            }
        }

        if span_guid in root_guid:
            
            root_guid[span_guid]["root_duration"] += event_duration
            root_guid[span_guid]["root_endtime"] = event_endtime

            return {
                "is_root": False,
                "total_duration": root_guid[span_guid]["root_duration"],
                "root_reference": span_guid
            }

        else:
            return {
                "is_root": True,
                "total_duration": event_duration,
                "root_reference": span_guid
            }


    