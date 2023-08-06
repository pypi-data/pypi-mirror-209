from esg import WaveformData
from esg.uquake import core
from uquake.core.logging import logger
from pathlib import Path
from time import time
from importlib import reload

reload(WaveformData)
reload(core)

input_path = Path('/data_2/GBC/')

for f in input_path.glob('*.hsf'):
    logger.info(f'reading the HSF file ({f})')
    t0 = time()
    st, head = WaveformData.hsf_to_obspy(f, print_out=False,
                                         groundmotion=False, return_head=True)

    t1 = time()
    logger.info(f'done reading the HSF file in {t1 - t0} seconds')

    hsf_handler = core.HSFHandler(st, head, 'GBC')

    krapout