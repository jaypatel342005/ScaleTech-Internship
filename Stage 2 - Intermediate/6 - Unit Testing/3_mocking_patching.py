import pytest
from unittest.mock import Mock, patch, MagicMock
from user_service import get_user, get_post_title, send_notification

# mocking = replacing real dependencies (APIs, DBs, emails) with fake objects during testing
# this makes tests fast, reliable, and independent of external services
# patch() temporarily replaces something only for the duration of that one test


# Mock() creates a fake object - you can call any method on it and set any return value
def test_mock_basic():
    mock_fn = Mock()
    mock_fn.return_value = 42   # whenever mock_fn() is called, it returns 42
    assert mock_fn() == 42


# mock a method on a fake object (simulating payment API without a real one)
def test_mock_return_value():
    payment_api = Mock()
    payment_api.pay.return_value = True   # fake pay() always succeeds

    result = payment_api.pay(500)
    assert result is True


# side_effect with a list - mock returns a different value on each successive call
def test_mock_side_effect_list():
    mock_fn = Mock()
    mock_fn.side_effect = [10, 20, 30]   # 1st call=10, 2nd=20, 3rd=30

    assert mock_fn() == 10
    assert mock_fn() == 20
    assert mock_fn() == 30


# side_effect with an exception - useful to test how your code handles failures
def test_mock_side_effect_exception():
    mock_fn = Mock()
    mock_fn.side_effect = ValueError("invalid input")   # every call raises ValueError

    with pytest.raises(ValueError):
        mock_fn()


# assert_called_once_with - verify the mock was called exactly once AND with specific args
# this ensures your code actually communicated with the dependency correctly
def test_mock_assert_called():
    mock_api = Mock()
    mock_api.send("hello")

    mock_api.send.assert_called_once()              # was it called exactly once?
    mock_api.send.assert_called_once_with("hello")  # was it called with "hello"?


# assert_not_called - verify the mock was never called (nothing triggered it)
def test_mock_not_called():
    mock_api = Mock()
    mock_api.send.assert_not_called()


# @patch replaces 'requests.get' inside user_service module for the duration of this test
# mock_get is the fake replacement - pytest injects it as the last parameter
# IMPORTANT: patch where the name is USED, not where it is defined
# so patch "user_service.requests.get" not "requests.get"
@patch("user_service.requests.get")
def test_get_user(mock_get):
    # set what the fake response returns when .json() is called
    mock_get.return_value.json.return_value = {
        "name": "Jay Patel",
        "email": "jay@example.com"
    }

    result = get_user(1)   # calls the real get_user() but hits our fake requests.get

    assert result["name"] == "Jay Patel"
    assert result["email"] == "jay@example.com"

    # also verify get_user() built the correct URL
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/1"
    )


# simulate a successful API response (status_code=200)
@patch("user_service.requests.get")
def test_get_post_title(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "title": "Learning Python"
    }

    result = get_post_title(1)
    assert result == "Learning Python"


# simulate a failed API response - test that ConnectionError is raised on 404
@patch("user_service.requests.get")
def test_get_post_title_fails(mock_get):
    mock_get.return_value.status_code = 404   # fake 404 Not Found

    with pytest.raises(ConnectionError):
        get_post_title(99)


# patch as a context manager - another way to use patch (no decorator needed)
# the patch is only active inside the 'with' block
def test_patch_context_manager():
    with patch("user_service.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "name": "Rahul",
            "email": "rahul@example.com"
        }

        result = get_user(2)
        assert result["name"] == "Rahul"
    # outside the 'with' block, requests.get is restored to the real function


# mock multiple methods on a fake database object
def test_mock_object_method():
    mock_db = Mock()
    mock_db.get_user.return_value = {"id": 1, "name": "Jay"}
    mock_db.save.return_value = True

    user = mock_db.get_user(1)
    assert user["name"] == "Jay"

    saved = mock_db.save(user)
    assert saved is True

    # verify the correct calls were made in the correct order
    mock_db.get_user.assert_called_once_with(1)
    mock_db.save.assert_called_once()


# MagicMock is like Mock but also supports Python's magic/dunder methods
# use MagicMock when you need to fake __len__, __str__, __getitem__, etc.
def test_magic_mock():
    mock_list = MagicMock()
    mock_list.__len__.return_value = 5   # fake len() to return 5

    assert len(mock_list) == 5


# patch a function inside user_service and call it via the module
# calling user_service.send_notification() ensures the patched version is used
@patch("user_service.send_notification")
def test_send_notification_called(mock_notify):
    mock_notify.return_value = True

    import user_service
    result = user_service.send_notification("jay@example.com", "welcome!")
    assert result is True
    mock_notify.assert_called_once_with("jay@example.com", "welcome!")
