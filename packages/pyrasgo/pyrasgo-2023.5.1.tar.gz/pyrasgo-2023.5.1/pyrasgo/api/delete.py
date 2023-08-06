"""
API Delete functions
"""
from pyrasgo import errors


class Delete:
    """
    API Delete Class
    """

    def __init__(self):
        from pyrasgo.api.connection import Connection
        from pyrasgo.config import get_session_api_key

        api_key = get_session_api_key()
        self.api = Connection(api_key=api_key)

    def dataset(self, dataset_id: int) -> str:
        """
        Delete a Dataset in Rasgo
        """
        response = self.api._delete(f"/datasets/{dataset_id}", api_version=2)
        if response.status_code == 200:
            return f"Dataset with id '{dataset_id}' successfully deleted"
        return f"Problem deleting Dataset {dataset_id}."

    def metric(self, metric_id: int) -> str:
        """
        Delete a Rasgo Metric by ID

        Args:
            metric_id: Rasgo ID of metric to delete
        """
        response = self.api._delete(f"/metric/{metric_id}", api_version=2)
        if response.status_code == 200:
            return f"Metric with id '{metric_id}' successfully deleted"
        elif response.status_code == 404:
            raise errors.RasgoResourceException(
                f"Could not find metric with id '{metric_id}' or user does not have access to delete"
            )
        return f"Could not delete metric '{metric_id}'"

    def transform(self, transform_id: int) -> str:
        """
        Delete a Rasgo User Defined Transform
        """
        # NOTE: We print out error msgs on the API side
        # in the function self.api._raise_internal_api_error_if_any(response)
        # so no need to print out logic like above
        response = self.api._delete(f"/transform/{transform_id}", api_version=1)
        if response.status_code == 200:
            return f"Transform with id '{transform_id}' successfully deleted"
        if response.status_code == 403:
            raise errors.RasgoResourceException(
                f"User does not have access to delete Transform with id '{transform_id}'"
            )
        return f"Problem deleting Transform {transform_id}."
