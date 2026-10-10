# 专利编号与论文信息二次核验

核验日期：2026-10-11。针对现行网站的17条专利、40条论文/章节/其他成果重新取源核对。上一轮审计中的旧网站快照不作为当前网页内容。

## 本轮结论与修订

- 现行专利申请号、公开文献号、已列授权文献号与新取得的来源相符；未发现新的号码、日期或发明人错误。
- 36个已列DOI的题名、作者顺序、DOI、期刊/会议、卷期页码与重新请求的Crossref出版商存档一致；35篇期刊/会议论文所链接PDF的题名均对应正确。部分本地PDF为作者版本，不能用其中的临时页码代替最终出版页码。
- 修订编号字段名称：Application no.（申请号）、Application publication（公开文献号）、Grant publication（授权公告/文献号）。为8项有历史授权依据的中国专利补列独立的Patent no.（ZL专利号），保留校验位。
- 将IP6文献链接换为EPO官方Publication Server；CN7增加明确标为Application document的A文献原件链接。
- 将专利审计JSON的current_text改名为original_website_text，明确它只是旧内容快照；grant_number改为grant_publication_number，避免术语混用。

国内专利号与授权公告号不是同一种编号：已授权专利号为ZL加申请号，CN…B为授权公告号。此项新增ZL号码依据已匹配的申请号、历史授权证据和官方编号规则整理，并非证书号。[国家知识产权局说明](https://www.cnipa.gov.cn/jact/front/mailpubdetail.do?sysid=12&transactId=520307)

## 逐项专利号码

| 项目 | 申请号 | 公开文献号 | ZL专利号（中国） | 授权文献号 |
|---|---|---|---|---|
| IP1 | PCT/CN2022/102301 | WO2023071264A1 | — | PCT公开不代表授权 |
| IP2 | PCT/CN2021/077059 | WO2022174418A1 | — | PCT公开不代表授权 |
| IP3 | PCT/CN2021/112812 | WO2022262104A1 | — | PCT公开不代表授权 |
| IP4 | PCT/EP2022/051724 | WO2022175035A1 | — | PCT公开不代表授权 |
| IP5 | US18/277,668 | US20240039592A1 | — | US12028139B2 |
| IP6 | EP22704879.0 | EP4295492A1 | — | EP4295492B1 |
| CN1 | CN202110673957.2 | CN113473499A | — | 未独立确认 |
| CN2 | CN202111271506.2 | CN114040478A | ZL202111271506.2 | CN114040478B |
| CN3 | CN202110138213.0 | CN112887906A | ZL202110138213.0 | CN112887906B |
| CN4 | CN201810258348.9 | CN108469600A | ZL201810258348.9 | CN108469600B |
| CN5 | CN202010052977.3 | CN111262755A | ZL202010052977.3 | CN111262755B |
| CN6 | CN201810433350.5 | CN108664024A | ZL201810433350.5 | CN108664024B |
| CN7 | CN202210112147.4 | CN116566446A | ZL202210112147.4 | CN116566446B |
| CN8 | CN202211578453.3 | CN118174757A | — | 未独立确认 |
| CN9 | CN202310539494.X | CN116260501A | ZL202310539494.X | CN116260501B |
| CN10 | CN202410254042.1 | CN118368017A | — | 未独立确认 |
| CN11 | CN202280015597.X | CN116868518A | ZL202280015597.X | CN116868518B |

## 来源和核验边界

国际/美国/欧洲6项重新下载正式文献首页并视觉核对；其中IP6直接来自EPO官方服务器，其余为WIPO/USPTO正式文献镜像。中国11项重新取得CNIPA文献首页：7份B文献、4份A文献。共17份新取文献首页，但其中CN7仅取得A首页；该项B号与2025-09-05授权公告日期仍依赖新取B文献索引及GR01事件，不能声称已读到其B首页。

- CN1、CN8、CN10：公开申请确认，未独立确认授权文献。继续显示Published application，不断言未授权。
- J9：DOI和题名确认；Crossref尚无最终volume/issue，1–6为临时页码，继续显示Early Access。[DOI](https://doi.org/10.1109/TVT.2026.3697200)
- J14：正式作者分别包含Zijian Zhang与Zexu Zhang，两个Z. Zhang缩写对应不同作者，当前顺序正确，保留。[IEEE ComSoc官方目录（PDF第25页）](https://www.comsoc.org/system/files/2022-08/Publications_Contents_Digest_2022_Aug.pdf)
- J21：IEEE ComSoc官方2026年8月目录确认完整9位作者及pp. 52–59，与Crossref的vol. 64, no. 8, Aug. 2026一致。[IEEE ComSoc官方目录（PDF第3页）](https://www.comsoc.org/system/files/2026-09/publications_contents_digest_2026-aug.pdf)
- C13：正式记录为VTC 2022-Spring；官方会期为2022-06-19至2022-06-22，Helsinki，当前Jun. 2022正确。[IEEE VTS官方会议](https://events.vtsociety.org/vtc2022-spring/)
- B2：按用户此前要求保留，准确出版记录仍未确认；不借用相近书名中他人章节的DOI、作者或页码。
- O1/O2：会议演示，不推定为有页码的正式会议论文。O3保留为RoboCup官方存档的team description paper。[RoboCup官方档案](https://tdp.robocup.org/tdp/2019-tdp-tinker-robocuphome-open-platform/)
- Granted表示有历史授权记录；本轮不判定各国或地区的当前法律效力，也不补写未经证书核实的证书号。

逐项来源、日期、匹配结果和证据限制见[机器可读核验记录](../data/metadata-recheck-2026-10-11.json)。现行数据见[专利记录](../data/patent-status.json)及[论文记录](../data/publication-metadata.json)。

## 中文专利名称补充

根据用户要求，在英文题名下新增16条中文名称：11项中国专利及IP1/IP3使用正式原文中文题名；IP4/IP5/IP6使用CN11同一PCT国家阶段的正式中文名称，并显示“中文名称（中国同族）”以说明来源。IP2的原始WO文献为英文，未核实其正式中文名称，保留英文，不以自行翻译代替正式题名。所有英文题名、申请/公开/授权编号、作者、日期与超链接均保留。中文名称与来源另记录在patent-status.json的chinese_title及chinese_title_source字段。
