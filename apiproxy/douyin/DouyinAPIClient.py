import http.client
import json
import apiproxy
from apiproxy.common import utils


class DouyinAPIClient:
    def __init__(self, host):
        self.host = host

    def send_request(self, path, headers, payload=None):
        conn = http.client.HTTPSConnection(self.host)
        conn.request("GET", path, payload, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data


    #ttwid=1%7CaE-xnVJ3i839CUWWZk5MsYn3roFzwPjwC5T6te0nkyU%7C1715494057%7Cfb2452724ad7da9cda108a50cf63fb919f913e8ebbe842d90fb7d66433d32e69;
    # bd_ticket_guard_client_web_domain=2;
    # passport_csrf_token=17fc56810232efce01c792e90e18c7a4;
    # passport_csrf_token_default=17fc56810232efce01c792e90e18c7a4;
    # UIFID_TEMP=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c28f7af8ae9d231c853dd5f22d3ea32a1370635b95be08d1d8bb197b35c2e854c0394f1266d36e6d23c8ba6bf972012715;
    # home_can_add_dy_2_desktop=%220%22;
    # dy_swidth=1463;
    # dy_sheight=823;
    # s_v_web_id=verify_lxxdm6qu_6deBUu39_nqa1_4uJZ_Ap3W_zUk253gTPLoo;
    # fpk1=U2FsdGVkX180r4YWvMfTMrH4RvYbIiipeUYC3c15eCR55JNkKTzwARe+1kNijt1Bu/l1/d2mJ3TobQgJG6uSWA==;
    # fpk2=f1f6b29a6cc1f79a0fea05b885aa33d0;
    # passport_assist_user=CjwTLJmeSzI0KrpC8zaJFNMYY8zO9toVHuczMann1cmE4BCH4PHPsSMx-aaqW1BAqaezQfL-Lbc7d2rThsUaSgo8cwFBRA8bGNKVZu10O9Aw-RFLgYB9swejHFrBE8PVkY7BqpAPpiSbik3xZGED3e46tR4oAgIuha5jqIytEL6S1Q0Yia_WVCABIgEDNdcvZA%3D%3D;
    # n_mh=e1UKDyzTxZxW5q-nm_B2PDgZ-s2W9lNXwOlv8G5ahSU;
    # sso_uid_tt=72b86a03211e2a9151e8b8b7d7a0a011;
    # sso_uid_tt_ss=72b86a03211e2a9151e8b8b7d7a0a011;
    # toutiao_sso_user=ad0fefc27af7f586740e2fa7f5118301;
    # toutiao_sso_user_ss=ad0fefc27af7f586740e2fa7f5118301;
    # sid_ucp_sso_v1=1.0.0-KDIyMGQ4OThkZGVhMWQ3YWRiMWVkZDc4YmNlZWVkZTUyMGUzYjQ0ZDcKHwjBu_LulwIQrvb1swYY7zEgDDDt0IzQBTgGQPQHSAYaAmxmIiBhZDBmZWZjMjdhZjdmNTg2NzQwZTJmYTdmNTExODMwMQ;
    # ssid_ucp_sso_v1=1.0.0-KDIyMGQ4OThkZGVhMWQ3YWRiMWVkZDc4YmNlZWVkZTUyMGUzYjQ0ZDcKHwjBu_LulwIQrvb1swYY7zEgDDDt0IzQBTgGQPQHSAYaAmxmIiBhZDBmZWZjMjdhZjdmNTg2NzQwZTJmYTdmNTExODMwMQ;
    # passport_auth_status=b76652ef0dd157a31e0bc4f62aee65cf%2C;
    # passport_auth_status_ss=b76652ef0dd157a31e0bc4f62aee65cf%2C;
    # uid_tt=9de55ef2bca671cf5eefed873f9abd9b;
    # uid_tt_ss=9de55ef2bca671cf5eefed873f9abd9b;
    # sid_tt=92c7d1d79eddf884bdb595fa88037d45;
    # sessionid=92c7d1d79eddf884bdb595fa88037d45;
    # sessionid_ss=92c7d1d79eddf884bdb595fa88037d45;
    # UIFID=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c28f7af8ae9d231c853dd5f22d3ea32a13dc264f5a7df4ca06d9cabb4b268a44c9139b780a597d312537aa5ec9b83803f96b620cbce89527ce4a75f330820c9132d897f46f380ea9db70d495e7a480b9d77d865692bc24002023e79c6d89522589ed4bb001db16de84351334a7777f398138bbc8374cd62fa46238df40f2cbb6f4;
    # _bd_ticket_crypt_doamin=2;
    # _bd_ticket_crypt_cookie=4afcd6247639e2ce4ea04cd84c6ecbd0;
    # __security_server_data_status=1;
    # sid_guard=92c7d1d79eddf884bdb595fa88037d45%7C1719499576%7C5183993%7CMon%2C+26-Aug-2024+14%3A46%3A09+GMT;
    # sid_ucp_v1=1.0.0-KDZkNTEzZDY0ZjA0MTNkOTMwYTNmMDk0NWY2N2ExNWY1YjZhNWJhODUKGQjBu_LulwIQuPb1swYY7zEgDDgGQPQHSAQaAmxxIiA5MmM3ZDFkNzllZGRmODg0YmRiNTk1ZmE4ODAzN2Q0NQ;
    # ssid_ucp_v1=1.0.0-KDZkNTEzZDY0ZjA0MTNkOTMwYTNmMDk0NWY2N2ExNWY1YjZhNWJhODUKGQjBu_LulwIQuPb1swYY7zEgDDgGQPQHSAQaAmxxIiA5MmM3ZDFkNzllZGRmODg0YmRiNTk1ZmE4ODAzN2Q0NQ;
    # store-region=cn-bj;
    # store-region-src=uid;
    # SEARCH_RESULT_LIST_TYPE=%22single%22;
    # xgplayer_device_id=64404488442;
    # xgplayer_user_id=23149409796;
    # WallpaperGuide=%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A28%2C%22cursor2%22%3A0%7D;
    # live_use_vvc=%22false%22;
    # stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22;
    # publish_badge_show_info=%220%2C0%2C0%2C1720793080645%22;
    # __live_version__=%221.1.2.1736%22;
    # live_can_add_dy_2_desktop=%221%22;
    # msToken=dtUCnxUZMk_kiJWiOQgpc0an2xGMWq3I3OlxsOPgAkDNo4r4U057weVwmGQs3jsjrx0hMyXW4HWi24WmSwM8AAAKKVlslIjjkxgVxI7UBmgwvYu0iOttIvIbRn-1HA==;
    # FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D;
    # download_guide=%222%2F20240712%2F1%22;
    # csrf_session_id=f51c15a148072e45845cab256bc92628;
    # strategyABtestKey=%221720841749.796%22;
    # biz_trace_id=e13ce4a6;
    # volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.248%7D;
    # passport_fe_beating_status=true;
    # bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1lHZkI5SE1KN2FxdGhQTSt6Y3EvUVJLQ3o1OStGZTB6NXV6dmNyN3lqbjNETjByTzFKMjljYnpYQmZteFYxMWVvWWYwUHl6Z3BVMVMxc0d2R1YzVjA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D;
    # odin_tt=48d9b6fcb15de3d35dd644cde4fcf092d7f73ad93a98871b1b5919a881e06676482ec099658040dcac4164b53b612a0b;
    # __ac_nonce=06692188c001c9be44928;
    # __ac_signature=_02B4Z6wo00f019QVBLQAAIDAQTrH3gE-Y8fUNQAAAJOge4;
    # IsDouyinActive=true;
    # stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1463%2C%5C%22screen_height%5C%22%3A823%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A7.8%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22;
    # FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAN8iXrq5CRr4rgsgr0ok7SgHFQrOlTS25Azb6zttbDxg%2F1720886400000%2F0%2F0%2F1720851176710%22;
    # FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAN8iXrq5CRr4rgsgr0ok7SgHFQrOlTS25Azb6zttbDxg%2F1720886400000%2F0%2F0%2F1720851776711%22



    #无登录态
    # ttwid=1%7CSNQR36fch7kHp3VofgJK52rOlSWDZaEYnqbzkSkZDdM%7C1720360459%7Cbcce4ba6893e57c23ad8761923cc0590969588b6a9448a7b82ffe4733e077fbf;
    # UIFID_TEMP=fa6cda412c16c7667c793c3549025f122b064c8fecfdcae9cd663ea2db1893d2fe55f8384f303a7ae2c2fe4cc40ec44736f341298d8ba397516955c629686eb6b6fed136226fc94a3e264928d7506262;
    # dy_swidth=1463;
    # dy_sheight=823;
    # s_v_web_id=verify_lybm81zd_HbU2wUIj_5NoM_4RJK_8q03_BxFFC0PEBvQX;
    # FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D;
    # fpk1=U2FsdGVkX19QD8csaTmF/1vuZ/QPHbFY0shEhF7l81RsXKKcoxa7XZd+q5YfEP1qVRjGmOwhJNq3UDgEVdRgHg==;
    # fpk2=e95fb8733ac3417b3aa284b34753f35d;
    # passport_csrf_token=c8f7041a6c36af85fcacb1097c11fdca;
    # passport_csrf_token_default=c8f7041a6c36af85fcacb1097c11fdca;
    # bd_ticket_guard_client_web_domain=2;
    # xgplayer_device_id=23478375501;
    # xgplayer_user_id=178697431983;
    # __ac_nonce=066924021003e757139da;
    # __ac_signature=_02B4Z6wo00f01vV1ePQAAIDBYFq7ntN2k2b1VXxAANvc2a;
    # UIFID=fa6cda412c16c7667c793c3549025f122b064c8fecfdcae9cd663ea2db1893d2fe55f8384f303a7ae2c2fe4cc40ec447b2145b702f0ac80c7bc1e3a8e630a5cd6f8b9322174f3c07f7e13767af73e0535a62435d1365bc38340b91f352d7522900cd3fd455cfbf3b5c4a521e1af1002b75f5c137b44d357d08b6ae56e39f2424689c3ebd17064e59aba474c751bd6297ee8c7d7b74e0c1c06ce12d1752699078;
    # douyin.com;
    # device_web_cpu_core=8;
    # device_web_memory_size=8;
    # architecture=amd64;
    # csrf_session_id=f51c15a148072e45845cab256bc92628;
    # strategyABtestKey=%221720860713.57%22;
    # stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22;
    # volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D;
    # odin_tt=73cecd23d1226da0045f18cc33d7ff92c0be17a267eb1bacbf3d96120d0b602f04000f704b116a78dec03775de0fe574b9ce413f5642b7567c3268ebdccde1074bfaf088f6958da8d8d36f1675d191c8;
    # download_guide=%222%2F20240713%2F0%22;
    # pwa2=%220%7C0%7C1%7C0%22;
    # biz_trace_id=a7072144;
    # bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ1FvdVB2Zmhma0JIU0U0aG5yamF4MjZ0NDVRTnBJamtQQm5yUGg3eHBDejJUeUpxRUFRYXRUbEIwR0YvR2hmazlESnJwQS92T3FLTWNIU0YxY2N6aEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D;
    # IsDouyinActive=true;
    # home_can_add_dy_2_desktop=%220%22;
    # stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1463%2C%5C%22screen_height%5C%22%3A823%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A8.15%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22




    def get_aweme(self, **params):
        # 构造查询字符串
        query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
        headers = {
            # 'dnt': '1',
            # 'priority': 'u=1, i',
            'Cookie': 'ttwid=1%7Cc5issOsVBgDf1ZP8JHc6i43LDAsJ3MseinRVCjKz0Sw%7C1720862915%7C122865e24b2d644c23a785380295956c0e9bc4ccdbd9fad9112e36834eae5017; UIFID_TEMP=fa6cda412c16c7667c793c3549025f122b064c8fecfdcae9cd663ea2db1893d2fe55f8384f303a7ae2c2fe4cc40ec4479c397ad7ba75ec4b897ecbbc6be08c8b2ed2a96b0ee1b1b413c16d2a60e2436c; dy_swidth=1463; dy_sheight=823; csrf_session_id=f51c15a148072e45845cab256bc92628; s_v_web_id=verify_lyjxcnv9_y99GqsXr_4Bxo_4rAo_A983_KMJAcElFexhf; strategyABtestKey=%221720862923.399%22; passport_csrf_token=d0c024845fa8a6d1b1a274bf68025108; passport_csrf_token_default=d0c024845fa8a6d1b1a274bf68025108; fpk1=U2FsdGVkX19uYf1kn7Gt2hxr62Gnj1AR5s3RN81SQ5OvCYbdi09GPTNHIiGE6KJAa908kXHowsAMM0255WaP5g==; fpk2=e95fb8733ac3417b3aa284b34753f35d; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; UIFID=fa6cda412c16c7667c793c3549025f122b064c8fecfdcae9cd663ea2db1893d2fe55f8384f303a7ae2c2fe4cc40ec447bc374f6d8c3f1c9a23664b693d7fbbc812609b77387d953433c4362f9a4466302b99f6832e0386317e81a81c7aa043c263e817c2d1b2560c335c3dc44e65158f3424f7a64300575af055843fb85f8534e517629a9da91eea5a104316a2c8e0a94a402c140bd048968cf683e62485108c; bd_ticket_guard_client_web_domain=2; download_guide=%222%2F20240713%2F0%22; __ac_nonce=06692512600f73b7348be; __ac_signature=_02B4Z6wo00f01DFHvDQAAIDDpGh.X7FbnGAxZ7iAAGrK48; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1463%2C%5C%22screen_height%5C%22%3A823%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A6.8%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ1FvdVB2Zmhma0JIU0U0aG5yamF4MjZ0NDVRTnBJamtQQm5yUGg3eHBDejJUeUpxRUFRYXRUbEIwR0YvR2hmazlESnJwQS92T3FLTWNIU0YxY2N6aEE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; biz_trace_id=9df2578a; IsDouyinActive=true',
            # 'Cookie': 'ttwid=1%7CaE-xnVJ3i839CUWWZk5MsYn3roFzwPjwC5T6te0nkyU%7C1715494057%7Cfb2452724ad7da9cda108a50cf63fb919f913e8ebbe842d90fb7d66433d32e69; bd_ticket_guard_client_web_domain=2; passport_csrf_token=17fc56810232efce01c792e90e18c7a4; passport_csrf_token_default=17fc56810232efce01c792e90e18c7a4; UIFID_TEMP=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c28f7af8ae9d231c853dd5f22d3ea32a1370635b95be08d1d8bb197b35c2e854c0394f1266d36e6d23c8ba6bf972012715; home_can_add_dy_2_desktop=%220%22; dy_swidth=1463; dy_sheight=823; s_v_web_id=verify_lxxdm6qu_6deBUu39_nqa1_4uJZ_Ap3W_zUk253gTPLoo; fpk1=U2FsdGVkX180r4YWvMfTMrH4RvYbIiipeUYC3c15eCR55JNkKTzwARe+1kNijt1Bu/l1/d2mJ3TobQgJG6uSWA==; fpk2=f1f6b29a6cc1f79a0fea05b885aa33d0; passport_assist_user=CjwTLJmeSzI0KrpC8zaJFNMYY8zO9toVHuczMann1cmE4BCH4PHPsSMx-aaqW1BAqaezQfL-Lbc7d2rThsUaSgo8cwFBRA8bGNKVZu10O9Aw-RFLgYB9swejHFrBE8PVkY7BqpAPpiSbik3xZGED3e46tR4oAgIuha5jqIytEL6S1Q0Yia_WVCABIgEDNdcvZA%3D%3D; n_mh=e1UKDyzTxZxW5q-nm_B2PDgZ-s2W9lNXwOlv8G5ahSU; sso_uid_tt=72b86a03211e2a9151e8b8b7d7a0a011; sso_uid_tt_ss=72b86a03211e2a9151e8b8b7d7a0a011; toutiao_sso_user=ad0fefc27af7f586740e2fa7f5118301; toutiao_sso_user_ss=ad0fefc27af7f586740e2fa7f5118301; sid_ucp_sso_v1=1.0.0-KDIyMGQ4OThkZGVhMWQ3YWRiMWVkZDc4YmNlZWVkZTUyMGUzYjQ0ZDcKHwjBu_LulwIQrvb1swYY7zEgDDDt0IzQBTgGQPQHSAYaAmxmIiBhZDBmZWZjMjdhZjdmNTg2NzQwZTJmYTdmNTExODMwMQ; ssid_ucp_sso_v1=1.0.0-KDIyMGQ4OThkZGVhMWQ3YWRiMWVkZDc4YmNlZWVkZTUyMGUzYjQ0ZDcKHwjBu_LulwIQrvb1swYY7zEgDDDt0IzQBTgGQPQHSAYaAmxmIiBhZDBmZWZjMjdhZjdmNTg2NzQwZTJmYTdmNTExODMwMQ; passport_auth_status=b76652ef0dd157a31e0bc4f62aee65cf%2C; passport_auth_status_ss=b76652ef0dd157a31e0bc4f62aee65cf%2C; uid_tt=9de55ef2bca671cf5eefed873f9abd9b; uid_tt_ss=9de55ef2bca671cf5eefed873f9abd9b; sid_tt=92c7d1d79eddf884bdb595fa88037d45; sessionid=92c7d1d79eddf884bdb595fa88037d45; sessionid_ss=92c7d1d79eddf884bdb595fa88037d45; UIFID=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c28f7af8ae9d231c853dd5f22d3ea32a13dc264f5a7df4ca06d9cabb4b268a44c9139b780a597d312537aa5ec9b83803f96b620cbce89527ce4a75f330820c9132d897f46f380ea9db70d495e7a480b9d77d865692bc24002023e79c6d89522589ed4bb001db16de84351334a7777f398138bbc8374cd62fa46238df40f2cbb6f4; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=4afcd6247639e2ce4ea04cd84c6ecbd0; __security_server_data_status=1; sid_guard=92c7d1d79eddf884bdb595fa88037d45%7C1719499576%7C5183993%7CMon%2C+26-Aug-2024+14%3A46%3A09+GMT; sid_ucp_v1=1.0.0-KDZkNTEzZDY0ZjA0MTNkOTMwYTNmMDk0NWY2N2ExNWY1YjZhNWJhODUKGQjBu_LulwIQuPb1swYY7zEgDDgGQPQHSAQaAmxxIiA5MmM3ZDFkNzllZGRmODg0YmRiNTk1ZmE4ODAzN2Q0NQ; ssid_ucp_v1=1.0.0-KDZkNTEzZDY0ZjA0MTNkOTMwYTNmMDk0NWY2N2ExNWY1YjZhNWJhODUKGQjBu_LulwIQuPb1swYY7zEgDDgGQPQHSAQaAmxxIiA5MmM3ZDFkNzllZGRmODg0YmRiNTk1ZmE4ODAzN2Q0NQ; store-region=cn-bj; store-region-src=uid; SEARCH_RESULT_LIST_TYPE=%22single%22; xgplayer_device_id=64404488442; xgplayer_user_id=23149409796; WallpaperGuide=%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A28%2C%22cursor2%22%3A0%7D; live_use_vvc=%22false%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; publish_badge_show_info=%220%2C0%2C0%2C1720793080645%22; __live_version__=%221.1.2.1736%22; live_can_add_dy_2_desktop=%221%22; msToken=dtUCnxUZMk_kiJWiOQgpc0an2xGMWq3I3OlxsOPgAkDNo4r4U057weVwmGQs3jsjrx0hMyXW4HWi24WmSwM8AAAKKVlslIjjkxgVxI7UBmgwvYu0iOttIvIbRn-1HA==; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; download_guide=%222%2F20240712%2F1%22; csrf_session_id=f51c15a148072e45845cab256bc92628; strategyABtestKey=%221720841749.796%22; biz_trace_id=e13ce4a6; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.248%7D; passport_fe_beating_status=true; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT1lHZkI5SE1KN2FxdGhQTSt6Y3EvUVJLQ3o1OStGZTB6NXV6dmNyN3lqbjNETjByTzFKMjljYnpYQmZteFYxMWVvWWYwUHl6Z3BVMVMxc0d2R1YzVjA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=48d9b6fcb15de3d35dd644cde4fcf092d7f73ad93a98871b1b5919a881e06676482ec099658040dcac4164b53b612a0b; __ac_nonce=06692188c001c9be44928; __ac_signature=_02B4Z6wo00f019QVBLQAAIDAQTrH3gE-Y8fUNQAAAJOge4; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1463%2C%5C%22screen_height%5C%22%3A823%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A7.8%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAN8iXrq5CRr4rgsgr0ok7SgHFQrOlTS25Azb6zttbDxg%2F1720886400000%2F0%2F0%2F1720851176710%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAN8iXrq5CRr4rgsgr0ok7SgHFQrOlTS25Azb6zttbDxg%2F1720886400000%2F0%2F0%2F1720851776711%22',  # 替换为您的 Cookie
            # 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'User-Agent': apiproxy.ua,
            # 'Accept': '*/*',
            'Host': self.host,
            # 'Connection': 'keep-alive',
        }
        # 构造请求路径
        path = f"/aweme/v1/web/aweme/post/?{query_string}"
        # 发送请求并获取响应数据
        data = self.send_request(path, headers)
        # 尝试解析响应数据为 JSON
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return None


# 使用示例
if __name__ == "__main__":
    client = DouyinAPIClient("www.douyin.com")
    aweme_data = client.get_aweme(aid=6383, channel='channel_pc_web', sec_user_id='MS4wLjABAAAAj7YQ465z-ilJkcexoC3slERNsnlpW_4oHkbAKtpIbLY')  # 替换参数
    if aweme_data:
        print(json.dumps(aweme_data, indent=2))
    else:
        print("Failed to get data or data is not in JSON format.")
