import os, json
import redis.asyncio as redis
from typing import Dict, Any

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])
class StateStore:
    """
        Redis Service Class
    """
    def __init__(self) -> None:
        self.state_store: redis.Redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

    async def save_user_state(self, token: str, state_data: Dict[str, Any]):
        """
            사용자 게임 진행 현황 정보를 저장하기 위해
        """
        await self.state_store.set(f"token:{token}", json.dumps(state_data))

    async def load_user_state(self, token: str) -> Dict[str, Any]:
        """
            토큰 정보를 이용 저장된 정보 가져오기
        """
        data = await self.state_store.get(f"token:{token}")
        if data:
            return json.loads(data)
        return {}