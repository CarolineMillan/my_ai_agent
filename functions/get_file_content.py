import os
from config import CHAR_LIMIT
from google.genai import types

def get_file_content(working_directory, filepath):
    abs_directory = os.path.abspath(working_directory)
    full_fp = os.path.abspath(os.path.join(abs_directory, filepath))
    # print(f"abs: {abs_directory}\nworking: {working_directory}\ndirectory: {directory}\nfp: {full_fp}")
    ans = ""
    if (not full_fp.startswith(abs_directory)):
        ans += f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'
    elif (not os.path.isfile(full_fp)):
        ans += f'Error: File not found or is not a regular file: "{filepath}"'
    else:
        # read in filepath
        # truncate at 10,000 chars and print
        try:
            with open(full_fp, "r") as f:
                file_content_string = f.read(CHAR_LIMIT)
                if (len(file_content_string) < 10000):
                    ans += file_content_string
                else:
                    ans += f"{file_content_string} ...File \"{filepath}\" truncated at 10000 characters"
        except:
            raise Exception("Error: cannot open file")
    return ans


# this schema tells the LLM how to use the function
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Prints the content of a file, truncated at 10,000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The file to be printed, relative to the working directory.",
            ),
        },
    ),
)