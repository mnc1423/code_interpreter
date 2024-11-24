from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


DOTENV_PATH = os.environ.get(
    "DOTENV_PATH", os.path.join(os.path.dirname(__file__), ".env")
)


class _ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="VERTEX_",
        env_file=DOTENV_PATH,
        extra="ignore",
        env_ignore_empty=True,
    )
    llm_model: Optional[str] = None
    embedding_model: Optional[str] = None
    code_interpreter: Optional[str] = None


class _GenerationConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="GCP_VERTEX_",
        env_file=DOTENV_PATH,
        extra="ignore",
        env_ignore_empty=True,
    )

    temperature: Optional[float] = 0.0
    top_p: Optional[float] = 1.0
    top_k: Optional[int] = None
    candidate_count: Optional[int] = None
    max_output_tokens: Optional[int] = 1000
    stop_sequences: Optional[List[str]] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    response_mime_type: Optional[str] = None
    response_schema: Optional[Dict[str, Any]] = None
    seed: Optional[int] = None
    logprobs: Optional[int] = None
    response_logprobs: Optional[bool] = None


class AppSettings(BaseSettings):
    gen_config: _GenerationConfig = _GenerationConfig()
    model: _ModelConfig = _ModelConfig()


app_settings = AppSettings()
