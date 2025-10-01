import unittest
from unittest.mock import Mock

import certifi
import requests

from TaqnyatSms import Client


def make_json_response(payload):
    response = Mock()
    response.raise_for_status = Mock()
    response.json = Mock(return_value=payload)
    response.text = ""
    response.content = b"{}"
    return response


def make_text_response(text):
    response = Mock()
    response.raise_for_status = Mock()
    response.json = Mock(side_effect=ValueError("no json"))
    response.text = text
    response.content = text.encode("utf-8")
    return response


def make_error_response(exception):
    response = Mock()
    response.raise_for_status = Mock(side_effect=exception)
    response.json = Mock(side_effect=ValueError("no json"))
    response.text = getattr(exception.response, "text", "")
    response.content = response.text.encode("utf-8") if response.text else b""
    return response


def make_session(response=None, side_effect=None):
    session = Mock()
    session.headers = {}
    request_mock = Mock()
    if side_effect is not None:
        request_mock.side_effect = side_effect
    else:
        request_mock.return_value = response
    session.request = request_mock
    return session


class ClientTests(unittest.TestCase):
    def test_send_msg_sends_expected_payload(self):
        payload = {"message": "queued"}
        response = make_json_response(payload)
        session = make_session(response=response)

        client = Client("token", session=session)
        result = client.sendMsg("hello", ["966"], "Sender", scheduled="2020-10-01T10:00")

        self.assertEqual(result, payload)
        session.request.assert_called_once()
        _, kwargs = session.request.call_args
        expected_payload = {
            "auth": "token",
            "recipients": ["966"],
            "sender": "Sender",
            "body": "hello",
            "scheduled": "2020-10-01T10:00",
        }
        self.assertEqual(kwargs["method"], "POST")
        self.assertEqual(kwargs["url"], "https://api.taqnyat.sa/v1/messages")
        self.assertEqual(kwargs["json"], expected_payload)
        self.assertEqual(kwargs["timeout"], client.timeout)
        self.assertEqual(kwargs["verify"], client.verify)

    def test_send_status_success_returns_json(self):
        payload = {"status": "available"}
        response = make_json_response(payload)
        session = make_session(response=response)

        client = Client("token", session=session)
        result = client.sendStatus()

        self.assertEqual(result, payload)
        session.request.assert_called_once()
        _, kwargs = session.request.call_args
        self.assertEqual(kwargs["method"], "GET")
        self.assertEqual(kwargs["url"], "https://api.taqnyat.sa/system/status")
        self.assertEqual(kwargs["json"], {"auth": "token"})

    def test_send_status_http_error_returns_message(self):
        error_response = Mock()
        error_response.text = "bad request"
        http_error = requests.exceptions.HTTPError("400 Client Error", response=error_response)
        response = make_error_response(http_error)
        session = make_session(response=response)

        client = Client("token", session=session)
        result = client.sendStatus()

        self.assertIn("HTTP Error", result)
        self.assertIn("bad request", result)

    def test_balance_ssl_error_returns_message(self):
        session = make_session(side_effect=requests.exceptions.SSLError("ssl failure"))

        client = Client("token", session=session)
        result = client.balance()

        self.assertTrue(result.startswith("SSL Error"))

    def test_senders_requires_authentication(self):
        session = make_session(response=make_json_response({"senders": ["alpha"]}))

        client = Client("", session=session)
        result = client.senders()

        self.assertEqual(result, "Add Authentication")
        session.request.assert_not_called()

    def test_senders_success_returns_json(self):
        payload = {"senders": ["Taqnyat"]}
        response = make_json_response(payload)
        session = make_session(response=response)

        client = Client("token", session=session)
        result = client.senders()

        self.assertEqual(result, payload)
        session.request.assert_called_once()
        _, kwargs = session.request.call_args
        self.assertEqual(kwargs["json"], {"auth": "token"})

    def test_delete_msg_with_key_returns_text(self):
        response = make_text_response("deleted")
        session = make_session(response=response)

        client = Client("token", session=session)
        result = client.deleteMsg("key-1")

        self.assertEqual(result, "deleted")
        session.request.assert_called_once()
        _, kwargs = session.request.call_args
        self.assertEqual(kwargs["method"], "DELETE")
        self.assertEqual(kwargs["url"], "https://api.taqnyat.sa/v1/messages")
        self.assertEqual(
            kwargs["json"],
            {"auth": "token", "deleteKey": "key-1"},
        )


if __name__ == "__main__":
    unittest.main()
