# Nahre

Computer vision research and prototype package.
Lets you dive straight into problem solving mindset.
You don't have to worry about tedious stuff.

- load your data set
- configure batch
- process records
- validate them

## Getting started

Be sure you have `virtualenv` installed on your machine.

```shell
pip install virtualenv
```

Clone this repository to your disk. Then install this package through `pip`.

```shell
cd [directory]
pip install .
```

## How to use

### Data

Put your image files in a single folder. This folder can only comprise of image files.

### Validation

Validation set is a simple csv file. In first column you define filenames that point out each image from data set.
In additional columns you write down expected results for each of these images.
Please refer to exemplary validation .csv, which can be found in `./tests/data` folder.

### Processor

Processor class must implement base Processor interface, which ships with this package.
When batch is executed, every record from data set is ran against `process` method.
This method must return results which matches your validation set.
If you want to omit validation step, just return empty dict.

```py
import skimage.feature

from austen import Logger

import nahre


class EdgeProcessor(nahre.Processor):

    def __init__(self, logger: Logger):
        super().__init__(logger)

    def process(self, src):
        src = record.load()
        edges = skimage.feature.canny(src)
        edges_count = np.count_nonzero(edges)

        return {
            'edges: edges
        },{
            'edges_count': edges_count
        }

```

### Batch configuration

```py

def batches():

    yield nahre.Batch(
        data=nahre.io.flat.DataSet(DATA),
        processors=[EdgeProcessor],
        validator=nahre.io.Validator(VALIDATION),
        logs_dir=LOGS
    )

```

### Make yourself comfortable and watch the fireworks

```py
nahre.execute(batches())
```

## Tests

```shell
cd [project-path]
python -m pytest .\tests\
```
