"""Module Contract."""
import re

from flunt.localization.flunt_regex_patterns import FluntRegexPatterns
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class EmailValidationContract(Notifiable):
    """
    Class Email Validation Contract.

    This class provides methods for validating email addresses and adding notifications based on the validation results.

    Methods:
        - is_email(value: str, key: str, message: str) -> self:
            Checks if the provided value is a valid email address and adds a notification if it is not.

        - is_not_email(value: str, key: str, message: str) -> self:
            Checks if the provided value is not a valid email address and adds a notification if it is.

    Note:
        - The validity of the email address is determined by the internal method `_valid_email`.
    """

    def is_email(self, value: str, key: str, message: str):
        """
        Check if the provided value is a valid email address and adds a notification if it is not.

        Args:
            value (str): The value to be checked as an email address.
            key (str): The key or identifier associated with the notification.
            message (str): The message of the notification to be added.

        Returns:
            self: The current instance of the class.

        Note:
            - The validity of the email address is determined by the internal method `_valid_email`.
            - If the provided value is not a valid email address, a notification is added to the current instance
            using the provided key and message.
            - If the provided value is a valid email address, no notification is added.

        Example:
            obj = MyClass()

            obj.is_email("example@example.com", "EmailCheck", "Please enter a valid email address")
        """
        if not self._valid_email(value):
            self.add_notification(Notification(key, message))

        return self

    def is_not_email(self, value: str, key: str, message: str):
        """
        Check if the provided value is not a valid email address and adds a notification if it is.

        Args:
            value (str): The value to be checked as an email address.
            key (str): The key or identifier associated with the notification.
            message (str): The message of the notification to be added.

        Returns:
            self: The current instance of the class.

        Note:
            - If the provided value matches the valid email address pattern, a notification is added to the current instance using the provided key and message.
            - If the provided value does not match the valid email address pattern, no notification is added.

        Example:
            obj = MyClass()

            obj.is_not_email("example@example.com", "EmailCheck", "Value should not be a valid email address")
        """
        if self._valid_email(value):
            self.add_notification(Notification(key, message))

        return self

    def _valid_email(self, value):
        """
        Check if the provided value matches the valid email address pattern.

        Args:
            value (str): The value to be checked as an email address.

        Returns:
            Match[str] | None
        """
        return re.match(
            FluntRegexPatterns().email_regex_pattern,
            value,
            re.IGNORECASE,
        )
