from logzero import logger
import pkg_resources
import subprocess
import threading
from colorama import Fore, Style

dockerfile_path = "resources/"
dockerfile_path = pkg_resources.resource_filename(__name__, dockerfile_path)

def create_docker_image(dockerfile_path, image_name):
    """Create a Docker image from the given dockerfile path with the given image name.

    Args:
        dockerfile_path (str): dockerfile path
        image_name (str): name of the image to be created
    """

    # Build the Docker image for the current plugin
    command = ["docker", "build", "-t", image_name, dockerfile_path]

    try:
        # Run the build command and capture the return code
        return_code = run_docker_build_command(command)

        # Check the return code to determine if the build was successful
        if return_code == 0:
            logger.info(f"{Fore.GREEN}Build Successful{Style.RESET_ALL}")
        else:
            logger.error(f"{Fore.RED}Build Failed{Style.RESET_ALL}")

    except subprocess.CalledProcessError as e:  # noqa: PERF203
        # Print the error message to the command screen
        logger.error(f"{Fore.RED}Error building image {image_name}: {e}{Style.RESET_ALL}")

def run_docker_build_command(command):
    """
    Run the Docker build command and capture the output in real-time.

    Args:
        command (list): The Docker build command to run.

    Returns:
        The captured output as a string.
    """

    def capture_output(process):
        for build_output in process.stdout:
            line = build_output.decode().strip()
            print(line)

    try:
        # Run the build command and capture the output
        with subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ) as process:
            output_thread = threading.Thread(target=capture_output, args=(process,))
            output_thread.start()

            # Wait for the process to complete
            process.wait()

            # Wait for the output thread to complete
            output_thread.join()

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    return process.returncode


def main():
    logger.debug(f"I am logging to {__name__}")
    image_name = "dummy-image"
    create_docker_image(dockerfile_path, image_name)


if __name__ == "__main__":
    main()
