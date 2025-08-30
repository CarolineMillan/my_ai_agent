import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abs_directory = os.path.abspath(working_directory)
    full_fp = os.path.abspath(os.path.join(abs_directory, directory))
    # print(f"abs: {abs_directory}\nworking: {working_directory}\ndirectory: {directory}\nfp: {full_fp}")
    ans = ""
    if (not full_fp.startswith(abs_directory)):
        ans += f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif (not os.path.isdir(full_fp)):
        ans += f'Error: \'{directory}\' is not a directory'
    else:
        contents = os.listdir(full_fp)
        contents = sorted(contents, key=lambda filename: (os.path.isdir(os.path.join(full_fp, filename)), filename))
        for thing in contents:
            thing_fp = os.path.join(full_fp, thing)
            ans += f"- {thing}: file_size={os.path.getsize(thing_fp)} bytes, is_dir={os.path.isdir(thing_fp)}\n"
    return ans.rstrip('\n')

# this schema tells the LLM how to use the function
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)