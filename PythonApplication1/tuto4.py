from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, runtime_checkable
import time
import functools

# ==================================================
# 1. 불변 설정 객체 (Immutable Configuration)
# ==================================================
@dataclass(frozen=True)  #dataclass frozen const 느낌
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