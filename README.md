# Odoo Apps Modules

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo](https://img.shields.io/badge/Odoo-18-purple)](https://www.odoo.com)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions)](../../actions)

---

## Overview

This repository contains free and open-source custom Odoo 18 modules developed by **Lema Core Technologies**.

> Goal: share practical Odoo solutions that help developers and businesses build better ERP systems.

---

## Modules

| Module | Description | Status |
|---|---|---|
| `lm_pos_auto_mrp` | Auto-create Manufacturing Orders from Point of Sale transactions | Stable |
| `lm_rfq_sequence` | Separate custom sequence numbering for RFQ vs Purchase Orders | Stable |
| `lm_sale_quotation_sequence` | Separate custom sequence numbering for Quotations vs Sale Orders | Stable |

---

## Installation

```bash
git clone https://github.com/aldirrss/odoo-apps-module.git
```

1. Copy the desired module folder into your Odoo `addons` directory
2. Restart Odoo server
3. Go to **Apps → Update Apps List**
4. Search and install the module

> Also available on [Odoo Apps Store](https://apps.odoo.com/apps/modules/browse?author=Lema%20Core%20Technologies)

---

## CI/CD - Auto Deploy & Upgrade

This repository uses GitHub Actions to automatically deploy and upgrade modules on push to `18.0`.

### How it works

```
Push to branch 18.0
        │
        ▼
Detect changed modules (git diff → find __manifest__.py)
        │
        ├── No changes → skip
        │
        ▼
SSH to server → git pull → docker compose restart
        │
        ▼
Wait for Odoo ready (health check)
        │
        ▼
XML-RPC upgrade changed modules (scripts/upgrade_modules.py)
        │
        ▼
Send email notification (success / failed)
```

### GitHub Secrets required

| Secret | Description |
|---|---|
| `SSH_PRIVATE_KEY` | SSH private key to the server |
| `SSH_HOST` | Server IP address |
| `SSH_USER` | SSH username |
| `ODOO_PATH` | Path to docker-compose folder on server |
| `COMPOSE_SERVICE` | Odoo service name in docker-compose.yml |
| `ODOO_URL` | Odoo URL (no trailing slash) |
| `ODOO_DB` | Database name |
| `ODOO_ADMIN_USER` | Admin username |
| `ODOO_ADMIN_PASSWORD` | Admin password |
| `UPGRADE_SCRIPT_PATH` | Path to upgrade script (`scripts/upgrade_modules.py`) |
| `EMAIL_RECIPIENTS` | Comma-separated recipient emails |
| `SMTP_SERVER` | SMTP server (e.g. `smtp.gmail.com`) |
| `SMTP_PORT` | SMTP port (e.g. `587`) |
| `SMTP_USER` | Sender email address |
| `SMTP_PASSWORD` | SMTP password / App Password |
| `EMAIL_FROM` | Sender display name and email |

> See [scripts/GITHUB_ACTION.md](scripts/GITHUB_ACTION.md) for detailed setup instructions.

### Manual force upgrade

Trigger from **GitHub → Actions → Run workflow** and enter module names manually (comma-separated).

---

## License

All modules are licensed under **LGPL-3** unless stated otherwise.

- Free to use for personal or commercial purposes
- Modification allowed
- If redistributed, license must remain LGPL-3

---

## Contributing

1. Fork this repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
4. Submit a pull request

---

## Contact

- **Email**: lemacoreofficial@email.com
- **GitHub Issues**: [Open an issue](../../issues)
- **Odoo Apps**: [Lema Core Technologies](https://apps.odoo.com/apps/modules/browse?author=Lema%20Core%20Technologies)
