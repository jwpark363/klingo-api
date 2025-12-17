## K-Lingo 프로젝트

언리얼 엔진, LLM, RAG, FastAPI를 이용한 외국인 대상 한국어 교육 솔루션 ( 현재 진행중 )
<img src="https://raw.githubusercontent.com/jwpark363/klingo-api/refs/heads/main/screen.png" width="480px">
- https://github.com/jwpark363/klingo-api

- 개요
    - 언리얼 엔진, FastAPI+SQLModel ORM+PostgreSQL+Redis+JOSE jwt, llm+stt+tts+ocr 기술을 이용한 외국인 대상 게임형식의 한국어 학습 시스템
    - 한국어 읽기, 듣기, 쓰기, 말하기 학습을 2인 협동 게임 형식 진행으로 재미있게 언어를 학습 할 수 있도록 구성
    - 사용자의 레벨을 감안하여 각 시나리오의 스테이지를 동적으로 생성(단어의 레벨은 세종학당의 레벨 기준 참고)
- 역할
    - FastAPI, ORM, JWT, Redis, RQ(Redis Queue)등 주요 시스템 설계 및 백엔드 개발 진행
    - 백엔드 요소별 기술 선정 및 적용, LLM 이용 시나리오 생성 및 번역 처리
    - 필요 관리 기능 개발
- 구현 기술
    
    <img src="https://raw.githubusercontent.com/jwpark363/klingo-api/refs/heads/main/system.png" width="480px">
    
    - Python FastAPI 백엔드 구성, SQLModel ORM 구현
    - Jose jwt 기능 구현, Redis 및 RQ 기능 구현, loguru 이용 console/file 로그 처리
    - llm 이용한 사전 시나리오 정보 생성 및 번역 에이전트 기능 구현(ollama + LG EXAONE)
    - 생성한 사전 정보를 이용 레벨 감안한 랜덤 스테이지 정보 생성 로직 구현
- 성과
    - FastAPI + JWT + ORM + PostgreSQL + Redis + RQ 이용한 백앤드 전체 구성 설계 및 개발
    - 국내 개발한 LLM(LG EXAONE) 테스트 및 적용
    - ollama 및 vllm 테스트 및 적용
- 리뷰
    - 백엔드 구성하면서 기능 개선 요구에 맞추어 Redis 와 Queue를 신속히 추가하여 개선함
        - 진행 시 개발된 사항들에 영향을 최소화 하면서 진행하는 부분들을 잘 수행하였음
    - 서비스를 개발함에 있어 LLM등 AI 에이전트 기술들로 인해 구현의 범위를 확장 할 수 있었음