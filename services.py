import base64
from vertexai.preview import extensions


async def run_code_interpreter(
    extension_code_interpreter: extensions.Extension,
    instructions: str,
    filenames: list[dict] = [],
    retry_num: int = 5,
    retry_wait_time: int = 15,
) -> dict["str", "str"]:

    written_files = []
    file_arr = [
        {
            "name": filename,
            "contents": base64.b64encode(open(filename, "rb").read()).decode(),
        }
        for filename in filenames
    ]

    attempts = 0
    res = {}

    while attempts <= retry_num:
        attempts += 1

        res = extension_code_interpreter.execute(
            operation_id="generate_and_execute",
            operation_params={"query": instructions, "files": file_arr},
        )

        written_files.extend([item["name"] for item in res["output_files"]])

        if not res.get("execution_error", None):
            return res
        elif attempts <= retry_num:
            print(
                f"The generated code produced an error {res.get('execution_error')}"
                f" -Automatic retry attempt # {attempts}/{retry_num}"
            )
