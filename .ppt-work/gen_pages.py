"""按 pptx-craft 骨架生成 8 页 HTML（page-N.pptx.html）。"""
import pathlib

OUT = pathlib.Path(__file__).parent / "pages"
OUT.mkdir(parents=True, exist_ok=True)
RED = "#D33941"

HEAD = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <script src="https://cdn.digitalhumanai.top/slidagent/pptx-craft/assets/vendors/tailwind.js"></script>
  <link href="https://cdn.digitalhumanai.top/slidagent/pptx-craft/assets/css/fonts.css" rel="stylesheet">
  <link href="https://cdn.digitalhumanai.top/slidagent/pptx-craft/assets/vendors/fontawesome/css/all.min.css" rel="stylesheet">
  {extra}
  <style type="text/tailwindcss">
    @layer utilities {
      .ppt-slide { @apply relative w-[1280px] h-[720px] mx-auto box-border overflow-hidden; }
      .ppt-slide *, .ppt-slide *::before, .ppt-slide *::after { @apply box-border; max-width: 100%; }
      .ppt-slide img, .ppt-slide video, .ppt-slide canvas, .ppt-slide svg,
      .ppt-slide .echarts-main, .ppt-slide .chart-container, .ppt-slide [id*="chart" i] {
        @apply max-w-full max-h-full object-contain;
      }
      .ppt-slide [id*="chart" i], .ppt-slide .chart-container, .ppt-slide .echarts-main {
        width: 100%; height: 100%; min-height: 160px;
      }
      .ppt-slide :has(> [id*="chart" i]), .ppt-slide :has(> .chart-container), .ppt-slide :has(> .echarts-main) {
        min-height: 160px;
      }
      .content-safe { @apply w-[1220px] h-[660px] my-[30px] mx-auto flex flex-col overflow-hidden; }
      .ppt-slide [class*="blur"], .ppt-slide [style*="blur"] { filter: none !important; backdrop-filter: none !important; }
      .ppt-slide [class*="gradient"] { background-image: none !important; }
      .ppt-slide [class*="backdrop-blur"], .ppt-slide [style*="backdrop-filter"] { backdrop-filter: none !important; }
      .ppt-slide { font-family: "WenYuan Sans SC", "Noto Sans SC", sans-serif !important; }
    }
  </style>
</head>
<body style="margin:0;padding:0;background:#ffffff;">
"""
ECHARTS = '<script src="https://cdn.digitalhumanai.top/slidagent/pptx-craft/assets/vendors/echarts.min.js"></script>'


def content_page(title, main, src, note="2026 级新生篮球迎新杯 · 宣传", typ="content", charts=False, script=""):
    return (HEAD.replace("{extra}", ECHARTS if charts else "") + f"""  <div class="ppt-slide flex flex-col" type="{typ}">
    <div class="content-safe">
      <header class="h-[60px] flex-shrink-0 flex items-center gap-4">
        <div class="w-[8px] h-[40px]" style="background:{RED};"></div>
        <h1 class="text-[37px] font-bold text-balance" style="color:#000000;">{title}</h1>
      </header>
      <main class="flex-1 min-h-0 flex flex-col gap-4 pt-4">
{main}
      </main>
      <footer class="h-[30px] flex-shrink-0 flex justify-between items-center text-[12px]" style="color:#898989;">
        <span>{src}</span><span>{note}</span>
      </footer>
    </div>
  </div>
{script}</body>
</html>
""")


def card(icon, head, body):
    return f"""        <div class="flex-1 p-5 flex flex-col gap-2" style="border:1px solid #DDDDDD;">
          <div class="flex items-center gap-3"><i class="fa-solid {icon} text-[22px]" style="color:{RED};"></i>
            <span class="text-[22px] font-bold" style="color:#000000;">{head}</span></div>
          <p class="text-[19px] leading-[1.5]" style="color:#555757;">{body}</p>
        </div>"""


def stat(num, unit, label):
    return f"""        <div class="flex-1 p-5 flex flex-col items-start gap-1" style="border:1px solid #DDDDDD;">
          <div><span class="text-[48px] font-bold" style="color:{RED};font-family:Arial;">{num}</span><span class="text-[21px] font-bold ml-1" style="color:#000000;">{unit}</span></div>
          <span class="text-[16px]" style="color:#555757;">{label}</span>
        </div>"""


PLAN = "来源：本次迎新杯活动策划方案"
pages = []

# P1 封面
pages.append(HEAD.replace("{extra}", "") + f"""  <div class="ppt-slide flex flex-col" type="cover" style="background:{RED};">
    <div class="content-safe justify-center gap-6 px-16">
      <p class="text-[22px] font-bold" style="color:#FFFFFF;">计算机学院 · 2026 级新生</p>
      <h1 class="text-[60px] font-bold leading-[1.25]" style="color:#FFFFFF;">篮球迎新杯：用一场球赛<br>认识你的新同学</h1>
      <div class="w-[120px] h-[6px]" style="background:#FFFFFF;"></div>
      <p class="text-[22px]" style="color:#FFFFFF;">16 支班级队伍 · 5 个比赛日 · 32 场比赛 · 冠军奖杯等你来拿</p>
      <p class="text-[19px]" style="color:#FFFFFF;">主办：计算机学院学生会体育部　｜　2026 年 10 月</p>
    </div>
  </div>
</body>
</html>
""")

# P2 赛事概览
pages.append(content_page(
    "迎新杯在 5 天内用 32 场比赛串起 16 个新生班级",
    f"""        <div class="flex gap-4">
{stat(16, "支", "参赛队伍（每个新生班级 1 支）")}
{stat(32, "场", "全部比赛场次")}
{stat(5, "天", "比赛日（10 月 12 日—16 日）")}
{stat(3, "块", "同时使用的室内标准场地")}
        </div>
        <div class="flex gap-4 flex-1">
{card("fa-location-dot", "比赛地点", "学校体育馆一层，3 块场地同时开赛，看台对全体师生开放")}
{card("fa-users", "参赛对象", "计算机学院 2026 级全体新生，以班级为单位组队")}
{card("fa-handshake", "活动目的", "以赛促融，帮助新生在开学第一个月结识同学、融入集体")}
        </div>""",
    PLAN))

# P3 赛程（图表）
pages.append(content_page(
    "小组赛占全部场次的四分之三，决赛日只留 2 场焦点战",
    """        <div class="flex gap-4 flex-1 min-h-0">
          <div class="flex-[3] min-h-0 p-4" style="border:1px solid #DDDDDD;">
            <div id="schedule-chart" class="w-full h-full"></div>
          </div>
          <div class="flex-[2] flex flex-col gap-4">
            <div class="p-5" style="border:1px solid #DDDDDD;"><p class="text-[22px] font-bold" style="color:#000000;">10/12—10/14 小组赛</p><p class="text-[19px] leading-[1.5]" style="color:#555757;">4 个小组单循环，每天 8 场</p></div>
            <div class="p-5" style="border:1px solid #DDDDDD;"><p class="text-[22px] font-bold" style="color:#000000;">10/15 淘汰赛</p><p class="text-[19px] leading-[1.5]" style="color:#555757;">1/4 决赛 4 场 + 半决赛 2 场</p></div>
            <div class="p-5" style="border:1px solid #D33941;background:#FFF1EF;"><p class="text-[22px] font-bold" style="color:#D33941;">10/16 决赛日</p><p class="text-[19px] leading-[1.5]" style="color:#000000;">季军赛 + 冠军决赛，19:00 开赛</p></div>
          </div>
        </div>""",
    PLAN, typ="data", charts=True,
    script="""  <script>
    var c = echarts.init(document.getElementById("schedule-chart"), null, { renderer: "svg" });
    c.setOption({ animation: false, grid: { left: 60, right: 30, top: 70, bottom: 50 },
      title: { text: "每日比赛场次", left: "center", textStyle: { fontSize: 18, color: "#000000" } },
      xAxis: { type: "category", data: ["10/12", "10/13", "10/14", "10/15", "10/16"], axisLabel: { fontSize: 16, color: "#555757" } },
      yAxis: { type: "value", axisLabel: { fontSize: 14, color: "#555757" }, splitLine: { lineStyle: { color: "#DDDDDD" } } },
      series: [{ type: "bar", barWidth: 56, data: [8, 8, 8, 6, 2], itemStyle: { color: "#D33941" },
        label: { show: true, position: "top", fontSize: 18, color: "#000000" } }] });
  </script>
"""))

# P4 赛制与规则
pages.append(content_page(
    "比赛采用 FIBA 标准规则，新生零基础也能快速上手",
    f"""        <div class="flex gap-4 flex-1">
{card("fa-stopwatch", "4 节 × 10 分钟", "沿用 FIBA 规则的标准节制；小组赛可缩短为 4 节 × 8 分钟")}
{card("fa-people-group", "每队最多 12 人", "场上 5 人，可无限次换人；鼓励每位队员都有上场时间")}
        </div>
        <div class="flex gap-4 flex-1">
{card("fa-sitemap", "小组循环 + 淘汰", "小组前 2 名晋级 8 强，之后单场淘汰决出名次")}
{card("fa-heart", "友谊第一", "设女生加分规则：女生进球额外 +1 分，鼓励混合组队")}
        </div>""",
    "来源：FIBA Official Basketball Rules 2024（比赛时间、球队人数条款）；赛制与加分规则为本次活动安排"))

# P5 奖项（图表）
pages.append(content_page(
    "8 类奖项覆盖团队、个人和体育精神，每位队员都有参与奖",
    """        <div class="flex gap-4 flex-1 min-h-0">
          <div class="flex-[3] min-h-0 p-4" style="border:1px solid #DDDDDD;">
            <div id="award-chart" class="w-full h-full"></div>
          </div>
          <div class="flex-[2] flex flex-col gap-4">
            <div class="p-5" style="border:1px solid #DDDDDD;"><p class="text-[22px] font-bold" style="color:#000000;">团队奖</p><p class="text-[19px] leading-[1.5]" style="color:#555757;">冠亚季军 + 最佳风尚队，共 4 支队伍</p></div>
            <div class="p-5" style="border:1px solid #DDDDDD;"><p class="text-[22px] font-bold" style="color:#000000;">个人奖</p><p class="text-[19px] leading-[1.5]" style="color:#555757;">MVP、得分王、最佳新人、最佳啦啦队</p></div>
            <div class="p-5" style="border:1px solid #DDDDDD;"><p class="text-[22px] font-bold" style="color:#000000;">参与奖</p><p class="text-[19px] leading-[1.5]" style="color:#555757;">所有队员获纪念队服与综测加分</p></div>
          </div>
        </div>""",
    PLAN, typ="data", charts=True,
    script="""  <script>
    var c = echarts.init(document.getElementById("award-chart"), null, { renderer: "svg" });
    c.setOption({ animation: false, grid: { left: 110, right: 50, top: 60, bottom: 30 },
      title: { text: "各奖项获奖名额", left: "center", textStyle: { fontSize: 18, color: "#000000" } },
      xAxis: { type: "value", minInterval: 1, axisLabel: { fontSize: 14, color: "#555757" }, splitLine: { lineStyle: { color: "#DDDDDD" } } },
      yAxis: { type: "category", data: ["最佳啦啦队", "最佳新人", "得分王", "MVP", "最佳风尚队", "季军", "亚军", "冠军"], axisLabel: { fontSize: 15, color: "#000000" } },
      series: [{ type: "bar", barWidth: 22, data: [1, 3, 1, 1, 1, 1, 1, 1], itemStyle: { color: "#D33941" },
        label: { show: true, position: "right", fontSize: 15, color: "#000000" } }] });
  </script>
"""))

# P6 报名方式
pages.append(content_page(
    "以班级为单位报名，10 月 8 日前完成三步即可参赛",
    f"""        <div class="flex gap-4 flex-1">
{card("fa-1", "组队", "班长或体育委员组织 8—12 名队员，推选 1 名队长")}
{card("fa-2", "提交名单", "10 月 8 日 18:00 前在学院小程序提交队员名单与队名")}
{card("fa-3", "参加抽签", "10 月 9 日 19:00 在学生活动中心抽签分组")}
        </div>
        <div class="p-5 flex items-center gap-4" style="border:1px solid #D33941;background:#FFF1EF;">
          <i class="fa-solid fa-circle-info text-[22px]" style="color:{RED};"></i>
          <p class="text-[19px]" style="color:#000000;">咨询：学生会体育部　｜　报名截止后不再增补队伍</p>
        </div>""",
    PLAN))

# P7 安全保障
pages.append(content_page(
    "医护、保险、热身三道保障，让每一场比赛都安心",
    f"""        <div class="flex gap-4 flex-1">
{card("fa-kit-medical", "现场医护", "校医院医护人员全程驻场，配备急救箱与冰袋")}
{card("fa-shield-halved", "意外保险", "学院为全部参赛队员统一购买赛事意外险")}
{card("fa-person-running", "赛前热身", "每场赛前预留 10 分钟热身，裁判检查护具与鞋袜")}
        </div>
        <div class="flex gap-4 flex-1">
{card("fa-user-check", "健康承诺", "参赛前签署健康承诺书，有心脏等疾病史者不宜上场")}
{card("fa-flag", "专业裁判", "邀请体育学院裁判协会执裁，保证判罚公正")}
        </div>""",
    PLAN))

# P8 结束页
pages.append(HEAD.replace("{extra}", "") + f"""  <div class="ppt-slide flex flex-col" type="ending">
    <div class="content-safe justify-center items-center gap-6">
      <i class="fa-solid fa-basketball text-[72px]" style="color:{RED};"></i>
      <h1 class="text-[56px] font-bold" style="color:#000000;">球场见，新同学！</h1>
      <div class="w-[120px] h-[6px]" style="background:{RED};"></div>
      <p class="text-[22px]" style="color:#555757;">10 月 8 日报名截止 · 10 月 12 日正式开赛</p>
    </div>
  </div>
</body>
</html>
""")

for i, html in enumerate(pages, 1):
    (OUT / f"page-{i}.pptx.html").write_text(html, encoding="utf-8")
print(f"wrote {len(pages)} pages to {OUT}")
