# PenWeb CLI Usage Guide

## Starting the CLI

There are several ways to start the interactive CLI:

### Method 1: Using the convenience script
```bash
./run.sh
```

### Method 2: Using Poetry
```bash
poetry run python src/main.py
```

### Method 3: Direct Python execution
```bash
python3 src/main.py
```

## CLI Features

The PenWeb CLI provides an interactive menu with 7 integrated tools (3 defensive, 2 utility, 2 offensive):

### 🛰️ [1] GPS (DEFENSIVE)
Device location tracking with multi-provider support.

**Default:** Uses free Traccar demo server with IP-based geolocation - NO hardware or account required!

**Use Cases:**
- Track device location
- Fleet management
- Personal location history

### 🔐 [2] VPN (DEFENSIVE)
Multi-provider VPN manager.

**Default:** Uses free VPNGate public servers - NO account required!

**Use Cases:**
- Privacy protection
- Bypass geo-restrictions
- Secure public WiFi usage

### 📧 [3] Email
Temporary email address manager.

**Default:** Uses free 1secmail API - NO account required!

**Use Cases:**
- Privacy protection for online registrations
- Testing email workflows
- Avoid spam

### 🌐 [4] Ping URL
Test URL availability and measure response time.

**Use Case:**
- Check if a website is online
- Measure server response time
- Validate endpoint accessibility

**Example Flow:**
1. Select option `4`
2. Enter target URL (e.g., `https://example.com`)
3. View status code and response time

### 📋 [5] Clone Website
Download website HTML, CSS, and JavaScript files for offline analysis.

**Use Case:**
- Create local copy of website for analysis
- Extract frontend resources
- Study website structure

**Example Flow:**
1. Select option `5`
2. Enter website URL
3. Specify output directory (default: `.output/cloned_site`)
4. Wait for download to complete

### 💥 [6] DDoS Test (OFFENSIVE)
Test rate limiting by making repeated requests to a URL.

**⚠️ WARNING:** This is an offensive tool. Only use on systems you own or have explicit permission to test.

**Use Case:**
- Test API rate limiting effectiveness
- Validate WAF (Web Application Firewall) configuration
- Stress test endpoint capacity

**Example Flow:**
1. Select option `6`
2. Confirm authorization
3. Enter target URL
4. Set request interval (e.g., `0.5` seconds)
5. Set max attempts (optional, press Enter for unlimited)
6. Monitor requests until blocked or limit reached
7. Press Ctrl+C to stop early

**Output:**
- Real-time request status
- Success/failure counts
- Final blocking status
- Error messages

### 🔐 [7] Login Test (OFFENSIVE)
Test login form security by attempting credential combinations.

**⚠️ WARNING:** This is an offensive tool. Only use on systems you own or have explicit permission to test.

**Use Case:**
- Test login rate limiting
- Verify CAPTCHA implementation
- Validate account lockout mechanisms
- Security audit compliance

**Example Flow:**
1. Select option `7`
2. Confirm authorization
3. Enter login page URL
4. Provide email addresses (comma-separated):
   - Example: `admin@site.com, user@site.com, test@site.com`
5. Provide password keywords (comma-separated):
   - Example: `password, admin, welcome`
   - Tool will generate variations: `Password123`, `admin!`, etc.
6. Set delay between attempts (e.g., `1.0` seconds)
7. Set max attempts (optional)
8. Monitor login attempts
9. Press Ctrl+C to stop early

**Output:**
- Detected form fields
- Generated password variations
- Real-time attempt status
- Blocking detection
- Summary with success/failure counts

## Navigation

- **Select option:** Enter number `0-7`
- **Cancel input:** Press `Ctrl+C`
- **Exit program:** Select option `0` or press `Ctrl+C`

## Legal and Ethical Considerations

**IMPORTANT:** 

1. ✅ **Always obtain proper authorization** before testing any system
2. ⚠️ **Unauthorized access is illegal** - you can face criminal charges
3. 📝 **Document your authorization** - keep written permission
4. 🛡️ **Test responsibly** - avoid disrupting services
5. 🤝 **Follow disclosure practices** - report vulnerabilities properly

### When you CAN use these tools:
- Testing your own websites and systems
- Authorized penetration testing with written permission
- Bug bounty programs with proper scope
- Security audits with client contracts
- Educational purposes on your own infrastructure

### When you CANNOT use these tools:
- Testing third-party websites without permission
- "Curiosity testing" on public websites
- Testing competitors' systems
- Any unauthorized access attempts

## Troubleshooting

### Import Errors
If you get module import errors:
```bash
# Make sure you're in the project root
cd /home/quantium/labs/websec

# Install dependencies
poetry install
```

### Dependencies Missing
If tools fail with missing dependencies:
```bash
poetry install
```

### Permission Issues
If script won't run:
```bash
chmod +x run.sh
```

## Examples

### Example 1: Quick Ping Test
```
Select option: 4
Enter URL to ping: https://google.com
Result: Status 200, 45ms response time
```

### Example 2: Clone a Simple Website
```
Select option: 5
Enter website URL: https://example.com
Output directory: (press Enter for default .output/cloned_site)
Result: Downloaded 5 files (1 HTML, 2 CSS, 2 JS)
```

### Example 3: Test Rate Limiting
```
Select option: 6
Authorization confirmed: yes
Enter URL: https://api.mysite.com/endpoint
Request interval: 0.5
Max attempts: 100
Result: Blocked after 47 requests with 429 status code
```

### Example 4: Test Login Security
```
Select option: 7
Authorization confirmed: yes
Enter login URL: https://mysite.com/login
Emails: admin@mysite.com, test@mysite.com
Keywords: password, admin
Delay: 1.0 seconds
Max attempts: 50
Result: Blocked after 15 attempts, CAPTCHA triggered
```

## Features

- ✨ Interactive menu with color-coded options
- 🎨 Beautiful ASCII art banner
- ⚖️ Legal warnings and authorization checks
- 🔍 Real-time progress monitoring
- 📊 Detailed result summaries
- ⌨️ Clean error handling
- 🛑 Graceful interruption (Ctrl+C)

## Output Colors

- 🟢 **Green:** Success messages, safe operations
- 🔴 **Red:** Errors, offensive tools
- 🟡 **Yellow:** Warnings, important notices
- 🔵 **Cyan:** User prompts, information
- ⚪ **Gray:** Secondary information

## Tips

1. **Start with Ping:** Test basic connectivity first
2. **Check Authorization:** Always verify you have permission before using offensive tools
3. **Start Conservative:** Use longer delays and lower attempt counts initially
4. **Monitor Resources:** Keep an eye on network traffic and system resources
5. **Document Everything:** Keep logs of your testing activities
6. **Respect Rate Limits:** Don't overwhelm systems even when authorized

## Support

For issues or questions:
1. Check the main [README.md](../README.md)
2. Review [docs/CLI_SETUP.md](CLI_SETUP.md) for installation help
3. Open an issue on [GitHub](https://github.com/alexcolls/websec/issues)

## Version

Current Version: **v0.3.1**
Last Updated: November 2025

---

**Remember:** With great power comes great responsibility. Use these tools ethically and legally! 🛡️

