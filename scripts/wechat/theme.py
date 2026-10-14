# -*- coding: utf-8 -*-
"""
微信公众号文章排版主题

配色与可读性说明：
- 正文统一使用深灰（#3f3f3f / #262626）而非纯黑，避免手机屏刺眼；
- 标题与强调色保证对比度：正文级 >=4.5:1，大号标题级 >=3:1（WCAG 2.1 AA）；
- 亮色（嫩绿、明黄、亮绿）只用于「底纹块 / 左边框 / 分隔」等装饰，
  文字一律使用同色系加深后的颜色，确保清晰可读。
- 每个主题的 h1 / h2 / h3 形态各不相同，避免千篇一律的长方形。
"""

THEMES = {
    # ========== 橙心 ==========
    "橙心": {
        "title": 'font-size: 24px; font-weight: bold; color: #D9640A; text-align: left; margin: 20px 0; padding: 10px 16px 10px 14px; border-left: 8px solid #FF7F00; background: #FFF4EA; border-radius: 0 12px 12px 0; letter-spacing: 1px;',
        "title_color": "#D9640A",
        "separator": 'color: #F0A868; font-size: 14px; text-align: left; margin-bottom: 20px; padding-left: 14px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.8; color: #3f3f3f; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #C85A00; margin: 22px 0 12px 0; padding-bottom: 6px; border-bottom: 3px solid #FF7F00;',
        "h3": 'font-size: 17px; font-weight: bold; color: #C85A00; margin: 16px 0 8px 0; padding-bottom: 4px; border-bottom: 2px solid #FF7F00;',
        "quote": 'border-left: 4px solid #FF9F45; background: #FFF8F0; padding: 10px 15px; margin: 12px 0; color: #6b5a45; border-radius: 0 6px 6px 0;',
        "code": 'background: #FFF8F0; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #B45309; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 墨黑 ==========
    "墨黑": {
        "title": 'font-size: 24px; font-weight: bold; color: #ffffff; text-align: center; margin: 20px 0; padding: 16px 20px 14px; background: #1a1a1a; border-radius: 50px 50px 0 0; letter-spacing: 2px;',
        "title_color": "#1a1a1a",
        "separator": 'color: #999; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.9; color: #262626; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #1a1a1a; margin: 24px 0 12px 0; padding-bottom: 6px; border-bottom: 4px double #1a1a1a;',
        "h3": 'font-size: 17px; font-weight: bold; color: #1a1a1a; margin: 16px 0 8px 0; padding-left: 8px; border-left: 2px solid #999;',
        "quote": 'border-left: 4px solid #1a1a1a; background: #f5f5f5; padding: 10px 15px; margin: 12px 0; color: #595959; border-radius: 0 6px 6px 0;',
        "code": 'background: #f5f5f5; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #1a1a1a; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 姹紫 ==========
    "姹紫": {
        "title": 'font-size: 24px; font-weight: bold; color: #8A2BE2; text-align: center; margin: 20px 0; padding: 12px 20px; background: #F6F0FF; border-radius: 0 25px 0 25px; letter-spacing: 1px;',
        "title_color": "#8A2BE2",
        "separator": 'color: #C4A3E8; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.8; color: #3f3f3f; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #7B2FBE; margin: 22px 0 12px 0; padding: 8px 14px; background: #F6F0FF; border-radius: 0 20px 0 20px;',
        "h3": 'font-size: 17px; font-weight: bold; color: #7B2FBE; margin: 16px 0 8px 0; padding-left: 10px; border-left: 3px solid #8A2BE2; border-bottom: 1px solid #C4A3E8;',
        "quote": 'border-left: 4px solid #B98BE8; background: #F8F4FF; padding: 10px 15px; margin: 12px 0; color: #5f5470; border-radius: 0 6px 6px 0;',
        "code": 'background: #F8F4FF; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #7B2FBE; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 嫩青（小清新 / 文艺）==========
    "嫩青": {
        "title": 'font-size: 23px; font-weight: bold; color: #3C7A4A; text-align: center; margin: 20px 0; letter-spacing: 2px; padding-bottom: 12px; border-bottom: 3px solid #A5D6A7;',
        "title_color": "#3C7A4A",
        "separator": 'color: #A5D6A7; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 6px;',
        "content": 'font-size: 16px; line-height: 1.9; color: #3f3f3f; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #2E6B3E; margin: 22px 0 12px 0; padding: 8px 14px; background: #E8F5E9; border-radius: 10px;',
        "h3": 'font-size: 17px; font-weight: bold; color: #2E6B3E; margin: 16px 0 8px 0; padding: 4px 10px; background: #E8F5E9; border-radius: 6px;',
        "quote": 'border-left: 4px solid #A5D6A7; background: #F1F8F2; padding: 10px 15px; margin: 12px 0; color: #5a6b5e; border-radius: 0 12px 12px 0;',
        "code": 'background: #F1F8F2; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #2E6B3E; border-radius: 8px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 绿意（森系 / 沉稳）==========
    "绿意": {
        "title": 'font-size: 22px; font-weight: bold; color: #1B5E20; text-align: center; margin: 20px 0; padding: 8px 0 10px 16px; border-left: 10px solid #2E6B3E; border-bottom: 2px solid #A5D6A7; letter-spacing: 2px;',
        "title_color": "#1B5E20",
        "separator": 'color: #4E8C5A; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.85; color: #333f34; padding: 0 10px;',
        "h2": 'font-size: 18px; font-weight: bold; color: #ffffff; margin: 22px 0 12px 0; padding: 8px 14px; background: #2E6B3E; border-radius: 3px; letter-spacing: 1px;',
        "h3": 'font-size: 17px; font-weight: bold; color: #2E6B3E; margin: 16px 0 8px 0; padding-left: 10px; border-left: 4px solid #2E6B3E;',
        "quote": 'border-left: 4px solid #2E6B3E; background: #EEF6EE; padding: 10px 15px; margin: 12px 0; color: #4a5a4d; border-radius: 0 3px 3px 0;',
        "code": 'background: #1B3B24; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #A5D6A7; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 红绯 ==========
    "红绯": {
        "title": 'font-size: 24px; font-weight: bold; color: #ffffff; text-align: center; margin: 20px 0; padding: 12px 20px 20px; background: #D9433E; border-radius: 0 0 40px 40px; letter-spacing: 1px;',
        "title_color": "#D9433E",
        "separator": 'color: #F0A9A6; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.8; color: #3f3f3f; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #C0392B; margin: 22px 0 12px 0; padding: 8px 14px; background: #FFF0F0; border-radius: 0 0 20px 0;',
        "h3": 'font-size: 17px; font-weight: bold; color: #C0392B; margin: 16px 0 8px 0; padding-bottom: 3px; border-bottom: 1px dashed #E74C3C;',
        "quote": 'border-left: 4px solid #F08080; background: #FFF0F0; padding: 10px 15px; margin: 12px 0; color: #6b4a4a; border-radius: 0 6px 6px 0;',
        "code": 'background: #FFF0F0; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #B03030; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== WeChat-Format（技术文档风）==========
    "WeChat-Format": {
        "title": 'font-size: 21px; font-weight: bold; color: #1677d1; text-align: left; margin: 20px 0; padding: 5px 0 5px 12px; border-left: 4px solid #1890ff; letter-spacing: 0.5px;',
        "title_color": "#1677d1",
        "separator": 'color: #8c8c8c; font-size: 12px; text-align: left; margin-bottom: 20px; padding-left: 12px;',
        "content": 'font-size: 16px; line-height: 1.7; color: #262626; padding: 0 15px;',
        "h2": 'font-size: 18px; font-weight: bold; color: #262626; margin: 24px 0 12px 0; border-left: 3px solid #1890ff; padding: 5px 0 5px 10px;',
        "h3": 'font-size: 16px; font-weight: bold; color: #262626; margin: 16px 0 8px 0; padding-left: 8px; border-left: 2px solid #1890ff;',
        "quote": 'border-left: 4px solid #1890ff; background: #f7f7f7; padding: 12px 16px; margin: 12px 0; color: #595959; border-radius: 0 4px 4px 0;',
        "code": 'background: #f7f7f7; padding: 12px 16px; font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; color: #C7254E; border-radius: 4px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 科技蓝 ==========
    "科技蓝": {
        "title": 'font-size: 23px; font-weight: bold; color: #0A78B5; text-align: center; margin: 20px 0; padding: 12px 0; border-top: 3px solid #00A0E9; border-bottom: 3px solid #00A0E9; letter-spacing: 2px;',
        "title_color": "#0A78B5",
        "separator": 'color: #7FBEE0; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.8; color: #3f4a52; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #0A78B5; margin: 22px 0 12px 0; padding: 6px 0; border-top: 2px solid #00A0E9; border-bottom: 2px solid #00A0E9; text-align: center;',
        "h3": 'font-size: 17px; font-weight: bold; color: #0A78B5; margin: 16px 0 8px 0; padding: 4px 10px; background: #E6F7FF; border-radius: 0 4px 4px 0;',
        "quote": 'border-left: 4px solid #00A0E9; background: #E6F7FF; padding: 10px 15px; margin: 12px 0; color: #4a5a66; border-radius: 0 6px 6px 0;',
        "code": 'background: #0B2239; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #7FD6FF; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 兰青（莫兰迪 / 雅致青绿）==========
    "兰青": {
        "title": 'font-size: 22px; font-weight: 600; color: #2F6B5F; text-align: left; margin: 20px 0; padding: 6px 0 6px 14px; border-left: 6px solid #4A8B7C; letter-spacing: 1px;',
        "title_color": "#2F6B5F",
        "separator": 'color: #8FBAB0; font-size: 14px; text-align: left; margin-bottom: 20px; padding-left: 14px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.9; color: #3f4a48; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: 600; color: #2F6B5F; margin: 24px 0 12px 0; padding: 7px 14px; border-left: 6px solid #4A8B7C; letter-spacing: 1px;',
        "h3": 'font-size: 17px; font-weight: 600; color: #2F6B5F; margin: 16px 0 8px 0; padding-left: 10px; border-left: 3px solid #4A8B7C; font-style: italic;',
        "quote": 'border-left: 3px solid #4A8B7C; background: #EDF4F2; padding: 10px 15px; margin: 12px 0; color: #52605d; font-style: italic;',
        "code": 'background: #EDF4F2; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #2F6B5F; border-radius: 4px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 山吹（暖金 / 明亮）==========
    "山吹": {
        "title": 'font-size: 24px; font-weight: bold; color: #ffffff; text-align: left; margin: 20px 0; padding: 10px 20px 10px 16px; background: #A67C00; border-radius: 50px 0 0 50px; letter-spacing: 1px;',
        "title_color": "#A67C00",
        "separator": 'color: #8B6914; font-size: 14px; text-align: left; margin-bottom: 20px; padding-left: 16px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.85; color: #4a4230; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #7A5C00; margin: 22px 0 12px 0; padding-bottom: 6px; border-bottom: 4px dotted #E8B800;',
        "h3": 'font-size: 17px; font-weight: bold; color: #7A5C00; margin: 16px 0 8px 0; padding-bottom: 4px; border-bottom: 3px dotted #E8B800;',
        "quote": 'border-left: 4px solid #E8B800; background: #FFFBEA; padding: 10px 15px; margin: 12px 0; color: #6B5A2E; border-radius: 0 6px 6px 0;',
        "code": 'background: #3A2E00; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #FFD666; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 前端之巅 ==========
    "前端之巅": {
        "title": 'font-size: 22px; font-weight: bold; color: #ffffff; text-align: left; margin: 20px 0; padding: 10px 16px 10px 20px; background: #ff4757; border-radius: 0 50px 50px 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;',
        "title_color": "#ff4757",
        "separator": 'color: #a4b0be; font-size: 12px; text-align: center; margin-bottom: 20px; letter-spacing: 2px;',
        "content": 'font-size: 15px; line-height: 1.7; color: #2f3542; padding: 0 12px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;',
        "h2": 'font-size: 18px; font-weight: 600; color: #2f3542; margin: 24px 0 12px 0; padding: 5px 0 8px 10px; border-left: 3px solid #ff4757; border-bottom: 1px solid #dfe4ea;',
        "h3": 'font-size: 16px; font-weight: 600; color: #2f3542; margin: 16px 0 8px 0; padding-left: 8px; border-left: 2px solid #ff4757;',
        "quote": 'border-left: 3px solid #ff4757; background: #fff1f2; padding: 12px 16px; margin: 12px 0; color: #57606f; border-radius: 0 4px 4px 0; font-size: 14px;',
        "code": 'background: #2f3542; padding: 14px 16px; font-family: "SF Mono", Monaco, Consolas, monospace; color: #ffa502; border-radius: 6px; font-size: 13px; line-height: 1.5;',
    },

    # ========== 极客黑 ==========
    "极客黑": {
        "title": 'font-size: 24px; font-weight: bold; color: #ffffff; text-align: center; margin: 20px 0; padding: 10px 30px; background: #5A67D8; border-radius: 50px; letter-spacing: 1px;',
        "title_color": "#5A67D8",
        "separator": 'color: #667eea; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.9; color: #e0e0e0; padding: 15px; background: #1a1a2e; border-radius: 8px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #5A67D8; margin: 22px 0 10px 0; padding: 6px 0 6px 12px; border-left: 4px solid #667eea;',
        "h3": 'font-size: 17px; font-weight: bold; color: #5A67D8; margin: 16px 0 8px 0; padding: 4px 0 4px 10px; border-left: 3px solid #667eea;',
        "quote": 'border-left: 4px solid #667eea; background: #16213e; padding: 10px 15px; margin: 10px 0; color: #b8b8c0; border-radius: 0 6px 6px 0;',
        "code": 'background: #0f0f23; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #00d2ff; border: 1px solid #667eea; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 蔷薇紫 ==========
    "蔷薇紫": {
        "title": 'font-size: 24px; font-weight: bold; color: #C71585; text-align: center; margin: 20px 0; padding-bottom: 10px; border-bottom: 6px double #C71585; letter-spacing: 1px;',
        "title_color": "#C71585",
        "separator": 'color: #E58FBD; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 4px;',
        "content": 'font-size: 16px; line-height: 1.8; color: #3f3f3f; padding: 0 10px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #B0146F; margin: 22px 0 12px 0; padding: 8px 14px; background: #FFF0F5; border-radius: 0 0 0 20px;',
        "h3": 'font-size: 17px; font-weight: bold; color: #B0146F; margin: 16px 0 8px 0; padding: 4px 10px; background: #FFF0F5; border-radius: 0 0 0 8px;',
        "quote": 'border-left: 4px solid #E754B0; background: #FFF0F5; padding: 10px 15px; margin: 12px 0; color: #6b4a5a; border-radius: 0 6px 6px 0;',
        "code": 'background: #FFF0F5; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #B0146F; border-radius: 6px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 萌绿（活力 / 青春）==========
    "萌绿": {
        "title": 'font-size: 22px; font-weight: bold; color: #ffffff; text-align: center; margin: 20px 0; padding: 14px 28px; background: #2E8B3E; border-radius: 4px 40px 4px 40px; letter-spacing: 2px;',
        "title_color": "#2E8B3E",
        "separator": 'color: #52A85E; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 6px;',
        "content": 'font-size: 16px; line-height: 1.85; color: #3f3f3f; padding: 0 10px;',
        "h2": 'font-size: 18px; font-weight: bold; color: #2E8B3E; margin: 22px 0 12px 0; padding: 6px 14px; background: #F1FFF2; border-left: 6px solid #32CD32; border-radius: 0 18px 18px 0;',
        "h3": 'font-size: 17px; font-weight: bold; color: #2E8B3E; margin: 16px 0 8px 0; padding: 4px 10px; background: #F1FFF2; border-radius: 0 10px 0 0;',
        "quote": 'border-left: 4px solid #32CD32; background: #F2FFF2; padding: 10px 15px; margin: 12px 0; color: #4a5a4d; border-radius: 0 16px 16px 0;',
        "code": 'background: #F2FFF2; padding: 10px 12px; font-family: Consolas, Monaco, monospace; color: #2E8B3E; border-radius: 10px; font-size: 13px; line-height: 1.6;',
    },

    # ========== 全栈蓝 ==========
    "全栈蓝": {
        "title": 'font-size: 22px; font-weight: 600; color: #007AFF; text-align: center; margin: 20px 0; padding: 10px 20px 12px; border-bottom: 3px solid #007AFF; border-left: 3px solid #007AFF; border-right: 3px solid #007AFF; border-radius: 0 0 14px 14px; letter-spacing: 0.5px;',
        "title_color": "#007AFF",
        "separator": 'color: #8e8e93; font-size: 13px; text-align: center; margin-bottom: 20px;',
        "content": 'font-size: 16px; line-height: 1.75; color: #1c1c1e; padding: 0 12px; font-family: -apple-system, BlinkMacSystemFont, sans-serif;',
        "h2": 'font-size: 19px; font-weight: 600; color: #007AFF; margin: 24px 0 12px 0; padding: 8px 14px; background: #F2F7FF; border-radius: 0 12px 0 0;',
        "h3": 'font-size: 17px; font-weight: 600; color: #007AFF; margin: 16px 0 8px 0; padding: 4px 10px; background: #F2F7FF; border-radius: 8px 0 0 0;',
        "quote": 'border-left: 3px solid #007AFF; background: #F2F7FF; padding: 12px 16px; margin: 12px 0; color: #636366; border-radius: 0 6px 6px 0;',
        "code": 'background: #1c1c1e; padding: 12px 16px; font-family: SF Mono, Menlo, Monaco, monospace; color: #64D2FF; border-radius: 8px; font-size: 14px; line-height: 1.6;',
    },

    # ========== 赛博蓝（科技 AI 感）==========
    "赛博蓝": {
        "title": 'font-size: 24px; font-weight: bold; color: #22D3EE; text-align: center; margin: 20px 0; padding: 14px 16px; background: #0F172A; border-top: 2px solid #22D3EE; border-bottom: 1px solid #1E40AF; border-left: 1px solid #1E40AF; border-right: 1px solid #1E40AF; letter-spacing: 3px;',
        "title_color": "#22D3EE",
        "separator": 'color: #22D3EE; font-size: 14px; text-align: center; margin-bottom: 20px; letter-spacing: 8px;',
        "content": 'font-size: 16px; line-height: 1.9; color: #CBD5E1; padding: 15px 16px; background: #0F172A; border-radius: 8px;',
        "h2": 'font-size: 19px; font-weight: bold; color: #22D3EE; margin: 22px 0 12px 0; padding: 8px 12px 8px 14px; background: #1a1f3a; border-left: 4px solid #22D3EE; border-bottom: 1px solid #22D3EE; border-radius: 0 6px 0 0; letter-spacing: 1px;',
        "h3": 'font-size: 17px; font-weight: bold; color: #67E8F9; margin: 16px 0 8px 0; padding: 5px 14px 5px 12px; background: #1a1f3a; border-left: 3px solid #22D3EE; border-right: 1px solid #1E40AF; border-radius: 0 12px 12px 0; letter-spacing: 0.5px;',
        "quote": 'border-left: 4px solid #8B5CF6; background: #141B34; padding: 10px 15px; margin: 12px 0; color: #C4B5FD; border-radius: 0 8px 8px 0;',
        "code": 'background: #1a1f3a; padding: 12px 14px; font-family: Consolas, Monaco, monospace; color: #E2E8F0; border-left: 4px solid #22D3EE; border-radius: 0 6px 6px 0; font-size: 14px; line-height: 1.7;',
    },
}

# 默认主题（"简"主题已移除，回退到素雅中性的"墨黑"）
DEFAULT_THEME = "墨黑"


def _md_inline(text: str) -> str:
    """处理行内 Markdown：**加粗** -> <strong>。

    代码块已在前面提取为占位符，不会被这里的替换影响。
    加粗只使用 <strong> 保持继承色，避免引入低对比度颜色。
    """
    import re as _re
    return _re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)


def format_with_theme(title: str, content: str, theme_name: str = None, image_urls: list = None) -> str:
    """
    根据主题格式化文章内容

    参数:
        - title: 文章标题
        - content: 文章正文（Markdown格式）
        - theme_name: 主题名称（默认使用 DEFAULT_THEME）
        - image_urls: 文章内图片URL列表

    返回:
        - HTML格式的文章内容
    """
    theme = THEMES.get(theme_name, THEMES[DEFAULT_THEME])

    # 处理内容，先提取代码块并替换为占位符
    import re

    # 提取代码块
    code_blocks = []
    def replace_code_block(match):
        # group(2) 是代码内容，group(1) 是语言标识符
        code = match.group(2) if match.lastindex == 2 else match.group(1)
        # 清理代码：去除多余空行但保留缩进
        lines = code.split('\n')
        # 去除开头和结尾的纯空行
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        code = '\n'.join(lines)
        code_blocks.append(code)
        idx = len(code_blocks) - 1
        return f"__CODE_BLOCK_{idx}__"

    # 处理代码块（```...```）
    content = re.sub(r'```(\w*)\n(.*?)```', replace_code_block, content, flags=re.DOTALL)
    content = re.sub(r'```(.*?)```', replace_code_block, content, flags=re.DOTALL)

    # 处理段落
    paragraphs = content.split("\n\n")
    content_html = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # 检测并恢复代码块
        if "__CODE_BLOCK_" in para:
            # 提取代码块内容
            import re
            match = re.search(r'__CODE_BLOCK_(\d+)__', para)
            if match:
                code_idx = int(match.group(1))
                code = code_blocks[code_idx]
                # 清理代码内容：去除首尾空白，但保留内部换行
                code = code.strip()
                # 转义 HTML 特殊字符
                code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                # 用 <br> 替换换行，套用当前主题的代码块样式（含深色主题）
                code_with_br = code.replace("\n", "<br>")
                content_html += f'<p style="{theme["code"]} white-space: pre-wrap; word-break: break-all; margin: 10px 0;">{code_with_br}</p>\n'
        # 三级标题（### ）需在二级标题之前判断
        elif para.startswith("### "):
            h3_style = theme.get("h3", "")
            content_html += f'<h3 style="{h3_style}">{_md_inline(para[4:])}</h3>\n'
        # 检测标题
        elif para.startswith("## "):
            h2_text = para[3:]
            content_html += f'<h2 style="{theme["h2"]}">{_md_inline(h2_text)}</h2>\n'
        elif para.startswith("# "):
            # 大标题忽略，用传入的title
            continue
        # 分隔线（--- / *** / ___）
        elif para in ("---", "***", "___"):
            content_html += '<p style="text-align: center; margin: 20px 0; color: #c8c8c8; letter-spacing: 8px; font-size: 13px;">· · ·</p>\n'
        # 文章内图片：![alt](url)
        elif re.match(r'^!\[(.*?)\]\((.*?)\)$', para):
            m_img = re.match(r'^!\[(.*?)\]\((.*?)\)$', para)
            content_html += f'<p style="text-align: center; margin: 15px 0;"><img src="{m_img.group(2)}" alt="{m_img.group(1)}" style="max-width: 100%; height: auto; display: block; margin: 0 auto; border-radius: 6px;"/></p>\n'
        # 多行引用（> 开头，逐行去前缀）
        elif para.startswith("> ") and not para.startswith(">]"):
            q_lines = []
            for ln in para.split("\n"):
                if ln.startswith("> "):
                    ln = ln[2:]
                elif ln.startswith(">"):
                    ln = ln[1:]
                ln = ln.strip()
                if ln:
                    q_lines.append(_md_inline(ln))
            quote_text = "<br>".join(q_lines)
            content_html += f'<blockquote style="{theme["quote"]}"><p>{quote_text}</p></blockquote>\n'
        # 有序列表（1. 2. ...）
        elif re.match(r'^\d+\.\s', para):
            content_html += f'<div style="{theme["content"]}"><ol style="margin: 10px 0; padding-left: 22px;">\n'
            for line in para.split("\n"):
                m_li = re.match(r'^\d+\.\s(.*)$', line.strip())
                if m_li:
                    content_html += f'<li style="margin: 6px 0;">{_md_inline(m_li.group(1))}</li>\n'
            content_html += '</ol></div>\n'
        # 无序列表（- / *）
        elif para.startswith("- ") or para.startswith("* "):
            # 列表
            lines = para.split("\n")
            content_html += f'<div style="{theme["content"]}"><ul style="margin: 10px 0; padding-left: 22px;">\n'
            for line in lines:
                if line.startswith("- ") or line.startswith("* "):
                    content_html += f'<li style="margin: 6px 0;">{_md_inline(line[2:])}</li>\n'
            content_html += '</ul></div>\n'
        else:
            # 普通段落
            para = _md_inline(para).replace("\n", "<br>")
            content_html += f'<p style="{theme["content"]}">{para}</p>\n'

    # 添加图片
    if image_urls:
        for img_url in image_urls:
            content_html += f'<p style="text-align: center; margin: 15px 0;"><img src="{img_url}" style="max-width: 100%; height: auto; display: block; margin: 0 auto;"/></p>\n'

    # 构建完整HTML
    html = f'''
<h1 style="{theme["title"]}">{title}</h1>

<p style="{theme["separator"]}">— · —</p>

<div>
{content_html}
</div>
'''

    return html


def list_themes():
    """列出所有可用主题"""
    return list(THEMES.keys())


# 如果直接运行，显示所有主题
if __name__ == "__main__":
    print("可用主题列表：")
    for i, theme in enumerate(THEMES.keys(), 1):
        print(f"  {i}. {theme}")
