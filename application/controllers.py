from multiprocessing import Pool
from datetime import datetime
from typing import List
from models import BatchedRequest, BatchedResponse
import logging

class Controllers:
    # Initialize logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def perform_addition(numbers: List[int]) -> int:
        with Pool() as pool:
            return sum(pool.map(lambda x: x, numbers))

    def handle_batched_addition(self,request: BatchedRequest) -> BatchedResponse:
        try:
            started_at = datetime.now().isoformat()
            result = [self.perform_addition(batch) for batch in request.payload]
            complete_at = datetime.now().isoformat()
            return BatchedResponse(
                batched=request.batched,
                response=result,
                status="complete",
                started_at=started_at,
                complete_at=complete_at,
            )
        except Exception as e:
            self.logger.error(f"Error performing batched addition: {str(e)}")
            raise