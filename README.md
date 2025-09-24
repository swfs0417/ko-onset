# 한국어 초성 검색기

## 사용법

```python
from koonset import find_onset

print(find_onset('ㅇㄴㅎ', '안녕하세요')) # 0
print(find_onset('ㅎㅎㅎ', '안녕하세요')) # -1
```