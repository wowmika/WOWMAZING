"""Serial background download queue for the WOWMAZING UI."""

from __future__ import annotations

from dataclasses import dataclass, replace
from queue import Queue
from threading import Event, Lock, Thread
from typing import Callable, Literal
from uuid import uuid4

from core.downloader import DownloadCancelled, download_media


DownloadStatus = Literal[
    "queued",
    "downloading",
    "processing",
    "completed",
    "failed",
    "cancelled",
]


@dataclass
class DownloadJob:
    """The UI-facing state for one media download."""

    url: str
    media_type: str
    id: str = ""
    status: DownloadStatus = "queued"
    progress: float = 0.0
    output_path: str | None = None
    error: str | None = None

    def __post_init__(self) -> None:
        if not self.id:
            self.id = uuid4().hex


JobUpdateCallback = Callable[[DownloadJob], None]
DownloadFunction = Callable[
    [str, str, str, str, Callable[[float, str], None], Callable[[], bool]],
    str | None,
]


class DownloadQueue:
    """Runs one download at a time while keeping job state safe to read from Tk."""

    def __init__(
        self,
        on_job_updated: JobUpdateCallback | None = None,
        downloader: DownloadFunction = download_media,
    ) -> None:
        self._on_job_updated = on_job_updated
        self._downloader = downloader
        self._jobs: dict[str, DownloadJob] = {}
        self._cancel_events: dict[str, Event] = {}
        self._pending: Queue[tuple[str, str, str]] = Queue()
        self._lock = Lock()
        self._worker = Thread(target=self._run, daemon=True, name="download-queue")
        self._worker.start()

    def add_job(self, url: str, media_type: str, start: str = "", end: str = "") -> DownloadJob:
        """Queue a job and return a snapshot of its initial state."""
        job = DownloadJob(url=url, media_type=media_type)
        with self._lock:
            self._jobs[job.id] = job
            self._cancel_events[job.id] = Event()
        self._pending.put((job.id, start, end))
        self._notify(job)
        return replace(job)

    def cancel_job(self, job_id: str) -> None:
        """Cancel a waiting job or request cancellation of the active download."""
        with self._lock:
            job = self._jobs.get(job_id)
            cancel_event = self._cancel_events.get(job_id)
            if job is None or cancel_event is None or job.status in {"completed", "failed", "cancelled"}:
                return
            cancel_event.set()
            if job.status == "queued":
                job.status = "cancelled"
                job.error = None
        self._notify(job)

    def get_jobs(self) -> list[DownloadJob]:
        """Return independent snapshots in submission order."""
        with self._lock:
            return [replace(job) for job in self._jobs.values()]

    def _run(self) -> None:
        while True:
            job_id, start, end = self._pending.get()
            try:
                self._download_job(job_id, start, end)
            finally:
                self._pending.task_done()

    def _download_job(self, job_id: str, start: str, end: str) -> None:
        with self._lock:
            job = self._jobs[job_id]
            cancel_event = self._cancel_events[job_id]
            if job.status == "cancelled":
                return
            job.status = "downloading"
        self._notify(job)

        def update_progress(progress: float, message: str) -> None:
            with self._lock:
                if job.status == "cancelled":
                    return
                job.progress = max(0.0, min(100.0, progress))
                job.status = "processing" if message == "Processing..." else "downloading"
            self._notify(job)

        try:
            output_path = self._downloader(
                job.url,
                job.media_type,
                start,
                end,
                update_progress,
                cancel_event.is_set,
            )
            with self._lock:
                if cancel_event.is_set():
                    job.status = "cancelled"
                else:
                    job.status = "completed"
                    job.progress = 100.0
                    job.output_path = output_path
                    job.error = None
        except DownloadCancelled:
            with self._lock:
                job.status = "cancelled"
                job.error = None
        except Exception as error:
            with self._lock:
                job.status = "failed"
                job.error = str(error)
        self._notify(job)

    def _notify(self, job: DownloadJob) -> None:
        if self._on_job_updated:
            self._on_job_updated(replace(job))
