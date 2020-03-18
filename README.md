# Nahre

Vanilla computer vision research and prototype package.
Lets you dive straight into problem solving mindset.
You don't have to worry about tedious stuff.

- loading data
- batch configuration
- record processing

## Getting started

```sh
pip install nahre
```

## How to use

### Data

Put your image files in a single folder. Both flat and nested structures are supported.

### Processor

Processor class must implement base `Processor` interface, which ships with this package.
When batch is executed, every record from data set is ran against `process` method.
This method must return results which matches next processor's interface on the list.

### Example

```py
from pathlib import Path

import numpy as np
from austen import Logger
from degas import FluentImage
from lazy import lazy
from pytest import fixture
from skimage import color, exposure, feature

from nahre import Batch, Processor, execute
from nahre.io import Data


class EdgeProcessor(Processor):

    def __init__(self, logger: Logger):
        super().__init__(logger)

    @lazy
    def _description(self):
        return 'Any description is better than none.'

    def __call__(self, src: np.ndarray):

        with FluentImage(src, self.logger, 'preprocessing') as preprocessed:

            preprocessed >> (
                color.rgb2gray
            ) >> (
                exposure.rescale_intensity
            ) >> (
                exposure.equalize_adapthist
            ) >> (
                feature.canny
            )

            return {
                'preprocessed': preprocessed.image
            }


batch = Batch(
    data=Data(Path('data')),
    processors=[EdgeProcessor],
    log_root=Path('log')
)

execute([batch])

```

`nahre` will dump any intermediate images using `austen` package. Additionally, final results will be dumped in separate folder.

## Tests

```shell
cd [project-path]
python -m pytest
```
