from typing import Any, Dict, Iterable, List, Optional

from airflow.hooks.base import BaseHook
from odd_models.api_client import ODDApiClient
from odd_models.models import DataEntity, DataEntityList
from requests import Response
from requests.exceptions import HTTPError


class ODDHook(BaseHook):
    """Hook for odd connection."""

    def __init__(
        self,
        odd_conn_id: Optional[str] = None,
        *args: Iterable[Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        """
        Base constructor to create hook.

        Args:
            odd_conn_id: airflow connection id
            *args: additional arguments for parent constructor of BaseHook
            **kwargs: additional keyword arguments for parent constructor of BaseHook
        """
        super().__init__(*args, **kwargs)
        self.odd_conn_id = odd_conn_id or 'odd_default'
        self.conn: Optional[ODDApiClient] = None

    # Violation disabled because of public API of airflow
    def get_conn(self) -> ODDApiClient:  # noqa: WPS615
        """
        Return new client ODD connection.

        Returns:
            client instance of ODDApiClient

        Raises:
            HTTPError: in case of unavailability to connect to OOD
        """
        conn = self.get_connection(self.odd_conn_id)
        client = ODDApiClient(base_url=conn.host)
        try:
            client.get('/acutator/health')
        except HTTPError as error:
            self.log.error('Could not connect to odd: {error}'.format(error=error))
            raise error
        return client

    def post_data_entity_list(
        self,
        data_source_oddrn: str,
        data_entities: List[DataEntity],
        headers: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ):
        """
        Create data entities in odd.

        Args:
            data_source_oddrn: oddrn to data_source related to entities
            data_entities: list of entities to create in odd
            headers: headers to post request
            timeout: max timeout to create entities

        Returns:
            http response
        """
        data_entities_list = DataEntityList(
            data_source_oddrn=data_source_oddrn,
            items=data_entities,
        )
        response: Response = self.get_conn().post_data_entity_list(
            data=data_entities_list,
            headers=headers,
            timeout=timeout,
        )
        response.raise_for_status()
        return response
