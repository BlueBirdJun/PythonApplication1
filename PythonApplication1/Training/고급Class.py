"""
advanced_engine.py

✔ 이 파일 하나에 담긴 것
- 추상 클래스(ABC)
- 의존성 주입(DI)
- 불변 설정 객체
- 데코레이터 (관측성)
- 컨텍스트 매니저 (자원 관리)
- 캐시 전략
- 시니어 설계 패턴

이 파일을 이해하면:
"파이썬 클래스는 어느 정도 안다" → "실무 고급자"
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, runtime_checkable
import time
import functools


# ==================================================
# 1. 불변 설정 객체 (Immutable Configuration)
# ==================================================
@dataclass(frozen=True)
class AppConfig:
    """
    애플리케이션 전역 설정

    frozen=True:
    - 런타임 중 설정 변경 방지
    - 장애 분석 / 재현에 매우 유리
    """
    cache_ttl: int
    timeout: int


# ==================================================
# 2. 추상 인터페이스 (Data Source Contract)
# ==================================================
class DataSource(ABC):
    """
    데이터 소스 인터페이스

    API, DB, 파일, 메시지큐 등
    어떤 구현체든 이 계약만 지키면 교체 가능
    """

    @abstractmethod
    def fetch(self, key: str) -> dict:
        """
        데이터를 가져오는 책임
        """
        pass


# ==================================================
# 3. Protocol (Cache 인터페이스)
# ==================================================
@runtime_checkable
class Cache(Protocol):
    """
    구조적 타이핑 (덕 타이핑)

    상속 필요 없음
    아래 메서드만 있으면 Cache 로 인정
    """

    def get(self, key: str):
        ...

    def set(self, key: str, value, ttl: int):
        ...


# ==================================================
# 4. 캐시 구현체 (In-Memory Cache)
# ==================================================
class MemoryCache:
    """
    간단한 메모리 캐시

    실무에선 Redis 등으로 교체 가능
    Engine 수정 필요 없음
    """

    def __init__(self):
        self._store = {}

    def get(self, key: str):
        data = self._store.get(key)
        if not data:
            return None

        value, expire_at = data

        # TTL 만료 검사
        if expire_at < time.time():
            del self._store[key]
            return None

        return value

    def set(self, key: str, value, ttl: int):
        self._store[key] = (value, time.time() + ttl)


# ==================================================
# 5. 실제 데이터 소스 구현 (API 예시)
# ==================================================
class ApiDataSource(DataSource):
    """
    외부 API 호출 흉내

    실제 requests / httpx 사용 가능
    """

    def fetch(self, key: str) -> dict:
        print(f"[API] 데이터 요청: {key}")
        time.sleep(0.2)  # 네트워크 지연 흉내
        return {
            "key": key,
            "value": "from_api",
            "ts": time.time()
        }


# ==================================================
# 6. 컨텍스트 매니저 (자원 관리)
# ==================================================
class ResourceContext:
    """
    외부 자원 관리

    DB Connection
    Lock
    API Session
    """

    def __enter__(self):
        print("[RESOURCE] 열기")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[RESOURCE] 닫기")

        if exc_type:
            print(f"[ERROR] {exc_val}")

        # False → 예외를 숨기지 않음
        return False


# ==================================================
# 7. 관측성 Decorator (로깅 / 메트릭)
# ==================================================
def observe(func):
    """
    메서드 실행 시간 측정

    비즈니스 로직과 완전 분리
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = (time.time() - start) * 1000
            print(f"[METRIC] {func.__name__} {elapsed:.2f}ms")
    return wrapper


# ==================================================
# 8. 핵심 엔진 (시니어의 얼굴)
# ==================================================
class DataEngine:
    """
    ⭐ 이 파일의 핵심 클래스 ⭐

    - 비즈니스 흐름 제어
    - 구현 세부사항에 의존하지 않음
    - 교체 / 테스트 / 확장 용이
    """

    def __init__(
        self,
        source: DataSource,
        cache: Cache,
        config: AppConfig
    ):
        self._source = source
        self._cache = cache
        self._config = config

    @observe
    def get_data(self, key: str) -> dict:
        """
        데이터 조회 흐름

        1. 캐시 확인
        2. 없으면 데이터 소스 조회
        3. 캐시 저장
        """
        cached = self._cache.get(key)
        if cached:
            print("[CACHE] HIT")
            return cached

        with ResourceContext():
            data = self._source.fetch(key)

        self._cache.set(key, data, self._config.cache_ttl)
        return data


# ==================================================
# 9. 조립 (Composition Root)
# ==================================================
if __name__ == "__main__":
    """
    애플리케이션 시작 지점

    모든 의존성은 여기서 조립
    """

    config = AppConfig(
        cache_ttl=3,
        timeout=5
    )

    engine = DataEngine(
        source=ApiDataSource(),
        cache=MemoryCache(),
        config=config
    )

    print(engine.get_data("A"))
    print(engine.get_data("A"))  # 캐시 히트
    time.sleep(4)
    print(engine.get_data("A"))  # 캐시 만료
