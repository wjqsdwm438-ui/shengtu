# V2.7.1 迁移说明

## 1. 迁移范围

本次只收口项目源码目录内的开发基线，范围包括：

1. 建立可回滚的本地 Git 基线；
2. 消除固定旧绝对路径；
3. 将 T线统一为 GPT Image 中文专用合同；
4. 将测试日志统一为 UTF-8 无 BOM、LF；
5. 统一六个 `agents/openai.yaml` 的最小 schema；
6. 增加统一离线检查入口 `run_all_checks.py`。

ALG-B01、ALG-C01 的进一步脚本化、真实 API 接入和真实项目端到端生产闭环不属于本次范围。

## 2. 项目根与外层快照边界

真正项目根是本文件所在目录。外层目录中的交接材料和 `SNAPSHOT_MANIFEST` 是 2026-08-14 快照的不可变来源证据，本次不改写。

原始 Git 提交实际纳入 89 个项目源码文件；外层 `SNAPSHOT_MANIFEST` 声明 `source_file_count=86`。差额是项目根的以下三个流程资产未列入 `manifest.files`，V2.7.1 Git 基线将其全部纳入：

- `课程视觉生产工具V2.7_项目节点与流程.drawio`
- `课程视觉生产工具V2.7_项目节点与流程-项目节点总览2.drawio.svg`
- `课程视觉生产工具V2.7_项目节点与流程-完整业务流程.drawio.svg`

该差异只说明两种边界的覆盖范围不同，不应通过修改外层 Manifest 消除。

## 3. GPT Image 合同迁移

### 当前合同

- 能力名称：GPT Image
- 当前请求模型：`gpt-image-2`
- T线输出：单套中文执行提示词
- 实际执行模型：仅依据工具或 API 回执填写；无回执时记录“未报告”
- 完整课程视觉页：默认不透明
- 素材层、抠图、可叠加组件：按需请求透明背景，格式为 PNG 或 WebP，Alpha/透明背景能力标记为 preview

### 历史合同

即梦、nanobanana 及旧三平台提示材料迁移到：

```text
legacy/platform-prompts-v2.7.0/
```

该目录是只读历史证据：当前 Skill 不自动读取，不作为默认示例，也不属于运行依赖。当前检查器只验证其文件存在、UTF-8 编码和迁移说明完整，不把历史正文中的旧术语当作当前合同。

## 4. C线入口迁移

| 旧入口 | 新入口 |
| --- | --- |
| `stage-cline-image2-execution-feedback/` | `stage-cline-gpt-image-execution-feedback/` |

不保留旧名转发 Skill。调用方、内部链接与元数据应直接改用新入口；需要查看旧结构时使用原始快照标签。

## 5. 路径与元数据迁移

- 文档路径以项目根为参照。
- Python 脚本从自身位置推导项目根，不使用固定盘符。
- YAML 默认提示中不写绝对磁盘路径。
- 六个 `agents/openai.yaml` 统一为：

```yaml
interface:
  display_name: "..."
  short_description: "..."
  default_prompt: "..."
policy:
  allow_implicit_invocation: false
```

该结构只是 Skill 的界面登记与调用策略，不改变各阶段业务权限，也不会开启隐式调用。

## 6. 验证与证据更新

日常验证：

```powershell
python run_all_checks.py
```

默认使用系统临时目录，不应改脏 Git 工作区。只有维护者明确决定刷新受管证据时才运行：

```powershell
python run_all_checks.py --update-evidence
```

检查过程不安装依赖、不修改全局配置、不注册全局 Skill，也不调用付费 API。

## 7. 回滚路径

- 回到原始开发快照：从 `v2.7.0-dev-snapshot-20260814` 创建检查分支。
- 回到收口后的稳定基线：从 `v2.7.1-baseline` 创建检查分支。

回滚前应先提交或另存当前未提交工作。不要删除或改写外层交接材料、原始 Manifest、历史目录或 Git 标签。
