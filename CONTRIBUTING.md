# Contributing to Faster Research Agent

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/faster-research-agent/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Relevant logs or error messages

### Suggesting Enhancements

1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Provide use cases and examples
4. Discuss potential implementation approaches

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests if applicable
5. Update documentation as needed
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

## 🏗️ Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/faster-research-agent.git
cd faster-research-agent

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Install development dependencies
uv pip install pytest black flake8 mypy
```

## 📝 Code Style

### Python Style Guide

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://github.com/psf/black) for formatting
- Maximum line length: 100 characters
- Use type hints where possible

### Formatting

```bash
# Format code
black research/

# Check linting
flake8 research/

# Type checking
mypy research/
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_tools.py

# Run with coverage
pytest --cov=research tests/
```

## 📚 Documentation

- Update README.md for new features
- Add docstrings to functions and classes
- Update type hints
- Include usage examples

### Docstring Format

```python
def search_web(query: str, num_results: int = 5) -> List[Any]:
    """
    Search the web using Exa's auto search.
    
    Args:
        query: Search query string
        num_results: Number of results to return (default: 5)
        
    Returns:
        List of search results with title, url, and text
        
    Raises:
        ExaAPIError: If the API call fails
        
    Example:
        >>> results = search_web("AI agents", num_results=3)
        >>> print(len(results))
        3
    """
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Unit tests for core modules
- [ ] Integration tests for LangGraph workflow
- [ ] Error handling improvements
- [ ] Performance optimizations

### Medium Priority
- [ ] Web UI (Streamlit/Gradio)
- [ ] Additional search providers
- [ ] Export functionality (PDF, Markdown)
- [ ] Logging and monitoring

### Nice to Have
- [ ] Multi-language support
- [ ] Custom agent creation
- [ ] Advanced visualization
- [ ] CLI improvements

## 🔍 Code Review Process

1. All PRs require at least one approval
2. CI/CD checks must pass
3. Code must follow style guidelines
4. Documentation must be updated
5. Tests should be included for new features

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 💬 Questions?

Feel free to:
- Open a [Discussion](https://github.com/yourusername/faster-research-agent/discussions)
- Comment on related issues
- Reach out to maintainers

## 🙏 Thank You!

Your contributions make this project better for everyone!
