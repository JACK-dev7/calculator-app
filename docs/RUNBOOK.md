# Python Calculator CI Project: Runbook

## 1. Purpose

This runbook describes how to set up, run, test, containerize, and troubleshoot the Python calculator project. It also explains how to trigger and verify the GitHub Actions Continuous Integration (CI) workflow.

## 2. Prerequisites

- Python 3.x.
- Git.
- Docker Desktop with the Docker engine running.
- A GitHub account with access to the repository.
- `pytest` installed through the project's `requirements.txt`.

## 3. Get the Source Code

Clone the repository:

```powershell
git clone https://github.com/JACK-dev7/calculator-app.git
cd calculator-app
```

## 4. Run Unit Tests Locally

Install the required dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the unit tests:

```powershell
python -m pytest -v
```

The tests cover addition, subtraction, multiplication, and invalid-input handling.

The calculator accepts positive integers only. Booleans, strings, floats, zero, and negative integers raise `ValueError`.

Confirm that all tests pass before committing changes.

## 5. Build the Docker Image

Ensure Docker Desktop is running, then execute:

```powershell
docker build -t calculator-app .
```

This builds the Docker image using the project's `Dockerfile`. The image includes the Python environment, pytest dependency, calculator package, and test files.

## 6. Run the Container

Execute:

```powershell
docker run --rm calculator-app
```

The Dockerfile's configured `CMD` runs the pytest test suite inside the container.

The `--rm` option removes the container after it exits. It does not remove the Docker image.

Confirm that all tests pass inside the container.

## 7. Run the CI Workflow

The GitHub Actions workflow is located at:

`.github/workflows/ci.yml`

The workflow is triggered automatically on every push.

1. Modify the calculator source code or tests.
2. Run the unit tests locally:

   ```powershell
   python -m pytest -v
   ```

3. Build the Docker image and run the tests inside the container:

   ```powershell
   docker build -t calculator-app .
   docker run --rm calculator-app
   ```

4. Stage and commit the changes:

   ```powershell
   git add .
   git commit -m "Describe the change"
   ```

5. Push the commit:

   ```powershell
   git push
   ```

6. Open the repository's Actions tab:

   https://github.com/JACK-dev7/calculator-app/actions

7. Open the latest `Calculator CI` workflow run and inspect the results.

The workflow checks out the repository, builds the Docker image, and runs the unit tests inside the container. If the build or tests fail, the CI workflow fails.

## 8. Troubleshooting

### Unit tests fail

- Read the pytest failure output.
- Compare the actual and expected results.
- Check the input validation logic and test cases.
- Correct the application or tests as appropriate.
- Run `python -m pytest -v` again.

### Docker engine is unavailable

- Open Docker Desktop.
- Wait for the Docker engine to start.
- Check availability with:

  ```powershell
  docker info
  ```

### Docker image build fails

- Confirm that `Dockerfile` exists in the project root.
- Check the build output for missing files, invalid instructions, or dependency errors.
- Verify that the required application and test directories are included in the build context.

### Tests fail inside Docker

- Rebuild the image after changing source code or tests.
- Confirm that the Dockerfile copies the latest application and test files.
- Run the container again and inspect the pytest output.

### GitHub Actions fails

- Open the failed workflow run in the Actions tab.
- Select the failed job and inspect its logs.
- Identify whether the failure occurred during checkout, image building, or testing.
- Fix the issue, verify it locally and inside Docker, then commit and push again.

### GitHub Actions does not start

- Confirm that `.github/workflows/ci.yml` is committed to the repository.
- Verify that the push reached the correct repository and branch.
- Check the Actions tab for workflow errors.

## 9. Cleanup

Remove the local Docker image when it is no longer needed:

```powershell
docker image rm calculator-app
```

Docker may refuse to remove the image while containers still depend on it. Inspect existing containers before removing anything.

The `docker run --rm calculator-app` command already removes the container after it exits, but the image remains available until explicitly removed.

## 10. Expected Outcome

The calculator should run its unit tests locally, build successfully as a Docker image, and execute its tests inside the container. Every push to GitHub should trigger the configured GitHub Actions CI workflow.

Successful builds and tests should produce a passing workflow, while failed builds or tests should cause the workflow to fail.
