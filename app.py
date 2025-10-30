import streamlit as st
import random
import time
import subprocess
import os

st.set_page_config(page_title="宝贝",page_icon="💗")

tips = ['我想你了', '今天过得开心吗', '早点休息', '天冷了，多穿衣',
        '今天有想我嘛', '我们都会有光明的未来', '我的身边还是你']
bg_colors = ["#C7EEFF", "#B8E0D2", "#95B8D1", "#E8D4D3", "#D8BFD5", "#BFA6CA"]

MAX_WIN = 50        # 浏览器里别太多，50 够浪漫

if st.button("点我开始弹窗"):
    # 生成随机位置的小窗口
    html = """
    <script>
    const tips = """ + str(tips) + """;
    const colors = """ + str(bg_colors) + """;
    const max = """ + str(MAX_WIN) + """;
    for(let i=0;i<max;i++){
        const w = 250, h = 60;
        const x = Math.random()*(screen.width-w);
        const y = Math.random()*(screen.height-h);
        const wnd = window.open(
            '',
            '_blank',
            `width=${w},height=${h},left=${x},top=${y},menubar=0,toolbar=0,location=0`
        );
        if(wnd){
            wnd.document.write(`
              <body style="margin:0">
              <div style="display:flex;align-items:center;justify-content:center;
                          height:100%;font-size:18px;font-family:楷体;
                          background:${colors[Math.floor(Math.random()*colors.length)]}">
                ${tips[Math.floor(Math.random()*tips.length)]}
              </div>
              </body>`);
            wnd.document.close();
        }
    }
    // 30 秒后逐个关
    let idx=0;
    const timer=setInterval(()=>{
        if(idx>=window.length) {clearInterval(timer); return;}
        window[idx].close();
        idx++;
    }, 150);
    </script>
    """
    st.components.v1.html(html, height=0)
    st.balloons()
    st.success("弹窗已发射！30 秒后自动逐个关闭~")