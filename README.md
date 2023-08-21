# Packaging Your Python Code With `pyproject.toml`

Inspired by: [Packaging Your Python Code With pyproject.toml | Complete Code Conversation](https://youtu.be/v6tALyc4C10) by RealPython

## Introduction

This guide is influenced by the video tutorial titled "Packaging Your Python Code With `pyproject.toml`" presented by RealPython. The tutorial covers the process of packaging Python code and utilizing the `pyproject.toml` configuration file.

## Steps to Package Your Code

1. **Create a Package Folder**: Begin by placing your code in a dedicated folder. The name of this folder will serve as the name of your package, and you will use it to reference your package.
2. **Add `__main__.py`**: Inside this package folder (referred to as the root folder), include a file named `__main__.py`.
3. **Utilizing `__main__.py`**: When attempting to execute the package using Python, the interpreter searches for a `__main__.py` file within the folder. If found, the file is executed; otherwise, a `FileNotFoundError` is raised.
4. **Automatic Path Inclusion**: When the package is called, Python automatically adds the current working directory to the Python path list.
5. **Transition from Distutils to Setuptools**: It's important to note that Distutils is set to be deprecated in Python 3.12. The recommended approach for building and using packages is now Setuptools.
6. **Using Setuptools**: Setuptools eliminates the need for a `setup.py` file (though it remains optional). Instead, you require a `pyproject.toml` file that contains the project's configuration.
7. **Organize Source Code**: It is advisable to create a subfolder for your source code within the package folder.
8. **Configuration in `pyproject.toml`**: Within the `pyproject.toml` file, you must add the following lines:

   ```toml
   [build-system]
   requires = ["setuptools", "setuptools-scm"]
   build-backend = "setuptools.build_meta"
   ```
9. **Building and Installing**: After configuration, building and installing your package can be achieved by using the following commands:

   - To build: `python3 -m build`
   - To install directly: `pip3 install <project-directory-name>`
10. **Calling Without Installation**: To execute the package without installation, use the command: `python -m <package-directory-name>`.
11. **Global Access After Installation**: Once installed, the package becomes accessible from any directory in the system.
12. **Enabling Terminal Command**: To enable calling your project without specifying "python" in the terminal, you must add a `[project.scripts]` section to the `pyproject.toml` file. Within this section, specify the entry name and entry point path, as demonstrated below:

    ```toml
    [project.scripts]
    doraemonsays = "doraemonsay.__main__.main"
    ```

    Following this configuration, the function can be directly invoked from the terminal without explicitly using "python."
13. **Creating a Wheel File**: To generate a wheel file, execute either `pip build .` or `python3 -m build <project-dir>`.
14. **Including Non-Python Files**: If your package includes non-Python files, follow these steps:

    - Add the following lines to the `pyproject.toml` file:

      ```toml
      [tool.setuptools]
      include-package-data = true
      ```
    - Create a new empty file named **MENIFEST.in** at the same level as `pyproject.toml`.
    - Inside **MENIFEST.in**, list the paths you wish to retain followed by "include," like so:

      `include doraemonsay/resources/*`
    - Access these paths from Python code using the **pkg_resources** module. Below is an example of accessing package resources:

      ```python
      import pkg_resources

      resource_path = "resources/DORAEMON"
      doraemon_path = pkg_resources.resource_filename(__name__, resource_path)
      ```

      This allows you to read content from `doraemon_path`.

Feel free to utilize this guide as a reference for packaging your Python code using the `pyproject.toml` configuration file. It streamlines the process and ensures efficient management of your packages.
