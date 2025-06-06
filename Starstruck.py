import requests
import time
from tqdm import tqdm
import concurrent.futures
import pandas as pd

# GitHub Token
TOKEN = "在这里填写你的GitHub Token"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {TOKEN}"
}

# 获取 Stargazers
def get_stargazers(owner, repo):
    users = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/stargazers?page={page}&per_page=100"
        res = requests.get(url, headers=HEADERS)
        if res.status_code != 200:
            print("Error:", res.json())
            break
        data = res.json()
        if not data:
            break
        users.extend([u["login"] for u in data])
        page += 1
    return users

# 获取用户仓库 Star 总数
def get_user_star_count(username):
    try:
        total_stars = 0
        page = 1
        while True:
            url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
            res = requests.get(url, headers=HEADERS)
            if res.status_code != 200:
                return (username, 0)
            repos = res.json()
            if not repos:
                break
            for repo in repos:
                total_stars += repo.get("stargazers_count", 0)
            page += 1
        return (username, total_stars)
    except Exception as e:
        return (username, 0)

def starstruck(owner, repo, max_workers=20):
    users = get_stargazers(owner, repo)
    star_data = []
    with concurrent.futures.ThreadPool.Executor(max_workers=max_workers) as executor:
        futures = {executor.submit(get_user_star_count, user): user for user in users}
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            result = future.result()
            if result:
                star_data.append(result)
    star_data.sort(key=lambda x: x[1], reverse=True)
    return star_data

if __name__ == "__main__":
    # 展示 Starstruck 符号logo
    print(r"""
  _________ __                         __                        __    
 /   _____//  |______ _______  _______/  |________ __ __   ____ |  | __
 \_____  \\   __\__  \\_  __ \/  ___/\   __\_  __ \  |  \_/ ___\|  |/ /
 /        \|  |  / __ \|  | \/\___ \  |  |  |  | \/  |  /\  \___|    < 
/_______  /|__| (____  /__|  /____  > |__|  |__|  |____/  \___  >__|_ \
        \/           \/           \/                          \/     \/ by TG-Twilight
""")
    
    owner = input("输入仓库所有者用户名（如 TG-Twilight）: ").strip()
    repo = input("输入仓库名（如 Starstruck，空格换成“-”）: ").strip()
    result = starstruck(owner, repo, max_workers=20)

    print("\n⭐ 前 10 用户（按 Star 总数排序）:")
    for user, star_sum in result[:10]:
        print(f"{user}: {star_sum}")

    # 保存为 Excel 文件
    df = pd.DataFrame(result, columns=["Username", "Total Stars"])
    filename = f"{owner}_{repo}_Starstruck.xlsx"
    df.to_excel(filename, index=False)
    print(f"\n✅ 全部数据已保存到 {filename}")
