## Cukcuk SDK

### Examples:
1. Get all invoices in a date range
```python
import cukcuk
from datetime import datetime, timedelta

session = cukcuk.LoginSession.from_json("login.json")
last_sync_date = datetime(2023, 5, 1)
before_date = datetime(2023, 5, 5)
invoices = session.get_invoices(last_sync_date=last_sync_date, before_date=before_date)
df = invoices.to_df() # Convert to pandas DataFrame
print(df)
```

2. Using asynchronous session to speed up requests
```python
import asyncio
import cukcuk
from datetime import datetime, timedelta

session = cukcuk.AsyncLoginSession.from_json("login.json")
last_sync_date = datetime(2023, 5, 1)
before_date = datetime(2023, 5, 5)
invoices = asyncio.run(session.get_invoices(last_sync_date=last_sync_date, before_date=before_date))
df = invoices.to_df() # Convert to pandas DataFrame
print(df)
```
