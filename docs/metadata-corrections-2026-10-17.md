# 主页引文与专利信息修订

修订日期：2026-10-17。根据当日现行网站复核结果，修订公开展示与对应内容源。专利状态按用户要求保持不变。

## 本次修订

- **J2 奖项名称**：将 `IEEE SPS Best Paper Award` 改为 `2025 IEEE Signal Processing Society Young Author Best Paper Award`，明确官方奖项类别和年度。依据为 [IEEE SPS 官方获奖名单](https://signalprocessingsociety.org/our-story/news-updates/2026/01/2025-ieee-signal-processing-society-awards-winners)；首页和 Awards 页此前已使用该奖项名称。
- **B2 书章节**：按用户要求，从网页、`.jemdoc` 内容源及当前 `data/publication-metadata.json` 清单移除尚未核实的 `Optimization of Active Metasurfaces` 条目。B1 已验证章节保留，首页同步改为对该章节的具体介绍；带日期的旧审计记录仍作为历史快照保存。
- **首页统计**：不再展示原先的 “two book chapters” 和缺少完整台账支持的 “24 ... patent applications” 数字，改为介绍 B1 所属图书及中国、国际专利共同发明人身份，并链接至选列专利。没有将总数擅自改为 17，也没有把不同国家或阶段的同族记录算作独立发明。
- **专利清单口径**：说明当前清单为选列，且同一专利族的相关申请分别展示，因此多条记录可能对应同一发明。
- **IP5 姓名写法**：按[美国授权文献首页第 (72) 项](https://patentimages.storage.googleapis.com/8e/3c/9a/a4c2f46a81ebe3/US12028139.pdf)，将该条的 `R. Mackenzie` 改为 `R. MacKenzie`。发明人身份和顺序不变；不将美国文献的大小写形式强加到使用全大写姓名的其他法域原件。

## 保留项

- CN9 及其他专利的授权标签、状态、申请号、公开文献号、授权文献号、ZL 专利号、日期和链接保持不变。
- J9 保留 Early Access；J14 的两个 `Z. Zhang` 对应不同作者，保留当前顺序。
- CN7 的 A 文献链接继续准确标为 Application document。未添加未经核实的 B 原件链接。
- O1/O2 的演示条目和 C8/C9 的通讯作者符号未发现反证，保留；未新增未经证实的正式卷页、DOI 或作者角色。
- 早期设计预览和带日期的历史审计记录不作为当前内容源，本次不回写历史快照。

## 同步与验证

HTML 和 `.jemdoc` 内容同步修订；`data/publication-metadata.json`、`data/patent-status.json` 记录当前显示文字及来源。未运行旧版 jemdoc 生成器。

验证包括：确认 B2 不在当前清单中、B1 和其余论文完整保留，确认 CN9 及所有专利状态和编号未变、其他论文引文及 DOI 未变，检查站内链接与锚点、解析 JSON 和检查 Git 差异。本次按用户要求将本轮修订一并上传 GitHub，并核对部署及线上页面。
