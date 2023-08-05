import os
import typing as t
from dataclasses import dataclass

from . import api_support

T = t.TypeVar("T")


@dataclass
class FreePlayPromptTemplate:
    name: str
    content: str


@dataclass
class FreePlayProjectSession:
    session_id: str
    prompt_templates: list[FreePlayPromptTemplate]

    def __all_names(self) -> list[str]:
        return [t.name for t in self.prompt_templates]

    def get_template(self, template_name: str) -> str:
        for t in self.prompt_templates:
            if t.name == template_name:
                return t.content

        raise Exception(f'Template with name {template_name} not found. Available names are: {self.__all_names()}')


@dataclass
class FreePlayTestRunRecord:
    project_id: str
    test_run_id: str
    input_collection: list[dict[str, str]]


@dataclass
class FreePlayTestRun:
    api_key: str
    api_url: str
    record: FreePlayTestRunRecord

    def get_inputs(self) -> list[dict[str, str]]:
        return self.record.input_collection

    def new_project_session(self, tag: str = 'latest') -> FreePlayProjectSession:
        return api_support.post(
            target_type=FreePlayProjectSession,
            api_key=self.api_key,
            url=f'{self.api_url}/projects/{self.record.project_id}/sessions/tag/{tag}',
            payload={'test_run_id': self.record.test_run_id},
        )


class FreePlay:
    def __init__(self, api_key: str, api_url: t.Optional[str] = None) -> None:
        self.api_key = api_key
        self.api_url = api_url or self.__get_default_url()

    @staticmethod
    def __get_default_url() -> str:
        return os.environ.get('FREEPLAY_API_URL', 'https://review.freeplay.ai/api')

    def new_test_run(self, project_id: str, playlist: str) -> FreePlayTestRun:
        record = api_support.post(
            target_type=FreePlayTestRunRecord,
            api_key=self.api_key,
            url=f'{self.api_url}/projects/{project_id}/test-runs',
            payload={'playlist_name': playlist},
        )
        return FreePlayTestRun(self.api_key, self.api_url, record)

    def new_project_session(self, project_id: str, tag: str = 'latest') -> FreePlayProjectSession:
        return api_support.post(
            target_type=FreePlayProjectSession,
            api_key=self.api_key,
            url=f'{self.api_url}/projects/{project_id}/sessions/tag/{tag}',
        )
