from typing import Any, Callable, Dict, Optional

import requests
import urllib3

import toolforge_weld
from toolforge_weld.kubernetes_config import Kubeconfig


class ToolforgeClient:
    """Toolforge API client."""

    def __init__(
        self,
        *,
        server: str,
        kubeconfig: Kubeconfig,
        user_agent: str,
        timeout: int = 10,
        exception_handler: Optional[Callable[..., BaseException]] = None,
    ):
        self.exception_handler = exception_handler
        self.timeout = timeout
        self.server = server
        self.session = requests.Session()

        self.session.cert = (
            str(kubeconfig.client_cert_file),
            str(kubeconfig.client_key_file),
        )

        self.session.verify = False

        # T253412: Disable warnings about unverifed TLS certs when talking to the
        # Kubernetes API endpoint
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.session.headers[
            "User-Agent"
        ] = f"{user_agent} toolforge_weld/{toolforge_weld.__version__} python-requests/{requests.__version__}"

    def _make_request(self, method: str, url: str, **kwargs) -> requests.Response:
        try:
            response = self.session.request(method, **self.make_kwargs(url, **kwargs))
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            if self.exception_handler:
                raise self.exception_handler(e)
            raise e

    def make_kwargs(self, url: str, **kwargs) -> Dict[str, Any]:
        """Setup kwargs for a Requests request."""
        kwargs["url"] = "{}/{}".format(
            self.server.removesuffix("/"), url.removeprefix("/")
        )

        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout

        return kwargs

    def get(self, url, **kwargs) -> Dict[str, Any]:
        """GET request."""
        r = self._make_request("GET", url, **kwargs)
        return r.json()

    def post(self, url, **kwargs) -> int:
        """POST request."""
        r = self._make_request("POST", url, **kwargs)
        return r.status_code

    def put(self, url, **kwargs) -> int:
        """PUT request."""
        r = self._make_request("PUT", url, **kwargs)
        return r.status_code

    def delete(self, url, **kwargs) -> int:
        """DELETE request."""
        r = self._make_request("DELETE", url, **kwargs)
        return r.status_code
