<div align="left">
<a href="/README.md">中文</a>&nbsp;|&nbsp;
<a href="/assets/README_en-US.md">English</a> &nbsp;|&nbsp;
<a href="https://awavenue.top/">Guest appearances😜</a> &nbsp;|&nbsp;
<a href="https://t.me/AWAvenue/893">Join Telegram Channel</a>
</div>
<br>

<p align="center">
   <img src="https://img.jsdelivr.com/raw.githubusercontent.com/TG-Twilight/Starstruck/main/assets/Starstruck.png">
</p>

# 🧊 Starstruck

*Most of this content was generated with ChatGPT — super handy! I just talked to it using the “Live” feature for a bit, and it wrote everything out. Total lifesaver — no way I’d type this much myself 😜.*

👀 **Starstruck** is a handy tool that helps you quickly find out **which famous developers have starred a GitHub repository**, along with some fun influence metrics.

What’s it for? Simple:
**For papers, presentations, social posts, or just plain flexing!**

> “Even *that* dev starred our project!”  
> “Our open-source repo is starred by 30 developers with 1k+ followers and 10k+ stars combined!”  
> “This isn’t bragging. It’s *data-driven storytelling*.”

---

## 🚀 Project Recommendation: Web-based Starstruck (Vercel Supported)

A community member has forked and further developed this project into a **fully functional, web-based version of Starstruck**, which requires no local setup and can be deployed to Vercel instantly:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Rovniced/Star-struck-vercel)

👉 GitHub Repository: [https://github.com/Rovniced/Star-struck-vercel](https://github.com/Rovniced/Star-struck-vercel)  

👉 Live Demo: [https://star.awads.cc](https://star.awads.cc/)

---

## 🧠 How It Works

1. You input any GitHub repository (e.g. `TG-Twilight/AWAvenue-Ads-Rule`).
2. The script fetches **all users** who starred the project.
3. It analyzes each user’s **total stars received** across all their own repos (aka "influence index").
4. It also grabs each user’s **follower count**.
5. Outputs to an Excel file, sorted by star count.

---

## 🛠️ How to Use

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

Don’t have `pip`? Bro, go install [Python from the Microsoft Store](https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=neutral&gl=HK&ocid=pdpshare) first!

### 2. Add your GitHub Token

Open `Starstruck.py` and replace:

```python
TOKEN = "your GitHub personal access token here"
```

with your actual token.

> [Generate a GitHub Token here](https://github.com/settings/tokens) – use a classic token with `public_repo` permissions. Expiration date doesn’t matter much.

### 3. Run the script

```bash
python Starstruck.py
```

Follow the prompts to enter a target repository (e.g. `TG-Twilight` and `AWAvenue-Ads-Rule`), and let the analysis run.

Example output:

```
⭐ Top 10 users by total stars:
Simon: 1290 stars, 12000 followers
Twilight: 1066 stars, 8000 followers
...
✅ Data saved to TG-Twilight_AWAvenue-Ads-Rule_Starstruck.xlsx
```

---

## 📦 Output Example (Excel)

| Username | Total Stars | Followers |
|----------|-------------|-----------|
| Jager    | 114514      | 416       |
| Steve    | 19198       | 2000      |
| ...      | ...         | ...       |

---

## ⚡ Features

- ✅ Multithreaded (default: 20 threads)
- ✅ Scales to big projects (handles thousands of stargazers)
- ✅ Excel export – use however you like
- ✅ Includes follower counts – see who’s GitHub-famous at a glance

---

## 🔒 Notes & Tips

- GitHub API has rate limits – **strongly recommend using a token**.
- For repository names with spaces, replace them with `-`.
- This tool is intended for **research, social analysis, and academic exploration**.
- Do not use for shady purposes or spammy behavior. Please respect GitHub’s ToS.

---

## 📎 TODOs

- [ ] Filter org users vs individual devs
- [ ] Add insights by location, language, etc.
- [ ] Track each user's followers in more detail

---

## 🧊 What does “Starstruck” mean?

> /ˈstɑː.strʌk/  
> “Awed or fascinated by someone famous.”

A tool that lets you *see the stars*… through GitHub stars.

---

## 📬 Contact

Got suggestions, found a bug, or want to collaborate? Feel free to open an issue or PR!

