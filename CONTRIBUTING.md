# Contributing to ModbusIM

Thank you for your interest in contributing to ModbusIM! We welcome all contributions, including bug reports, feature requests, documentation improvements, and code contributions.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Install the development dependencies:
   ```bash
   poetry install
   ```
4. Create a new branch for your changes:
   ```bash
   git checkout -b my-feature-branch
   ```

## Development Workflow

### Running Tests

Run the test suite with:

```bash
make test
```

### Code Style

We use `black` for code formatting and `flake8` for linting. You can automatically format your code with:

```bash
make format
```

And check for style issues with:

```bash
make lint
```

### Documentation

Please ensure that all public APIs are documented with docstrings following the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

## Submitting Changes

1. Ensure all tests pass
2. Update the documentation if necessary
3. Commit your changes with a descriptive commit message
4. Push your changes to your fork
5. Open a pull request against the main repository

## Reporting Issues

When reporting issues, please include:

- A clear description of the issue
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any relevant error messages
- Version information (Python version, package version, etc.)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing to ModbusIM, you agree that your contributions will be licensed under the [MIT License](LICENSE).
