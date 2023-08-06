import logging
import typing
from irisml.core import JobDescription
from irisml.core.cache_manager import create_storage_manager, CacheManager
from irisml.core.context import Context
from irisml.core.job import Job

logger = logging.getLogger(__name__)


class JobRunner:
    """Helper class to run a job."""
    def __init__(self, job_dict: typing.Dict, env_vars: typing.Dict[str, str], cache_storage_url: str = None, no_cache_read: bool = False):
        job_description = JobDescription.from_dict(job_dict)
        self._job = Job(job_description)
        self._env_vars = env_vars
        self._cache_storage_url = cache_storage_url
        self._no_cache_read = no_cache_read

    def run(self, dry_run=False):
        logger.debug("Loading task modules.")
        self._job.load_modules()

        logger.info("Running a job.")

        cache_manager = CacheManager(create_storage_manager(self._cache_storage_url), self._no_cache_read) if self._cache_storage_url and not dry_run else None
        if cache_manager:
            logger.info(f"Cache is enabled: {self._cache_storage_url}")

        context = Context(self._env_vars, cache_manager)

        # Note that the random seed will be reset in each Task.execute().
        for task in self._job.tasks:
            logger.debug(f"Running a task: {task}")
            try:
                task.execute(context, dry_run)
            except Exception as e:
                logger.exception(f"Failed to run a task {task}: {e}")
                self.on_error(context, e)
                raise

        logger.info("Completed.")

    def on_error(self, context, e):
        context.add_environment_variable('IRISML_EXCEPTION', e)
        for task in self._job.on_error:
            logger.info(f"Running an error handler: {task}")
            task.execute(context)
