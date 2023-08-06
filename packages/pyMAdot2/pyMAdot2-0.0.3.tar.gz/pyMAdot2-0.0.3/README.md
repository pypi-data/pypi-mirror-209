# pyMAdot2

<img src="https://xom.malighting.com/xom-rest/assets/da4da7d0-4cfe-40da-9023-4fa866e38f25/preview?access_token=A9OYsVma9vxvXaaqzsVFtsR6K14&mimeType=image%2Fpng&width=1170&height=700" width=20% height=20%>

Asynchronous library to control [MA Lighting dot2](https://www.malighting.com/de/produktarchiv/produkt/dot2-core-120211/) light console.

**This library is under development**

## Requirements

- Python >= 3.10
- aiohttp

## Install
```bash
pip install pyMAdot2
```

## Example

```python
from pymadot2 import Dot2

import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        await run(session)

async def run(session):
    console = await Dot2.create(
        session,
        "127.0.0.1",
        "test"
    )

    await console.command("Fixture 1")
    await console.command("At 100")
    await asyncio.sleep(1)
    await console.disconnect()

asyncio.run(main())
```
