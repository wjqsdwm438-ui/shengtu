# T线 GPT Image 中文提示词合同

```yaml
状态: T线GPT Image中文提示词已就绪
模式: GPT Image 中文单提示词
候选方案ID: 方案A_稳妥版 / 方案B_探索版 / 方案A_参考锁定版
用户选择记录:
GPT_Image中文合同:
  目标能力: GPT Image
  请求模型: gpt-image-2
  实际执行模型: 未报告
  执行类型: standard / reference_locked_full_page / remotion_transparent_foreground
  reference_inputs:
    reference_set_id:
    primary_layout_reference:
    secondary_references:
    reference_selection_confirmed: yes/no
    reference_attachment_required: yes/no
    text_only_execution_forbidden: yes/no
  template_identity:
    template_id:
    template_version:
  非哈希参考清单:
    - 参考编号:
      真实路径:
      文件名:
      尺寸:
      模板版本:
      参考角色:
      用户确认结果:
  context_isolation:
    explicit_reference_paths_only: yes/no
    include_previous_conversation_images: no
    include_failed_images_automatically: no
    include_entire_reference_folder: no
  must_show_text_verbatim:
    title:
    subtitle:
    lead:
    section_titles:
    body:
    labels:
    numbers:
    english_terms:
    punctuation:
  text_accuracy:
    must_be_verbatim: yes/no
    deterministic_text_overlay_forbidden: yes/no
    maximum_local_text_revisions: 2
  母版描述:
  主视觉描述:
  中文执行提示词:
  中文负面约束:
  输出设置:
    尺寸:
    质量:
    背景: opaque（不透明） / transparent（透明，仅素材或叠加组件） / auto（自动，不用于绕过完整页不透明默认）
    格式: png / webp
    opaque_fallback: allowed / forbidden
  中文局部修改模板:
    保留项:
    仅修改项:
    禁止修改项:
    最小修改指令:
备用候选方案: 仅保留在B线，不转译
remotion_asset_handoff:
  gate_status: not_applicable / pending / confirmed
  derived_from_final_visual_id:
  canvas_size:
  coordinate_origin: top_left
  crop_to_content: forbidden
```

## 交付前最小检查
- `输出设置.尺寸` 必须是完整的具体值。
- `母版描述` 与 `主视觉描述` 必须明确、完整，并与 `中文执行提示词` 一致。
- 不得残留占位符、空句、截断句或未经用户确认的视觉方向。
- 任一项不通过时停止，不得交给 C线补全。

## 背景规则
- 完整课程视觉页：默认 `背景: opaque`。
- 素材层、抠图对象或可叠加组件：有明确 Alpha 需求时可用 `背景: transparent`，并选 `png` 或 `webp`。
- 透明背景目前是预览能力；合同必须保留降级为不透明背景的可能。
- 例外：经用户确认的Remotion透明前景必须输出带真实Alpha的PNG，禁止降级为不透明图。
