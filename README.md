# pairwise-animation-layer-blend

## 领域

游戏、图形与多媒体

## 主题

动画分层混合

## 说明

权重归一、root motion 单层与同步组对齐。

初始状态下 `render/animation_layer_blend.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
