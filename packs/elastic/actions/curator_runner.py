from easydict import EasyDict
from lib.curator_action import CuratorAction
import logging
import sys

logger = logging.getLogger(__name__)


class CuratorRunner(CuratorAction):

    def run(self, action=None, log_level='warn', dry_run=False, operation_timeout=600, **kwargs):
        """Curator based action entry point
        """
        self.action = action
        kwargs.update({
            'timeout': int(operation_timeout),
            'log_level': log_level,
            'dry_run': dry_run,
        })

        self.config = EasyDict(kwargs)
        self.set_up_logging()
        self.do_command()
