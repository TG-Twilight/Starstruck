<div align="left">
<a href="/README.md">中文</a>&nbsp;|&nbsp;
<a href="/assets/README_en-US.md">English</a> &nbsp;|&nbsp;
<a href="https://awavenue.top/">友情客串😜</a> &nbsp;|&nbsp;
<a href="https://t.me/AWAvenue/893">加入频道</a>
</div>
<br>

<p align="center">
   <img src="https://img.jsdelivr.com/raw.githubusercontent.com/TG-Twilight/Starstruck/main/assets/Starstruck.png">
</p>

# 🧊 Starstruck

*以下大部分内容使用ChatGPT生成，真好使，对着Live唠了一会就给全整出来了，解放双手，要我打这么多字简直太幸苦了😜。*

👀 **Starstruck** 是一个能让你快速统计某个 GitHub 仓库被哪些“显赫人物” Star 过的工具，顺便也能看看这些大佬各自的“影响力值”。

用来做什么？很简单：  
**写论文、做展示、朋友圈发疯、吹牛逼的时候用！**

> “这个项目可是 XX 大佬也 Star 过的！”  
> “我们的开源库被 30 个粉丝过千、总 Star 过万的开发者关注了！”  
> “我不是在卷，我只是在拿数据说话。”

---

## 🧠 项目原理

1. 输入任意 GitHub 仓库（比如 `TG-Twilight/AWAvenue-Ads-Rule`）。
2. 抓取所有 Star 了这个项目的 GitHub 用户。
3. 多线程分析每位用户自己被 Star 的总数（= 影响力指标）。
4. 顺带统计每位用户的粉丝数（Followers）。
5. 导出为 Excel 表格，按总 Star 排序。

---

## 🛠️ 使用方式

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

什么，无法识别pip命令？哥们，先去Microsoft Store安装 [python](https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=neutral&gl=HK&ocid=pdpshare) 吧！

### 2. 填入 GitHub Token  
打开 `Starstruck.py`，在 `TOKEN = "在这里填写你的GitHub Token"` 位置填入你的 GitHub personal access token。
<br>
<br>
[点我生成你自己的GitHub Token](https://github.com/settings/tokens)，建议 classic token，权限仅需 `public_repo` 即可，日期随意。

### 3. 运行脚本

```bash
python Starstruck.py
```

按照提示输入目标仓库（例如 `TG-Twilight` 和 `AWAvenue-Ads-Rule`），等待分析完成。

输出示例：

```
⭐ 前 10 用户（按 Star 总数排序）:
Simon: 1290 stars, 12000 followers
Twilight: 1066 stars, 8000 followers
...
✅ 全部数据已保存到 TG-Twilight_AWAvenue-Ads-Rule_Starstruck.xlsx
```

---

## 📦 输出内容（Excel 文件）

| Username | Total Stars | Followers |
|----------|-------------|-----------|
| Jager    | 114514      | 416       |
| Steve    | 19198       | 2000      |
| ...      | ...         | ...       |

---

## ⚡ 特性

- ✅ 多线程：分析飞快（默认使用 20 线程）
- ✅ 支持大项目（几千 Star 用户也不怕）
- ✅ 输出 Excel，随便怎么用
- ✅ 附带粉丝数，谁是 GitHub 网红一目了然

---

## 🔒 注意事项

- GitHub API 有速率限制，**强烈建议使用 token**。
- 如果名称中有空格，请用“-”替换。
- 提瓦特大陆用户请自行解决cmd访问GitHub的问题。
- 本工具仅用于数据探索、社交分析、学术交流等良性用途。
- 不建议用于黑产或滥用行为，请遵守 GitHub ToS。

---

## 📎 TODO

- [ ] 支持筛选企业用户 / 组织用户
- [ ] 增加按地域、语言等标签分析
- [ ] 爬取关注者数量

---

## 🧊 Starstruck 是什么意思？

> /ˈstɑː.strʌk/  
> “目睹名人时的震惊、仰慕状态。”

用 Star 看 Star，感受“星光熠熠”。

---

## 📬 联系作者

有建议、Bug 或想一起开发？欢迎提 Issue 或 PR！
