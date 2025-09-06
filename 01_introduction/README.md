# OS01 - Introduction

**한줄 핵심**: 운영체제(OS)는 사용자/응용과 하드웨어 사이의 **중재자**이자 **자원 할당자**다.

**키워드**: 운영체제 목표, 컴퓨터 시스템 계층, 부팅/인터럽트, 시스템 콜, 듀얼 모드(User/Kernel),  
멀티프로그래밍 vs 시분할, 스토리지 계층·캐싱

## 배운 것
- OS의 두 관점: **Resource Allocator** & **Control Program**
- 부팅 흐름: 부트스트랩 → 커널 적재 → 데몬/서비스 시작
- 인터럽트/트랩과 **시스템 콜**의 호출/반환 흐름
- **멀티프로그래밍**(CPU 유휴시간 최소화) vs **시분할**(응답시간 최적화)
- **듀얼 모드**와 **특권 명령**(커널에서만 실행)
- 저장장치 **계층 구조**와 **캐싱** 아이디어

## 실습/예제
- (예시) `code/01_syscall_getpid.c` — 사용자 프로그램이 **시스템 콜**을 통해 커널 서비스를 이용
  - 빌드: `gcc code/01_syscall_getpid.c -o getpid_demo`
  - 실행: `./getpid_demo`
  - (선택) 리눅스: `strace ./getpid_demo | grep -E '(execve|getpid|write)'`

## 체크포인트
- “**프로세스 = 실행 중인 프로그램**” 정의를 말로 설명할 수 있는가?
- 시분할은 **상호작용/응답시간**, 멀티프로그래밍은 **CPU 활용도**를 목표로 함
- 시스템 콜 시 **유저→커널 모드 전환**과 반환 흐름을 그림 없이 말로 설명 가능?

## 참고
- 강의 슬라이드: Chapter 1 Introduction
- Silberschatz, Galvin, Gagne, *Operating System Concepts*, 10th Ed.