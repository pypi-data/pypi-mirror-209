import sys
import requests

# パラメータ定義
EASYPATENT_HOST = "ip-data.jpo.go.jp"
EASYPATENT_CONTENT_TYPE = "application/x-www-form-urlencoded"
EASYPATENT_HEADER = {
    "Host": EASYPATENT_HOST,
    "Content-Type": EASYPATENT_CONTENT_TYPE 
}

def get_token(user, password, token_path):
    grant_type = "password"
    data = {
        "grant_type": grant_type,
        "username": user,
        "password": password
    }
    return requests.post(url=token_path, data=data, headers=EASYPATENT_HEADER)

def get_token_by(refresh_token, token_path):
    grant_type = "refresh_token"
    data = {
        "grant_type": grant_type,
        "refresh_token": refresh_token,
    }
    return requests.post(url=token_path, data=data, headers=EASYPATENT_HEADER)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: %s "username" "password"' % sys.argv[0])
        exit()
    user = sys.argv[1]
    password = sys.argv[2]
    response = get_token(user, password)
    print(response.text)

