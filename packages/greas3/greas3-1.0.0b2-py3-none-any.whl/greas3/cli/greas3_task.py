from logging import DEBUG
from pathlib import Path

from ansiscape import light
from cline import CommandLineArguments, Task
from slash3 import S3Uri

from greas3.cli.paths_args import PathsArgs
from greas3.logging import logger
from greas3.operations import put


class Greas3Task(Task[PathsArgs]):
    @classmethod
    def make_args(cls, args: CommandLineArguments) -> PathsArgs:
        return PathsArgs(
            debug=args.get_bool("debug", False),
            destination=args.get_string("destination"),
            dry_run=args.get_bool("dry_run", False),
            source=args.get_string("source"),
        )

    def invoke(self) -> int:
        if self.args.debug:
            logger.setLevel(DEBUG)

        source = Path(self.args.source)
        destination = S3Uri(self.args.destination)

        if self.args.dry_run:
            logger.info(light("Performing a dry-run only."))

        put(
            source,
            destination,
            dry_run=self.args.dry_run,
            session=self.args.session,
        )

        return 0
