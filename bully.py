from flask import Flask
from flask import request
from flask import jsonify
from flask import json

app = Flask(__name__)

@app.route("/keyboard")
def keyboard():
    response = {
        "type" : "buttons",
        "buttons" : ["산책", "사료","배변훈련","입양","미용"]
    }
    response = json.dumps(response, ensure_ascii=False)
    return response


@app.route("/message", methods=["POST"])
def message():
    data = json.loads(request.data)
    content = data["content"]
    if content == "산책":
        text = "--------------- 준비물 ---------------\n▷ 강아지 - 목줄, 하네스 (몸줄)\n▷ 견주 - 배변봉투, 휴지, 물통, 간식\n-------------- 주의사항 --------------\n▷ 최소한의 훈련 후 산책해라\n▷ 강아지의 의사를 존중해라\n▷ 기온과 날씨를 고려해라\n▷ 배설하는 버릇은 좋지않아\n-------------- 미세먼지 --------------\n▷ 호흡기에 치명적인 영향이 있지\n만 난 나가는게 좋더라"
        url = "https://qkrwlgml0704.github.io/chat/img/bottle.jpg"
        label = "강사모카페"
        home_url = "https://cafe.naver.com/dogpalza"
    elif content == "사료":
        text = "-------------- 주의사항 --------------\n▷ 너무 많은 양을 주지마\n▷ 사료는 정해진 규칙대로 줘\n( 아니면 버릇나빠짐 )\n▷ 자율배식은 좋지않다. \n( 관리자네 강아지처럼 뚱뚱해짐 )\n--------------- 급여량 ----------------\n▷ 공식이 있어 근데 귀찮지?\n사료 뒷면에 나이나 체중에 따\n라 권장량이 있으니까 그거 봐"
        url = "https://qkrwlgml0704.github.io/chat/img/b.jpg"
        label = "네이버쇼핑"
        home_url = "https://msearch.shopping.naver.com/search/all.nhn?origQuery=%EA%B0%95%EC%95%84%EC%A7%80%20%EC%82%AC%EB%A3%8C&pagingIndex=1&viewType=lst&sort=rel&showFilter=true&frm=NVSHSRC&selectedFilterTab=brand&query=%EA%B0%95%EC%95%84%EC%A7%80%20%EC%82%AC%EB%A3%8C"
    elif content == "배변훈련":
        text = "-------------- 훈련방법 --------------\n▷ 배변을 하는 장소가 중요함! ★\n▷ 장소를 강아지가 이해하도록 한다\n▷ 배변 성공시 칭찬과 간식 지급\n▷ 잘못된 자리에 실수를 해도 혼\n내지 않고 학습을 시켜라"
        url = "https://qkrwlgml0704.github.io/chat/img/ddong.jpg"
        label = "배변훈련영상"
        home_url = "https://www.youtube.com/results?search_query=%EA%B0%95%EC%95%84%EC%A7%80+%EB%B0%B0%EB%B3%80%ED%9B%88%EB%A0%A8"
    elif content == "입양":
        text = "-------------- 주의사항 --------------\n▷ 샵에서 분양하는 강아지들은 대\n부분 강아지공장 출신이니 분양\n 을 많이 고민해봐. 진짜로.\n▷ 가정을 분양받고 싶다면 그 자\n리에서 실시간으로 사진 요구! \n강아지 혼자 있거나 시간끌면 \n100% 구라임\n▷ 길거리에 분양받지 마. 거의 \n사기꾼들임"
        url = "https://qkrwlgml0704.github.io/chat/img/E.jpg"
        label = "입양사이트"
        home_url = "http://www.parkzoo.net/default/"
    elif content == "미용":
        text = "-------------- 발톱깎기 --------------\n▷ 한 달에 한 번 정도만 깎아줘라\n▷ 강아지가 싫어하면 목욕이 끝나\n고 말랑해졌을 때 스-을쩍 해줘\n--------------- 털 미용 ---------------\n▷ 컷을 해도 탈모는 줄지 않아.. \n▷ 너무 짧게 밀면 열과 자외선\n등의자극이 가해져서 트러블이 일어남( 그거 개 아픔.. )"
        url = "https://qkrwlgml0704.github.io/chat/img/M.jpg"
        label = "미용사이트"
        home_url = "http://puppylounge.co.kr/category/%EA%B0%95%EC%95%84%EC%A7%80-%EB%AF%B8%EC%9A%A9/49/"

    response = {
      "message": {
        "text": text,
        "photo": {
          "url": url,
          "width": 640,
          "height": 600
        },
        "message_button": {
          "label": label,
          "url": home_url
        }
      },
      "keyboard": {
        "type": "buttons",
        "buttons": [
            "산책",
            "사료",
            "배변훈련",
            "입양",
            "미용"
        ]
      }
    }

    response = json.dumps(response, ensure_ascii=False)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # app.run(host="localhost", port=80)
    # app.run(host="127.0.0.1", port=80)
    # flask 예시 : app.run(host="0.0.0.0", port=5000)
