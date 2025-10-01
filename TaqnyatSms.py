from __future__ import annotations

from typing import Any, Dict, Optional, Sequence, Union

import certifi
import requests


class Client:
    """Lightweight client for the Taqnyat SMS API using requests."""

    base_url = "https://api.taqnyat.sa"

    def __init__(
        self,
        auth: str,
        verify: Optional[Union[bool, str]] = True,
        timeout: int = 15,
        session: Optional[requests.Session] = None,
        base_url: Optional[str] = None,
    ) -> None:
        self.auth = auth or ""
        self.timeout = timeout
        self.error: str = ""
        self.base_url = base_url or self.base_url

        if verify is True:
            self.verify = certifi.where()
        else:
            self.verify = verify

        self.session = session or requests.Session()
        if self.auth:
            self.session.headers.update({"Authorization": f"Bearer {self.auth}"})
        self.session.headers.setdefault("Content-Type", "application/json")

    def check_user_info(self) -> Optional[str]:
        if not self.auth:
            self.error = "Add Authentication"
            return self.error

        auth_header = f"Bearer {self.auth}"
        if self.session.headers.get("Authorization") != auth_header:
            self.session.headers["Authorization"] = auth_header

        self.error = ""
        return None

    def _request(
        self,
        method: str,
        path: str,
        payload: Optional[Dict[str, Any]] = None,
    ):
        url = f"{self.base_url}{path}"
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                json=payload if payload is not None else {},
                timeout=self.timeout,
                verify=self.verify,
            )
            response.raise_for_status()

            if not response.content:
                return ""

            try:
                return response.json()
            except ValueError:
                return response.text
        except requests.exceptions.SSLError as exc:
            return f"SSL Error: {exc}"
        except requests.exceptions.HTTPError as exc:
            body = exc.response.text if exc.response is not None else ""
            return f"HTTP Error: {exc} - Body: {body}"
        except requests.exceptions.RequestException as exc:
            return f"Request Error: {exc}"

    def sendMsg(
        self,
        body: str,
        recipients: Sequence[str],
        sender: str,
        scheduled: Optional[str] = None,
    ):
        if self.check_user_info():
            return self.error

        payload: Dict[str, Any] = {
            "auth": self.auth,
            "recipients": list(recipients),
            "sender": sender,
            "body": body,
        }
        if scheduled:
            payload["scheduled"] = scheduled

        return self._request("POST", "/v1/messages", payload)

    def sendStatus(self):
        if self.check_user_info():
            return self.error

        payload = {"auth": self.auth}
        return self._request("GET", "/system/status", payload)

    def balance(self):
        if self.check_user_info():
            return self.error

        payload = {"auth": self.auth}
        return self._request("GET", "/account/balance", payload)

    def senders(self):
        if self.check_user_info():
            return self.error

        payload = {"auth": self.auth}
        return self._request("GET", "/v1/messages/senders", payload)

    def deleteMsg(self, deleteKey: Optional[str] = None):
        if self.check_user_info():
            return self.error

        payload: Dict[str, Any] = {"auth": self.auth}
        if deleteKey:
            payload["deleteKey"] = deleteKey

        return self._request("DELETE", "/v1/messages", payload)


client = Client
__all__ = ["Client", "client"]
