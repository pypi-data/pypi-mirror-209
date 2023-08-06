#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : _🏆_主页.py
# @Time         : 2023/5/21 17:13
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 

from meutils.pipe import *
import streamlit as st



def set_footer(prefix="Made with 🔥 by ", author='Betterme', url=None):  # 链接门户、微信
    _ = f"""
<style>
  .footer {{
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
  }}
  footer:after {{
    content: "{prefix}";
    visibility: visible;
    display: block;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -100%);
  }}
  footer:after a {{
    content: '{author}';
    color: #999;
    text-decoration: underline;
    margin-left: 5px;
  }}
</style>
    """
    st.markdown(_, unsafe_allow_html=True)
set_footer()