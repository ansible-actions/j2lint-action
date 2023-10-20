#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Action to run j2lint
"""
import subprocess
import os
import sys

# pylint: disable=R0903
class EnvironmentManager:
    """
    Parsing Enviroment Variables
    """
    def __init__(self, env_var_name):
        self.env_var_name = env_var_name
        self.env_var_value = os.getenv(env_var_name)

    def check_required_environment_variable(self):
        """
        Check if required Variable is defined.
        exit if undefined
        """
        if self.env_var_value is not None:
            print(f"The value of {self.env_var_name} is: {self.env_var_value}")
            return f"{self.env_var_value}"
        print(f"The variable {self.env_var_name} is not set but needs to be defined.\nFAILED")
        sys.exit(1)

# pylint: disable=R0903
class YamlCommandExecution:
    """
    running j2lint command
    """
    def run_command(self, command):
        """
        Running command as subprocess.
        Printing error on fail and exit
        """
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as error:
            print(f"Error running Ansible command: {error}\n\n{error.stdout}\n{error.stderr}")
            sys.exit(1)

if __name__ == "__main__":
    # define known enviroment vars
    ENV_TARGET_NAME = "TARGET"

    # check for target variable
    env_target = EnvironmentManager(ENV_TARGET_NAME)
    target = env_target.check_required_environment_variable()
    if target == "":
        print("Target needs to be defined")
        sys.exit(1)

    # execute linting commands
    execute = YamlCommandExecution()

    # run j2lint
    linting_command = ["j2lint", f"{target}"]
    linter_run = execute.run_command(linting_command)
    print(f"---start+linter---\n{linter_run}\nJinja2 Linting run successful\n---end+linter---")
