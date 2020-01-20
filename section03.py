# Section03
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 현재 실습은 파이썬에서 하지만 이미 아나콘다 환경을 사용중이기에
# 파이썬만 설치되어 실습하는 내용과는 상이하여
# 계속 콘다에서 파이썬이 실행되고 있다.
# 그냥 콘다 환경에 simplejson 을 설치하여 해결
# 아마 .vscode 폴더의 settings.json 의 인터프리터를
# 콘다의 파이썬이 아닌 가상환경의 파이썬으로 잡아주면 될듯하다

# 외부 설치 패키지 테스트
import simplejson as json  

test_dict = {'1':95, '4':77, '3':65, '5':100, '2':88}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))