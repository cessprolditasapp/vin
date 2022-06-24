import os

try:
    env_file = os.getenv('GITHUB_ENV')
    with open(env_file, "a") as env_file:
        env_file.write("ENV_VAR=1")
    print(f"+++ Environment variable is set +++")

except Exception as e:
    print(f"+++ Error while setting the environment variable :: {e} +++")
