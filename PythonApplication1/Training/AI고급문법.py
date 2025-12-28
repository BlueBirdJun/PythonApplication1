# Dependency Injection (FastAPI / 테스트 핵심)
class Repo:
    def get(self):
        return "data"

class Service:
    def __init__(self, repo: Repo):
        self.repo = repo

    def run(self):
        return self.repo.get()

# 전략 패턴 (모델 교체용)
class Strategy:
    def run(self, x): ...

class AddOne(Strategy):
    def run(self, x): return x + 1

class MultiplyTwo(Strategy):
    def run(self, x): return x * 2

def execute(strategy: Strategy, x):
    return strategy.run(x)

print(execute(AddOne(), 3))
print(execute(MultiplyTwo(), 3))

# Factory 패턴 (모델 로딩)
def model_factory(name: str):
    if name == "gpt":
        return lambda x: f"GPT:{x}"
    if name == "bert":
        return lambda x: f"BERT:{x}"
    raise ValueError()

model = model_factory("gpt")
print(model("hello"))


# Lazy Loading (무거운 모델 지연 로딩)
class ModelLoader:
    _model = None

    @property
    def model(self):
        if self._model is None:
            print("모델 로딩...")
            self._model = lambda x: x.upper()
        return self._model

loader = ModelLoader()
print(loader.model("hi"))



# Cache 패턴 (AI 응답 가속)
from functools import lru_cache

@lru_cache(maxsize=100)
def infer(text: str) -> str:
    print("실제 계산")
    return text.upper()

infer("hello")
infer("hello")  # 캐시

# Pipeline 패턴 (전처리 → 추론 → 후처리)
def preprocess(x): return x.strip()
def infer(x): return x.upper()
def postprocess(x): return f"[{x}]"

def pipeline(x):
    for step in (preprocess, infer, postprocess):
        x = step(x)
    return x

print(pipeline(" hello "))

# Context Manager (리소스 관리)
from contextlib import contextmanager

@contextmanager
def db_session():
    print("OPEN")
    yield "session"
    print("CLOSE")

with db_session() as s:
    print(s)


# Async 병렬 처리 (AI API 호출)
import asyncio

async def call(i):
    await asyncio.sleep(1)
    return i

async def main():
    results = await asyncio.gather(
        call(1), call(2), call(3)
    )
    print(results)

asyncio.run(main())


# Retry 패턴 (외부 AI API 안정성)
import time

def retry(fn, retries=3):
    for i in range(retries):
        try:
            return fn()
        except Exception:
            time.sleep(1)
    raise RuntimeError("실패")

retry(lambda: 1 / 0)

# Feature Toggle (실험용 모델)
USE_NEW_MODEL = False

def infer(x):
    if USE_NEW_MODEL:
        return f"NEW:{x}"
    return f"OLD:{x}"
