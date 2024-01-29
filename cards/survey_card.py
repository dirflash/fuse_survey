def survey_card(survey_link: str) -> dict:
    main_msg = (
        "Hello, SE!\n\nThank you for participating in the most recent Fuse session. Your feedback is important. "
        "Once you complete the survey, you will have a chance to win some Connected Recognition!"
    )
    send_survey_card = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
                {
                    "type": "ImageSet",
                    "images": [
                        {
                            "type": "Image",
                            "url": "https://user-images.githubusercontent.com/10964629/225653491-e3c2920c-419d-45ab-ba9f-b0add6138e33.png",
                            "height": "100px",
                            "width": "400px",
                            "size": "Medium",
                        }
                    ],
                },
                {
                    "type": "TextBlock",
                    "text": "Fuse Bot Mission Control",
                    "wrap": True,
                    "horizontalAlignment": "Center",
                    "fontType": "Monospace",
                    "size": "Large",
                    "weight": "Bolder",
                },
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "TextBlock",
                                    "wrap": True,
                                    "fontType": "Monospace",
                                    "text": "Post Session Survey Request",
                                    "horizontalAlignment": "Center",
                                    "size": "Medium",
                                    "color": "Default",
                                    "weight": "Bolder",
                                }
                            ],
                        }
                    ],
                },
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": main_msg,
                            "wrap": True,
                            "fontType": "Monospace",
                            "size": "Small",
                            "weight": "Bolder",
                        },
                        {
                            "type": "Container",
                            "items": [
                                {
                                    "type": "ColumnSet",
                                    "columns": [
                                        {"type": "Column", "width": "stretch"},
                                        {
                                            "type": "Column",
                                            "width": "stretch",
                                            "items": [
                                                {
                                                    "type": "ActionSet",
                                                    "actions": [
                                                        {
                                                            "type": "Action.OpenUrl",
                                                            "id": "survey_url",
                                                            "title": "Launch Survey",
                                                            "url": survey_link,
                                                        }
                                                    ],
                                                }
                                            ],
                                        },
                                        {"type": "Column", "width": "stretch"},
                                    ],
                                }
                            ],
                        },
                    ],
                },
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.3",
        },
    }
    return send_survey_card
