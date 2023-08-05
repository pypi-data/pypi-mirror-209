## Advanced Example

### Show received Data in a plot

```shell
poetry new my-nista-client
cd my-nista-client
poetry add nista-library
poetry add structlog
poetry add matplotlib
```

```python
import matplotlib.pyplot as plt
from structlog import get_logger

from nista_library import KeyringNistaConnection, NistaDataPoint, NistaDataPoints

log = get_logger()

connection = KeyringNistaConnection()

data_point_id = "56c5c6ff-3f7d-4532-8fbf-a3795f7b48b8"
data_point = NistaDataPoint(connection=connection, data_point_id=data_point_id)

data_point_data = data_point.get_data_point_data()
log.info("Data has been received. Plotting")
data_point_data.plot()
plt.show()

```

### Filter by DataPoint Names

```shell
poetry new my-nista-client
cd my-nista-client
poetry add nista-library
poetry add structlib
poetry add matplotlib
```

```python
import matplotlib.pyplot as plt
from structlog import get_logger

from nista_library import KeyringNistaConnection, NistaDataPoint, NistaDataPoints

log = get_logger()

connection = KeyringNistaConnection()

dataPoints = NistaDataPoints(connection=connection)
data_point_list = list(dataPoints.get_data_point_list())

for data_point in data_point_list:
    log.info(data_point)

# Find Specific Data Points
filtered_data_points = filter(
    lambda data_point: data_point.name.startswith("371880214002"), data_point_list
)
for data_point in filtered_data_points:
    # get the data
    data_point_data = data_point.get_data_point_data()
    log.info(data_point_data)
    data_point_data.plot()
    plt.show()

```
