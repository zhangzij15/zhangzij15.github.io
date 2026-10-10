# 网站英文与成果信息核验记录

核验日期：2026-10-10。覆盖当前五个正式页面及其 `.jemdoc` 内容参考文件。历史设计预览保留原样。

## 英文修订

统一了简介、教育经历、学术服务、研究项目摘要、演示说明、奖项及导航的语法和术语。采用克制的学术表述，保留原有研究结果、个人经历和数值。正式发表的论文题名按出版社记录呈现；中文专利的英文题名为依据正式中文名称整理的译名。

## 论文、章节与其他成果

共检查40条：35条正式出版信息完整核实（1个书章节、20篇期刊论文、14篇会议论文），3条部分核实，2条尚未独立核实。为36条可确认DOI的成果增加链接；14篇会议论文补齐正式页码。Projects中的16篇精选期刊论文和Demos中的相关引文同步更新。

出版社存入Crossref的元数据用于核对卷号、期号、页码和DOI；必要时结合出版社页面、原论文及官方会议档案。原始条目、正式信息、变更、来源与未核字段见 [publication-metadata.json](../data/publication-metadata.json)。

主要更新：

- J21：*IEEE Communications Magazine*, vol. 64, no. 8, pp. 52–59, Aug. 2026，并补全9位作者。[IEEE出版商存档](https://api.crossref.org/works/10.1109%2FMCOM.001.2500610)
- J9：正式题名和DOI确认，仍无可核实的最终卷期，标为 *Early Access, 2026*；不把临时页码1–6当作最终页码。[IEEE出版商存档](https://api.crossref.org/works/10.1109%2FTVT.2026.3697200)
- C13：修正为VTC 2022-Spring、Helsinki、Jun. 2022，pp. 1–5。原Aug. 2022为数据库收录时间，并非会期。[IEEE正式记录](https://ieeexplore.ieee.org/document/9860745/)
- J2与J7为年度连续分页卷，按年度列出，未增加不存在的期号。
- C4的正式题名为“High-Efficient Ranging Algorithms for Wireless Sensor Network”，保留出版商原题名。[IEEE出版商存档](https://api.crossref.org/works/10.1109%2Fwcsp.2019.8928120)
- O1/O2作为会议演示列出，不填写未证实的论文DOI或正式页码；O1原PDF是幻灯片。
- O3作为RoboCup@Home 2019 Open Platform League的team description paper列出。[RoboCup官方档案](https://tdp.robocup.org/tdp/2019-tdp-tinker-robocuphome-open-platform/)
- B2“Optimization of Active Metasurfaces”未找到相同题名和作者组合的可靠出版社记录。用户要求保留，故原条目及2024信息不变；未借用相近书名中他人的章节信息。

## 专利

逐项检查17条，匹配申请号、公开/授权文献号、发明人和日期。10条有历史授权依据（美国1条、欧洲1条、中国8条），均标注 **Granted**、正确授权文献号及授权日期。另4条为PCT国际公开申请；CN1、CN8、CN10的公开文献可以确认，授权状态未独立证实，保留 **Published application**。没有根据搜索不到授权文献推断“未授权”。详细依据见 [patent-status.json](../data/patent-status.json)。

16条核对了正式专利文献首页（公报文献镜像）；CN7的证据为B号文献索引及2025-09-05的GR01授权事件，证据层级在JSON中注明。

主要修正：

- IP5：公开文献号为 **US20240039592A1**；授权文献号 **US12028139B2**，2024-07-02。[USPTO授权文献](https://patentimages.storage.googleapis.com/8e/3c/9a/a4c2f46a81ebe3/US12028139.pdf)
- IP6：**EP4295492A1**是公开文献号，授权文献号为 **EP4295492B1**，2024-10-09；申请号补为EP22704879.0。[EPO授权文献](https://patentimages.storage.googleapis.com/43/78/0a/41531d3c36fdf5/EP4295492B1.pdf)
- CN9：申请CN202310539494.X对应的授权文献为 **CN116260501B**，2023-07-14；删除原错误关联CN113452642B。后者属于不同申请、发明人及申请人。[CNIPA授权文献](https://patentimages.storage.googleapis.com/d9/f7/06/10182f8a06a3fb/CN116260501B.pdf)
- CN8：根据正式公开文献修正发明人名单，补充X. Yang、L. Song并移除原不匹配的J. Li。[CNIPA公开文献](https://patentimages.storage.googleapis.com/91/6a/2c/147cefa7d8d672/CN118174757A.pdf)
- CN11：补充R. Mackenzie、M. Hao；中文“透射”译为*transmissive*。[CNIPA授权文献](https://patentimages.storage.googleapis.com/2e/ed/fc/1c82dd25de032a/CN116868518B.pdf)
- PCT申请号统一为PCT/CN…或PCT/EP…格式；明确列出公开日期和授权日期，消除原来未说明含义的年月。

这里的Granted表示曾获授权，不表示当前法律效力。CN9的聚合记录另有2026-05-12年费终止事件（尚未经CNIPA登记簿独立核实），因此不宣称其当前有效；各项当前法律状态不在本次授权历史结论之内。EP正式文献标题中的“reconfigureable”拼写保留，其他文献按其正式标题或中文译名呈现。

## 保留待核对的个人信息

- 首页National Scholarship为2019、2024；Awards为2020、2024。原年份保留，需以个人获奖证明确认。
- 简介学位专业为electronic engineering，教育列表为Electrical Engineering。原有两个专业名称保留，需以学位证或正式履历确认。
- 引用数、专利申请总量、奖项与名单等简介数值沿用原材料，本次未将其当作经过实时统计的结论。

## 验证范围

保留57条成果与专利记录、21张期刊代表图、原论文/代码/证书/媒体链接、7个研究方向和每方向最多3篇精选期刊论文。核验本地链接与页内锚点、HTML结构、共享导航和侧栏、HTML与内容参考文件的元数据一致性，并检查桌面及手机布局。验证结果另存于 [site-verification-2026-10-10.json](../data/site-verification-2026-10-10.json)。
