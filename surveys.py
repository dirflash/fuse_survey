import asyncio

import aiohttp

from cards import survey_card  # noqa: F401
from utils import preferences as p

TEST = True

fuse_date = p.test_fuse_date
attendees: set[str] = set()

max_retries = 3
retry_delay = 5  # Delay between retries in seconds

post_msg_url = "https://webexapis.com/v1/messages/"

headers = {
    "Authorization": p.test_webex_bearer,
    "Content-Type": "application/json",
}


async def send_message(session, email, payload):
    max_retries = 3
    too_many_requests_counter = 0
    too_many_requests_limit = 1
    for i in range(max_retries):
        try:
            async with session.post(
                post_msg_url, json=payload, headers=headers
            ) as response:
                if response.status == 429:
                    # Use the Retry-After header to determine how long to wait
                    retry_after = int(
                        response.headers.get("Retry-After", 5)
                    )  # Default to 5 seconds if Retry-After header is not provided
                    if too_many_requests_counter < too_many_requests_limit:
                        print(
                            f"Too many requests, retrying in {retry_after} seconds..."
                        )
                        too_many_requests_counter += 1
                    await asyncio.sleep(
                        retry_after
                    )  # Pause execution for 'retry_after' seconds
                    continue
                response.raise_for_status()
        except Exception as e:
            print(f"Failed to send message to {email} due to {str(e)}")
        else:
            print(f" Sent message to {email}")
            break


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for person in attendees:
            if TEST:
                email = p.test_email
            else:
                email = f"{person}@cisco.com"
            payload = {
                "toPersonEmail": email,
                "markdown": "Adaptive card response. Open the message on a supported client to respond.",
                "attachments": survey_card.survey_card(p.test_survey_url),
            }
            tasks.append(send_message(session, email, payload))

        await asyncio.gather(*tasks)


if TEST:
    print("Running in test mode")

# add all SEs in the collection to attendees set if they have an "assignments.{fuse_date}" entry
for se in p.cwa_matches.find({"assignments": {"$exists": True}}):
    if se["assignments"].get(fuse_date):
        attendees.add(se["SE"])

print(f"Number of attendees: {len(attendees)}")

# Run the main function
asyncio.run(main())
