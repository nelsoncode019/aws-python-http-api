from requests import get


def hello(event, context):
    response = get("https://dev.to/api/articles?tag=python")
    return {"statusCode": 200, "body": response.text}
