from lib.request_time import *
from unittest.mock import Mock
import json

def test_time():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    time_mock = Mock()
    time_mock = 1668512312
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = json.dumps({"unixtime":1668512312})
    time = TimeError(requester_mock,time_mock)
    result = time.error()
    assert result == 0