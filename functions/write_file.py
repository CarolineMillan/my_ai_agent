import os
from google.genai import types


def write_file(working_directory, filepath, content):
    abs_directory = os.path.abspath(working_directory)
    full_fp = os.path.abspath(os.path.join(abs_directory, filepath))
    # print(f"abs: {abs_directory}\nworking: {working_directory}\ndirectory: {directory}\nfp: {full_fp}")
    ans = ""
    if (not full_fp.startswith(abs_directory)):
        return f'Error: Cannot write to \"{filepath}\" as it is outside the permitted working directory'
    
    # x means we create the file only if it doesn't already exist, so an already existing file isn't overwritten
    # w means we create a file if it doesn't exist, but if it does exist then we overwrite anything in it
    try:
        with open(full_fp, 'w') as f:
            f.write(content)
    except:
        raise Exception("Error: couldn't open file")
        
    return f'Successfully wrote to "{filepath}" ({len(content)} characters written)'


# this schema tells the LLM how to use the function
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file in the specified directory, overwriting the file if it already exists, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The file to be run, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file.",
            )
        },
    ),
)