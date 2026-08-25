# V2.7.0 历史平台提示词材料

本目录保存 V2.7.0 时代的即梦、Image2、nanobanana 与“三平台”提示词合同，仅用于审计、迁移和版本追溯。

## 状态
- `legacy: true`
- `deprecated: true`
- 不属于 V2.7.1 当前 T线运行依赖。
- 当前 Skill 不得自动读取、默认引用或输出本目录材料。

## 目录
- `templates/`：旧多平台输出模板。
- `references/`：旧平台规则。
- `examples/`：旧成功示例。
- `anti_examples/`：旧反例与保护规则。

## 当前替代方案
V2.7.1 使用 GPT Image 能力和请求模型 `gpt-image-2`，默认只输出一套中文执行提示词合同。当前入口位于 `stage-tline-prompt-translation/`，执行反馈入口位于 `stage-cline-gpt-image-execution-feedback/`。

不要直接修改本目录来改变当前行为；需要恢复历史规则时，应从原始 Git 标签创建独立分支，并重新经过范围、依赖、回滚和验证 Gate。
