from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello, world!"


@app.route("/expert/review", methods=['POST'])
def review():
    excel_file = request.files['file']
    # 엑셀 파일 받아서 파싱
    # 검증 필요한 열들 플랫폼에 검증 요청
    excel_rows = __parse_excel(excel_file)

    review_results = []
    for row in excel_rows:
        validate_result = __request_part_to_platform(row)
        review_results.append(validate_result)

    # response = review_results
    # 응답 예시
    response = {
        "targetName": "Diode",
        "passReview": False,
        "reviewResults": [
            {
                "partName": "row 1 part name",
                "designValue": 1,
                "passValidate": True,
            },
            {
                "partName": "row 2 part name",
                "designValue": 2.5,
                "passValidate": False,
            },
            {
                "partName": "row 3 part name",
                "designValue": 30,
                "passValidate": True,
            },
            {
                "partName": "row 4 part name",
                "designValue": 400.4,
                "passValidate": False,
            }
        ]
    }

    return response


def __parse_excel(excel_file):
    # 엑셀 파싱후 검증 필요한 rows 반환

    return []


def __request_part_to_platform(parsed_row):
    # dockerized url
    url = "http://platform/review/part"

    # local url
    # url = "http://localhost:8080/review/part"
    headers = {'Content-Type': 'application/json'}
    example_body = {
        "partName": "minTa",
        "note": "1",
        "unit": "℃",
        "designValue": "2"
    }

    # body = parsed_row
    body = example_body

    response = requests.post(url, json=body, headers=headers)
    return response.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
