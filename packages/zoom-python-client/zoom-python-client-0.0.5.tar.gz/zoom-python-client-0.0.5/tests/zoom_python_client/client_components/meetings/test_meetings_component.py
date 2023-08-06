import responses

from tests.zoom_python_client.base_test_case import TestCaseWithAuth
from zoom_python_client.client_components.meetings.meetings_component import (
    MeetingsComponent,
)
from zoom_python_client.zoom_api_client import ZoomApiClient


class TestMeetingsComponent(TestCaseWithAuth):
    @responses.activate
    def test_get_meeting(self):
        responses.add(
            responses.GET,
            "http://localhost/meetings/12345",
            json={"response": "ok"},
            status=200,
        )
        zoom_client = ZoomApiClient("aaa", "bbb", "ccc", "http://localhost")
        component = MeetingsComponent(zoom_client)
        user = component.get_meeting("12345")
        assert user == {"response": "ok"}

    @responses.activate
    def test_get_meeting_token(self):
        responses.add(
            responses.GET,
            "http://localhost/meetings/12345/token",
            json={"response": "ok"},
            status=200,
        )
        zoom_client = ZoomApiClient("aaa", "bbb", "ccc", "http://localhost")
        component = MeetingsComponent(zoom_client)
        user = component.get_meeting_token("12345")
        assert user == {"response": "ok"}
