# GPT Image 中文提示词规则

## 单一输出
T线默认且唯一的当前输出是用户明确选择方案的一套中文 GPT Image 合同。中文执行提示词应简洁、可直接用于图像生产，并忠实继承 B线的版式、视觉焦点、素材政策、文字政策、参考图继承关系和样张状态边界。若两案均可用，T线不得按评分、风险或推荐自动选择。

## Reference Inputs
For a reference-locked task, copy the selected real file paths exactly. C-line must attach them as image inputs. Never write only `参考原图`, never attach every image in the folder, and never use recent conversation images as an implicit substitute.

```yaml
reference_inputs:
  primary_layout_reference:
  secondary_references:
  reference_attachment_required: yes
  text_only_execution_forbidden: yes
```

## Verbatim Text
Copy all `must_show_text_verbatim` fields without paraphrase. GPT Image renders the text directly. Initial generation plus at most two local text revisions is allowed; deterministic text overlay is forbidden for this contract.

## 模型字段
- `目标能力`：写 `GPT Image`，表示稳定的业务能力名称。
- `请求模型`：写 `gpt-image-2`，表示期望的执行目标。
- `实际执行模型`：只依据执行回执填写；无回执时写 `未报告`。

## 负面约束
用中文列出 3—5 条与当前页面有关的硬禁项。不要堆砌泛化修饰词，也不要引入 B线没有授权的新约束。

## 输出设置
- 完整课程视觉页默认 `opaque`。
- `transparent` 仅用于明确需要 Alpha 的素材层、抠图对象或叠加组件，格式必须是 `png` 或 `webp`。
- 透明背景属于预览能力，执行合同应允许不透明降级。
- Exception: user-confirmed Remotion transparent foreground requires real Alpha and forbids opaque fallback.
- `auto` 只在背景不影响交付合同且无需预先锁定时使用。

## 中文局部修改模板
每次输出都包含 `保留项`、`仅修改项`、`禁止修改项` 和 `最小修改指令`。该模板用于阻止 C线局部修订改变冻结结构或扩张为整页重绘。

## 写入与完整性
正式合同写入前先提议产物、文件、是否修改旧文件、C线接收内容和非交付记录，再只问 `是否按上述产物与交接方案执行？`。一次授权只写一个合同并立即停止。交付前必须确认具体尺寸、完整母版描述、完整主视觉描述、无占位符或空句，且没有未经用户确认的视觉方向。

## 哈希禁令
不得计算、记录、传递或推荐哈希、摘要或指纹。输入含此要求时停止，只问是否改用包含参考编号、真实路径、文件名、尺寸、模板版本、参考角色和用户确认结果的非哈希清单。

## 历史边界
旧的多平台提示词规则已迁移到 `legacy/platform-prompts-v2.7.0/`，只用于审计和迁移追溯，不得被当前 T线自动读取或默认输出。
