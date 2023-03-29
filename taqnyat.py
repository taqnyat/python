import json
import requests

class Client:
    def __init__(self, api_key,raise_exception=True):
        # Initialize the Client object with an api key and default values for result and method
        self.api_key = api_key
        self.base = "https://api.taqnyat.sa"
        self.result = ""
        self.method = ""
        self.error = None
        # 
        self.raise_exception = raise_exception


    def send_msg(self, body:str, recipients:list, sender:str, scheduled:str=None,delete_id:int=None):
        """
        Sends a message via an HTTP POST request and returns the JSON object returned by the server.

        Parameters:
        - body (str): the message body.
        - recipients (list): a list of recipients' phone numbers in international format.
        - sender (str): the sender's name or phone number.
        - scheduled (str): the date and time at which the message is scheduled to be sent in ISO 8601 format.
        - delete_id (int): the ID of the message to be deleted.

        Returns:
        - The JSON object returned by the server.
        """
        # Create a JSON object containing the message data
        if scheduled:
            data = json.dumps({
                "body": body,
                "recipients": recipients,
                "sender": sender,
                "scheduledDatetime": scheduled,
                "deleteId":delete_id
            })

        else:
            data = json.dumps({
                "body": body,
                "recipients": recipients,
                "sender": sender
            }) 

        # Add the authorization token to the headers
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }

        # Send the message via an HTTP POST request using the requests library
        response = requests.post(self.base + "/v1/messages", data=data, headers=headers)

        # Check if the response was successful; if not, raise an exception
        if not response.ok:
            if self.raise_exception:
                response.raise_for_status()
            else:
                self.error=response.json()
        # Return the JSON object returned by the server
        return response.json()

    def send_status(self):
        """
        Sends an HTTP GET request to get the system status and returns the JSON object returned by the server.

        Returns:
        - The JSON object returned by the server.
        """
        headers = {
            "Content-Type": "application/json",
        }

        # Send an HTTP GET request to get the system status
        response = requests.get(self.base + "/system/status", headers=headers)

        # Check if the response was successful; if not, raise an exception
        if not response.ok:
            if self.raise_exception:
                response.raise_for_status()
            else:
                self.error=response.json()
        # Return the JSON object returned by the server
        return response.json()


    def balance(self):
        """
        Sends an HTTP GET request to get the balance of the account and returns the JSON object returned by the server.

        Returns:
        - The JSON object returned by the server.
        """
        self.check_user_info()

        # Add the authorization token to the headers
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }
        
        # Send an HTTP GET request to get the balance of the account
        response = requests.get(self.base + "/account/balance", headers=headers)

        # Check if the response was successful; if not, raise an exception
        if not response.ok:
            if self.raise_exception:
                response.raise_for_status()
            else:
                self.error=response.json()
        # Return the JSON object returned by the server
        return response.json()



    def senders(self):
        """
        Sends an HTTP GET request to get a list of senders for the account and returns the JSON object returned by the server.

        Returns:
        - The JSON object returned by the server.
        """
        # Add the authorization token to the headers
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }

        # Send an HTTP GET request to get a list of senders for the account
        response = requests.get(self.base + "/v1/messages/senders", headers=headers)

        # Check if the response was successful; if not, raise an exception
        if not response.ok:
            if self.raise_exception:
                response.raise_for_status()
            else:
                self.error=response.json()
        # Return the JSON object returned by the server
        return response.json()

    def delete_msg(self, delete_id:int):
        """
        Deletes a message with the given ID via an HTTP
        Parameters:
        - delete_id (int): the ID of the message to be deleted.

        Returns:
        - The JSON object returned by the server.
        """
        self.check_user_info()

        # Create a JSON object containing the ID of the message to be deleted
        data = json.dumps({
            "deleteId":delete_id
        })

        # Add the authorization token to the headers
        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }

        # Send an HTTP DELETE request to delete a message
        response = requests.delete(self.base + "/v1/messages", headers=headers, data=json.dumps(data))
        if not response.ok:
            if self.raise_exception:
                response.raise_for_status()
            else:
                self.error=response.json()
        return response.json()


