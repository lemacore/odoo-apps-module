# Odoo CI/CD - Setup Guide

## File Structure

```
your-repo/
├── .github/
│   └── workflows/
│       └── deploy.yml          ← GitHub Actions workflow
├── scripts/
│   └── upgrade_modules.py      ← Helper script (manual testing)
├── module_a/
│   ├── __manifest__.py
│   └── ...
├── module_b/
│   └── ...
└── README.md
```

---

## 1. GitHub Secrets to Configure

Go to: **GitHub repo → Settings → Secrets and variables → Actions → New repository secret**

### SSH Access

| Secret Name | Example Value | Description |
|---|---|---|
| `SSH_PRIVATE_KEY` | paste private key | SSH private key to the server |
| `SSH_HOST` | `xxx.xxx.xxx.xxx` | Public IP of the server |
| `SSH_USER` | `root` or `ubuntu` | SSH username on the server |

### Path & Docker

| Secret Name | Example Value | Description |
|---|---|---|
| `ODOO_PATH` | `/opt/odoo` | Path to the docker-compose.yml folder on the server |
| `ODOO_ADDONS_PATH` | `/opt/odoo/addons` | Path to the addons git repository folder on the server |
| `COMPOSE_SERVICE` | `odoo` or `web` | Odoo service name in docker-compose.yml |

### Odoo Credentials (for XML-RPC upgrade)

| Secret Name | Example Value | Description |
|---|---|---|
| `ODOO_URL` | `https://erp.lemacore.com` | Odoo URL (no trailing slash) |
| `ODOO_DB` | `my_database` | Odoo database name |
| `ODOO_ADMIN_USER` | `admin` | Odoo admin username |
| `ODOO_ADMIN_PASSWORD` | `your_password` | Odoo admin password |
| `UPGRADE_SCRIPT_PATH` | `scripts/upgrade_modules.py` | Path to the upgrade script inside the repository |

### Email Notifications

| Secret Name | Example Value | Description |
|---|---|---|
| `EMAIL_RECIPIENTS` | `aldi@lemacore.com,cto@lemacore.com` | Recipient emails, comma-separated |
| `SMTP_SERVER` | `smtp.gmail.com` | SMTP server |
| `SMTP_PORT` | `587` | SMTP port (587 for TLS) |
| `SMTP_USER` | `noreply@lemacore.com` | Sender email address |
| `SMTP_PASSWORD` | `app_password` | Password / App Password |
| `EMAIL_FROM` | `"Odoo CI/CD <noreply@lemacore.com>"` | Sender display name |

---

## 2. SSH Key Setup

On your server, generate or use an existing key:

```bash
# Generate a new dedicated key for GitHub Actions (run on local PC)
ssh-keygen -t ed25519 -C "github-actions-deploy" -f ~/.ssh/github_deploy -N ""

# Copy public key to the server
ssh-copy-id -i ~/.ssh/github_deploy.pub root@YOUR_SERVER_IP

# Or manually append to authorized_keys on the server
cat ~/.ssh/github_deploy.pub >> ~/.ssh/authorized_keys
```

Set `SSH_PRIVATE_KEY` to the full contents of `~/.ssh/github_deploy`:

```bash
cat ~/.ssh/github_deploy
# Copy everything including -----BEGIN and -----END lines
```

---

## 3. Email Setup (Gmail)

1. Enable **2-Step Verification** on your Google account
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Create an App Password for "Mail"
4. Use that App Password as `SMTP_PASSWORD`
5. `SMTP_SERVER` = `smtp.gmail.com`, `SMTP_PORT` = `587`

---

## 4. How the Workflow Works

```
Push to branch 18.0
        │
        ▼
┌───────────────────┐
│  Detect Changed   │  ← git diff HEAD~1 HEAD
│  Modules          │  ← find folders with __manifest__.py
└────────┬──────────┘
         │ Changes detected?
    Yes  │              No → ℹ️ Skip (no-changes job)
         ▼
┌───────────────────┐
│  Deploy to Server │  ← SSH → git pull → docker compose restart
│                   │  ← Wait for Odoo to be ready
│                   │  ← XML-RPC upgrade modules
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Send Email       │  ← Email notification (multi-recipient)
└───────────────────┘
```

---

## 5. Manual Trigger (Force Upgrade)

You can trigger the workflow manually from the GitHub UI:

1. Go to the **Actions** tab in your repo
2. Select the **Odoo CI/CD - Auto Deploy & Upgrade** workflow
3. Click **Run workflow**
4. Enter the modules to force-upgrade (optional, comma-separated)
5. Click **Run workflow**

---

## 6. Manual Script Testing

```bash
# Test module upgrade manually before using in CI/CD
python3 scripts/upgrade_modules.py \
  --url https://erp.lemacore.com \
  --db my_database \
  --user admin \
  --password your_password \
  --modules sale,purchase,lm_pos_auto_mrp

# Or via environment variables
export ODOO_URL=https://erp.lemacore.com
export ODOO_DB=my_database
export ODOO_ADMIN_USER=admin
export ODOO_ADMIN_PASSWORD=your_password
python3 scripts/upgrade_modules.py --modules lm_pos_auto_mrp
```

---

## 7. Troubleshooting

### Deployment not triggered
- Make sure there is a `__manifest__.py` file in the module root folder
- Check git diff: `git diff --name-only HEAD~1 HEAD`

### SSH connection refused
- Verify the server IP is correct in `SSH_HOST`
- Check firewall: open port 22 for GitHub Actions IP ranges
- Test manually: `ssh -i ~/.ssh/github_deploy root@SERVER_IP "echo ok"`

### Odoo XML-RPC failed
- Make sure `ODOO_URL` has no trailing slash
- Verify `ODOO_DB` matches the active database name
- Test manually using `scripts/upgrade_modules.py`

### Email not delivered
- For Gmail: make sure you use an **App Password**, not your regular password
- Check SMTP_PORT: Gmail TLS = 587, SSL = 465
- Verify `EMAIL_RECIPIENTS` is set in GitHub Secrets
