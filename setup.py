from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ticket-tailor-mcp",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Ticket Tailor API integration for MCP server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ticket_tailor_mcp_server",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "mcp",
        "httpx>=0.24.0",
        "python-dotenv>=1.0.0",
    ],
) 