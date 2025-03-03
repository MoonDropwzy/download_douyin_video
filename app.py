"""
@Project        ：PyCharm 
@File           ：app.py
@IDE            ：PyCharm 
@Author         ：Moondrop
@Date           ：2024/7/5 上午10:52 
@Description    ：
"""
import re
import time
import requests
import streamlit as st
from io import BytesIO


cookies = {
    'passport_assist_user': 'CkF5fvCn7vxEe0EEB3rt68o0B4jeL4G5nFtEn6snrq7q3fONIuLo-Ayrk33E6JByQuiLO3_IlaQqvi7MIfC6quCszRpKCjxJmTqHh5D5oRi7grBSKuRTofl6Tmc3z9Xs3L_FZVu461oMuQVZwMlbHfwgeLQFbtXTXaTDDNw7X-Q6K00QkOvKDRiJr9ZUIAEiAQNRMi6X',
    'LOGIN_STATUS': '1',
    'store-region': 'cn-cq',
    'store-region-src': 'uid',
    'live_use_vvc': '%22false%22',
    'sid_guard': 'f8a25d3053ad183fd58a6f856afec7ba%7C1711689187%7C5184001%7CTue%2C+28-May-2024+05%3A13%3A08+GMT',
    '__live_version__': '%221.1.1.9068%22',
    'odin_tt': '01adf87da2e9db0af7f316d0a9cbf875e5771d953fe68f734d7ca026e1e3ecf076dc19b738d81afea013aa638a5d24471e387604f5412e3c4d26bd34aa2f1a3b',
    'ttwid': '1%7CBAvlL0Y5PPEO6HtKp-St-Au2HouEOCCdUdShJj8J6ZI%7C1720141506%7Ce5be43a0ef598408c298b1c8a713daaed5e32b6a4463ed7cb8a00c691c74ccf5',
    'UIFID_TEMP': '50e9ecd8f8a80ccc1068760eba6358973f2507e307da116bb148a43844661363f67f9aae954843ebb0c634cbbcae0e4f7df136d4553cd697ae2b3f1b221ff27b5add9fc76ac19f38d9e1ab45216b2008',
    'strategyABtestKey': '%221720141509.907%22',
    'passport_csrf_token': 'c7d5ef89ae2e3192d30ab48d09c6d5f8',
    'passport_csrf_token_default': 'c7d5ef89ae2e3192d30ab48d09c6d5f8',
    'bd_ticket_guard_client_web_domain': '2',
    'UIFID': '50e9ecd8f8a80ccc1068760eba6358973f2507e307da116bb148a438446613630f1537372ae589af50ddad577d18d3d7879fb630cadb3c9f04d00940c8e3087f4615ba9d2bdb5004e8b43591f38baedf72f0668d4f12f3ec174307a7a87eee001d61c137dca7a98655e6ae70bf01cb9e4651eacebe60453d6a1c8517171a5beebf8636f3818fae8d0f9f018e98ff3f7ed2f59cf2a0bacc743bc4b03c306394a4',
    'stream_recommend_feed_params': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22',
    'FORCE_LOGIN': '%7B%22videoConsumedRemainSeconds%22%3A180%7D',
    'volume_info': '%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.646%7D',
    'bd_ticket_guard_client_data': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSW5IcnJCOHpvUzh6WVlXc0hlT1kwVlhlZDM5djNTV0NCRXBhbEtlYXRHdmxWdXF2bWhSWDYxRnJZNUZrbmpQKzlFMCs2ZXdZVFBVTTN5N2lYRDAvbEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D',
    'home_can_add_dy_2_desktop': '%221%22',
    'biz_trace_id': 'bcd41be9',
    'IsDouyinActive': 'false',
    'x-web-secsdk-uid': 'f140d744-dd60-4ba3-bd44-c7991dc8ae34',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'passport_assist_user=CkF5fvCn7vxEe0EEB3rt68o0B4jeL4G5nFtEn6snrq7q3fONIuLo-Ayrk33E6JByQuiLO3_IlaQqvi7MIfC6quCszRpKCjxJmTqHh5D5oRi7grBSKuRTofl6Tmc3z9Xs3L_FZVu461oMuQVZwMlbHfwgeLQFbtXTXaTDDNw7X-Q6K00QkOvKDRiJr9ZUIAEiAQNRMi6X; LOGIN_STATUS=1; store-region=cn-cq; store-region-src=uid; live_use_vvc=%22false%22; sid_guard=f8a25d3053ad183fd58a6f856afec7ba%7C1711689187%7C5184001%7CTue%2C+28-May-2024+05%3A13%3A08+GMT; __live_version__=%221.1.1.9068%22; odin_tt=01adf87da2e9db0af7f316d0a9cbf875e5771d953fe68f734d7ca026e1e3ecf076dc19b738d81afea013aa638a5d24471e387604f5412e3c4d26bd34aa2f1a3b; ttwid=1%7CBAvlL0Y5PPEO6HtKp-St-Au2HouEOCCdUdShJj8J6ZI%7C1720141506%7Ce5be43a0ef598408c298b1c8a713daaed5e32b6a4463ed7cb8a00c691c74ccf5; UIFID_TEMP=50e9ecd8f8a80ccc1068760eba6358973f2507e307da116bb148a43844661363f67f9aae954843ebb0c634cbbcae0e4f7df136d4553cd697ae2b3f1b221ff27b5add9fc76ac19f38d9e1ab45216b2008; strategyABtestKey=%221720141509.907%22; passport_csrf_token=c7d5ef89ae2e3192d30ab48d09c6d5f8; passport_csrf_token_default=c7d5ef89ae2e3192d30ab48d09c6d5f8; bd_ticket_guard_client_web_domain=2; UIFID=50e9ecd8f8a80ccc1068760eba6358973f2507e307da116bb148a438446613630f1537372ae589af50ddad577d18d3d7879fb630cadb3c9f04d00940c8e3087f4615ba9d2bdb5004e8b43591f38baedf72f0668d4f12f3ec174307a7a87eee001d61c137dca7a98655e6ae70bf01cb9e4651eacebe60453d6a1c8517171a5beebf8636f3818fae8d0f9f018e98ff3f7ed2f59cf2a0bacc743bc4b03c306394a4; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.646%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSW5IcnJCOHpvUzh6WVlXc0hlT1kwVlhlZDM5djNTV0NCRXBhbEtlYXRHdmxWdXF2bWhSWDYxRnJZNUZrbmpQKzlFMCs2ZXdZVFBVTTN5N2lYRDAvbEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; biz_trace_id=bcd41be9; IsDouyinActive=false; x-web-secsdk-uid=f140d744-dd60-4ba3-bd44-c7991dc8ae34',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}


def url_parse(text: str) -> object:
    st.info(f"正在解析，链接{text[:10]}...", icon="ℹ️")
    try:
        c = "[a-zA-z]+://[^\s]*"
        url = re.findall(c, text)[0]
        logger.info(f"get url {url}")
        response = requests.get(url=url, cookies=cookies, headers=headers)
        response = response.text.replace("\n", "")
        rc = '"play_addr":.*?video_id=(.*?)&'
        video_name = re.findall('<title .*?>(.*?)</title>', response)[0]
        logger.info(f"name {video_name}")
        video_id = re.findall(rc, response, re.S)[0]
        logger.info(f"is {video_id}")
        video_url = "https://www.iesdouyin.com/aweme/v1/play/?video_id=" + video_id
        st.success("解析成功，即将开始获取！", icon="✅")
        return video_url, video_name
    except Exception as e:
        logger.error(e)
        st.error(f"解析失败，链接{text[:10]}...异常", icon="🚨")


def download_video(url, name):
    temp = requests.get(url=url).content
    # with open(f"{id}.mp4", 'wb') as f:
    #     f.write(temp)
    progress_text = "正在请求，请等待..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.success("获取成功！", icon="✅")
    width = 80
    side = 100
    _, container, _ = st.columns([side, width, side])
    container.video(data=temp)
    temp = BytesIO(temp)

    st.download_button("保存至本地", data=temp, file_name=f'{name}.mp4', mime='video/mp4')


def main():
    st.title("抖音无水印下载！")
    input_text = st.chat_input(placeholder="此处粘贴视频分享链接：")

    if input_text:  # st.button("开始") or
        video_url, video_name = url_parse(input_text)
        if video_url:
            download_video(video_url, video_name)


if __name__ == "__main__":
    try:
        main()
    except:
        pass
