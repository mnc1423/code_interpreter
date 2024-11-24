from vertexai.preview import extensions
from models import app_settings
from prompt_template import code_interpreter_file
from services import run_code_interpreter


async def code_interpreter():
    try:
        extension_code_interpreter = extensions.Extension(
            app_settings.model.code_interpreter
        )
    except:
        return {}
    instruct = code_interpreter_file()
    run_code_interpreter(
        extension_code_interpreter=extension_code_interpreter,
        instructions=instruct,
        filenames="",
    )
