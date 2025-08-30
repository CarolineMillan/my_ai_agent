import os, subprocess, sys

def run_python_file(working_directory, filepath, args=[]):
    abs_directory = os.path.abspath(working_directory)
    full_fp = os.path.abspath(os.path.join(abs_directory, filepath))
    # print(f"abs: {abs_directory}\nworking: {working_directory}\ndirectory: {filepath}\nfp: {full_fp}")
    ans = ""
    if (not full_fp.startswith(abs_directory)):
        return f'Error: Cannot execute \"{filepath}\" as it is outside the permitted working directory'
    elif (not os.path.isfile(full_fp)):
        return f'Error: File \"{filepath}\" not found.'
    elif (not full_fp.endswith('.py')):
        return f'Error: \"{filepath}\" is not a Python file.'
    else:
        try:
            my_args = ['python', full_fp]
            my_args.extend(args)
            completed = subprocess.run(args=my_args, cwd=abs_directory, capture_output=True, text=True, timeout=30)
            ans = f'STDOUT: {completed.stdout}, STDERR: {completed.stderr}.'
            # if exit code non zero, add "Process exited with code X"
            if completed.returncode != 0:
                ans += f' Process exited with code {completed.returncode}.'
            # if no output is produced, add "No output produced"
            if completed.stdout == None:
                ans += ' No output produced.'
            return ans
        except Exception as e:
            raise Exception(f"Error: executing python file {e}")