190709



### git 기본

```
git init
```

* 주의! master 없을 때 해야 함 



```git
git add helloworld.py
git commit -m 

#-로 시작하면 보통 옵션 "로그인 기능 구현"

"git congif --global user.name "John"
```

add 커밋할 목록에 추가

commit 커밋 만들기(snapshot)

push 로컬 현재까지의 커밋 기록된 곳에 새로 생산한 커밋들 반영하기 (원격저장소에 반영시키는 것)





```
git status
```

* 등록 안 한 것 체크 



```
git log
```



```
git remote -v
```

* 원격 저장소 관리 키워드

```
git pull remote origin
```

추가 commit 내역 업데이트 시키기...



##### 집에서 작업하고 싶을 때

```
$ mkdir 우리집
$ cd 우리집
$ git clone https://github.com/susuminmin/TIL.git
```

...

다시 commit하고... 



