# 🚀 Railway Deployment Guide — Agro System

---

## ✅ STEP 1 — Get a Gmail App Password (for email features)

Your app sends emails for registration, password reset, etc. Gmail blocks normal passwords for apps — you need an **App Password**.

1. Go to your Google Account → https://myaccount.google.com
2. Click **Security** (left sidebar)
3. Under "How you sign in to Google", click **2-Step Verification** → turn it ON if not already
4. Go back to Security → scroll down → click **App passwords**
5. Select app: **Mail** | Select device: **Other** → type "Agro System" → click **Generate**
6. Copy the **16-character password** shown (like: `abcd efgh ijkl mnop`) — remove spaces when using it
7. Save it — you'll use it as `MAIL_PASSWORD` below

---

## ✅ STEP 2 — Push your code to GitHub

1. Go to https://github.com → create a **New repository** (name: `agro-system`, set to Private)
2. Open terminal/command prompt on your PC and run:

```bash
cd path/to/agro_system    # go into your project folder

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/agro-system.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

## ✅ STEP 3 — Create Railway account and new project

1. Go to https://railway.app → click **Login** → sign in with GitHub
2. Click **New Project**
3. Choose **Deploy from GitHub repo**
4. Select your `agro-system` repository
5. Railway will detect the Dockerfile automatically → click **Deploy**

---

## ✅ STEP 4 — Add MySQL Database

1. In your Railway project dashboard, click **+ New** (top right)
2. Select **Database** → choose **MySQL**
3. Railway creates a MySQL service and auto-generates connection variables
4. Click on the MySQL service → go to **Variables** tab
5. Note these values (you'll need them in the next step):
   - `MYSQLHOST`
   - `MYSQLUSER` 
   - `MYSQLPASSWORD`
   - `MYSQLDATABASE`
   - `MYSQLPORT`

---

## ✅ STEP 5 — Set Environment Variables

1. In Railway, click on your **Flask app service** (not the MySQL one)
2. Go to the **Variables** tab
3. Click **Raw Editor** and paste the following — fill in YOUR values:

```
SECRET_KEY=pick-any-long-random-string-like-this-abc123xyz789
MYSQL_HOST=<paste MYSQLHOST value from MySQL service>
MYSQL_USER=<paste MYSQLUSER value>
MYSQL_PASSWORD=<paste MYSQLPASSWORD value>
MYSQL_DB=<paste MYSQLDATABASE value>
MYSQL_PORT=3306
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-gmail@gmail.com
MAIL_PASSWORD=abcdefghijklmnop
MAIL_DEFAULT_SENDER=Agro System <your-gmail@gmail.com>
ADMIN_EMAIL=your-gmail@gmail.com
JAZZCASH_NUMBER=03001234567
EASYPAISA_NUMBER=03001234567
OWNER_NAME=Your Full Name
```

**Things to change:**
- `SECRET_KEY` → type any random text (longer = better)
- `MYSQL_HOST/USER/PASSWORD/DB` → copy exact values from Railway MySQL service Variables tab
- `MAIL_USERNAME` → your Gmail address
- `MAIL_PASSWORD` → the 16-char App Password from Step 1 (no spaces)
- `ADMIN_EMAIL` → your Gmail (admin login email)
- `JAZZCASH_NUMBER` / `EASYPAISA_NUMBER` → your real numbers
- `OWNER_NAME` → your name

4. Click **Save** → Railway redeploys automatically

---

## ✅ STEP 6 — Get your live URL

1. Click on your Flask service in Railway
2. Go to **Settings** tab → **Networking** section
3. Click **Generate Domain** — Railway gives you a URL like:
   `https://agro-system-production.up.railway.app`
4. Open that URL — your app should load!

---

## ✅ STEP 7 — Login as Admin

The app auto-creates an admin account on first run:

- **Username/Email:** whatever you set as `ADMIN_EMAIL`
- **Password:** `admin123`

⚠️ **Change the admin password immediately** after first login → go to Profile → Change Password

---

## 🔧 TROUBLESHOOTING

### App crashes / won't start
- Click on your service → **Deployments** tab → click on the failed deploy → **View Logs**
- Most common cause: wrong MySQL connection variables — double-check Step 5

### Emails not sending
- Make sure 2-Step Verification is ON in your Google account
- Make sure you used the App Password (16 chars), not your normal Gmail password
- Check that `MAIL_USERNAME` matches the Gmail account that generated the App Password

### Database connection error
- Go to Railway → MySQL service → **Connect** tab — copy the exact host/user/password
- Make sure `MYSQL_PORT=3306`

### After code changes — redeploy
```bash
git add .
git commit -m "describe your change"
git push
```
Railway auto-deploys on every push to `main`.

---

## 📋 SUMMARY CHECKLIST

- [ ] Gmail App Password generated
- [ ] Code pushed to GitHub
- [ ] Railway project created from GitHub repo
- [ ] MySQL plugin added to Railway project
- [ ] All environment variables set in Flask service
- [ ] Domain generated and app opens
- [ ] Admin password changed from default `admin123`
