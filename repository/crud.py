from odmantic import AIOEngine
from repository.models import Counter

async def generate(engine: AIOEngine, category: str, code: str) -> str:
    key = f"{category}_{code}"
    counter = await engine.find_one(Counter, Counter.key == key)

    if not counter:
        counter = Counter(key=key, sequence_value=1)
    else:
        counter.sequence_value += 1

    await engine.save(counter)
    seq_str = str(counter.sequence_value).zfill(3)
    return f"{seq_str}/{category}/{code}"
