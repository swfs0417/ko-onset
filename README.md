# 한국어 초성 검색기

## 사용법
해당하는 초성 문자(열)이 대상 문자(열)의 어디에 위치하는지 인덱스를 반환합니다. 존재하지 않으면 -1을 반환합니다.

```python
from koonset import find_onset

print(find_onset('ㅇㄴㅎ', '안녕하세요')) # 0
print(find_onset('ㅎㅎㅎ', '안녕하세요')) # -1
```