# Contributing to PenWeb

Thank you for your interest in contributing to PenWeb! We welcome contributions from the community and are grateful for your support.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand what actions will and will not be tolerated.

## How to Contribute

### Types of Contributions

We welcome several types of contributions:

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit bug fixes or new features
- **Documentation**: Improve or expand our documentation
- **Testing**: Add or improve test coverage

### Getting Started

1. **Fork the Repository**: Click the 'Fork' button at the top right of the repository page
2. **Clone Your Fork**: 
   ```bash
   git clone https://github.com/YOUR_USERNAME/websec.git
   cd websec
   ```
3. **Add Upstream Remote**:
   ```bash
   git remote add upstream https://github.com/alexcolls/websec.git
   ```
4. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Poetry for dependency management
- Git

### Installation Steps

1. **Initialize Git Submodules** (required for GPS, VPN, Email CLI tools):
   ```bash
   git submodule update --init --recursive
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install Dependencies**:
   ```bash
   poetry install
   ```

4. **Set Up Environment Variables**:
   ```bash
   cp .env.sample .env
   # Edit .env with your configuration (optional - tools work with defaults)
   ```

5. **Run the Application**:
   ```bash
   ./run.sh
   # or
   poetry run python src/main.py
   ```

## Coding Standards

We maintain high code quality standards to ensure the project remains maintainable and consistent.

### Code Style

- **Python Version**: Python 3.9+
- **Formatter**: [Black](https://github.com/psf/black) with 100 character line length
- **Linter**: [Flake8](https://flake8.pycqa.org/)
- **Type Checker**: [Mypy](http://mypy-lang.org/) with type hints where appropriate

### Running Code Quality Checks

Before submitting a pull request, ensure your code passes all quality checks:

```bash
# Format code with Black
poetry run black src/ test/

# Run Flake8 linting
poetry run flake8 src/ test/

# Run Mypy type checking
poetry run mypy src/

# Run all tests
poetry run pytest test/ -v

# Run tests with coverage
poetry run pytest test/ --cov=src --cov-report=html
```

### Code Style Guidelines

1. **Follow PEP 8**: Adhere to Python's style guide
2. **Use Type Hints**: Add type hints to function signatures
3. **Write Docstrings**: All functions and classes should have docstrings
4. **Keep Functions Small**: Each function should do one thing well
5. **Avoid Magic Numbers**: Use named constants instead
6. **Handle Errors Gracefully**: Use try-except blocks and provide meaningful error messages

### Example

```python
"""Module for handling URL operations."""
from typing import Dict, Any


def ping_url(url: str, timeout: int = 10) -> Dict[str, Any]:
    """
    Ping a URL and return response information.
    
    Args:
        url: The URL to ping
        timeout: Request timeout in seconds (default: 10)
        
    Returns:
        Dictionary containing status_code and response_time_ms
        
    Raises:
        ValueError: If URL is invalid
        requests.RequestException: If request fails
    """
    # Implementation here
    pass
```

## Testing Requirements

All code contributions must include appropriate tests.

### Test Structure

```
test/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_ping.py
│   ├── test_clone.py
│   ├── test_d2.py
│   └── test_attempt_login.py
└── e2e.py
```

### Writing Tests

1. **Unit Tests**: Test individual functions and classes
2. **Integration Tests**: Test component interactions
3. **End-to-End Tests**: Test complete workflows

### Test Guidelines

- Use descriptive test function names: `test_ping_url_returns_status_code()`
- Test both success and failure cases
- Mock external dependencies (network requests, file I/O, etc.)
- Aim for at least 80% code coverage
- Use pytest fixtures for common setup code

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest test/unit/test_ping.py

# Run with verbose output
poetry run pytest -v

# Run with coverage report
poetry run pytest --cov=src --cov-report=html
```

## Commit Message Guidelines

We follow a convention of using emojis in commit messages to make the git history more readable and expressive.

### Commit Message Format

```
<emoji> <type>: <subject>

<body (optional)>

<footer (optional)>
```

### Common Emoji Prefixes

| Emoji | Type | Usage |
|-------|------|-------|
| ✨ | feat | New feature or functionality |
| 🐛 | fix | Bug fix |
| 📝 | docs | Documentation changes |
| 🎨 | style | Code style/formatting changes |
| ♻️ | refactor | Code refactoring |
| ⚡ | perf | Performance improvements |
| ✅ | test | Adding or updating tests |
| 🔧 | chore | Build process or auxiliary tool changes |
| 🔒 | security | Security fixes or improvements |
| 🏷️ | release | Version tags or releases |
| 🚀 | deploy | Deployment changes |
| 📦 | build | Build system or dependencies |
| 🔥 | remove | Removing code or files |
| 🚧 | wip | Work in progress |

### Examples

```bash
✨ feat: add GPS tracking feature to CLI menu
🐛 fix: resolve import error in lambda entrypoint
📝 docs: update README with installation instructions
✅ test: add unit tests for ping utility
🔧 chore: update dependencies to latest versions
```

### Commit Message Best Practices

1. **Use Present Tense**: "add feature" not "added feature"
2. **Be Descriptive**: Explain what and why, not how
3. **Keep Subject Line Short**: Under 72 characters
4. **Add Body for Complex Changes**: Explain the reasoning
5. **Reference Issues**: Include issue numbers when applicable

## Pull Request Process

### Before Submitting

1. ✅ Ensure all tests pass
2. ✅ Run code quality checks (Black, Flake8, Mypy)
3. ✅ Update documentation if needed
4. ✅ Add tests for new features
5. ✅ Update CHANGELOG.md with your changes
6. ✅ Rebase on latest main branch

### Submitting a Pull Request

1. **Push Your Branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**: Go to GitHub and create a PR from your branch to `main`

3. **Fill Out PR Template**: Provide a clear description of your changes

4. **Link Related Issues**: Use "Fixes #123" or "Closes #456" to link issues

5. **Request Review**: Tag maintainers for review

### PR Title Format

```
<emoji> <type>: <description>
```

Example: `✨ feat: add VPN connection status indicator`

### PR Description Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] CHANGELOG.md updated

## Related Issues
Fixes #(issue number)

## Screenshots (if applicable)
```

### Review Process

1. At least one maintainer must approve the PR
2. All CI checks must pass
3. Resolve all review comments
4. Maintainers will merge your PR once approved

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Clear Title**: Summarize the bug in the title
2. **Description**: Detailed description of the issue
3. **Steps to Reproduce**: List steps to reproduce the behavior
4. **Expected Behavior**: What you expected to happen
5. **Actual Behavior**: What actually happened
6. **Environment**:
   - OS: (e.g., Ubuntu 22.04, macOS 13)
   - Python version: (e.g., 3.9.7)
   - Poetry version: (e.g., 1.6.1)
   - PenWeb version: (e.g., 0.3.1)
7. **Logs/Screenshots**: Include relevant logs or screenshots
8. **Additional Context**: Any other relevant information

### Feature Requests

When requesting features, please include:

1. **Clear Title**: Summarize the feature in the title
2. **Problem Statement**: Describe the problem this feature would solve
3. **Proposed Solution**: Describe your proposed solution
4. **Alternatives**: Describe alternatives you've considered
5. **Additional Context**: Any other relevant information

### Security Issues

**DO NOT** report security vulnerabilities through public GitHub issues. Please follow our [Security Policy](SECURITY.md) instead.

## License

By contributing to PenWeb, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to reach out to the maintainers if you have any questions:

- Open a [Discussion](https://github.com/alexcolls/websec/discussions)
- Contact: alex@alexcolls.com

---

Thank you for contributing to PenWeb! 🎉
