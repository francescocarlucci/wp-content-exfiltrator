# PoC: Data Exfiltration via WordPress Search REST API

## Overview

This Proof-of-Concept (PoC) demonstrates a vulnerability that enables **data exfiltration via WordPress's Search REST API**. The issue occurs when **search endpoints return metadata or protected content** identifiers based on partial string matches, even when the content itself is access-controlled.

By leveraging blind enumeration techniques, an attacker can **brute-force the protected content** character-by-character using search queries and response metadata (e.g., known post ID presence in results).

## Vulnerability Details

**Vulnerability Class**: Information Disclosure / Insecure Data Exposure

**Attack Vector**:
- Send crafted search queries (e.g., quoted substrings starting with specific characters).
- Infer correct characters based on whether a known post ID appears in the API response.
- Build the target content string incrementally.

## How It Works

1. **Target Identification**: The attacker must know a valid post ID (`target_id`) of a protected or private post.

2. **Character Brute-Forcing**:
   - Starts with a special symbol like `>` to avoid prefix collision.
   - Encodes characters individually in a search query.
   - Observes presence of `target_id` in results as a signal of a match.

3. **Data Recovery**:
   - Builds the post content progressively, one character at a time.
   - Exfiltrates sensitive or private content without direct access.

## Script Usage

### Prerequisites

- Python 3
- `requests` library

### Example

```bash
python3 exfiltrate_wp_content.py
```

#### Parameters (set in script)

- `base_url`: Base URL of the WordPress instance (e.g., `http://private.local`)
- `target_id`: The known ID of a post that should be protected (e.g., `31`)

## Example Output

```
Starting exfiltration...
Testing first character: 'T'
First character found: 'T'
Testing next character: 'e' -> >Te
Character added: 'e' -> >Te
...
Exfiltration complete.
Exfiltrated Content: Test content here
```

## Sample CVEs

- CVE-2024-1129
- CVE-2024-11153
- CVE-2024-11090
- CVE-2024-11290
- CVE-2024-11282
- CVE-2024-11297
- CVE-2024-11291
- CVE-2024-11295
- CVE-2024-11294
- CVE-2024-11280
- CVE-2024-11008
- CVE-2024-11351
- CVE-2024-11106
- CVE-2024-11292
- CVE-2024-11083
- CVE-2024-11089

## Disclaimer

This code is for **educational and responsible disclosure purposes only**. Do **not** use against systems without **explicit authorization**. The author assumes **no liability** for misuse.

## License

This PoC is released under the MIT License.
