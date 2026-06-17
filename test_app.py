import unittest
from unittest.mock import patch

from app import process_user_data, unused_function


class TestProcessUserData(unittest.TestCase):
    def test_empty_list_returns_empty(self):
        self.assertEqual(process_user_data([]), [])

    def test_all_users_have_name(self):
        users = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
        self.assertEqual(process_user_data(users), ["Alice", "Bob", "Charlie"])

    def test_mixed_users_only_named_included(self):
        users = [{"name": "Alice"}, {}, {"name": "Bob"}, {}]
        self.assertEqual(process_user_data(users), ["Alice", "Bob"])

    def test_no_users_have_name(self):
        users = [{}, {"age": 30}, {"email": "x@example.com"}]
        self.assertEqual(process_user_data(users), [])

    def test_single_user_with_name(self):
        users = [{"name": "Solo"}]
        self.assertEqual(process_user_data(users), ["Solo"])

    def test_user_with_extra_keys_and_name_is_included(self):
        users = [{"name": "Alice", "age": 25, "email": "alice@example.com"}]
        self.assertEqual(process_user_data(users), ["Alice"])

    def test_user_with_empty_string_name_is_included(self):
        # "name" key presence (not value truthiness) determines inclusion
        users = [{"name": ""}]
        self.assertEqual(process_user_data(users), [""])

    def test_user_with_none_name_is_included(self):
        # Only key presence is checked; None values are still appended
        users = [{"name": None}]
        self.assertEqual(process_user_data(users), [None])

    def test_preserves_order_of_names(self):
        users = [{"name": "C"}, {"name": "A"}, {"name": "B"}]
        self.assertEqual(process_user_data(users), ["C", "A", "B"])

    def test_returns_list_type(self):
        self.assertIsInstance(process_user_data([]), list)

    def test_duplicate_names_all_appended(self):
        users = [{"name": "Alice"}, {"name": "Alice"}]
        self.assertEqual(process_user_data(users), ["Alice", "Alice"])

    def test_mixed_with_only_last_having_name(self):
        # Regression: ensure trailing named user is not skipped
        users = [{}, {}, {"name": "Last"}]
        self.assertEqual(process_user_data(users), ["Last"])


class TestUnusedFunction(unittest.TestCase):
    @patch("app.time.sleep")
    def test_returns_unused_string(self, mock_sleep):
        result = unused_function()
        self.assertEqual(result, "unused")

    @patch("app.time.sleep")
    def test_calls_sleep_with_5_seconds(self, mock_sleep):
        unused_function()
        mock_sleep.assert_called_once_with(5)

    @patch("app.time.sleep")
    def test_sleep_is_called_exactly_once(self, mock_sleep):
        unused_function()
        self.assertEqual(mock_sleep.call_count, 1)


if __name__ == "__main__":
    unittest.main()
