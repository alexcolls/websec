# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.3.x   | :white_check_mark: |
| 0.2.x   | :x:                |
| < 0.2   | :x:                |

## Reporting a Vulnerability

We take the security of PenWeb seriously. If you believe you have found a security vulnerability in PenWeb, we encourage you to let us know right away.

### How to Report

**DO NOT** report security vulnerabilities through public GitHub issues.

Instead, please report them via one of the following methods:

1. **Email**: Send details to [alex@alexcolls.com](mailto:alex@alexcolls.com)
2. **GitHub Security Advisories**: Use the [Security tab](https://github.com/alexcolls/websec/security/advisories/new) in our repository

### What to Include

When reporting a security issue, please include:

- **Type of issue**: (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths of source file(s)** related to the manifestation of the issue
- **Location of the affected source code**: (tag/branch/commit or direct URL)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact of the issue**: including how an attacker might exploit it
- **Any special configuration** required to reproduce the issue

### What to Expect

After you submit a vulnerability report:

1. **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
2. **Assessment**: We will send you a more detailed response within 7 days indicating the next steps
3. **Updates**: We will keep you informed about our progress toward a fix and announcement
4. **Fix Development**: We will work on a fix and coordinate release with you
5. **Public Disclosure**: Once a fix is available, we will release an update and publicly disclose the vulnerability

### Responsible Disclosure

We kindly ask you to:

- **Allow reasonable time** for us to fix the issue before you publicly disclose it
- **Act in good faith** toward our users' privacy and data
- **Avoid disrupting or degrading** our services
- **Do not access or modify** data that is not your own
- **Do not perform attacks** that could harm the reliability or integrity of our services

### Recognition

We value the security community's efforts in improving our project's security:

- We will acknowledge your contribution in our security advisories (unless you prefer to remain anonymous)
- We will credit you in our CHANGELOG for security fixes (with your permission)
- For significant security improvements, we may feature you in our README

## Security Best Practices for Users

### For Developers

1. **Keep Dependencies Updated**: Regularly update all dependencies to patch known vulnerabilities
   ```bash
   poetry update
   ```

2. **Use Environment Variables**: Never commit sensitive data (API keys, passwords) to version control
   - Always use `.env` files for sensitive configuration
   - Ensure `.env` is in `.gitignore`

3. **Run Security Checks**: Use security scanning tools regularly
   ```bash
   # Check for known vulnerabilities in dependencies
   poetry run pip-audit
   
   # Run security linting
   poetry run bandit -r src/
   ```

4. **Code Review**: Review all code changes for potential security issues before merging

### For Tool Usage

**⚠️ IMPORTANT: Legal and Ethical Use**

PenWeb includes powerful security testing tools that can be misused. Users must:

1. **Obtain Explicit Authorization**: Only test systems you own or have written permission to test
2. **Follow Laws and Regulations**: Unauthorized access to computer systems is illegal
3. **Use Responsibly**: Do not use these tools to harm, disrupt, or exploit others
4. **Document Your Authorization**: Keep records of your testing authorization
5. **Report Vulnerabilities Responsibly**: Follow responsible disclosure practices

**Legal Disclaimer**: The authors and contributors assume NO LIABILITY for misuse of these tools. Users are SOLELY RESPONSIBLE for their actions and must ensure compliance with all applicable laws.

### Data Security

1. **Log Files**: If using file logging (`SAVE_LOGS=true`), ensure logs are secured:
   - Logs may contain sensitive URLs, IP addresses, and other data
   - Regularly review and clean up old log files
   - Do not share logs publicly without redacting sensitive information

2. **Output Files**: When cloning websites or generating reports:
   - Store outputs in secure locations (default: `.output/` directory)
   - Review outputs before sharing to ensure no sensitive data is exposed
   - Clean up outputs when no longer needed

3. **AWS Credentials**: If using Lambda deployment:
   - Use IAM roles with minimum required permissions
   - Never hardcode AWS credentials in code
   - Use environment variables or AWS credential files
   - Rotate credentials regularly

## Security Features

### Current Security Measures

1. **Input Validation**: All user inputs are validated before processing
2. **Error Handling**: Sensitive information is not exposed in error messages
3. **Logging Controls**: File logging is optional and user-controlled via environment variables
4. **Authorization Checks**: Offensive tools require user confirmation before execution
5. **Legal Warnings**: Clear warnings displayed about authorized use only

### Planned Security Enhancements

- [ ] Rate limiting for API endpoints
- [ ] Enhanced input sanitization
- [ ] Security headers for web components
- [ ] Automated dependency vulnerability scanning in CI/CD
- [ ] Security-focused unit tests

## Vulnerability Disclosure Policy

### Severity Levels

We classify vulnerabilities using the following severity levels:

- **Critical**: Issues that allow remote code execution or full system compromise
- **High**: Issues that allow unauthorized data access or privilege escalation
- **Medium**: Issues that allow limited unauthorized access or information disclosure
- **Low**: Issues with limited impact or requiring significant user interaction

### Disclosure Timeline

- **Critical/High Severity**: Fix and release within 7-14 days
- **Medium Severity**: Fix and release within 30 days
- **Low Severity**: Fix and release within 60 days

### Public Disclosure

Once a fix is released:

1. We will publish a security advisory on GitHub
2. We will update the CHANGELOG with security fix details
3. We will credit the reporter (with their permission)
4. We will notify users through release notes

## Security Tools and Resources

### Recommended Tools for Security Testing

- **Static Analysis**: Bandit, Pylint
- **Dependency Scanning**: pip-audit, Safety
- **Secret Scanning**: detect-secrets, git-secrets
- **Container Scanning**: Trivy, Snyk (for Docker images)

### Security Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE (Common Weakness Enumeration)](https://cwe.mitre.org/)
- [CVE (Common Vulnerabilities and Exposures)](https://cve.mitre.org/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)

## Contact

For security-related questions or concerns, contact:

- **Email**: alex@alexcolls.com
- **GitHub Security Advisories**: [Report a vulnerability](https://github.com/alexcolls/websec/security/advisories/new)

---

**Last Updated**: November 2025  
**Version**: 0.3.1

Thank you for helping keep PenWeb and its users safe! 🔒
