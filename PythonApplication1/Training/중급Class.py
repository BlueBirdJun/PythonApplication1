import time
import functools
from typing import Callable, Any


# =========================
# 1. Descriptor (속성 접근 제어)
# =========================
class PositiveInt:
    """
    양수만 허용하는 Descriptor
    (설정값 검증용)
    """
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("값은 양수여야 합니다.")
        setattr(obj, self.private_name, value)


# =========================
# 2. Decorator (재시도 로직)
# =========================
def retry(max_retry: int = 3, delay: float = 1.0):
    """
    함수 실패 시 자동 재시도
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retry + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retry:
                        raise
                    print(f"[RETRY] {attempt}/{max_retry} 실패: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator


# =========================
# 3. Context Manager (자원 관리)
# =========================
class ApiSession:
    """
    API 세션 관리 (열고 / 닫기)
    """
    def __enter__(self):
        print("API 세션 열림")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("API 세션 닫힘")
        if exc_type:
            print(f"예외 발생: {exc_val}")
        return False  # 예외 전파


# =========================
# 4. 메인 실무 클래스
# =========================
class ApiClient:
    """
    실무용 API Client
    """

    timeout = PositiveInt()   # Descriptor 사용
    retry_count = PositiveInt()

    def __init__(self, base_url: str, timeout: int = 3, retry_count: int = 3):
        self.base_url = base_url
        self.timeout = timeout
        self.retry_count = retry_count

    @retry()
    def _request(self, endpoint: str) -> dict:
        """
        내부 전용 API 호출
        """
        print(f"요청: {self.base_url}{endpoint}")
        # 일부러 실패 상황 흉내
        if endpoint == "/fail":
            raise ConnectionError("네트워크 오류")
        return {"status": "ok", "endpoint": endpoint}

    def get(self, endpoint: str) -> dict:
        """
        외부 노출 메서드
        """
        with ApiSession():
            return self._request(endpoint)
