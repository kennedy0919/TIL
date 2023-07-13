작성된 Markdown 문서는 다른 프로그램에 의해 변환되어 출력됨

# 개발자로 성장하기
- 대체 어디서부터 시작해서 어디까지 해야할까? -> 이런식으로

# 마크다운 미리보기 켜는 법
1. 마크다운 파일 마우스 우측 클릭(파일의 확장자는.md)
2. Open Preview클릭

# Heading
문서의 단계별 제목으로 사용
#의 개수에 따라 제목의 수준을 구별
# 제목1
## 제목2
### 제목3

# 리스트
- 목록을 표시하기 위해 사용
- 순서가 있는 리스트와 순서가 없는 리스트 제공
1. 순서가
    1. 있는
2. 리스트

- 순서가
    - 없는
- 리스트

# 링크 & 이미지
- 특정 주소를 사용해 다른 페이지로 이동하는 링크 혹은 이미지를 출력

[google](https://www.google.com)
![이미지](https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzA1MjFfMTU3%2FMDAxNjg0NjUyMjUxMzU2.F2VS2eN4cCZ5Paj1hOgLR5zcER6Fhk4FS9AhHbr8JEEg.rVg2bxK84mcEBeE1Ndik6v-RgSru8_XRnlULvEXKWjgg.JPEG.edenpet6434%2F1684652252414.jpg&type=sc960_832)
# 텍스트 관련 문법
**굵게**
*기울임*
~~취소선~~
# 수평선
- 단락을 구분할때 사용하는 수평선
- '-(hypen)'을 3개이상 적으면 작동
# CLI 
- 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
# GUI
- 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

# CLI 기초문법
- touch   파일생성
- mkdir   새 디렉토리 생성
- ls      현재 작업 중인 디렉토리 내부의 폴더/파일 목록을 출력
- cd   현재 작업 중인 디렉토리를 변경
- start 폴더/파일을 열기
- rm 파일삭제

# git 이란?
- 분산 버전 관리 시스템(버전관리란 변화를 기록하고 추적하는 것)

# git 의 역할
- 코드의 버전(히스토리)을 관리
    - 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

# git의 3가지 영역
1. Working directory (작업영역) 
2. Staging Area (중간단계 버전관리가 필요한 파일들은 여기를 거처감), 
3. Repository (변경사항을 기록하는곳)

# commit 
- 버전
- 변경된 파일들을 저장하는 행위이다

# git 의 동작
1. git init : 로컬 저장소 설정
2. git add : 변경사항이 있는 파일을 staging area에 추가
3. git commit : staging area에 있는 파일들을 저장소에 기록

# git 의 관리를 받는지 확인하는 방법
1. git 의 관리를 받기 시작한 디렉토리 내에서는 (master) 가 표시됨
2. 파일에 .git이라는 파일이 생성됨

# git 파일생성 순서
1. git init 
2. git add .
3. git commit -m ""
    1. git config 메일주소
    2. git config 유저네임
    3. global로 설정 후 앞으로 재입력하지 않음
4. git push origin master
# 원격저장소
- gitlab 혹은 github와 같은 원격저장소에 저장할 수 있음

# git 파일 원격저장소 연결방법
1. git remote add origin 주소

# git 파일 원격저장소에서 clone 하는 방법
1. cd 원격저장소 파일명
2. git clone 주소

