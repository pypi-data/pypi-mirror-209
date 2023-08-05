from typing import Callable, List
from typedef.block import Block

from typedef.rss import InteractiveRssType


InteractiveFunctionType = Callable[[InteractiveRssType], List[Block]]
