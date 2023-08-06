#!/usr/bin/env python3
# www.jrodal.com

import logging
import re
from typing import Optional, Pattern

from youtube_transcript_api import YouTubeTranscriptApi  # pyright: ignore
from youtube_transcript_api.formatters import TextFormatter  # pyright: ignore

from .ai_interface import AiInterface
from .exception import TldrwlVideoUrlParsingException
from .summarize_text import TextSummarizer, TextSummary


class YoutubeSummarizer(AiInterface):
    _pattern: Pattern[str] = re.compile(
        r"(?:[?&]v=|\/embed\/|\/1\/|\/v\/|https:\/\/(?:www\.)?youtu\.be\/)([^&\n?#]+)"
    )

    def __init__(self) -> None:
        super().__init__()
        self._text_summarizer = TextSummarizer()
        self._logger = logging.getLogger(__name__)

    @classmethod
    def get_video_id(cls, url: str) -> Optional[str]:
        match = cls._pattern.search(url)
        if match:
            return match.group(1)
        return None

    def _get_video_transcript(self, url: str) -> str:
        video_id = self.get_video_id(url)
        if not video_id:
            raise TldrwlVideoUrlParsingException.make_error(video_url=url)
        self._logger.debug(f"Getting transcript for {video_id}")
        transcript = YouTubeTranscriptApi.get_transcript(video_id)  # type: ignore
        self._logger.debug(f"Done getting transcript for {video_id}")
        return TextFormatter().format_transcript(transcript)  # type: ignore

    async def summarize_video_async(self, url: str) -> TextSummary:
        transcript = self._get_video_transcript(url)
        return await self._text_summarizer.summarize_text_async(transcript)

    def summarize_video(self, url: str) -> TextSummary:
        transcript = self._get_video_transcript(url)
        return self._text_summarizer.summarize_text(transcript)


# text = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
