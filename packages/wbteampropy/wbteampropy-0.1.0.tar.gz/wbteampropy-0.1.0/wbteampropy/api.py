import requests


class WBTEAMPRO:
    """
        WBTeamPro Interface
    """

    def __init__(self, url, username, password):
        """
          Create a new instance.

          Args:
              url (str): The URL to the WBProTeam api.
              username (str): A valid Administrator username that is within a
                 WHMCS Administrative Role that has been granted access to the wbTeamPro system.
              password (str): The password for
                 the valid Administrator

          """
        self.url = url
        self.username = username
        self.password = password

    def _format_array_params(self, params):
        """
        Format lists as array params.

        A list should be formatted in a certain way (PHP-ish?) in order to be
        processable by WHMCS.
        The params dict is modified to contain the new params.

        Args:
            params (dict): The params to process.

        """
        for key, value in list(params.items()):
            if isinstance(value, list):
                for index, item in enumerate(value):
                    params[f'{key}[{index}]'] = item
                del params[key]

    def call(self, action, **params):
        """
        Call the WBTeamPro api.

        This is an abstract way to call the WBTeamPro API. Basically only the
        action and additional params are required to make a call.

        Args:
            action (str): The action to perform.
            **params: Additional params.

        Returns:
            json: The result of the call.

        Raises:
            MissingPermission: When access is denied due to a missing
                permission.
            Error: Whenever the call fails.
        """
        payload = {
            'action': action,
            'username': self.username,
            'password': self.password,
        }
        self._format_array_params(params)
        payload.update(params)
        response = requests.post(
            self.url,
            verify=True,
            params=payload)
        response_ = response.json()

        '''try:
            result = response_['request']['message']
        except KeyError:
            result = response_['request']['message']
        if result == 'Error':
            if response.status_code == 403:
                raise MissingPermission(response_['message'])
            raise Error(response_['message'])
            '''
        return response_

    def get_action(self, action_id, **params):
        """
        Get an action.

        Args:
            action_id (int): The action ID

        Returns:
            json: The action requested in JSON format

        Hint:
            For additional params, see the official API docs (Using the API Developers Sandbox section):
            https://docs.holodyn.com/WHMCS/wbTeamPro/v3/Web_API

        """

        result = self.call('v1.actions.{}.json'.format(action_id), method='get', **params)
        return result

    def get_project(self, project_id, **params):
        """
        Get a project.

        Args:
            project_id (int): The project ID

        Returns:
            json: The project requested in JSON format

        Hint:
            For additional params, see the official API docs (Using the API Developers Sandbox section):
            https://docs.holodyn.com/WHMCS/wbTeamPro/v3/Web_API

        """

        result = self.call('v1.projects.{}.json'.format(project_id), method='get', **params)
        return result

    def get_project_actions(self, project_id, **params):
        """
        Get the project actions.

        Args:
            project_id (int): The project ID

        Returns:
            json: The actions of the requested project in JSON format

        Hint:
            For additional params, see the official API docs (Using the API Developers Sandbox section):
            https://docs.holodyn.com/WHMCS/wbTeamPro/v3/Web_API
        """

        result = self.call('v1.projects.{}.actions.json'.format(project_id), method='get', **params)
        return result

    def update_action_notes(self, action_id, action_notes, **params):
        """
                Update the action note.

                Args:
                    action_id (int): The action ID
                    action_notes (str): The note text


                Returns:
                    json: The actions result in JSON format

                Hint:
                    For additional params, see the official API docs (Using the API Developers Sandbox section):
                    https://docs.holodyn.com/WHMCS/wbTeamPro/v3/Web_API
                """

        parametres = '{{\"action_id\":\"{}\",\"action_notes\":\"{}\"}}'.format(action_id, action_notes)

        result = self.call('v1.actions.{}.json'.format(action_id), method='put', params=parametres, **params)
        return result


class Error(Exception):
    """
    An unspecified error.

    """


class MissingPermission(Error):
    """
    Missing permission when calling the API.

    """
