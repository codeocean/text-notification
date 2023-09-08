import argparse
import sys
import time

from co_tools.get_logger import LOGGER
from twilio.rest import Client

import capsule_secrets
import util

account_sid = capsule_secrets.SID
auth_token = capsule_secrets.AUTH_TOKEN
account_phone = capsule_secrets.PHONE

def main():
    if not account_sid or not auth_token or not account_phone:
        sys.exit("Please attach all required secrets to this capsule. See README.md")
    parser = argparse.ArgumentParser(description="A text notification capsule.")
    parser.add_argument(
        "--phone",
        required=True,
        help="The phone number to send the text notification to",
    )
    parser.add_argument(
        "--notification",
        default="Code Ocean text notification capsule",
        help="The message to be sent in your text notification.",
    )

    if args := parser.parse_args():
        LOGGER.info("args successfully parsed")
    else:
        LOGGER.error("args not successfully parsed")
        parser.print_usage()

    if not int(args.phone):
        sys.exit("You must enter a phone number in the app panel.")
    send_to_phone = util.scrub_phone(phone=args.phone)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=f"+1{send_to_phone}",
        from_=f"{account_phone}",
        body=args.notification,
    )

    # error and above log levels print to console
    LOGGER.error(
        f"Sent the following message to {message.to}: {message.body}\nsid={message.sid}\ncurrent status={message.status}"
    )

    while True:
        status = client.messages(message.sid).fetch()
        # https://www.twilio.com/docs/sms/guides/outbound-message-logging#message-statuses
        if (
            "delivered" in status.status
            or "undelivered" in status.status
            or "failed" in status.status
        ):
            LOGGER.error(
                f"Notification with sid={message.sid} is now in status '{status.status}'."
            )
            break
        else:
            LOGGER.error(
                f"Notification with sid={message.sid} is currently in status '{status.status}'. Will check status again in 5 seconds..."
            )
            time.sleep(5)


if __name__ == "__main__":
    main()
